#using for Loop
print("How many times you want to print smile face")
smile=int(input())
smile=smile+1
for num in range(1,smile):
    print("\U0001f600"*num)

#using while Loop
print("How many times you want to print smile face")
smile=int(input())
x=1
while(x<=smile):
    print("\U0001f600"*x)
    x=x+1
