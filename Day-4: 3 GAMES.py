import random
n=int(input("""We have something for you...Games!!!

1)Who is paying bill today?-1
2)Heads or Tails-2
3)Rock paper Scissors game-3

"Enter the no. 1, 2 ,3 for the following Games.\n"""))
if n==1:
#Who is paying bill today?-1
    print(""" You have selected: 1-Who is paying bill today?
This game help in chossing who will pay the bill today by giving Random Names of your name 
list.(No need of Waiter to chose for you...hehehehe.
Lets Start.  """)
    names_string = input("Give me everybody's names, separated by a comma and then space.\n ")
    names = names_string.split(",")
    x=len(names)
    person=random.randint(0,x-1)
    print(names[person],"is going to pay today...HEHEHE..Bad Luck bro.")

elif n==2:
#Heads or Tails-2
    print(""" You have selected: 2-Heads or Tails Game,
No need of coin lets play online...""")
    
    ramdom_seed=int(input("Create a seed number:"))
    random.seed(ramdom_seed)
    if random.randint(0,1)==1:
        print("You get Heads")
    else:
        print(" You get Trails")

elif n==3:
#Rock paper Scissors game-3
     print(""" You have selected: 3-Rock paper Scissors Game,
Feeling bored and lonely?
Lets Play with Computer...Rock paper Scissors""")
    
     Rock=("""
     _______
     ---'   ____)
           (_____)
           (_____)
          (____)
     ---.__(___)
     """)
     Paper=("""
          _______
     ---'    ____)____
                ______)
               _______)
              _______)
     ---.__________)
     """)

     Scissors=("""
         _______
     ---'   ____)____
               ______)
            __________)
           (____)
     ---.__(___)
     """)
     list=(Rock,Paper,Scissors)
     index=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
     print(list[index])
     computer_index=random.randint(0,2)
     print("Computer Chose:")
     print(list[computer_index])

     if index==0 and computer_index==1:
        print("You loss and Computer wins!")
     elif index==1 and computer_index==2:
        print("You loss and Computer wins!")
     elif index==2 and computer_index==0:
        print("You loss and Computer wins!")  
     elif index==0 and computer_index==0:
        print("Its a Draw")
     elif index==1 and computer_index==1:
        print("Its a Draw")
     elif index==2 and computer_index==2:
        print("Its a Draw")
     else:
        print("You Win!!!")

else:
    print("Enter correct number:")
    
