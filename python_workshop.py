a={101:"durga",102:"koushik",103:"siva",104:"prasad",105:"vamsi"}

roll_number =int(input("Enter roll number: "))
name = input("Enter name: ")

for x in a:
    if roll_number in a:
        print(f"{roll_number}:{name} already registered.")
        break
    else:
        a.update({roll_number:name})
        print(f"This student: {roll_number} with name: {name} don't have account,So Create a account.")
        break

print("Final dictionary:", a)