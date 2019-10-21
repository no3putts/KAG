from helper import GameColors as fcolor
import helper
import pickle
import os
import random
from enum import Enum

class Hero:
    def __init__(self, name):
        self.name = name
        self.trinkets = list()
        self.resources = list()
        self.enemies = list()
        self.companion = Companion("Unknown")
        self.hp = 100
        self.baseHP = 100
        self.attackPower = 20

    def decHealth(self, amt):
        self.hp -= amt

    # when actor finds health resource, increase
    def addHealth(self, amt):
        self.hp += amt

    def addTrinket(self, t):
        self.trinkets.append(t)

    def addReource(self, r):
        self.resources.append(r)

    def setCompanion(self, c):
        self.companion = c

    def addEnemies(self, e):
        self.enemies.append(e)

    def showHeroStats(self):
        print("*** Your stats ***")
        print("HP:", self.hp)
        print("Attack Pwr:", self.attackPower)
        print("Companion HP:", self. companion.hp)
        print("Companion Attack Pwr:", self.companion.pwr)
        print("Companion Defense:", self.companion.pwr)

    def summary(self):
        print("Name: ", self.name)
        print("Companion: ", self.companion.name)
        if self.hp < 1:
            print("You lost in this adventure")
        else:
            print("You won in this adventure.  Great Job!!!")
        helper.showHealthBar(self)
        print("Trinkets Found: ")
        print("\t", self.trinkets)
        print("Monsters Fought: ")
        print("\t", self.enemies)
        print("Resources Found: ")
        print("\t", self.resources)

# companions provide defense for hero
class Companion:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(5, 30)
        self.pwr = random.randint(5, 15)
        self.defense = random.randint(1, 25)

class Resource:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(10, 40)

class Monster:
    def __init__(self, name, hp, atk, greet):
        self.name = name
        self.hp = hp
        self.baseHP = hp
        self.attack = atk
        self.greeting = greet
        self.attackPower = random.randint(10, 50)
        self.doge = random.randint(5, 30)

class NPC:
    def __init__(self):
        self.monsters = createEnemies()

    def deployMonster(self):
        # make sure monster still has enough HP to fight
        while True:
            m = self.monsters[random.randint(0, 4)]
            if m.hp > 0:
                return m


class CompanionEnum(Enum):
    PHIPPY = "Phippy"
    GOLDIE = "Goldie"
    ZEE = "Zee"
    CAPT_KUBE = "Captain Kube"

class MonsterEnum(Enum):
    CORE_DUMPER = "CoreDumper"
    NULL_POINTERMINATOR = "NullPointerminator"
    DIVIDE_BY_ZERO = "DivideByZeroExceptionator"
    OUT_OF_MEMORYZER = "OutOfMemoryzer"
    ILLEGAL_ARG = "IllegalArgunentator"


def createEnemies():
    enemies = list()
    e = Monster(MonsterEnum.CORE_DUMPER.value, random.randint(10, 60), "a Power Dump", "Prepare to get dumped on!!!!")
    enemies.append(e)
    e = Monster(MonsterEnum.NULL_POINTERMINATOR.value, random.randint(10, 50), "a Nullifiery Projectile", "I am going to Nullify you!!!!")
    enemies.append(e)
    e = Monster(MonsterEnum.DIVIDE_BY_ZERO.value, random.randint(20, 70), "a Divided by Zero fiery ball", "Here comes a Zero suckerazor!!!!")
    enemies.append(e)
    e = Monster(MonsterEnum.OUT_OF_MEMORYZER.value, random.randint(20, 70), "Infinite Looper", "I am Going to suck your brain dry!!!!")
    enemies.append(e)
    e = Monster(MonsterEnum.ILLEGAL_ARG.value, random.randint(10, 60), "an Invalid Argument Parameter", "I will argue you to death!!!!")
    enemies.append(e)

    return enemies

def getRandomEntrance(monster):
    ind = random.randint(1, 3)
    ent = {
        "1": "There is rustling behind the bush and all of the sudden " + monster.name + " jumps out and yells, " + monster.greeting,
        "2": "You hear someone or something has been following you and out of nowhere you hear a faint hoarse voice saying: I am " + monster.name + ", " + monster.greeting,
        "3": "Through the trees ahead, you noticed eyes staring at you.  With in a split second, " + monster.name + " charges at you while chanting " + monster.greeting + " repeatedly, ",
    }
    return ent.get(str(ind))

def getRandomAttackIntro(monster):
    ind = random.randint(1, 3)
    ent = {
        "1": "Without warning, " + monster.name + " jumps out and yells, " + monster.greeting,
        "2": "With a faint hoarse voice chanting: I am " + monster.name + ", " + monster.greeting,
        "3": "With in a split second, " + monster.name + " charges at you while yelling: " + monster.greeting + "!!!",
    }
    return ent.get(str(ind))


def getTrinket(ind):
    trinket = {
        "1": "100,000Gi Ram Memory",
        "2": "AMD EPYC CPU",
        "3": "100 PB SSD",
        "4": "Box of Crayons",
        "5": "Cray Supercomputer",
        "6": "Red Stapler"
    }
    return trinket.get(str(ind))

def getResource(ind):
    res = {
        "1": Resource("Health"),
        "2": Resource("Food"),
        "3": Resource("Water")
    }
    return res.get(str(ind))

def saveHero(h):
    filename = 'hero.dat'
    outfile = open(filename, 'wb')
    pickle.dump(h, outfile)
    outfile.close()

def loadHero():
    filename = 'hero.dat'
    if not os.path.exists(filename):
        open(filename, 'w+')

    infile = open(filename, 'rb')
    try:
        h = pickle.load(infile)
    except EOFError:
        h = Hero("Unknown")
    finally:
        infile.close()
    return h

def showCompanion(comp):
    if comp.upper() == CompanionEnum.PHIPPY.value:
        showPhippy()
    if comp.upper() == CompanionEnum.GOLDIE.value:
        showGoldie()
    if comp.upper() == CompanionEnum.ZEE.value:
        showZee()
    if comp.upper() == CompanionEnum.CAPT_KUBE.value:
        showCaptKube()

def showMonster(name):
    if name == MonsterEnum.CORE_DUMPER.value:
        showCoreDumper()
    if name == MonsterEnum.DIVIDE_BY_ZERO.value:
        showDivideByZero()
    if name == MonsterEnum.ILLEGAL_ARG.value:
        showIllegalArgumentator()
    if name == MonsterEnum.NULL_POINTERMINATOR.value:
        showNullPointerminator()
    if name == MonsterEnum.OUT_OF_MEMORYZER.value:
        showOOM()

def showPhippy():
    print(fcolor.YELLOW + '''                                                                                                                                                                                      
                      *###     /###                    
                 ,,,,*/#(*.,,,*####  **                
                 ,,,*,/#(,,,,##,,,,,,*,*,              
                 .,,,,* /,,,,* ,,,,,/,,,               
                   ,,,&/ ,,,,&( ,,,,*,,                
                  .,,,,/,,,,,,*,,,,,,                  
                  ,,,,/,,,*,,,,,,,,,,                  
                 ,,/,,,,,,*,,/,,,,,,,                  
                 ,*,,,,,,,,,,,,,,,,,,                  
                  (,,,,,,,/(,,*,,,,,,                  
                   ,,,,(/**/,,,,,,*,                   
                     /,,/,**,,,,,,,*                   
                       ,,,,,,,,,,,,/                   
                      .,,,,,,,,,,*(/                   
                      .*##,,,,,,####                   
                      /####,,,,,####                   
                      (###,,,,/#####.                  
                      /###,,,,,####,*                  
                      ####,,,,,,,,,,,                  
                     .,,,,(####(,,,,,*                 
                     *,,,,#######,,,,,                 
                     ,,,,,#######,,,,,,,,,,,,,         
                     ,,,,,,,,,,,,,,,,,,,,,######*      
                    ,,,,#,,,,,,,###,,,,,,,,,*#####     
                    /,,(####,,,,(##,,,,,,,,,,,*##(,*   
                    *,,,####*,,,,,,,,,####,,,,,,,*,*,* 
                    .,,,,,,,,,,*###,,#####,,,,,#####/,/
                     ,,,#/,,,,####*,,####,,,,#######*##
                     (,####*,,/###,,,,,,,*,,,(###/*#*  
                     .,,,(##(,,,,,,,,,,,,,,,(,,,,,,,*  
                      ,,,,,,,,,,,,,,,,,,,**##**/,##**  
                      *,,,,,,*(*,,,,,,,,,//(*,,,,,,,,  
                       ,,,,,,,,,,,,,,,,,,,,*,,,,,,,,   
                       /,,,,,,* *,,,,,,,*   /,,,,,,*   
                                 /*****.                                 
        '''
          + fcolor.DEFAULT)

def showHero():
    print(fcolor.BLUE + '''                                                
                           *(%###%/,                             
                          /*#(*##%##%                            
                         @(@#/## @(%#&                           
                         *(#(##./////@ ..%%                      
                        *(###&.//% ..@#&&//@,                    
                    @  .((#(%*@(/,&&.&&&&&,&*&@                  
                    *#(/((#%/, (&@&@&.,&,&,                  
                        #@((#,./@(////((///#(                  
                            #///.#/,%# .%@.@@*                   
                           ,%////@/..(....#,(                    
                              #/@@/..,../,,*#                    
                                *@&@&&&@&.                       
                           %///.##///.&///,                      
                         //  .,/.%/...&...//                     
                       %(%,@..,/#%/....... /#                    
                    @((@%%###,(@#//....,...(/                    
                  (,#%%%%@#%###/(@(/,.,#,,.#@/                
                  (####%(#,##(#/#@#(//(@((%%##*        
                  (#######@######@###/(*./%%%##%                 
                  ((###########@%%%@(%(&@ &%%(*,*              
                  /##############&/.&(((((./ &/**/%@             
                  &@###########(,%..******@.(  (/@/.&            
                   (@#####//(##,%/.#***#***/%     .,*...         
                    *(&%%##(@,@(((**/#((*****       *,(  &       
                       @(@,%(((/***( @((*****        @,,#..*     
                            @*,/,%(   @(****%/.       ,,,,(..%   
                            /%.,,,.    &(((,*,/         ,,,,*    
                           %%/#/(@     #(//(*/%           .@/.*  
                          @/..../@     %////.                    
                          #....*@      &//..@                    
                          /....%        #/.                      
                         %(##(          .(/@                   
                        * ...&          &(%#....@                
                        #(//,@            @&/,///,               
                         (&,                  .                  
    ''' + fcolor.DEFAULT)

def showGoldie():
    print(fcolor.BLUE + '''
                               .#*                           
                              ,/.##                          
                              #  ,#,                 .##/    
                              #*.#%##((((((((((.    ((/##.   
                        /  / /((##################%#   /#    
                      ,     %######################(  *#*    
                      &*    ##########################%      
                    /      ##################.     /####     
                        .###################   .     ####.   
                     ,(#####/,,*(##########    &&    ,####.  
                     (####........%########.         (#####  
                    ######........%#########*       #######. 
                   ,(######/,/*%###########################( 
              /....#########  %############################/ 
              .....(#######################################  
                ///#######################################   
                  .######################################    
                  .######*.........(##################.....* 
                   ####(.............(################......,
                   ###(.............../#################%/*/ 
                   ##/................./#################    
                   .(...................(################.   
                    /....................################.   
                     .....................###############    
                     ......................(############%    
                       ......................##########%.    
                       //......................*(#####,....  
                       ,..,/................,......(         
                        /......*,.......,,**,......,         
                                             ,......         
     ''' + fcolor.DEFAULT)

def showZee():
    print(fcolor.CYAN + '''                                                 
                         /                                       
                        *            * (                         
                         #  %%/ %%, .  /(                        
                       %&  %% %%%%.    .                         
                      *&(%. % &     ..                         
                      %% .%%%(&                                
                    *  %%%  %%%%%%   (/                          
                   %%%%%%%&%%  %%                */%%/ /         
                  #%%%%%%%%,   %%   / %/    .%%    %%            
                    %%&&&&%%   .*   /%#                     (    
                     %%%%%%      .%%% %%       %     %       (   
                              /(/.  ,%%   .   *%/    %(          
                           ,    .%%%*     %%   %%%   %%%      /( 
                            (              %*   %%%   %%%      % 
                             /              %   ,%%    %%        
                              /                  .      .     (. 
                              ,.           /                  %% 
                              ###.*        (       *         .   
                              %#%%#%########*######%#######%   
                         /%###*,%##%#########(####%##%%######,   
                          (* #(##/.######%## /(%#,*%#######%   
                          /  .(%####%#,    #/  ./%#####%(.   /   
                              *(((((/           *((((((,         
    ''' + fcolor.DEFAULT)

def showCaptKube():
    print(fcolor.YELLOW + '''                                                 
                                    (&@@@@&%,                    
                                ,@@@@@@@@@@@@@@@,                
                              .@@@@@@@@@@@@@@@@@@@.              
                             .@@@@@@@@@(%@@@@@@@@,             
                             #@@@@@@@*   .@@@@@@@@@#             
                             .@@@@@@* *@@@@@@@@@@@@,             
                              ,@@@@@   /%*(@@@@@@@*              
                               .@@@@@.     &@@@@@,               
                                *@@@@@@@@@@@@@@@(                
                           &@@@@@@@@@@@@@@@@@@@@@@@@@@           
                    (#*,,,,#@@@@@@@@@@@@@@@@@@@@@@@@@%*,,,,#(    
                    (,,,,,,,*&@@@@@@@@@@@@@@@@@@@@@&*,,,,,,,/    
                    .,,,,,,,,,,,,,/#&&@@@@@@&%(*,,,,,,,,,,,,.    
                     ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     
                     /,,,%@@@&/,,,,,,,,,,,,,,,,,,,(@@@@*,,,*     
                     /,,,/@@@@@@&*,,,,,,,,,,,,,/@@@@@@@,,,,/     
                     (,,,,,%@@@@@@@(,,,,,,,,,%@@@@@@@/,,,,,/     
                     *,,,,/@&  &(@@@/,,,,,,,&@@@## .@@,,,,,*     
                    .,,,,,#@&    @@@,,,(@/,,/@@&    @@*,,,,,,    
                    /,,,,,,(@@&&@@&,,,&@@@&,,(@@@%&@@*,,,,,,/    
                    *,,,,,,,,,**,,,,,&@@@@@&,,,,*/*,,,,,,,,,*    
                    ,,,,,,,,,,,,,,,,,*(@@@/*,,,,,,,,,,,,,,,,,    
                    *,,,,,,,,,,,,,,,,,**(**,,,,,,,,,,,,,,,,,,    
                   .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.   
                   (,,,*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*,,,(   
                   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*,,,,   
                  /,,,,,/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/,,,,,/  
                  *,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*  
                 ,,,,,,,,,(,,,,,,,,,,,,,,,,,,,,,,,,,,,(,,,,,,,,, 
                 *,,,,,,,/,,,,,,,,,,,,,,,,,,,,,,,,,*,,,*,,,,,,,/ 
                  ,,,,,,/*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*(,,,,,,. 
                  ./,/**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,****,,*  
                   /**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**/   
                   (,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(   
                   *,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*   
                   (,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(   
                    *,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
                     /,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*     
                      /***********************************(      
                         (/****************************(.        
                              ,/((//////////////((*.             
    ''' + fcolor.DEFAULT)

def showCoreDumper():
    print(fcolor.RED + '''                                                 
                                              ////               
                          *//// /////////////////                
                            //((((/(((((/////////                
                            ,/@@,.(%@&...//////////              
                            //....//....////**/////              
                            ////////////@//*/*///////////*       
                        ///////@ ./*    @@//////////      //     
                      //.   ,/@@@ (@ @  @@@//////////     /////  
                     /     *//@&@@@@@@@@@@@@///////// (   *  *   
                  ////      /&@@@@@@@@@@#@@@@//////// ((         
                 *//. /     /@@@@@@ @@ ( (@@@///////   *(        
                           /%@%% @#       @@@//////     (/.      
                            /@##   ./////////////       (*.      
                             ////////////////////     /(((       
                            /////////////////////((((((((        
                            ////// .    //////     /(*           
                           //////*      //////                   
                          ///////*     ///////                   
    ''' + fcolor.DEFAULT)

def showNullPointerminator():
    print(fcolor.RED + '''        
                                  &%         (&                  
                                 &&%         /&&            
                     %&&&&&      &&&         &&&      &&&&&%     
                  &&&&&&&&&&&&/  &&&&&&&&&&&&&&&. ,&&&&&&&&&&&&  
                ,&&&&&/,(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,*&&&&
                &&&&       .&&&&&&&&&&&&&&&&&&&&&&&&&        &&&&
                &&  .&&&&  &&&&&&&&&&&&&&&&&&&&&&&  #&&&*  ,&&&
                &&&&. *  &&  %&&&&&&& . .   &&&&&&&&  &&  ,  &&&&
                 %&&&&&&&&&  &&&&&&&. .&&&,  &&&&&&&  &&&&&&&&&& 
                   .&&&&&    &&&&&&&  &&&&&  &&&&&&&    &&&&&,   
                             %&&&&&&%  (  (&&&&&&&            
                             %&&&&&&&&%   #&&&&&&&&&            
                             %&&&&&&&&&&&&&&&&&&&&&&             
                             &&&&&&   ,  .(   %&&&&&             
                             /&&&&&&&*     .&&&&&&&%        
                              &&&&&&&&&&&&&&&&&&&&&           
                               &&&&&&&&&&&&&&&&&&&              
                                 &&&&&&&&&&&&&&&                 
                                   /&&&&&&&&&%                   
                                .&&&&&&& &&&&&&&*               
                               &&&&&&&&& &&&&&&&&&            
    ''' + fcolor.DEFAULT)

def showDivideByZero():
    print(fcolor.RED + '''          
                                 /@@@@@@@@@@@@@@            
                              @@@@@@@@@@@@@@@@@@@@@,             
                            @@@@@@@@@@@@@@@@@@@@@@@@@            
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
                   *@@@@@@@@@@  .@@@@@@@@@@@@@@@%  @@@@@@@@@@@   
                     @@@@@@@@@@     @@@@@@@@@     .@@@@@@@@@(    
                         &@@@@@@.@@*.#@@@@@@  @@ ,@@@@@@%        
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@*         
                          .@@@@@@@@@@@%../  @@@@@@@@@@           
                    . . . . .@@@@@ ,@@@@@@@@@% @@@@@@            
                    . . . . . .@@@@@@@@@@@@@@@@@@@/              
                    . . . . . . . .@@@@@@@@@@@@                  
                  . . . . . .    @@@@@@@@@@@@@@@             . . 
                  . . . . . .   @@@@@@@@@@@@@@@@@#           . . 
                  . . . .      @@@@@@@@@@@@@@@@@@@&      . . . . 
                  . . . .    @@@@@@@@@@@@@@@@@@@@@@@     . . . . 
                  .           @@@@@@@@@@@@@@@@@@@@@. . . . . . . 
                  .             @@@@@@     @@@@@@    . . . . . . 
                              .@@@@@@       @@@@@@%. . . . .     
                             @@@@@@@@       (@@@@@@@ . . . .     
                              %@@@@@,        @@@@@@. . . . .     

    ''' + fcolor.DEFAULT)

def showOOM():
    print(fcolor.RED + '''                                                 
                                    &&&&&&&&&                    
                                  &&&&&&&&&&&&&                  
                                .&&&&&&&&&&&&&&&/                
                               *&&&&&&&&&&&&&&&&               
                              .&&&&&&&&&&&&&&&&&&&(              
                              &&&&    &&&&&    &&&&.             
                             &&&&  && ,&& &&  &&&&             
                            %&&&&&&  &&&&&&&  %&&&&&&            
                            &&&&&&&&&&&&&&&&&&&&&&&&&            
                           &&&&&&&&&&&&&&&&&&&&&&&&&&&           
                          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&,         
                       %&&&&&&&&&&             &&&&&&&&&&&       
                   /&&&&&&&&&&&&&&&           &&&&&&&&&&&&&&   
                ,&&&&&&&&&&&&&&&&&&&&&%   %&&&&&&&&&&&&&&&&&&&&&(
                  (&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  
                      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      
                      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      
                      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      
                      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,     
                                 #&&&&&&&&&&&&&%       
                                    &&&&&&&&&                 
                                      #&&&%                   
    ''' + fcolor.DEFAULT)

def showIllegalArgumentator():
    print(fcolor.RED + '''
                                                     ,(%#        
                                %&&&@&,        .&&%(%@%          
                                  &%##&&@@,  .&%#/&@&*           
                         *((%&&%.#&(#(%&@@&*#&&%/            
                            %@%/(((&@#/&%&@&&&@@&&%###%&%&&.   
                           ..,&@@%#%#&@(#%%@&%&//(#%%%&&&&&&&%&
                    ,##((((((#(/(#%%%&@@&%(%&&@%%&%&&&&&%%%&%*,
                   ,(&&&&&&&&%%%###&&&%%&&&&@%@@&@&&&&@%*        
                         *&&&@&&%%(////(#%&&&&&@@@@@@@@@@@@%*    
                       (%%%&&%//((#%%&%%%/##%&&@@@####%%%&@, 
                         %##%%&%#%&&&&@@(##%%&@@@@@&&@@&&@@&&%&&@
                       (%%&&&&@@@@@@@@%(#%%@#&%@%%@&%%&%&%##%&&@&
                     (&@@&@&@@#%%%#%#%%@@(%&&@@@@&&&@&%%     
                    ,   (&@&%%%&@@@@%(%&@%#/&&(/*(@&(%&&&&%&*    
                          (#@@%##%&@##&@, /(&,...*(@%(&@@@&%%    
                         &  #@%%(,(&%&@%#%,%.....*%%%@# .@&    
                              &&//*,&&.*#/**@..(%,%  &* &   ,,   
                                / &@#. .(#%*..,//(* ..           
                                  #%#.   ..../&//                
                                     (/,....,/(/,                
                                   ((&../#%&%.                   
                               .#((#&%%%,*((#%##                 
                              (%/,,*&%(#(#%***%%%##,             
                             /@(.   .*&%&%&(%&             
                             @&/*.  ..(%%%&(&&%&(&&(*            
                            ,%&%/**,  ,&(*%&&&&%%%#&/*           
                            (%&&%#%*,   %(*%%%%@%/,&/**          
                            (#&@%#(*.   .,..%%#&&%&(,,         
                             #&%&%#%%&/,.....,*&#,...(         
                              #%%&%&%&/*(//((@##((((#(         
                               ,#&%%@%%%%&&&&&&&&&%.             
                                 # *&&&&%%%%&%%%%%&              
                                   &%%%%%%&&&&&%%%&*                        
    ''' + fcolor.DEFAULT)

def showTrophy():
    print(fcolor.YELLOW + '''                                                 
                  #*,*%,                                 %,.,%   
                 &,,***,%                              &,,**,,#  
                 /,@   &/ %,,.   .,,*****,**,,///,,,*@ (/   (*,# 
                 /*.   #(/ %(/(.../***/*,/(/(*/#((/// .%,*   /,# 
                 #,&   @,,,#&(#(/((((((/,*/(/*/////@&*,,(   &,*, 
                 ,*,#   @@/.*,.   ,,,,,,,,,,****,,,// &&   %,,&  
                  .(,(      *#%/**/%*////*////&&.       &,*%   
                    &,**      .*,,.  ,,,,,*,,//*,&       #,&     
                     .(,#      (*,, .,,,,,,,,//*,%     (**%      
                       ./*,    &,      ,,,,,,//*,(    (*&        
                         */%&* %,,,,   ,,,,,,//,,* @#,#          
                           ,*,*/,*,    ,,,,,,//,*,(*#            
                              #&**      *****((#%&*              
                              .*,,..,,*****//((***(              
                                 @(/**((*//#(%/#                 
                                    .@,,,///%                    
                                        ,/.                      
                                        ,/,                      
                                      %*,*/**                    
                                    &(*,,,//*&                   
                                   &(#####%%%#&*                 
                               .#,,,,,,,,,,*///*//@              
    ''' + fcolor.DEFAULT)

def showGrave():
    print(fcolor.RED + '''                                                 
                                    &%#########&.                
                                    &%#########&.                
                                    &%#########&.                
                                  *&(((######&&(               
                               .&&(*##############%@/            
                             *./###################&/          
                            /&/.####&&(&%###&(%%######%&         
                     ,/////#%.,###&*   &%###%*  .#####&/////*  
                     #####*,###&,    &%###%*    &%#########%&, 
                     ##### (##%&&&&&&%####%&&&&&&###########%&, 
                     ##### #################################%&, 
                     ##### (################################%&, 
                     #####*,###&,    &%###&*    %%##%%%%%%%%%&, 
                     /#####%# ,###&*   &%###%*   &%###%%@######  
                            ##*.####&&,&%###%*#&%###%%%&         
                             /&( /#####%##########%%%&/          
                               ,&%*,###########%%%%&(            
                                  /&%(**/(####%&@#.              
                                    &%########%&.                
                                    &%########%&.                
                                    &%########%&.                
                                    &%########%&.                
                                    &%########%&.                
                                    &%########%&.                
                                    &%########%&.                
                                    &%########%&.                
                                    &%########%&.                     
                            &&&&&&&&&&&&&&&&&&&&&&&&&&&& 
                        &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& 
                       &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&   
    ''' + fcolor.DEFAULT)
