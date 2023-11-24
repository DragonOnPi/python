name = input("What's your name?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case_:
        print("Who?")
