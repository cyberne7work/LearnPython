from random import randint
ch="Y"
while ch=="Y":
    computer=randint(1,10)
    while ch!='N':
        user=int(input("Enter a Number Between 1 To 10="))
        if user==computer:
            print("You Win")
            break
        elif user>computer:
            print("Two High")
        elif user<computer:
            print("Too Low")
    ch=input("Do you want to Play Agian=")
