import json
import plantuml

def load_data():
  with open("./profile_service_response.json", encoding="utf-8") as profile_file:
    profile_json = json.load(profile_file)

  with open("./posts_management_service_response.json", encoding="utf-8") as posts_file:
    posts_json = json.load(posts_file)

  with open("./moderation_service_response.json", encoding="utf-8") as mod_file:
    mod_json = json.load(mod_file)

  # context = {
  #   "name": profile_json["name"],
  #   "username": profile_json["username"],
  #   "biography": profile_json["biography"],
  #   "posts": []
  # }

  # for post in posts_json:
  #   context_post = {
  #     "post_id": post["post_id"],
  #     "post_caption": post["post_caption"]
  #   }

  #   for mod_post in mod_json:
  #     if mod_post["post_id"] == context_post["post_id"]:
  #       context_post["is_reported"] = mod_post["is_reported"]
  #       context_post["is_manual"] = mod_post["is_manual"]
  #       context_post["reason"] = mod_post["reason"]

  #   context["posts"].append(context_post)

  # return context
  return(profile_json, posts_json, mod_json)

def write_plantuml_file(profile_data,posts_data, mods_data):
  with open("plantuml.txt","w", encoding="utf-8") as pf:
    pf.write("@startuml \n")
    # object nameOfNode
    pf.write("object " +profile_data["username"] + "\n")
    # nameOfNode : nameOfAttribute = attributeValue
    pf.write(profile_data["username"] + " : name = " + str(profile_data["name"]) + "\n")
    pf.write(profile_data["username"] + " : biography = " + str(profile_data["biography"]) + "\n")

    for post in posts_data:
      pf.write("object post_" + str(post["post_id"]) + "\n")
      pf.write("post_" + str(post["post_id"]) + " : post_caption = " + post["post_caption"] + "\n")

      # nameOfNodeOne -> nameOfNodeTwo
      pf.write(profile_data["username"] + "-down->" + "post_" + str(post["post_id"]) + "\n")

    pf.write("@enduml \n")

def create_plantuml_img():
  plantuml.PlantUML("http://plantuml.com/plantuml/img/").processes_file("plantuml.txt", outfile=None, errorfile="None")

if __name__ == '__main__':
  profile,posts, mods = load_data()
  write_plantuml_file(profile,posts, mods)
  create_plantuml_img()
