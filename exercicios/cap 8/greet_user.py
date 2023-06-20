def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

ursernames = ["hanna", "ty", "margot"]

greet_users(ursernames)