import os
import random
import time

import actors
from actors import Companion as Companion
from actors import CompanionEnum as CompEnum
from actors import Hero as Hero
from actors import NPC as NPC
from helper import GameColors as fcolor
from helper import getClsCommand as cls
from helper import showBanner as showBanner
from helper import showEndBanner as showEndBanner
from helper import showHealthBar as showHealthBar
from helper import showIntro as showIntro


# *****************************************************
# Start a game with a new toon
# This is destroy old saved data
# *****************************************************
def startNewGame():
    showBanner()
    hero = Hero("Unknown")
    while True:
        name = input('What is your name: ')
        if len(name) < 1:
            print("Please enter you hero name")
        else:
            break

    hero.name = name
    showBanner()
    actors.showHero()
    print("\tGreetings", name + ", prepare youeself for this adventure in Kubernetes realm,\n"
          "\tan open-source container-orchestration system for automating application deployment, scaling, and management")
    pause()

    while True:
        print('Pick your companion: ')
        print('[1]', CompEnum.PHIPPY.value)
        print('[2]', CompEnum.GOLDIE.value)
        print('[3]', CompEnum.ZEE.value)
        print('[4]', CompEnum.CAPT_KUBE.value)

        avatar = input('')
        os.system(cls())
        if avatar == '1':
            actors.showPhippy()
            hero.companion = Companion(CompEnum.PHIPPY.value)
            break
        elif avatar == '2':
            actors.showGoldie()
            hero.companion = Companion(CompEnum.GOLDIE.value)
            break
        elif avatar == '3':
            actors.showZee()
            hero.companion = Companion(CompEnum.ZEE.value)
            break
        elif avatar == '4':
            actors.showCaptKube()
            hero.companion = Companion(CompEnum.CAPT_KUBE.value)
            break
        else:
            print("Please select a companion")

    showHeroInto(hero)
    pause()
    return hero

# *****************************************************
# Display Hero stats along with companion stats
# *****************************************************
def showHeroInto(hero):
    print('Your name is', hero.name, 'and you chose', hero.companion.name, 'as your companion. Lets us begin!')
    hero.showHeroStats()
    actors.saveHero(hero)

# *****************************************************
# Begin the adventure
# *****************************************************
def enterRealm(hero):
    distance = 10  # in nautical_league
    nautical_mile = 3.45234
    # only allow 10 iterations before reaching destination
    for step in range(distance):
        showBanner()
        showHealthBar(hero)
        print()
        input(hero.name + ", hit the Enter Key to move forward: ")
        eventOccurred = False
        print("You are moving", step * nautical_mile, "nautical mile forward with", hero.companion.name, " ", end='')
        #  increase the chance of something happening
        #  using 4 as in 1 nautical mile rounded up.  Each mile may encouter a monster or find items
        #  this is to increase the frequeny of events
        for mile in range(4):
            ev = False
            print('░', end='')
            time.sleep(.1)
            #  increase the chance of something happening
            #  looping to increase of a chance event
            for y in range(2):
                ev = checkEvent(hero, step, distance)
                if ev:
                    break

            if False is eventOccurred and ev:
                eventOccurred = ev

        if not eventOccurred:
            print("\nNothing happened, you did not encounter anything out of the ordinary")
            pause()
        if hero.hp < 30:
            print("\nYou are growing weary and tired.  Must find resources soon")
            time.sleep(.1)
            if hero.hp < 1:
                print("\nYou are out of energy and fainted")
                pause()
                checkEndGame(hero)
                return
            pause()

        # use up some of hero's health on every turn.
        # if no additional resource are found, it is posible for hero to die before reaching destination
        hero.decHealth(8)
        print()
    pause()
    showBanner()

    checkEndGame(hero)

# *****************************************************
# This checks to see if a random event was encountered
# *****************************************************
def checkEvent(hero, step, distance):
    # check if the steps trigger an event
    npc = NPC()
    raiseEnv = random.randint(1, int(distance))
    if step == raiseEnv:
        # decide which event to do
        print("debug: monster frequency level: ", monster_frequency)
        ev = random.randint(1, (3 + monster_frequency*2))
        if ev == 1:
            respack = actors.getResource(random.randint(1, 3))  # find one of 3, health, food, water
            print("\nYou found a resource pack and started opening it...")
            time.sleep(1)
            print("...inside you found", respack.name + ". You consumed its content to add", respack.hp, "to your HP. You feel refreshed")
            hero.addHealth(respack.hp)
            hero.addReource(respack.name)
            pause()
        elif ev == 2:
            trink = actors.getTrinket(random.randint(1, 6))  # find one of six trinkets
            print("\nYou found a trinket:", trink + ". You picked it and put it in your bag")
            hero.addTrinket(trink)
            pause()
        elif ev >= 3:  # giving monsters more chances
            print()
            monster = npc.deployMonster()
            actors.getRandomEntrance(monster)
            os.system(cls())
            hero.addEnemies(monster.name)
            doBattle(hero, monster, step)

        actors.saveHero(hero)
        return True

    return False

# *****************************************************
# Batlle Sequence whichs give two turns to each actor
# *****************************************************
def doBattle(hero, monster, step):
    heroIntro = False
    monsterIntro = False
    nautical_league = 3.45234
    print()
    actors.showMonster(monster.name)
    print(fcolor.YELLOW + "\t\t<<you encounterd a monster at", (step * nautical_league), "nautical miles>>" + fcolor.DEFAULT, "\n")
    pause()
    for x in range(4):
        # don't enter battle if either actors have no HP
        if hero.hp < 1:
            print("The battle with" + monster.name, "was too much. You are dead.")
            pause()
            break
        if monster.hp < 0:
            print("You landed a critcal blow on", monster.name, "Its dead!")
            pause()
            break

        showHealthBar(hero)
        showHealthBar(monster)
        print()
        if (x % 2) == 0:
            #  Only do intro once
            if not heroIntro:
                print(actors.getRandomEntrance(monster), "\nYou launched your first attack with", hero.companion.name)
                heroIntro = True
            else:
                print("You attacked again with", hero.companion.name)

            cur = monster.hp
            monster.hp = monster.hp - ((hero.attackPower + hero.companion.pwr) - monster.doge)   # reduce hero attack power by monster dodge
            if monster.hp > 0:
                if cur == monster.hp:
                    print("Your attack missed")
                else:
                    print("Your attack did some damage but the monster still live")

        else:
            #  Only do intro once
            if not monsterIntro:
                print(actors.getRandomAttackIntro(monster), "\nand attacks you with its", monster.attack)
                monsterIntro = True
            else:
                print(monster.name, "throws", monster.attack)

            cur = hero.hp
            hero.decHealth(monster.attackPower - hero.companion.defense)  # reduce monster attack power by hero companion defense
            if hero.hp > 0:
                if cur == hero.hp:
                    print(monster.name + "\'s attack missed you by a hair")
                else:
                    print(monster.name + "'s attack landed and you took some damage but you are still alive")
        pause()

    print()
    showHealthBar(hero)
    showHealthBar(monster)
    if hero.hp > 0 and monster.hp > 0:
        print("\nThe battle is over")
        print(monster.name, "retreated. You won that round")

    pause()


# *****************************************************
# Check to see if the Hero Won or Lost
# *****************************************************
def checkEndGame(hero):
    if hero.hp > 0:
        actors.showTrophy()
        print("Congratulations, you made it!  You successfully delivered and implemented a kubernetes cluster")
    else:
        actors.showGrave()
        print("You FAILED!  The kingdom of the Internets will now forever be doomed.")

    hero.showHeroStats()
    hero.summary()
    actors.saveHero(hero)
    pause()

# *****************************************************
# Pause gameplay
# *****************************************************
def pause():
    return input(fcolor.YELLOW + '\nHit enter to continue' + fcolor.DEFAULT)

# *****************************************************
# Checks previous game data
# *****************************************************
def welcomeBack(hero):
    print()
    actors.showCompanion(hero.companion.name)
    print(
        "\tWelcome back", hero.name, "\n "
        "\tOutcome of your prevous adventure:\n")
    hero.summary()
    return input("Would you like to start a new adventure using the same charater and companion? (Y/N): ")

showIntro()
pause()

# *****************************************************
# MAIN LOOP
# *****************************************************
monster_frequency = 0
while True:
    showBanner()
    print('[1] Start New Game')
    print('[2] Show Previous Outcome')
    print('[3] Options')
    print('[4] Exit')
    theHero = actors.loadHero()
    heroname = theHero.name
    companion = theHero.companion
    if heroname.upper() != "UNKNOWN":
        print("Welcome back", heroname, "and", companion.name)

    print()
    choice = input('Make a your selection: ')
    if choice == '1':
        theHero = startNewGame()
        enterRealm(theHero)
    elif choice == '2':
        ans = 'N'
        if heroname.upper() != "UNKNOWN":
            ans = welcomeBack(theHero)
        else:
            print('No previous adventure data found')
            pause()

        if ans.upper() == 'Y':
            theHero.hp = 100
            actors.saveHero(theHero)
            enterRealm(theHero)

    # increase frequency of moneters
    elif choice == '3':
        f = input("Enter monster frequency(0-4): ")
        if not f.isdigit():
            monster_frequency = 1
        else:
            if int(f) > 4:
                monster_frequency = 4
            else:
                monster_frequency = int(f)

    elif choice == '4':
        showEndBanner()
        if heroname.upper() != "UNKNOWN":
            theHero.summary()

        exit()

