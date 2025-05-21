def prompt():
    while True:
        Character= input("Enter a character :")
        if len(Character)==1 and Character.isalpha():
            return Character
            break
            
        print("Please enter single alphabet character!")
    


Uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase= "abcdefghijklmnopqrstuvwxyz"

Character=prompt()

IsCapital=None


if Character in Uppercase:
    IsCapital=True
    print(f"Character {Character} is Uppercase")
elif Character in lowercase:
    IsCapital=False
    print(f"Character {Character} is lowercase")
