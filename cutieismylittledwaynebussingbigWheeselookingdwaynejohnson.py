print("Dude")
Dude = 5000000 
Pow = 6000000
Joseph = 15000000
Milk = 12000000
Cat = 0
John = 0.058685768

print('Dude has 6 guests including himself to a party. Sadly, people are given best quality if they have good ROK power. If they have bad power they will be given poor service.')
print('Dude has 5 million power, Pow has 6 million power, Joseph has 15 million power, Milk has 12 million power, Cat has 0 power and John has 0.58')
print('What would be the likely scenario between what would happen to the people in the party?')

made_choice = False

while not made_choice:
    try:
        choice_input = int(input('Your question goes here: [choose 1 or 2 or 3 or 4]:  '))
    except:
        print('Invalid. Try again')
    else:
        match choice_input:
            case 1:
                print('Dude will get average service, Pow will be given a private jet and a 10k dollars, Joseph will be allowed to do anything he wants be given all the things in the universe, Milk will be given 30 wishes which he could wish for anything, John will be put in a dungeon, be given Ohio food, just sit and do nothing for the rest of the party, and finally Cat will be assassinated once she steps inside the party place.')
                made_choice = False 
                print("If you picked this option your an Npc! Of course life won't go so boring like If you picked this you don't know the efinition of fate.")
            case 2:
                print('Dude will be there just to pick on his next victims, Pow will get terminated, same for Joseph, Milk, and Cat, but John will be kept alive and given whatever he wants because his name makes him a sussy imposter in Among Us.')
                made_choice = False
                print("Ayo! Are you a monkey? Why? Just Why? This isn't the 70s people!")
            case 3:
                print("Everyone dies! Dude decides to ram over every party guest once they get ther. Once the job is done, Dude just pulls the trigger on his head, killing him.")
                made_choice = False
                print("I am sorry to say if you picked this your either extremely depressed person or your just adopted.")
            case 4:
                print("Dude welcomes everyone to the party and says screw the ROK rule because it's bad. They all get free youtube premium. Sadly, John is assassinated because nobody likes him. Poor John! But he did had it coming.")
                made_choice = True
                print("Good job! Obviously! Easy question! Your the 99.99% who actually has common sense!")
            case _:
                print('Invalid. Try again')