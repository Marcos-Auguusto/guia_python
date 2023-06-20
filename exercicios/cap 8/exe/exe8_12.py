def build_profile(first, last, **info_user):
    user_info = {}
    user_info["first_name"] = first
    user_info["last_name"] = last
    for key, value in info_user.items():
        user_info[key] = value
    return user_info

user_profile = build_profile("marcos", "augusto", location="sao paulo")

print(user_profile)