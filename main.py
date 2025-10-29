import json

with open("./profile_service_response.json", encoding="utf-8") as profile_file:
  profile_json = json.load(profile_file)

with open("./posts_management_service_response.json", encoding="utf-8") as posts_file:
  posts_json = json.load(posts_file)

with open("./moderation_service_response.json", encoding="utf-8") as mod_file:
  mod_json = json.load(mod_file)

context = {
  "name": profile_json["name"],
  "username": profile_json["username"],
  "biography": profile_json["biography"],
  "posts": []
}

for post in posts_json:
  context_post = {
    "post_id": post["post_id"],
    "post_caption": post["post_caption"]
  }

  for mod_post in mod_json:
    if mod_post["post_id"] == context_post["post_id"]:
      context_post["is_reported"] = mod_post["is_reported"]
      context_post["is_manual"] = mod_post["is_manual"]
      context_post["reason"] = mod_post["reason"]

  context["posts"].append(context_post)

print(context)