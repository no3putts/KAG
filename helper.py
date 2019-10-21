import sys
import os
import random

def getClsCommand():
    platforms = {
        'linux1': 'clear',
        'linux2': 'clear',
        'darwin': 'clear',
        'win32': 'cls'
    }
    if sys.platform not in platforms:
        return 'clear'

    return platforms[sys.platform]

def showHealthBar(actor):

    health = actor.hp
    length = actor.baseHP - health
    print(actor.name + '\'s HP:[', end='')
    for i in range(health):
        print(GameColors.GREEN + '█' + GameColors.DEFAULT, end='')
    for x in range(length):
        print(GameColors.RED + '█' + GameColors.DEFAULT, end='')
    print(']')

def rollDie():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def showIntro():
    print('''
        A long time ago, in a land far far away, in the kingdom of the Internet, chaos abounds
        Demand for services was growing exponetially as the population of consumers grow
        demanding 99.9% uptime. People chanting WE WANT IT NOW, WE WANT IT FAST
        Their factories can't keep up with the demand. Processes are overloading. Resources are drained 
        causing factories to shut down.  Consumers are starving and threating to go elsewhere.
        The troubled King consulted the mighty kingdom of Google for advice. The emperor of Google
        agreed to help the King of the Internet kingdom and ask for his mightiest Hero to deliver
        to the kingdom of the Internet Google's highly scalable and resillient factory, the Kubernetes.
     ''')
    showHelm()
    print('''
        The King have choosen you to deliver a solution to the kingdom of the Internet.
        You have been tasked to replace their aging and failing factories with something
        that will Scale as the Demand grows.  The kingdom cannot afford to starve consumers. 
        You Goal is to seek the help of the might Google, travel through the rough and perilous
        jungle of the Internet Highway and deliver the Kubernetes to this kingdom.

        Kubernetes can speed up the development process by making easy, automated deployments, 
        updates (rolling-update) and by managing apps and services with almost zero downtime. 
        Kubernetes is originally developed by Google, it is open-sourced since its launch and 
        managed by a very large community of contributors.

        Good luck Hero, choose your companion wisely that will help you in your journey
        and prepare to enter the KAG. Beware hero, the only direction is forward.....
        
        (note: Characters taken from Phippy and Friends. A story about kubernetes https://www.cncf.io/phippy)
    ''')

def showEndBanner():
    print(GameColors.RED + '''
            THANK YOU FOR PLAYING THE
            
             ██ ▄█▀▄▄▄        ▄████ 
             ██▄█▒▒████▄     ██▒ ▀█▒
            ▓███▄░▒██  ▀█▄  ▒██░▄▄▄░
            ▓██ █▄░██▄▄▄▄██ ░▓█  ██▓
            ▒██▒ █▄▓█   ▓██▒░▒▓███▀▒
            ▒ ▒▒ ▓▒▒▒   ▓▒█░ ░▒   ▒ 
            ░ ░▒ ▒░ ▒   ▒▒ ░  ░   ░ 
            ░ ░░ ░  ░   ▒   ░ ░   ░ 
            ░  ░        ░  ░      ░ 
    ''' + GameColors.DEFAULT)

def showBanner():
    os.system(getClsCommand())
    print(GameColors.RED + "\t**********************************************************************")
    print("\t***********************   Welcome to the KAG   ***********************")
    print("\t********************   Kubernetes Adventure Game  *********************")
    print("\t**********************************************************************")
    print('''
     ██ ▄█▀ █    ██  ▄▄▄▄   ▓█████  ██▀███   ███▄    █ ▓█████▄▄▄█████▓▓█████   ██████ 
     ██▄█▒  ██  ▓██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓█   ▀ ▒██    ▒ 
    ▓███▄░ ▓██  ▒██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒███   ░ ▓██▄   
    ▓██ █▄ ▓▓█  ░██░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒
    ▒██▒ █▄▒▒█████▓ ░▓█  ▀█▓░▒████▒░██▓ ▒██▒▒██░   ▓██░░▒████▒ ▒██▒ ░ ░▒████▒▒██████▒▒
    ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░
    ░ ░▒ ▒░░░▒░ ░ ░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░░ ░░   ░ ▒░ ░ ░  ░   ░     ░ ░  ░░ ░▒  ░ ░
    ░ ░░ ░  ░░░ ░ ░  ░    ░    ░     ░░   ░    ░   ░ ░    ░    ░         ░   ░  ░  ░  
    ░  ░      ░      ░         ░  ░   ░              ░    ░  ░           ░  ░      ░  
                          ░                                                           
     ▄▄▄      ▓█████▄  ██▒   █▓▓█████  ███▄    █ ▄▄▄█████▓ █    ██  ██▀███  ▓█████    
    ▒████▄    ▒██▀ ██▌▓██░   █▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▓█   ▀    
    ▒██  ▀█▄  ░██   █▌ ▓██  █▒░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒███      
    ░██▄▄▄▄██ ░▓█▄   ▌  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄    
     ▓█   ▓██▒░▒████▓    ▒▀█░  ░▒████▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒░▒████▒   
     ▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░   
      ▒   ▒▒ ░ ░ ▒  ▒    ░ ░░   ░ ░  ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░   
      ░   ▒    ░ ░  ░      ░░     ░      ░   ░ ░   ░       ░░░ ░ ░   ░░   ░    ░      
          ░  ░   ░          ░     ░  ░         ░             ░        ░        ░  ░   
               ░           ░                                                          
                          ▄████  ▄▄▄       ███▄ ▄███▓▓█████                                               
                         ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀                                               
                        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███                                                 
                        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄                                               
                        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒                                              
                         ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░                                              
                          ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░                                              
                        ░ ░   ░   ░   ▒   ░      ░      ░                                                 
                              ░       ░  ░       ░      ░  ░                                              
    ''' + GameColors.DEFAULT)

def showHelm():
    print(GameColors.BLUE + '''                                                                                                       
                              (((((((((((((((((((((((((((((           
                           ((((((((((((((((( (((((((((((((((((      
                         ((((((((((((((((((( (((((((((((((((((((     
                        (((((((((((((((.         ((((((((((((((((    
                        ((((((   (((      (   (      (((   ((((((    
                       ((((((((((     (((((   (((((     ((((((((((   
                       ((((((((((      ((((   ((((      ((((((((((   
                      ((((((((((   ((               ((   ((((((((((  
                      (((((((((*  (((((           (((((  ((((((((((  
                     ((((((((((   ((((     (((     ((((   (((((((((( 
                     ((((((((((.            ,            ,(((((((((( 
                     ((((((        ((((((       ((((((        ((((((
                     ((((((((((((   ((((   (((   ((((   (((((((((((
                      ((((((((((((   .(   (((((   (.   ((((((((((((  
                       (((((((((((((     (((((((     (((((((((((((   
                         (((((((((((((             (((((((((((((     
                          (((((((((((  (((((((((((  ((((((((((*      
                            ((((((((  (((((((((((((  ((((((((        
                              (((((((((((((((((((((((((((((          
    ''' + GameColors.DEFAULT)


class GameColors:

    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    LIGHTBLUE = '\033[36m'
    DEFAULT = '\033[0m'  # reset color back
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    BLACK = "\033[30m"

class ActorType:

    HERO = 1
    ENEMY = 2
    TRINKET = 3
    RESOURCE = 4
