import random

lists=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
,
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

number_enter_by_user=int(input('Enter 0 for rock ;1 for ' \
'paper and also 2 for scissors:"0","1","2"\n'))

if number_enter_by_user >= 3 or number_enter_by_user < 0:
    print("You entered a wrong number!!! You lose!")
else:
    print(lists[number_enter_by_user])

    Computer_random_choose=random.randint(0,len(lists)-1)
    print(lists[Computer_random_choose])
    
    if(number_enter_by_user == Computer_random_choose):
        print("!!!Draw!!!")
    elif(number_enter_by_user == 0 and Computer_random_choose==1):
        print("!!!Computer Wins!!!")    
    elif(number_enter_by_user ==0 and Computer_random_choose==2):
        print("!!!User Wins!!!")  
    elif(number_enter_by_user==1 and Computer_random_choose==0):
        print("!!!User Wins!!!")
    elif(number_enter_by_user==1 and Computer_random_choose==2):
        print("!!!Computer Wins!!!")
    elif(number_enter_by_user ==2 and Computer_random_choose==1):
        print("!!!User Wins!!!")
    elif(number_enter_by_user ==2 and Computer_random_choose==0):
        print("!!!Computer Wins!!!")