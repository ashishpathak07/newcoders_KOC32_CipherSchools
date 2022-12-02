import math
import random                       #math and random  imported

def pos_neg(a,b):
    if c > 0:
        print("       -positive")
    elif c < 0:
        print("       -negative")
    else:
        False                       #postive -neg checked here 
                                    
def odd_even(a,b):
    if c%2==0:
        print("       -even")
    elif c%2!=0:
        print("       -odd")
    else:
        False                       #odd - even checked here

                                      
def prime_composite(a,b):
    factors = 0
    index = 1
    while(index <= c):

        if((c % index) == 0):
            factors = factors + 1
          
        index = index + 1

    if(factors == 2):
        print("       -Prime")
    else:
        print("       -Composite")  #prime - composite checked

def run(a,b,c):
    print("     The number chosen randomly is:",c)
    print("     This number is :-")
    pos_neg(a,b)
    odd_even(a,b)
    prime_composite(a,b)


#main
    
while True:
    print("Enter two nuumbers for range")
    a=int(input(" Enter number 1:"))
    b=int(input(" Enter number 2:"))

                                    #two integers taken from user
    print("-------------------------")
    
    if a>b:                         #If use enters wrong range
        print("invalid range given")
        x=input("Swap the numbers?, yes or no :")
        if x=="yes" or x=="Yes" or x=="":
            
            print("numbers will be swapped, to create valid range")
            c = random.randint (b,a)    #random integer picked,by swapping the numbers
            run(a,b,c)
        else:
            print("numbers not swapped! enter range again")
            continue

        y=input("Do you want to run program again? \n press y (for yes) or n (for no):")
        if y=="n" or y=="N":
            break                   #used while loop to run the the program again
        else:
            print("-------------------------")
        continue
        
    else:
        c = random.randint(a,b)     #random integer picked
        run(a,b,c)
        print("-------------------------")
        y=input("Do you want to run program again? \n press y (for yes) or n (for no):")
        if y=="n" or y=="N":
            break                   #used while loop to run the the program again
        else:
            print("-------------------------")
        continue


