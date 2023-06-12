def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
print("\nPlease tell me your name: ")
print("Enter 'exit' at any time to quit")

while True:
    f_name = input("First name: ")
    if f_name == "exit":
        break
    l_name = input("Last name: ") 
    if l_name == "exit":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    
    print("\nHello, " + formatted_name + "!")
    
