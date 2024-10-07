#Created by BCL NASA App Team 
# - writer: Caitlyn Castañeda, (debug helper: Brianna Ramos, data collectors: Cindy Vega and Elizabeth Reyes) 

import time
import requests
from bs4 import BeautifulSoup
from colorama import Fore
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW,  Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
#import beautifulsoup4 as bs4
atmosdata = 'https://education.nationalgeographic.org/resource/atmosphere/'
atmosres = requests.get(atmosdata)
disdata = 'https://exoplanets.nasa.gov/search-for-life/habitable-zone/'
disres = requests.get(disdata)
gasdata = 'https://www.nasa.gov/universe/exoplanets/webb-discovers-methane-carbon-dioxide-in-atmosphere-of-k2-18-b/'
gasres = requests.get(gasdata)
atmosphere = "n" 
atmosans = 0
distance = "n" 
distans = 0 
gas = "n"
gasans = 0
check_count = 0
surface = "n"
surfans = 0
eligibility_meter = 70 
help_meter = 0 
LINE_UP = '\033[1A' 
LINE_CLEAR = '\033[K '
CONSOLE_HEIGHT = 500
bag = []
bagone = False
bagtwo = False
kep7 = False
bag2one = False
bag2two = False 
bag2three = False
bag2four = False
bag2five = False
kiwihealth = 50
defeat = False
userhealth = 30

def border():
    print(Fore.WHITE, "╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮╭─〔❨✧✧❩〕─╮")
def clear_console(): 
  for a in range(CONSOLE_HEIGHT): 
    print('\033[2J', LINE_UP, end='', flush=True)
 
def atmospherecheck(): #This is the function for users to input how much oxygen they want in their planet's atmosphere
  global help_meter 
  global eligibility_meter
  global atmosphere
  global atmosdata
  global atmosres
  global FORES
  global atmosans
  atmosphere = "y"
  help = 'N' 
  print("----------------------------")
  print("The first step to designing a potential habitable planet is by checking its atmosphere.")
  help = input("Do you need more information on a habitable atmosphere? [ANSWER Yes/No]")
  if help == "Yes":
    help_meter = help_meter + 1 
    print("~~~~~~ \n")
    soup = BeautifulSoup(atmosres.text, 'html.parser')
    info = soup.get_text()  
    print(Fore.CYAN, info[1262:-4338]) 
    print(Fore.GREEN, "From: https://education.nationalgeographic.org/resource/atmosphere/", Fore.WHITE)
    print("~~~~~~~")
  global atmosphereinput 
  atmosphereinput = input("What percent of oxygen will you add to your exoplanet's atmosphere? [INTEGER INPUT, DO NOT PUT '%', ONLY THE NUMBER.]")
  if int(atmosphereinput) > 21 and int(atmosphereinput) < 19.5: #checks user input 
    eligibility_meter = eligibility_meter - 10 #lowers score because answer is not suitable for life 21
    print("Answer taken.")
    atmosans = 1
    clear_console() 
    distancecheck() 
  elif int(atmosphereinput) > 21 : #checks user input 
    eligibility_meter = eligibility_meter - 10 
    print("Answer taken.")
    atmosans = 2
    clear_console() 
    distancecheck() 
  elif int(atmosphereinput) == 21 or int(atmosphereinput) < 21 and int(atmosphereinput) >= 19.5:
    print("Answer taken.")
    atmosans = 3
    clear_console() 
    distancecheck() 

def distancecheck(): 
  global eligibility_meter
  global distance
  global distans 
  global help_meter
  print("----------------------------")
  print("Distance is one of the biggest factors of whether a planet is habitable or not. It affects many factors, with a major one being availability of a water source.") 
  help2 = input("Do you need more information on a planet's habitable zone? [ANSWER Yes/No]")
  if help2 == "Yes":
    help_meter = help_meter + 1 
    print("~~~~~~ \n")
    soup2 = BeautifulSoup(disres.text, 'html.parser')
    info = soup2.get_text()  
    print(Fore.CYAN, info[3234:-6159]) 
    print(Fore.GREEN, "From: https://exoplanets.nasa.gov/search-for-life/habitable-zone/", Fore.WHITE)
    print("~~~~~~~")
  distanceinput = input("How far would your planet be from their sun?[ENTER DISTANCE OF PLANET TO SUN IN (n) MILLION KILOMETERS]")
  distance = "y"
  if int(distanceinput) > 150:
    eligibility_meter = eligibility_meter - 10 
    print("Answer taken.")
    distans = 1
    clear_console() 
    gascheck() 
  elif int(distanceinput) < 150:
    eligibility_meter = eligibility_meter - 10 
    print("Answer taken.")
    distans = 2
    clear_console() 
    gascheck()
  elif int(distanceinput) == 150:
    print("Answer taken.")
    distans = 3
    clear_console() 
    gascheck()

def gascheck(): 
  global gas 
  global eligibility_meter
  global gasans
  global gasdata
  global gasres
  global help_meter
  print("----------------------------")
  print("There are more gases in the atmosphere, other than oxygen, that make Earth habitable.")
  help3 = input("Do you need more information on a planet's habitable gasses? [ANSWER Yes/No]")
  if help3 == "Yes":
    help_meter = help_meter + 1 
    print("~~~~~~ \n")
    soup3 = BeautifulSoup(gasres.text, 'html.parser')
    info = soup3.get_text()
    print(Fore.CYAN, info[7731:-7144]) 
    print(Fore.GREEN, "From: https://www.nasa.gov/universe/exoplanets/webb-discovers-methane-carbon-dioxide-in-atmosphere-of-k2-18-b/", Fore.WHITE)
    print("~~~~~~~")
  gasesinput = int(input("What kinds of gases do you want on your planets atmosphere?\n CHOOSE ONE FROM THIS LIST:\n 1) NITROGEN\n 2) ARGON \n 3) CARBON DIOXIDE\n 4) METHANE]\n"))
  if gasesinput == 1:
    eligibility_meter = eligibility_meter - 5 
    print("Answer taken.")
    gasans = 2
    clear_console()
    surfacecheck()
  if gasesinput == 2:
    eligibility_meter = eligibility_meter - 5 
    print("Answer taken.")
    gasans = 2
    clear_console()
    surfacecheck()
  if gasesinput == 3:
    print("Answer taken.")
    gasans = 4
    clear_console()
    surfacecheck()
  if gasesinput == 4:
    print("Answer taken.")
    gasans = 4
    clear_console()
    surfacecheck()

def surfacecheck():
  global surface
  global disres 
  global help_meter
  global FORES
  global Fore
  global eligibility_meter
  global surfans
  print("----------------------------")
  print("The final step to complete your potential habitable world you need to pick a type of surface. Depending on the surface you choose it affects how life will grow on your planet.")
  help4 = input("Do you need more information on a planet's habitable surface condition? [ANSWER Yes/No]")
  if help4 == "Yes":
    help_meter = help_meter + 1 
    print("~~~~~~ \n")
    soup2 = BeautifulSoup(disres.text, 'html.parser')
    info = soup2.get_text()  
    print(Fore.CYAN, info[3234:-6159]) 
    print(Fore.GREEN, "From: https://exoplanets.nasa.gov/search-for-life/habitable-zone/", Fore.WHITE)
    print("~~~~~~~")
  surfaceinput = int(input("What surface do you want you planet to have? [CHOOSE ONE OF THE THREE:\n 1) ICE\n 2) GAS\n 3) ROCK\n"))
  if surfaceinput == 1:
    eligibility_meter = eligibility_meter - 10 #Life has a hard time growing in ice, lowering the score.
    print("Answer taken.")
    surfans = 1
    clear_console ()
    score()
  elif surfaceinput == 2:
    eligibility_meter = eligibility_meter - 10 #Life cannot grow on gas, lowering the score.
    print("Answer taken.")
    surfans = 2
    clear_console()
    score()
  elif surfaceinput == 3:
    print("Answer taken.")
    surfans = 3
    clear_console()
    score()
  else:
    clear_console() 
    print("Not a valid option, please read the directions carefully")
    surfacecheck() 


def score():
  global eligibility_meter 
  global atmosans
  global distans 
  global gasans 
  global surfans
  print("Your habitability score is:" + str(eligibility_meter) + " out of 70")
  #checking atmosphere answers
  if atmosans == 1: 
    print("Your answer for the oxygen percentage present in your atmopshere was too low. It should be fairly around 21%, with 19% still being acceptable but based off old Earth statistics.")
  if atmosans == 2: 
    print("Your answer for the oxygen percentage present in your atmosphere was too high. It should not be above 21% because it would affect the organisms too much for sustainable life.")
  if atmosans == 3:
    print("Your answer for the oxygen percentage present in your atmosphere was just right. It was historically and currently safe enough for organisms to live in.")
  #checking distance answers
  if distans == 1:
    print("Your answer for how far your exoplanet would be too far for it to be properly heated for life. Heat is a major component, as it allows liquid water to be present at the surface, like Earth. Earth is 150M km away from our sun, or 3 AU (astronomial units).")
  if distans == 2: 
    print("Your answer for how far your exoplanet would be is too close for it to be properly heated for life. Heat is a major component, as it allows liquid water to be present and not entirely evaporated from the surface. Earth is 150M km away from our sun, or 3 AU (astronomial units)")
  if distans == 3: 
    print("Your answer for how far your exoplanet would be is just right for it to be properly heated for life. Heat is a major component, and like Earth, your distance from the sun is 150M km or 3 AU.")
  #checking gas answers
  if gasans == 4: 
    print("Your answer for what gas would be most present was sustainable for life. While gases like argon and nitrogen are also present in Earth's atmosphere, carbon dioxide and methane are the greenhouse gases, sustaining life.")
  if gasans == 2:
    print("Your answer for what gas would also be present is sustainable for life, but it was not the best answer of the four. While gases like nitrogen and argon are present in the Earth's atmosphere, carbon dioxide and methane  are greenhouse gases, sustaining life the most.")
  if surfans == 1:
    print("Your answer for what your exoplanet's surface would be like would offer a hard time sustaining life. Ice is not a proper enviornment for important systems like plants to grow in.")
  if surfans == 2: 
    print("Your answer for what your exoplanet's surface would be like cannot sustain life. Gas planets do not have a clearly defined surface so there is no possibility for life to be grown on an almost nonexistent surface.")
  if surfans == 3:
    print("Your answer for what your exoplanet's surface would be like sustains life. Worlds with rocky terrain are able to grow plant life.")
  print(Fore.CYAN, "Please note that, despite the score, we are still unsure of how other planets can stimulate life, their qualifications may be different from Earth's. For now, the most we can truly do is infer! Thank you for testing.")


def crmenu():
  print("In this section, we will determine whether a planet of your making would be habitable for life.")
  print("If you do not understand a certain term, then an explanation will be provided.")
  input("Your exoplanet's name: ")
  understand = input("Continue? Input 'Y' if you understand and would like to continue, and any other letter to cancel the program.")
  if understand == "Y": 
    clear_console() #clears screen
    atmospherecheck() #goes to first question
    understand = "n/a" 


def spaceship():
    clear_console()
    border()
    print(Fore.WHITE, "░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░\n░░░░░░░░██░░░░░░░░\n░░░░░░░░██░░░░░░░░\n░░░░░████████░░░░░\n░░░░░█░░░░░░█░░░░░\n░░░░██████████░░░░\n░░░░░█░░░░░░█░░░░░\n░░░░░█░████░█░░░░░\n░░░░░█░█░░█░█░░░░░\n░░░░░█░████░█░░░░░\n░░░░░█░░░░░░█░░░░░\n░░░███░░░░░░███░░░\n░░██░█░░░░░░█░██░░\n░░█░░████████░░█░░\n░░██░█▒▒▒▒▒▒█░██░░\n░░░███▒▒▒▒▒▒███░░░\n░░░░░░▒▒▒▒▒▒░░░░░░\n░░░░░░▒░░▒░▒░░░░░░\n░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░")
    time.sleep(2)
    clear_console()
    border()
    print("░░░░░░░░██░░░░░░░░\n░░░░░░░░██░░░░░░░░\n░░░░░████████░░░░░\n░░░░░█░░░░░░█░░░░░\n░░░░██████████░░░░\n░░░░░█░░░░░░█░░░░░\n░░░░░█░████░█░░░░░\n░░░░░█░█░░█░█░░░░░\n░░░░░█░████░█░░░░░\n░░░░░█░░░░░░█░░░░░\n░░░███░░░░░░███░░░\n░░██░█░░░░░░█░██░░\n░░█░░████████░░█░░\n░░██░█▒▒▒▒▒▒█░██░░\n░░░███▒▒▒▒▒▒███░░░\n░░░░░░▒▒▒▒▒▒░░░░░░\n░░░░░░▒▒▒▒▒▒░░░░░░\n░░░░░░▒░▒▒░▒░░░░░░\n░░░░░░▒░▒░░▒░░░░░░\n░░░░░░▒░░░░▒░░░░░░\n░░░░░░░░░░░░░░░░░░")
    time.sleep(2)

def kiwiboard():
    global kiwihealth
    global defeat
    global userhealth
    print(Fore.RED, "Infected Kiwi's HP: " + str(kiwihealth))
    print(Fore.WHITE, "Your HP: " + str(userhealth))
    
    
def KIWIBOSS():
  global kiwihealth
  global userhealth
  global defeat 
  kiwihealth = 50
  userhealth = 30
  import random
  clear_console()
  while kiwihealth > 0:
    border()
    kiwiboard()
    print(Fore.WHITE, "1) Attack")
    print("2) Heal")
    kchoice = random.randint(1,2)
    try: 
      choice = int(input("What will you do? Input number 1 or 2."))
    except ValueError:
      print("Please type only 1 or 2.")
      time.sleep(5)
      KIWIBOSS() 
    damage = random.randint(0,25)
    kdamage = random.randint(0,15)
    heal = random.randint(0,15)
    kheal = random.randint(0,25)
    if choice == 1:
      kiwihealth = kiwihealth - damage
      print("You dealt " + str(damage) + " damage!")
    else:
      if choice == 2:
        userhealth = userhealth + heal
        print("You grabbed some bandage and healed " + str(heal) + " HP")
    if kchoice == 1:
      userhealth = userhealth - kdamage
      print("Kiwi attacked you. You lost " + str(kdamage) + " HP!")
    else:
      if kchoice == 2:
        kiwihealth = kiwihealth + kheal 
        print("Kiwi regeneterated themself. They gained " + str(kheal) + " HP")
    if kiwihealth == 0 or kiwihealth < 0:
      print(Fore.WHITE, "You kicked the parasite out of Kiwi!")
      keplerend()
    if userhealth == 0 or userhealth < 0: 
      print(Fore.RED, "The parasite has defeated you as well.")
      print("Try again?")
      tryagain = input("Press K to try again. ")
      if tryagain == "K":
        kiwihealth = 50
        userheath = 30
        kepler452()
      else:
        quit()     

def keplerend():
  global username
  print(Fore.CYAN, "Kiwi was restored to proper health and functioning, as the parasite was now gone.")
  print(Fore.GREEN,"'Thank you, " + str(username) + " for saving me. Here, let's take a walk, no codes or anything.'")
  time.sleep(3)
  print(Fore.CYAN, "The two of you walk through Kepler-452 b.")
  print(Fore.GREEN, "'You know, Kepler-452 b is pretty rocky, and, like Earth, liquid weather exists here.\n It has a 384.8 orbit, and is actually considered to be a bigger older cousin to Earth.")
  time.sleep(3)
  print("'It's great, huh? There are things that are so great out here, on these exoplanets. But I think, this one has become my new favorite.\n Do you know why?")
  time.sleep(5)
  print("'Because it's so similar to Earth, which means, perhaps one day there will be living beings similar to you. Daring, brave, and honorable. Thank you, " + username + ", for saving me once again.'")
  end = input("Press K to continue.")
  if end == "K":
    spaceship()
    menu()
  else:
    quit()
def kepler452():
  print(Fore.GREEN, "'Welcome to Kepler-452 b! We are 1,799 light years away from Earth!'")
  print("'Now- like before, you wi- hey- WHAT'S THAT??'")
  print(Fore.CYAN, "You see an parasitic-looking alien leech itself onto Kiwi. It penetrates through, infecting their brain.")
  print(Fore.CYAN, "Kiwi tries to speak out to you," + Fore.RED, "'Y-you need to knock me out so it'll get out of my head!")
  startfight = input("Press K to continue: ")
  if startfight == "K":
    KIWIBOSS() 
    
def kepler7(): 
    global bag2one
    global bag2two
    global bag2three
    global bag2four
    global bag2five

    print(Fore.GREEN, "'Welcome to Kepler-7 b! We are 3,009 light years away from Earth.'")
    print("'Again, you will need to unlock the safe with a LARGER code! No initial numbers for you this time! Have fun!")
    print(Fore.WHITE, "1) Rock 1\n 2) Rock 2\n 3) Behind the spaceship\n 4) Rock 3\n 5) Rock 5\n 6) Rock 7\n Shaded side\n 8) Plain land\n 9) In front of the spaceship\n 10) Safe")
    move2 = int(input("Choose where you'd like to go: "))
    if move2 == 1:
        print(Fore.CYAN, "You go over to the first rock you see. There's ...")
        time.sleep(3)
        print("Nothing there.. oh well.")
        ok1 = input(Fore.WHITE, "Press K to continue: ")
        if ok1 == "K":
            kepler7() 
    if move2 == 2:
        print(Fore.CYAN, "You go over to a different small rock from the one near the spaceship. You flip it over and ...")
        time.sleep(3)
        print("There's a code number there! You put it in your bag.")
        bag2one = True
        ok2 = input(Fore.WHITE, "Press K to continue: ")
        if ok2 == "K":
            kepler7() 
    if move2 == 3:
        print(Fore.CYAN, "You go behind the spaceship. There's ...")
        time.sleep(3)
        print("Nothing there. Not sure why it'd be hidden in the same spot.")
        ok3 = input(Fore.WHITE, "Press K to continue: ")
        if ok3 == "K":
            kepler7() 
    if move2 == 4: 
        print(Fore.CYAN, "You go over to a rock. And...")
        time.sleep(3)
        print("There's a code number there! You put it in your bag.")
        bag2two = True
        ok4 = input(Fore.WHITE, "Press K to continue: ")
        if ok4 == "K":
            kepler7()   
    if move2 == 5: 
        print(Fore.CYAN, "You go to a rock that's a bit large. You look behind it since you can't lift it up. There's ...") 
        time.sleep(3)
        print("Another piece of the code! You put it in your bag.")
        bag2three = True
        ok5 = input(Fore.WHITE, "Press K to continue: ")
        if ok5 == "K":
            kepler7() 
    if move2 == 6: 
        print(Fore.CYAN, "You go to a rock. You are able to flip it over and ...")
        time.sleep(3)
        print("There's nothing there... ")
        ok6 = input(Fore.WHITE, "Press K to continue: ")
        if ok6 == "K":
            kepler7()        
    if move2 == 7:
        print(Fore.CYAN, "You walk far enough to get to the a shady part of the exoplanet. You look over and ...")
        time.sleep(3)
        print("There's a piece of the code on the ground! Perhaps Kiwi didn't expect you to walk that far out. You put it in your bag.")
        bag2four = True
        ok7 = input(Fore.WHITE, "Press K to continue: ")
        if ok7 == "K":
            kepler7()
    if move2 == 8:
        print(Fore.CYAN, "You go to explore the out open land. There's ...")
        time.sleep(3)
        print("There's nothing there.")
        ok8 = input(Fore.WHITE, "Press K to continue: ")
        if ok8 == "K":
            kepler7()    
    if move2 == 9: 
        print(Fore.CYAN, "You look around the front of the spaceship. Somehow ...")
        time.sleep(3)
        print("Another piece of the code was there! You put it in your bag.")
        bag2five = True
        ok9 = input(Fore.WHITE, "Press K to continue: ")
        if ok9 == "K":
            kepler7()    
    if move2 == 10:
        clear_console()
        print(Fore.CYAN, "You go over to the safe, next to the space ship.")
        bagtwo = " "
        if bag2one == True:
            bagtwo = bagtwo + " 8 "
        if bag2two == True:
            bagtwo = bagtwo + " 9 "
        if bag2three == True:
            bagtwo = bagtwo + " 6 " 
        if bag2four == True:
            bagtwo = bagtwo + " 3 "
        if bag2five == True:
            bagtwo = bagtwo + " 7 "
        print(Fore.WHITE, bag)
        codeinput2 = input("What is the code? _ _ _ _ _")
        if codeinput2 == "96378":
            print(Fore.GREEN, "Correct! Here's the information that was inside: ")
            print(Fore.WHITE, "Kepler-7 b is an exoplanet simiilar to Jupiter's terrain\n It has no tides\n One side of its planet is scorching hot, whereas the other is freezing cold\n It has a 4.9 orbit\n It is the first exoplanet to have its clouds mapped")
            con5 = input("Press K to continue: ")
            if con5 == "K":
                con5 = ""
                clear_console()
                print(Fore.RED, "upon getting on the spaceship.. you notice something.. odd, entering through the side.")
                time.sleep(2)
                spaceship()
                kepler452() 
  
def kepler22():
    global bagone
    global bagtwo
    global bag
    global kep7
    border() 
    print(Fore.GREEN, "'Welcome to Kepler-22 b, an exoplanet that is 635 light years away from Earth!'")
    print("'For exploring the exoplanet, you will need to find 3 hidden numbers to unlock this safe!'")
    print("")
    print(Fore.GREEN, "'This safe has information on Kepler-22 b, so have fun looking for the safe code while also exploring the exoplanet!'")
    print(Fore.GREEN, "'Also, you have already been given one of the three numbers, which you can find in your bag.'")
    print(Fore.WHITE, "1) Clouds\n 2) Jet Stream\n 3) Behind the spaceship\n 4) Water\n 5) Safe")
    move = int(input("Choose where you'd like to go: "))
    if move == 1:
        print(Fore.CYAN, "*You set yourself up and go into the clouds. There's not much around, but after flying through, you notice a note and put it in your bag.*")
        con = input("Press K to continue: ")
        if con == "K":
            con = ""
            bagone = True 
            kepler22()
    if move == 2:
        print(Fore.CYAN, "*You observe the air and decide to enter a jet stream. You get stuck for a few seconds, zooming at 250 mph, before falling back down and landing on the ground.")
        con2 = input("Press K to continue: ")
        if con2 == "K":
            con2 = ""
            kepler22()
        kepler22()
    if move == 3:
        print(Fore.CYAN, "You look behind the spaceship, and unsuprisingly, there's nothing there.")
        con3 = input("Press K to continue: ")
        if con3 == "K":
            con3 = ""
            kepler22()
    if move == 4:
        print(Fore.CYAN, "You walk only a few steps and come across a massive body of water. At the surface, you find a note floating. You pick it up and put it in your bag.")
        con4 = input("Press K to continue: ")
        if con4 == "K":
            con4 = ""
            bagtwo = True 
            kepler22() 
    if move == 5:
        clear_console()
        print(Fore.CYAN, "You go over to the safe, next to the space ship.")
        bag = " 3 "
        if bagone == True:
            bag = bag + " 9 "
        if bagtwo == True:
            bag = bag + " 5 "
        print(Fore.WHITE, bag)
        codeinput = input("What is the code? _ _ _  ")
        if codeinput == "953":
            print(Fore.GREEN, "Congratulations! You got it correct. Here's more information on Kepler-22 b!!")
            print(Fore.WHITE, "Kepler-22 b is a water covered planet, containing clouds and jet streams\n It has a 290 day orbit\n It was the first exoplanet discovered that orbits in a habitable zone of its star, just like Earth!")
            next = input("Press K to continue: ")
            if next == "K":
              next = ""
              kepler7()
        else:
            print("Incorrect.")
            kepler22()
              
                
def vimenu():
    global kep7
    print(Fore.GREEN, "'Hello!'")
    print(Fore.WHITE, "This is Kiwi, your astronaut buddy who will come along with you on your exoplanet adventure!\n Here is the program line-up:\n Kepler-22 b\n Kepler-7 b\n Kepler-452 b")
    con6 = input("Press K to continue: ")
    if con6 == "boss":
        kepler452()
    if con6 == "K":
        con6 = ""
        clear_console()
        border()
        for i in range(4):
            spaceship()
            clear_console()
        if kep7 == True:
            kepler7() 
        else: 
            kepler22()

def menu():
  global username
  print(Fore.WHITE, "Hello! Please enter the following:")
  username = input("Name: ")
  print("Greetings " + username + "!")
  print("In this installment of EXOPLANET EXPLORATION, you will be able to explore exoplanets with puzzles and adventure or try to create your own!\n 1) Visit Exoplanets\n 2) Create My Own Exoplanet")
  chosmenu = int(input("Write the number of the activity you would like to do: "))
  if chosmenu == 1:
    vimenu()
  if chosmenu == 2:
    crmenu()

menu() #begins the code 

