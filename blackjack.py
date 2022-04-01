# Imports
import time
import random
# Lists
usedcard = []

face = ["Hearts", "Spades", "Diamonds", "Clubs"]

value = ["ace", '2', '3', '4', '5', '6', '7', '8', '9', '10', "jack", "king", "queen"]

# Define varribles
cumulative = 0
wins = 0
gamestateplayer = 0
gamestateplayer = int(gamestateplayer)
ai1cumulative = 0
gamestateai = 0
loss = 0
betvalue = 0
dealercumulative = 0
Game = 0

# Rules

print("Welcome To The Missouri Belle Casino, located in Osage Beach ")
time.sleep(1)
print("Today you will be playing blackjack")
time.sleep(1)
print('''Watch this video to learn the rules of blackjack if you are unsure how:
https://www.youtube.com/watch?v=gjjVmPwThCE
''')
# Gatehering the number of opponets you want to play against
while True:
    botcount = input("How much opponets do you want to have (not includeing dealer)\n0 or 1\nEnter here: ")
    if botcount == "1":
        #gatherer name of bot
        botname = input("What would you like your bots name to be?\nEnter here:")
        break
    elif botcount == "0":
        print("you have 0 opponents.")
        break
    else:
        print("Enter a valid input")
   #gather name of dealer
dealername = input("What would you like your dealers name to be?\nEnter Here:")

time.sleep(1)


# Card deck creation.
def card():
    while True:

        global card9

        global usedcard

        global face

        global value

        global card11

        global card10

        global totalvalue

        number = random.randint(0, 12)

        facetype = random.randint(0, 3)

        card11 = value[number]

        card10 = face[facetype]

        card9 = str(card11) + str(card10)

        usedcard.append(card9)
#duplicite card checker
        if usedcard.count(card9) == 1:
            #i needed somthing here so put a random varrible
            zzz = 7
        else:
            break
#gathering the value of the dealers card that is drawn
def dealercardsfinalvalue():
#globals take the place of return and allow me to use outside of functions
    global totalvalue

    global dealercumulative

#making the value of a face card = to 10
    if card11 == "jack" or card11 == "queen" or card11 == "king":
        totalvalue = 10
        dealercumulative = dealercumulative + totalvalue
        time.sleep(2)
        print("The total amount of the dealers hand is " + str(dealercumulative) + "\n")
    elif card11 == '10':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    elif card11 == '9':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    elif card11 == '8':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    elif card11 == '7':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    elif card11 == '6':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    elif card11 == '5':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    elif card11 == '4':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    elif card11 == '3':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    elif card11 == '2':
        totalvalue = int(card11)
        dealercumulative = dealercumulative + totalvalue
        print("The total amount of the dealers hand is " + str(dealercumulative)+ "\n")
    # determineing ace value
    elif card11 == "ace":
        if dealercumulative < 11:
            totalvalue = 11
        elif dealercumulative < 20:
            totalvalue = 1
        else:
            print("Enter a valid input you nut"+ "\n")

# Defineing the value of the AIs cards
def ai1cardsfinalvalue():
    # globals take the place of return and allow me to use outside of functions

    global ai1cumulative
    #getting value of face cards
    if card11 == "jack" or card11 == "queen" or card11 == "king":
        totalvalue = 10
        print("The value of " + botname + "'s card is " + str(totalvalue)+ "\n")
        ai1cumulative = ai1cumulative + totalvalue
        time.sleep(2)
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '10':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '9':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '8':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '7':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '6':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '5':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '4':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '3':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    elif card11 == '2':
        totalvalue = int(card11)
        ai1cumulative = ai1cumulative + totalvalue
        print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
    #determineing acevalue
    elif card11 == "ace":
        if ai1cumulative < 11:
            totalvalue = 11
            print("The value of " + botname + "'s card is " + str(totalvalue)+ "\n")
            ai1cumulative = ai1cumulative + totalvalue
            time.sleep(2)
            print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
        elif ai1cumulative < 20:
            totalvalue = 1
            print("The value of " + botname + "'s card is " + str(totalvalue)+ "\n")
            ai1cumulative = ai1cumulative + totalvalue
            time.sleep(2)
            print("The total amount of " + botname + "'s hand is " + str(ai1cumulative)+ "\n")
#printing out the card that was drawn varribles taken from card()
def ai1cardvalue():
    card()
    print(botname + "'s card is " + str(card11) + " of " + str(card10)+ "\n")

#calculating the value of the players cards
def playercardsfinalvalue():
#globals in place of return
    global totalvalue

    global cumulative
#determineing face card value
    if card11 == "jack" or card11 == "queen" or card11 == "king":
        totalvalue = 10
        print("The value of this card is " + str(totalvalue)+ "\n")
        cumulative = cumulative + totalvalue
        time.sleep(2)
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '10':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '9':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '8':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '7':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '6':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '5':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '4':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '3':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    elif card11 == '2':
        totalvalue = int(card11)
        cumulative = cumulative + totalvalue
        print("The total amount of your hand is " + str(cumulative)+ "\n")
    #asking usere for what ace will be
    elif card11 == "ace":
        while True:
            acevalue = input("What value would you like the ace to be? 1 or 11?\nEnter here: ")
            if acevalue == "1":
                totalvalue = 1
                print("The value of this card is " + str(totalvalue)+ "\n"+ "\n")
                cumulative = cumulative + totalvalue
                time.sleep(2)
                print("The total amount of your hand is " + str(cumulative)+ "\n")
                break
            elif acevalue == "11":
                totalvalue = 11
                print("The value of this card is " + str(totalvalue)+ "\n")
                cumulative = cumulative + totalvalue
                time.sleep(2)
                print("The total amount of your hand is " + str(cumulative)+ "\n")
                break
            else:
                print("Please enter a valid input you nut")


#printing out what the dealer card is
def dealercardvalue():

    card()

    print("The dealers card is " + str(card11) + " of " + str(card10)+ "\n")
#printing out what the players card is
def playercardvalue():

    card()

    print("Your card is " + str(card11) + " of " + str(card10)+ "\n")
#The betting system
def bet():

    global betvalue

    global wallet

    while True:
        while True:
            betvalue = input("How much are you willing to bet?\nEnter here: ")
            try:
                # try and convert the string input to a number
                age = int(betvalue)
                break
            except ValueError:
                # tell the user its wrong
                print("that is not a number, please enter a number only".format(input=betvalue)+ "\n")
        time.sleep(1)
        #determineing if the user can do this operation or not

        betvalue = int(betvalue)

        if betvalue > wallet:

            print("You don't have this much money, Try again."+ "\n")

        elif betvalue == 0:

            print("You must enter a value to play, try again."+ "\n")
#subtracting bet from wallet
        else:

            wallet = wallet - int(betvalue)

            print("your new wallet value is "+ str(wallet)+ "\n")

            break
def botcount0 ():
    print("This is the start of Game " + str(int(Game) + 1) + "\n")
    time.sleep(1)
    print("Shuffle in proces..." + "\n")
    time.sleep(3)
    playercardvalue()
    time.sleep(2)
    playercardsfinalvalue()
    time.sleep(2)
    dealercardvalue()
    time.sleep(2)
    dealercardsfinalvalue()
    time.sleep(2)
    print("This is your 2nd card..." + "\n")
    time.sleep(2)
    playercardvalue()
    time.sleep(2)
    playercardsfinalvalue()
    time.sleep(2)
    print("The dealers 2nd card is hidden" + "\n")
    time.sleep(2)
#function telling you how much you ended with
def my_function(fname):
  print("You ended the game with " + fname + " Dollars"+ "\n")
#main code
while True:
    wallet = input("What is your wallet for the day?\nEnter Here: ")

    try:
        # try and convert the string input to a number
        age = int(wallet)
        break
    except ValueError:
        # tell the user off
        print("that is not a number, please enter a number only".format(input=wallet)+ "\n")
#asking useres how much money is in originaly
print("Your wallet is " + wallet + " dollars"+ "\n")

wallet = int(wallet)

time.sleep(1)

bet()
#this is the code used for 0 opponets, only dealer
if botcount == "0":
    while True:
#determineing all the players and dealers cards that are delt

            Game = Game + 1
            print("This is the start of Game " + str(Game)+ "\n")
            time.sleep(1)
            print("Shuffle in proces..."+ "\n")
            time.sleep(3)
            playercardvalue()
            time.sleep(2)
            playercardsfinalvalue()
            time.sleep(2)
            dealercardvalue()
            time.sleep(2)
            dealercardsfinalvalue()
            time.sleep(2)
            print("This is your 2nd card..."+ "\n")
            time.sleep(2)
            playercardvalue()
            time.sleep(2)
            playercardsfinalvalue()
            time.sleep(2)
            print("The dealers 2nd card is hidden"+ "\n")
            time.sleep(2)
# asking to hit or stand code
            while True:
                print("The total amount of your hand is " + str(cumulative)+ "\n")
                time.sleep(2)
                hittrick = input("Do you want to hit or stand?\nEnter here:")
#hit code
                if hittrick == "hit":
                    print("The dealer," + str(dealername) + " says another one? Here you go."+ "\n")
                    playercardvalue()
                    time.sleep(2)
                    playercardsfinalvalue()
                    time.sleep(2)
                    #culmitive grabbed from playercardsfinalvalue()
                    if cumulative > 21:
                        time.sleep(2)
                        print("You lost your bet. jokes on you."+ "\n")
                        #win calc
                        loss = loss + 1
                        time.sleep(2)
                        print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                        time.sleep(2)
                        cumulative = 0
                        dealercumulative = 0
                        usedcard.clear()
                        my_function(str(wallet))
                        #this loop is for asking the player if they wanna quit or continue playing
                        while True:
                            quitter = input("Are you done gambling your life away? yes or no?\nEnter here: ")
                            if quitter == "yes":
                                my_function(str(wallet))
                                exit()
                            if quitter == "no":
                                print("Another round starts in 5s\n\n\n\n\n\n\n"+ "\n")
                                time.sleep(5)
                                botcount0()
                                break
                            else:
                                print("Enter valid input.")
                                #stand code
                elif hittrick == "stand":
                    print("you stood"+ "\n")
                    time.sleep(2)
                    dealercardvalue()
                    time.sleep(2)
                    dealercardsfinalvalue()
                    # a possibility of losing
                    if dealercumulative > cumulative:
                        print("You lost your bet. jokes on you."+ "\n")
                        loss = loss + 1
                        print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                        cumulative = 0
                        dealercumulative = 0
                        usedcard.clear()
                        time.sleep(2)
                        my_function(str(wallet))
                        #this loop is for asking the player if they wanna quit or continue playing
                        while True:
                            quitter = input("Are you done gambling your life away? yes or no?\nEnter here: ")
                            if quitter == "yes":
                                my_function(str(wallet))
                                exit()
                            if quitter == "no":
                                print("Another round starts in 5s\n\n\n\n\n\n\n"+ "\n")
                                time.sleep(5)
                                botcount0()
                                break
                            else:
                                print("Enter valid input.")
                        #another possibility of losing
                    elif dealercumulative == cumulative:
                        print("You were even but you lost. House always wins loser."+ "\n")
                        time.sleep(2)
                        loss = loss + 1
                        print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                        time.sleep(2)
                        cumulative = 0
                        dealercumulative = 0
                        time.sleep(2)
                        my_function(str(wallet))
                        time.sleep(2)
                        #this loop is for asking the player if they wanna quit or continue playing
                        usedcard.clear()
                        while True:
                            quitter = input("Are you done gambling your life away? yes or no?\nEnter here: ")
                            if quitter == "yes":
                                my_function(str(wallet))
                                exit()
                            if quitter == "no":
                                print("Another round starts in 5s\n\n\n\n\n\n\n"+ "\n")
                                time.sleep(5)
                                botcount0()
                                break
                            else:
                                print("Enter valid input."+ "\n")

                    # a possibility of wining. determines if it works
                    elif dealercumulative < cumulative:
                        print("You won, congrats. You have won twice your bet."+ "\n")
                        time.sleep(2)
                        wallet = betvalue * 2 + wallet
                        wins = wins + 1
                        print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                        time.sleep(2)
                        cumulative = 0
                        dealercumulative = 0
                        usedcard.clear()
                        time.sleep(2)
                        while True:
                            quitter = input("Are you done gambling your life away? yes or no?\nEnter here: ")
                            if quitter == "yes":
                                my_function(str(wallet))
                                exit()
                            if quitter == "no":
                                print("Another round starts in 5s\n\n\n\n\n\n\n"+ "\n")
                                time.sleep(5)
                                botcount0()
                                break
                            else:
                                print("Enter valid input."+ "\n")
                else:
                    print("please enter a valid input"+ "\n")
                #end of code against 0 bots
#start of code against 1 bot
if botcount == "1":

    while True:
        #determineing all of the cards that are originly delt.
        #game counter
        Game = Game + 1
        print("This is the start of Game " + str(Game)+ "\n")
        time.sleep(2)
        print("Shuffle in proces..."+ "\n")
        time.sleep(2)
        playercardvalue()
        time.sleep(2)
        playercardsfinalvalue()
        time.sleep(2)
        ai1cardvalue()
        time.sleep(2)
        ai1cardsfinalvalue()
        time.sleep(2)
        dealercardvalue()
        time.sleep(2)
        dealercardsfinalvalue()
        time.sleep(2)
        print("This is your 2nd card..."+ "\n")
        time.sleep(2)
        playercardvalue()
        time.sleep(2)
        playercardsfinalvalue()
        time.sleep(1)
        print("This is " + str(botname) + "'s 2nd card"+ "\n")
        ai1cardvalue()
        time.sleep(2)
        ai1cardsfinalvalue()
        time.sleep(2)
        print("The dealers 2nd card is hidden"+ "\n")
        time.sleep(2)
        #this combines the hit and stand code with the win or loss code.
        while True:
            #this loop offers the player the option to stay or hit
            while True:
                #determineing if you wandt to hit or stand. Oncce you stand this code does not run as gamestaeplayer = 1
                if gamestateplayer == 0:
                    print("The total amount of your hand is " + str(cumulative)+ "\n")
                    time.sleep(2)
                    hittrick = input("Do you want to hit or stand?\nEnter here:")
                    #code for the hit
                    if hittrick == "hit":
                        print("The dealer," + str(dealername) + " says another one? Here you go."+ "\n")
                        playercardvalue()
                        time.sleep(2)
                        playercardsfinalvalue()
                        time.sleep(2)
                        #things that can make you lose if you hit
                        if cumulative > 21:
                            print("You lost your bet. You went over 21. jokes on you.\nTime to see the value of your opponents hand"+ "\n")
                            time.sleep(2)
                            gamestateplayer = 1
                            cumulative = 0
                            break
                            # a winning possibility if you hit
                        elif cumulative == 21:
                            print("Your hands value is 21! Time to wait to see the result of your oppositions hand"+ "\n")
                            time.sleep(2)
                            gamestateplayer = 1
                            break
                        else:
                            time.sleep(2)
                            break
                            #code for stand
                    elif hittrick == "stand":
                        gamestateplayer = 1
                        print("You stood, Waiting for the other players to stand or bust."+ "\n")
                        time.sleep(2)
                    else:
                        print("please enter a valid input"+ "\n")
                else:
                    break
                    #determineing the AIs hit or stand
                #this loop decides if the AI hits or stands
            while True:
                #once the AI stands this code will not run
                if gamestateai == 0:
                    #determine if value is 21
                    if ai1cumulative == 21:
                        print("Your enemy got 21. Now waiting for the result of yours and the dealers hand"+ "\n")
                        break
                        #determines wether AI will hit or stand
                    elif ai1cumulative <= 15:
                        print(botname + " decided too hit."+ "\n")
                        time.sleep(2)
                        ai1cardvalue()
                        time.sleep(2)
                        ai1cardsfinalvalue()
                        time.sleep(2)
                        break
                        # a losing possibility for the AI
                    elif ai1cumulative > 21:
                        print("Your opponent lost their bet. They went over 21. Jokes on them."+ "\n")
                        #setting this to 1 causes this code not to run again
                        gamestateai = 1
                        ai1cumulative = 0
                        break
                        # AI stand code
                    elif ai1cumulative > 15:
                        print(botname + " looked at his cards for a long while and decided to stand."+ "\n")
                        time.sleep(1)
                        print("His hand has a value of " + str(ai1cumulative)+ "\n")
                        time.sleep(2)
                        #setting this to 1 causes this code not to run again
                        gamestateai = 1
                        break


                    break
                break

    #determining who is the winner
            if gamestateai == 1 and gamestateplayer == 1:
                time.sleep(1)
                cumulative = ai1cumulative + 1
                print("The dealer reveals his 2nd card."+ "\n")
                time.sleep(2)
                dealercardvalue()
                time.sleep(2)
                dealercardsfinalvalue()
                #what happens if dealer hand is greater than player hand
                if dealercumulative > cumulative:
                    print("You lost your bet. jokes on you."+ "\n")
                    time.sleep(1)
                    print("The dealer had a better hand than you."+ "\n")
                    loss = loss + 1
                    print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                    cumulative = 0
                    dealercumulative = 0
                    gamestateai = 0
                    gamestateplayer = 0
                    usedcard.clear()
                    my_function(str(wallet))
                    print("You are kicked out because you suck."+ "\n")
                    exit()
                    #what happens if dealer and player are equal
                elif dealercumulative == cumulative:
                    print("You were even with the dealer but you lost. House always wins loser."+ "\n")
                    loss = loss + 1
                    print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                    cumulative = 0
                    dealercumulative = 0
                    gamestateai = 0
                    gamestateplayer = 0
                    usedcard.clear()
                    my_function(str(wallet))
                    print("You are kicked out because you suck."+ "\n")
                    exit()
                    #what happens if player hand is greater than dealer hand
                if dealercumulative < cumulative:
                    if ai1cumulative < cumulative:
                        print("You won, congrats. You have won twice your bet."+ "\n")
                        time.sleep(2)
                        print("You hand was greater than " + botname + "'s"+ "\n")
                        wallet = betvalue * 2 + wallet
                        wins = wins + 1
                        print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                        cumulative = 0
                        dealercumulative = 0
                        gamestateai = 0
                        gamestateplayer = 0
                        usedcard.clear()
                        my_function(str(wallet))
                        print("You are kicked out because you suck."+ "\n")
                        exit()
                    #what happens if ai hand is greater than player hand
                elif ai1cumulative > cumulative:
                    print("Your enemy " + botname + " Had a greater hand than you"+ "\n")
                    loss = loss + 1
                    print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                    cumulative = 0
                    dealercumulative = 0
                    gamestateai = 0
                    gamestateplayer = 0
                    usedcard.clear()
                    my_function(str(wallet))
                    print("You are kicked out because you suck."+ "\n")
                    exit()
                    #what happens if player hand is greater than ai hand
                elif ai1cumulative < cumulative:
                    print("You had a greater had than your enemy.")
                    wins = wins + 1
                    print("You have " + str(wins) + " wins and " + str(loss) + " losses"+ "\n")
                    cumulative = 0
                    dealercumulative = 0
                    gamestateai = 0
                    gamestateplayer = 0
                    usedcard.clear()
                    my_function(str(wallet))
                    print("You are kicked out because you suck."+ "\n")
                    exit()
                    #what happens if scores are even
                elif ai1cumulative == cumulative:
                    print("You tied. You don't win ore lose anything"+ "\n")
                    wallet = wallet + betvalue
                    cumulative = 0
                    dealercumulative = 0
                    gamestateai = 0
                    gamestateplayer = 0
                    usedcard.clear()
                    my_function(str(wallet))
                    print("You are kicked out because you suck."+ "\n")
                    exit()

if wallet <= 0:
    print("You went broke you loser. You are kicked out of the casino"+ "\n")
    exit()
