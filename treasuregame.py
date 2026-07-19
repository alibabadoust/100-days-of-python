print(''' ,-----------------------------.----------------------------------.
|                             |                                  |
|    .    .    ,---------     |     ------------------------.    |
|    |    |    |              |                             |    |
|    |    `----"--------------'    ,-------------------.    |    |
|    |                             |                   |    |    |
|    :--------------.--------------"----     ,---------:    |    |
|    |              |                        |         |    |    |
|    :---------     |    .    ,---------.    |    .    |    `----:
|    |              |    |    |         |    |    |    |         |
|    |     ---------'    |    :----     |    |    |    |    .    |
|    |                   |    |         |    |    |    |    |    |
|    `-------------------'    |     ----'    |    |    |    |    |
|                             |              |    |    |    |    |
:--------------.---------.    :--------------'    |    :----'    |
|              |         |    |                   |    |         |
|    .    .    |    .    |    |    ,--------------:    `----     |
|    |    |    |    |    |    |    |              |              |
|    |    |    "    |    |    |    |     ---------"---------.    |
|    |    |         |    |    |    |                        |    |
|    |    `---------"----'    |    |    ,---------.    .    |    |
|    |                        |    |    |         |    |    |    |
|    :---------.--------------:    |    |    .    |    |    |    |
|    |         | X            |    |    |    |    |    |    |    |
|    "    .    `---------     |    |    `----'    |    `----'    |
|         |                   |    |              |              |
`---------"-------------------'    `--------------"--------------''''')

print("Welcome to this island for finding treasure")
choice1=input('Which road you want to go through it :"Right"or"Left"').lower()
if choice1=="left":
 #continue
  choice2=input('Now what are you want to do:"Swim"or "Wait"').lower()
  if choice2 =="wait":
     #continue
     choice3=input('Which door would you choose:"red"or"yellow"or"blue"').lower()
     if choice3=="yellow":
        print("you finally find treasure .congragulations")
     elif choice3=="red":
        print("You chose dragon house .game over!!!")
     elif choice3=="blue":
        print("you chose wizard room so she magic you.game over!!")
     else:
        print("!!!!you enter room that is not found.game over!!!!")
    
  else:
     print("you drown into ocean.game over!!")

else:
    print("you choose wrong path.game over")
