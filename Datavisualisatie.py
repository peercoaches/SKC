import turtle as t
screen = t.getscreen()

def drawbord():
  t.color('black')
  t.width(5)
  t.penup()
  t.goto(-250, -250)
  t.pendown()
  for _ in range(4):
    t.forward(500)
    t.left(90)

def drawLine(Positions, color = 'blue'):
  t.color(color)
  t.width(5)
  t.penup()
  t.goto(-250, -250)
  t.pendown()

  TotalLength = len(Positions)

  for n in Positions:
    index = Positions.index(n) + 1
    yas = n - 250
    HorizontalPostion = int((float(index) / float(TotalLength) * 500) - 250)
    t.goto(HorizontalPostion, yas)

t.reset()
drawbord()

###########################
## Werken vanaf dit punt ##
###########################

# TODO 1: Maak een lijst aan met data.
GetallenReeks = [80, 10, 50, 90, 30]

# TODO 2: Zorg ervoor dat de lijn ook wordt weegegeven in de grafiek.
drawLine(GetallenReeks, 'Green')

# TODO 3: Voeg nog een derde set aan data toe aan de grafiek.
