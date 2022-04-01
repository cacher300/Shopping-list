# Define variables
print("Welcome. You will be playing a game today.")
age = input("Enter your real age. Must be over 10 to play: ")
age = int(age)

# imports
import random
import time

# verify age
if age <= 10:
    print("You are too young")
    exit()
# Start the story
else:
    print('''
    You are at a crossroads and there is 2 paths.
    Which will you choose?
    1.Light
    2.Dark
    ''')
    # Define which path you will take
    path = input("Enter here:")
    path = int(path)
    if path == 1:
        print('''
    The light path is too bright for you. You hear gunshots.
    You choOse to go back and choose the dark path.''')
if path == 2 or path == 1:
    print(''' 
    You hear a noise in the bush.
    What do you do?
    1. Turn and fight
    2. Run for your life   
    ''')
    fight = input("Enter choice here: ")
    fight = int(fight)
    # First encounter with hobo
if fight == 2:
    print('''
    You run for your life
    You don't feel like getting into a fight
    you encounter a hobo on the side of the road
    He offers you some magic powder
    Do you accept?''')
    powder = input("1 for yes 2 for no:")
    powder = int(powder)
    # Powder encounter with hobo
    if powder == 2:
        print("You are forced to take the powder. Please wait 2 seconds")
        time.sleep(2)
    if powder == 1 or powder == 2:
        print('''
        You are become extremely high and start to hallucinate
        You wander around very high not knowing what to do
        You see all sorts of monsters and such.
        You wake up laying in the middle of woods on top of a bunch of 
        garbage bags.
        What will you do?
        1. Dig through the trash
        2. Go to the streetlight down the path
        ''')
        # First putin encounter
        highchoice = input("Enter here: ")
        highchoice = int(highchoice)
        if highchoice == 2:
            print('''
            You walk towards the lamp Post
            You see putin standing under the light
            what do you do?
            1. Say hello
            2. Continue walking
            ''')
            greet = input("enter here: ")
            greet = int(greet)
            # Convo with putin
            if greet == 2:
                print("Putin stops you and tells you to come talk")
                time.sleep(1)
            if greet == 1 or greet == 2:
                print('''
                Putin wants to talk to you about what you are doing this fine winter night.
                You say you are on a walk
                Putin asks what your favourite song is. 
                What do you say?
                1. USA Anthem
                2. Russian anthem
                ''')
                anthem = input("Enter here: ")
                anthem = int(anthem)
                if anthem == 1:
                    print('''
                    Wrong answer.
                    The KGB is after you now.
                    You are sent to siberia
                    Do you steal vodka from a store in siberia?
                    1. Yes
                    2. No
                    ''')
                    robbery = input("Enter here: ")
                    robbery = int(robbery)
                    if robbery == 1:
                        print("You are caught by the cops and deported to new zeAland")
                        print("You hitchhike around new zealand for eternity.")
                    if robbery == 2:
                        print('''
                        You die of thirst and cold because you did not have vodka, 
                        which is essential for life in russia''')
                if anthem == 2:
                    print('''
                    Correct answer
                    Putin now asks you what your favourite country is
                    1. Russia
                    2. USA
                    ''')
                    country = input("Enter here: ")
                    country = int(country)
                    if country == 1:
                        print('''
                        Correct answer.
                        You become best friends with Putin.
                        You become Putin's replacement in office when he dies.
                        Congratulations on leading the worlds largest country.
                        Do you make peace with NATO?
                        1. Yes 
                        2. No 
                        ''')
                        warrrr = input("Enter here: ")
                        warrrr = int(warrrr)
                        if warrrr == 1:
                            print('You now peacefully rule russia')
                        else:
                            print("Nato destroys russia and you die. RIP")
                    if country == 2:
                        # Hunger strike code. FIX!!!!!!!
                        print('''
                        Wrong answer. You are sent to gulag.
                        What do you do in gulaug
                        1. Dig a hole
                        2. Go on hunger strike
                        ''')
                        hunger = input("Enter here:")
                        hunger = int(hunger)
                        if hunger == 1:
                            print(" You were awarded for you hardwork. You are released early")
                        else:
                            print("You die from starvation. The guards dont care. RIP")
                            # End of this interaction with putin.
        # Will you pick up a gun
        if highchoice == 1:
            print("while digging through the trash you find a gun. Do you take the gun?")
            print("1. Yes 2. No")
            gun = input("Enter here:")
            gun = int(gun)
            if gun == 2:
                print("You think twice and decide to pick it up")
            if gun == 1 or gun == 2:
                # KGB Encounter
                print('''
                now you walk along the path that you noticed which leads into the woods
                someone starts to shoot at you!
                Its putin and the KGB!
                Do you shoot back.
                1. Yes
                2. No
                ''')
                gunfight = input("Enter Here: ")
                gunfight = int(gunfight)
                # Captured By the KGB
                if gunfight == 2:
                    print('''
                    You have been captured by the KGB.
                    They want to interrogate you on how you discovered their location.
                    What do you say?
                    1. I was sent here by biden to kill him
                    2. I followed a path into the bush
                    ''')
                    question = input("Enter here: ")
                    question = int(question)
                    # Questioning by KGB
                    if question == 1:
                        print('''
                        You shall die for your crimes against the motherland.
                        You will be killed by a firing squad at 1500 hours.
                        will you try to escape?
                        1. Yes
                        2. No
                        ''')
                        escape = input("Enter here:")
                        escape = int(escape)
                        # Escaping KGB
                        if escape == 2:
                            print("You didnt want to escape, but there was a opportunity")
                            print("That was too good to pass up so you escaped")
                        if escape == 1 or escape == 2:
                            print('''
                            You have sucsessfully escaped from the grips of 
                            the russians
                            They have placed a massive bounty of your head of 
                            $100000000000000000000000000000000000000000000000
                            Where do you want to hide?
                            1. Behind a dumpster
                            2. In plain sight
                            ''')
                            hide = input("Enter choice here: ")
                            hide = int(hide)
                            # Hiding
                            if hide == 2:
                                print('''
                                You hid in plain sight but you just stood there
                                you didnt hide.
                                you are dumb, your iq is 0
                                you are caught by the russians. they bring you to the gulag.
                                you take the remaining magic powder you have from the hobo.
                                you feel good.
                                what will you do in gulag.
                                1. Try to escape
                                2. live your life in gulag.
                                ''')
                                gulag = input("Enter here: ")
                                gulag = int(gulag)
                                # Deportation To gulag
                                if gulag == 2:
                                    print('''
                                    You live the rst of your life in gulag.
                                    Putin whishes to meet you while you are in your final years
                                    Do you accept the meeting?
                                    1. Yes
                                    2. no
                                    ''')
                                    putin = input("Enter here: ")
                                    putin = int(putin)
                                    # Meeting with putin
                                    if putin == 2:
                                        print('''
                                        You are ordered to go the meeting.
                                        putin's guards beat you up and then you go to the meeting
                                        ''')
                                        time.sleep(2)
                                    if putin == 1 or putin == 2:
                                        print('''
                                        You see putin and putin stares at you
                                        For an hour. \n Finaly he says why did you want to kill me?
                                        you say i never did, I never wanted to.
                                        and putin says are you telling the truth?
                                        Type a paragraph to putin why you are innocent
                                        ''')
                                        truth = input("Enter here:")
                                        print('''
                                        putin says You are telling the truth
                                        He lets you go to america.
                                        You die at 99 in portland.
                                        Good life you lived.
                                        ''')
                                        # End of meeting with putin
                                # Assasination
                                if gulag == 1:
                                    print('''
                                    You tried to escape. You succeeded.
                                    You gather firearms and are on your way to the kremlin to kill putin.
                                    Do you use a sniper and snipe him or a AK?
                                    1. Sniper
                                    2. AK
                                    ''')
                                    sniper = input("Enter here:")
                                    sniper = int(sniper)
                                    # Capture Putin
                                    if sniper == 2:
                                        print('''
                                        You get a AK and storm the kremlin.
                                        you run through all the guards.
                                        The magic powder makes you invincible.
                                        You capture putin.
                                        The world congratulates you
                                        You are king of the world.
                                        ''')
                                        print('''
                                        KING
                                        ''')
                                        # Snipe putin
                                    if sniper == 1:
                                        print('''
                                        You try to snipe putin. 
                                        You wait in a window 
                                        you have the perfect oppurtunity.
                                        you whiff the shot.
                                        The kgb locate your room and ask you to open the door up
                                        1. Open the door
                                        2. keep it closed
                                        ''')
                                        door = input("Enter here")
                                        if door == 1:
                                            print('''
                                            You are shot after you open the door
                                            RIP you
                                            shouldn't have whiffed.
                                            ''')
                                        else:
                                            print("You are shot through the door")
                                            print("RIP")
                                            # End of KGB Invasion

                            if hide == 1:
                                print('''The russians seached for you for 
                                years but they were unable to locate you
                                You are a free man.
                                What will you do next?
                                1. Go see your mother who you havent seen in years
                                2. Go to the pub
                                ''')
                                pub = input("Enter here: ")
                                pub = int(pub)
                                # Pub choice
                                if pub == 2:
                                    print("You stayed in the pub for the rest of your life")
                                    print('''drowning you sorrows was the worst choice you ever made as your
                                    mother now hates you. 
                                    ''')
                                    # Visit mother choice
                                if pub == 1:
                                    print('''
                                    You went to see your mother
                                    You mother rejoiced when she saw you.
                                    you live with your mother now and play games in her basement.
                                    You live a good life with your mother.
                                    ''')
                # Gunfight battle
                if gunfight == 1:
                    print('''
                    You have killed putin.
                    You also killed all the KGB
                    Now all russian civilians are after you.
                    What do you do?
                    1. run
                    2. stand still
                    ''')
                    run = input("Enter here: ")
                    run = int(run)
                    # Running from KGB
                    if run == 1:
                        print('''
                        You really thought you could get away.
                        Pathetic
                        ''')
                        time.sleep(2)
                        # Sent to gulaug again
                    if run == 1 or run == 2:
                        print("You are sent to gulag and now rot there for years. ")
                        print("Do you accept a final meeting with putin?")
                        print("1 for yes. 2 for no")
                        meeet = input("Enter here: ")
                        print("Putin doesn't care what you think.")
                        print("You are meeting with him")
                        time.sleep(2)
                        print('''
                        You meet with putin. He stares at you for an hour
                        He asks you why you are in gulaug 
                        You say for trying to kill you.
                        He says why.
                        What do you respond with?
                        Type a paragraph below.
                        ''')
                        essay = input("Enter here: ")
                        time.sleep(2)
                        print('''
                        He says you shouldn't have tried to kill me.
                        Because of that You are dead.
                        You are executed.
                        What are your last words?
                        ''')
                        last = input("Enter here: ")
                        last = str(last)
                        print("You say " + str(last) + " ,You proceed to die")
                        # Ending of final meeting with putin


# Fishting goblin. Fight path
elif fight == 1:
    print('''
    You encounter a goblin and are forced to fight.
    What will your attack be?
    punch or kick?
    ''')
    # Punching goblin
    attack = input("Enter here:")
    attack = str(attack)
    if attack == ("punch"):
        print('''
        You got mauled by the beast.
        You are bleeding out and your head 
        is near a used diaper.
        Do you want to continue to live or give up on life?
        1. Continue
        2. Give up and die beside a diaper
        ''')
        # Chooseing to die or not
        deathchoice = input("Enter choice: ")
        deathchoice = int(deathchoice)
        if deathchoice == 1:
            print(''' You continue to live
                You cry out for help
                But instead of getting help 
                the monster hears you and you have to 
                make a decision
                1. Hold your breath so the monster dosent hear you.
                2. Continue breathing
                ''')
            breathe = input("Enter choice here:")
            breathe = int(breathe)
            # Escaping from monster
            if breathe == 2:
                print('''
                    The monster hears you and eats you.
                    You then wake up from the dream, do drugs and die at the age of ''' + str(age))
                print("are you happy with your life")
                happy = input("yes or no: ")
                # Death message
                if happy == ("yes"):
                    print("You shouldnt be. you were a hopeless person")
                else:
                    print("good")
                    # escaping monster
            elif breathe == 1:
                print(''' You escaped the monster.......
                    but at a price.
                    You held your breath for so long that
                    you died from lack of oxygen
                    RIP you. At least you didn't die of drugs
                    will you go th heaven or hell?
                    enter 1 for heaven. 2 for hell
                    ''')
                sin = input("enter choice")
                sin = int(sin)
                if sin == 1:
                    print("You went to heaven")
                else:
                    print("You will burn in hell forever")
        # Continuation of deathcoice

        if deathchoice == 2:
            print('''
                You chose to die but instead of dying
               you wake up from your dream.
                Its late at night, you cant go back to sleep
                so you decide to do somthing.
                1. Do drugs and vape
                2. Do your unfinished homework
                 ''')
            drugs = input("Enter choice: ")
            # Doing drugs or not
            drugs = int(drugs)
            if drugs == 1:
                print('''
                    You have died of drugs alone late at night with poop in you pants.
                    Such a sad existence you have
                    dont do drugs kids
                    The end of your pathetic life
                    ''')
                time.sleep(66666666666666666666666666666666666666666666666666666666666)
                # Code gives avnnoying error when this is not here. This gets rid of it

            # Deciding education
            if drugs == 2:
                print('''You did your work and now you can either go to MIT or clown college.
                    1.MIT
                    2.Clown collage
                    ''')
                education = input("Enter here: ")
                education = int(education)
                # Doing Net worth evaluation
                NetWorth = age * 10000
                # Defineing net worth as a string
                NetWorth = str(NetWorth)
                if education == 1:
                    print("You became CEO of the world. Congrats")
                    print("You now have a net worth of " + NetWorth + " dollars")
                    # Code also breaks here
                    time.sleep(1000000000000000000000000000000000000000000000000000000000000000000000)

                if education == 2:
                    print("You are a world famous clown. Congrats")
                    # End of this paths story
    # Begining of kick attack
    if attack == ("kick"):
        print('''
        YOU KILLED THE BEAST
        You contine to walt down the path.
        you encounter a hobo that wants to gamble.
        you say no but he thretans you if you don't.
        you now say yes.
        ''')
        time.sleep(2)
        ('''
        He says he will roll the die and if the number is 5,10,15 or 20 you win
        the prize for winning is you get his service for the rest of your life
        if you lose you must follow him around forever.
        ''')
        # Rolling the die
        time.sleep(2)
        print(" Your roll begins in 3 seconds")
        # Sleeping code
        time.sleep(3)
        # Defineing random parameters
        randomvariable = random.randint(0, 20)
    # Calculating for a win or loss
    # If this if statment works its a loss
    if int(randomvariable) == 5 or int(randomvariable) == 10 or int(randomvariable) == 15 or int(randomvariable) == 20:
        print('''
        you lost. You are now enslaved to a hobo.
        The hobo says we are going fishing.
        1. Agree and fish
        2. Say no
        ''')
        # Going fishing or not
        fishing = input("Enter here: ")
        fishing = int(fishing)
        if fishing == 2:
            print("You are going fishing anyways")
        if fishing == 1 or fishing == 2:
            print('''You finished fishing. You caught 50 fishes.
            Now you go hunting.
            1. Agree and hunt
            2. firmly say no.
            ''')
            # Hunting or not
            hunting = input("Enter here: ")
            hunting = int(hunting)
            if hunting == 2:
                print("You are hunting anyways")
            if hunting == 1 or hunting == 2:
                print("You got 10 deer")
                time.sleep(2)
                # Predicting time of death
                print('''
                You do whatever the hobo tells you for the rest of your life.
                Such a painful existance.
                You die at age 36 at 3 AM.
                ''')

    # What happens if you win the die roll
    else:
        print('''YOU WON. You rolled: ''' + str(randomvariable) + '''
        The game was rigged against you but you managed to win.
        now this hobo must follow you around and be your servant
        ''')
        time.sleep(3)
        print('''Now that the hobo is under your control, what do you want to do with him
        1. continue walking down the dark and spooky path
        2. wander into the woods
        ''')
        # Wandering in woods with a hobo
        hobodirections = input("Enter here: ")
        hobodirections = int(hobodirections)
        if hobodirections == 2:
            print(''' You wanderd in the woods for 5 days and found nothing 
            other than putins nuclear bunker, ancient gold
            Bill cosbys RV, and hitlers retirement house. 
            You return to the dark and spooky path
            ''')
            time.sleep(4)
            # finding which way to go with hobo
        if hobodirections == 1 or hobodirections == 2:
            print('''
            You come across a old wizard sitting down on a bench
            He tells you and the hobo to sit down in front of him
            You obey his instructions
            he tells you he knows everything about you.
            What do you respond with?
            ''')
            response = input("Enter anything here")
            print("He says,I know your age. you are " + str(age) + " years old.")
            print(''' I know many more things about you, and i can do many
            things to you you and the hobo are both mine now. Or I will end you
            1. Fight the wizard
            2. submit to the wizard
            ''')
            # Battleing wizzard
            wizardbattle = input("Enter choice here:")
            wizardbattle = int(wizardbattle)
            if wizardbattle == 1:
                print('''Fight is initiated. what do you want to do?
                1. Rush the wizard with the hobo
                2. Take the magic powder the hobo offers you and then rush the wizard
                ''')
                # Choosing how to battle wizard
                wizfightchoice = input("Enter Choice here: ")
                wizfightchoice = int(wizfightchoice)
                if wizfightchoice == 2:
                    print('''
                    The magic powder worked!!!
                    the magic powder allowed you to go through the wiazrds force fields.
                    You are now feeling very weird but you have won the war.
                    What do you do now?
                    1. Go to the pub and celebrate with the hobo
                    2. Search the wizards pockets
                    ''')
                    # Celebrating
                    celebration = input("enter here: ")
                    celebration = int(celebration)
                    # Null statments
                    # if celebration == 2:
                    # print(" Death to you")
                    if celebration == 1:
                        print("You get extremly drunk with the hobo. You have the time of your life.")
                        print("You buy the bar from the owner because you like it so much")
                        print('''
                        Do you force the hobo to be your slave or will you pay him?
                        1. for slave
                        2. for paid
                        ''')
                        # Deciding on slavery
                        slave = input("Enter here: ")
                        slave = int(slave)
                        if slave == 1:
                            print(''' 
                            The cops have been alerted and you are arrested for slavery.
                            You are brutally assaulted by the cops for keeping slaves.
                            Do you plead guilty or innocent to the court.
                            1. Guilty
                            2. Innocent
                            ''')
                            pleadslave = input("Enter here: ")
                            pleadslave = int(pleadslave)
                            if pleadslave == 1:
                                print('''
                                You are sent to jail for 100s of years. 
                                The magic powder made you immortal so you existed in jail forever.
                                Do you start a gang or no
                                1. yes, 2. no
                                ''')
                                # Gang creation
                                gang4life = input("Enter here:")
                                gang4life = int(gang4life)
                                if gang4life == 1:
                                    print(" You created a gang with more influence than the mafia, congrats.")
                                else:
                                    print("You are a loser in solidary confinement. Take the L my guy")
                                    # Slave decision 2.0
                            if pleadslave == 2:
                                print(" You received a light sentence of 1 million years.")
                                print("You joined the Mob. The end")
                        if slave == 2:
                            print('''
                            You pay the hobo a healthy wage and you become rich.
                            You open up 100s more bars but then you lose you wife maria.
                            How do you mourn?
                            1. drown your sorrows in alcohol
                            2. Get remarried quickly
                            ''')
                            # Marrige choice
                            marrige = input("Enter choice here: ")
                            marrige = int(marrige)
                            if marrige == 1:
                                print("You have died of alchohol poisining. RIP you")
                            else:
                                print("You got re married to the hobos Ex wife ")
                                print("Do you tell him")
                                print("1. Yes 2. No")
                                sunnydays = input("Enter here: ")
                                # Telling hobo or not
                                sunnydas = int(sunnydays)
                                if sunnydays == 1:
                                    print("THe hobo hates you and procedes to murder you."
                                          "RIP")
                                else:
                                    print("The hobo never found out and died at 44. You lived happily married forever")
                    # Alternitive celebration
                    if celebration == 2:
                        print(''' 
                        You find a crown and alot of diamonds in his pockets.
                        What do you do with this new found richness?
                        1. give some to the hobo
                        2. keep it all to yourself.''')
                        # Fighting wizzard agai
                if wizfightchoice == 1:
                    print("You attack the wizard but he uses his force field to push you back and repel you.")
                    time.sleep(2)
                    print("You are blown back into the real world and you wake up in a dumpster")
                    time.sleep(2)
                    print('''
                    The dumpster is on fire.
                    You see the hobo is also in the dumpster but he is not moving.
                    Do you rescue the hobo or save yourself?
                    1. Rescue hobo
                    2. Save yourself
                    ''')
                    # Save hobo or not
                    hobosave = input("Enter choice here:")
                    hobosave = int(hobosave)
                    if hobosave == 1:
                        print("You got stuck while saving the hobo and now you are both burning")
                        print(''' 
                        Luckily, someone starts throwing water on the dumpster and you are both saved.
                        You are than transported to the hospital where you and the hobo will recover.
                        A doctor comes in and asks you if you have already received your medication. (You have)
                        Do you lie to get more medication or tell the truth?
                        1. Lie
                        2. Truth
                        ''')
                        # Do drugs or not
                        medication = input("Enter choice here: ")
                        medication = int(medication)
                        if medication == 1:
                            print("You are now addicted to morphine.")
                            print('''
                        When you get out of the hospital you live on the street
                        and do drugs for a living.
                        You eventually drown after you rolled into a river while sleeping
                        you shouldnt have saved the hobo
                            ''')
                        else:
                            print('''
                            You got out of the hospital, got a job in IT and worked at a school for the rest 
                            of your life
                            Congrats
                            Do you play video games during work or help students?
                            1. games
                            2. work
                            ''')
                            # Slack off on job or nah
                            videogames = input("Enter here: ")
                            videogames = int(videogames)
                            if videogames == 1:
                                print("good choice")
                            else:
                                print("go play game dofus")
                                # Not saving the hobo outcome
                    if hobosave == 2:
                        print('''
                        You chose not to rescue the hobo.
                        someone calls the cops on you for suspected murder
                        you are arrested.
                        your trial is scheduled and its time to see what will happen to you.
                        Do you plead innocent or guilty. 
                        1. innocent
                        2. Guilty
                        ''')
                        # Pleading innocent or guilty

                        plead = input("enter choice here: ")
                        plead = int(plead)
                        if plead == 1:
                            print("you are found guilty.")
                            print(''' You are sentanced to 69 years in prison
                            You slowly rot in prision as you are unpopular. The end of your life
                            (You also dropped some body cleansing chemichal but you were able to pick it up in time)

                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::::::::::::::::::::::::::
                            ::::::::::::::::::::::::::::


                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::
                            ::::::::::::::::::::::::::::::::
                            ::::::::::::::::::::::::::::::::
                            ''')
                        if plead == 2:
                            print("You are found guilty and are sent to prison for 20 years")
                            print("You become a gang leader and continue gang activities after prison")
                            print("You have a good life")
                            # End of story


