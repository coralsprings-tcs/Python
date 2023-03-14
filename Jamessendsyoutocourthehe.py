James = ('I will put you to jail noobie! Give me all your ip adress you broke noob! I shave your bald head buddy! I will headbutt you to Jupiter! Big bald fraud!')
print (James)
Question= ("How will James put bald fruad in eternal sleep?")
print(Question)

made_choice = False

while not made_choice:
    try:
        choice_input = int(input('Your question goes here: [choose 1 or 2 or 3 or 4]:  '))
    except:
        print('Invalid. Try again')
    else:
        match choice_input:
            case 1:
                print("James will grab his RPG and will expload bald fraud in to a million pieces!")
                made_choice = False 
                print("James doesn't have an RPG, he is chill and cool!")
            case 2:
                print("James will do nothing but just stare at the bald fraud malisciously! Sadly, we will never know James' next move but I heard the bald fraud is no where to be seen!")
                made_choice = True
                print("Good job! That's the James we know and love!")
            case 3:
                print("James will do it the old-fashioned way and physically assault bald fraud with his fists. After a while, the bald fraud will not take it anymore and will be put in eternal sleep.")
                made_choice = False
                print("James wasn't born in the 40s, so no!")
            case 4:
                print("James will call his lawyer and sue the bald fraud, causing the bald fraud to faint!")
                made_choice = False
                print("People don't die from lawyer cases, common sense people!")
            case _:
                print('Invalid. Try again')

