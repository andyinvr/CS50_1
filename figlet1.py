import sys, random
from pyfiglet import Figlet


figlet = Figlet()

if len(sys.argv) == 1:
    rand_font = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    rand_font = False
else:
    print("Invalid usage")
    sys.exit(1)

#You can then get a list of available fonts with code like this:
figlet.getFonts()

if rand_font == False:
    try:
        figlet.setFont(font = sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = f)


word = input('Input: ')

#You can set the font with code like this, wherein f is the font’s name as a str:
#figlet.setFont(font=f)

#And you can output text in that font with code like this, wherein s is that text as a str:
print(f"Output: \n {figlet.renderText(word)}")