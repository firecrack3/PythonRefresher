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




if Character in Uppercase:

    print(f"Character {Character} is Uppercase")
elif Character in lowercase:
   
    print(f"Character {Character} is lowercase")
