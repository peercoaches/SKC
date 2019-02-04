import random

def Random(list):
    return random.choice(list)

Words = ["tweevoud", "retour", "personeel"] #voeg eigen worden toe als je dat wil

Word = Random(Words) #kiest random woord uit de lijst

choices = []
chances = 10

game = True
while game:
    print("U heeft nog " + str(chances) + " beurten")
    print('Uw gekozen letters: ' + str(choices))
    #laat speler een keuze maken om een letter in te vullen
    choices.append('''voeg gemaakte keuze toe''')

    output = ""

    for i in range(len(Word)):
        if Word[i] in '''selecteer variable om te vergelijken''':
            output += Word[i]
        else:
            output += "_"

    #print de output
    #chances moet verminderen

    #create win/lose condition
