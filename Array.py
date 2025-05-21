def prompt():
    lst = []
    while len(lst)<5:
        Num=(input("Enter a number:"))
        try:
            Num=float(Num)
            lst.append(Num)
        
        except ValueError: 
            print("Please enter a number!")
    return lst


list2=prompt()

total=0
count=0
for numbers in list2:
    total+=numbers
    count+=1

average=total/count

print(f"The average of the 5 numbers, ({list2}) is {average:.3f} ")