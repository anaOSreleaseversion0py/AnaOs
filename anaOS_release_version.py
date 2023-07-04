import time, webbrowser
warning_ = ("Invalid Entry: Ensure entry is correct")

def converters_():
    print("Converters")
    print(" ")
    while True:
        converterType = input("""Select conversion type
        1) Weight
        2) Height
         > """)
        if converterType == "1":
            wConversion()
            print(" ")
            break
        elif converterType == "2":
            hConversion()
            print(" ")
            break
        else:
            print(warning_)
            print(" ")

def wConversion():
    print("Weight Converter")
    while True:
        wType = input("""Convert:
        1) lbs to kg 
        2) kg to lbs
        > """)
        print(" ")
        if wType == "2":
            kgWeight = float(input("Enter weight in kg > "))
            lbsWeight = kgWeight*2.205
            print(" ")
            print(kgWeight,"kg is equal to",lbsWeight,"lbs")
            break
        elif wType == "1": 
            lbsWeight = float(input("Enter weight in lbs > "))
            kgWeight = lbsWeight/2.205
            print(" ")
            print(lbsWeight,"lbs is equal to",kgWeight,"kg")
            break
        else:
            print(warning_)


def hConversion():
    print("Height Converter")
    hType = input("""Convert: 
    1) ft to cm
    2) cm to ft
    > """)
    print(" ")
    if hType == "1":
        ftHeight = float(input("Enter height in feet (enter 0 here to measure only in inches) > "))
        inHeight = float(input("Enter height in inches (enter 0 here to measure only in feet) > "))
        print(" ")
        cmHeight = (ftHeight*30.48)+(inHeight*2.54)
        print(ftHeight,"ft",inHeight,"in is ",cmHeight,"cm")
    if hType == "2":
        cmHeight = float(input("Enter height in cm > "))
        print(" ")
        ftHeight = cmHeight/30.48
        inHeight = cmHeight/2.54
        ftHeightInt = int(ftHeight)
        inFtHeight = (ftHeight-ftHeightInt)*12
        print(ftHeight,"ft")
        print(inHeight,"in")
        print(int(ftHeightInt),"ft",(inFtHeight),"in")
    else:
        print(warning_)



def bmiCalc():
    print("BMI Calculator")
    while True:
        bmiType = input("""Select version:
        (Old version is standard in ED spaces)
        1) Old 
        2) New 
        3) Whats the difference? 
        > """)
        if bmiType == "1":
            weight = float(input("Enter weight in kg only (for conversion select: Weight Conversion) > "))
            height = float(input("Enter height in cm only (for conversion select: Height Conversion) > "))
            oldBMI = weight/((height/100)**2)
            print("Your BMI is",oldBMI)
            break
        elif bmiType == "2":
            weight = float(input("Enter weight in kg only (for conversion select: Weight Conversion) > "))
            height = float(input("Enter height in cm only (for conversion select: Height Conversion) > "))
            newBMI = 1.3*weight/((height/100)**2.5)
            print("Your BMI is",newBMI)
            break
        elif bmiType == "3":
            webbrowser.open("https://people.maths.ox.ac.uk/trefethen/bmi.html",new=1)
        else:
            print(warning_)


   
def info_():
    print("AnaOS - version 1.0.1")
    print("Made by slash </3 (contact Slasher#6424 on discord)")
    print("Built in Python version 3.8")
    print(" ")
    print("I can custom add links for you if you are unsure of how to yourself")
    print("Contact me via discord if there are any issues/bugs/suggestions")
    print("Please consider recovery !! Life can be better than this")
    print("Access the recovery option in the main menu to see recovery resources")
    print("")
    continue_ = input("Press enter to continue")
    
print("Welcome to AnaOS")
time.sleep(0.2)
print("NOTE: options 4 to 8 are user input links! Right click the file, and click 'edit with IDLE'.")                       #DELETE ME !!
print("Scroll to the bottom of the file and replace the green text where it says 'url for X' with your desired URL")        #DELETE ME !!
print("Contact Slasher#6424 on discord if you need help :) Feel free to delete these lines once done")                          #DELETE ME !!
while True:
    print(" ")
    print(" ")
    print("1. Info")
    print("2. BMI calculator")
    print("3. Converters")
    print("4. Ana music playlist")
    print("5. Thinspo")
    print("6. Accountability")
    print("7. Other links")
    print("8. Weight log")
    print("9. Recovery")
    print("0. Exit AnaOS")
    selection = input("Make a Selection > ")
    print(" ")
    print(" ")
    if selection == "1":
        info_()
    elif selection == "2":
        bmiCalc()
    elif selection == "3":
        converters_()
    elif selection == "4":
        webbrowser.open("url for playlist",new=1) #Playlist (youtube/spotify/etc)
    elif selection == "5":
        webbrowser.open("url for thinspo",new=1) #Thinspo (imgur/tumblr/instagram)
    elif selection == "6":
        webbrowser.open("url for accountability",new=1) #Accountability (Personally use MPA forum here, but where ever you post yours)
    elif selection == "7":
        webbrowser.open("url for other links",new=1) #other links (Carrd maybe?)
    elif selection == "8":
        webbrowser.open("url for weightlog",new=1) # weight log 
    elif selection == "9":
        webbrowser.open("https://edresources.carrd.co/",new=1) #RECOVERY
    elif selection == "0":
        exit()
    