magics = ["mike", "jhonny", "thomas",]

def show_magicians():
    for magic in magics:
        print("Hello, " + magic.title() + "!")    

def make_great():
    for magic in magics:
        print("Hello, great magician " + magic.title() + "!")

show_magicians()
make_great()
