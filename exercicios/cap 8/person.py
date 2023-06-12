# Devolvendo um dicionário

def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name}
    full_name_person = person["first"] + " " + person["last"]
    return full_name_person.title()
        
musician = build_person("jimi", "hendrix")
print(musician)
