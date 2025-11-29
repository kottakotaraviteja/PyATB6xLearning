def vwo_login(user):

    if user != "admin":
        raise Exception("user is not admin")
    return "welcome"

print(vwo_login("admin"))

