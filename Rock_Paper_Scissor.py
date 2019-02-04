import random

def Random(list):
    return random.choice(list)

def Handeler(choice, pc):
    #choice = eigen keuze
    #pc =  computer zijn keuze

    if choice == pc: # checkt of ze gelijk zijn
        result = "Draw"
    elif choice == "Rock": # als je voor rock kiest
        #vul in
    elif choice == "Paper": # als je voor paper kiest
        #vul in
    elif choice == "Scissors": # als je voor scissors kiest
        #vul in

    print("Uw keuze: " + choice + " Comps keuze: " + pc + ". Result: " + result)

list = ['Rock', 'Paper', 'Scissors']

loop = True
while loop: # de Loop zorgt dat blijft door gaan
    choice = input("Maak een keuze uit rock (r), paper (p) of scissors(s)")
    pc = Random(list) # laat de computer een random kiezen uit rock, paper, scissrs

    if choice == "r":
        Handeler("Rock", pc)
    elif choice == "p":
        Handeler("Paper", pc)
    elif choice == "s":
        Handeler("Scissors", pc)
    else:
        print("Something went wrong")

    if input("Wilt u doorgaan? (y/n)") == "n":
        loop = # verander de bool (True or False)
