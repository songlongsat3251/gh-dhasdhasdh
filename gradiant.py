#!/usr/bin/python3
# TOOL BY DarkVPS
# DO NOT SELL THIS TOOL OR CHANGE THE CODE
import argparse
from sys import exit
from os import path

desc = """
Gradiant tool By DarkVPS
If you paid for this program you were scammed

How to use:
1) Put your banner in a text file
2) Run python3 gradiant.py banner.txt [color1] [color2]
3) To save your output to a text file, run python3 gradiant.py [color1] [color2] > output.txt

Colors can be specified by name or by using RGB values

Ex: python3 gradiant.py banner.txt yellow turquoise
    or
    python3 gradiant.py info.txt white grey

Colors list: pink,purple,blue,cyan,turquoise,lime,
                    green,white,grey,red,yellow
"""

clear="\033[0;00m"


colors = {
        'pink':(222,31,171),
        'purple':(81,15,138),
        'blue':(11,25,222),
        'cyan':(5,189,245),
        'turquoise':(14,161,129),
        'lime':(5,255,9),
        'green':(4,85,6),
        'white':(255,255,255),
        'grey':(50,50,50),
        'red':(252,8,8),
        'yellow':(255,202,0)
        }
def gradiant(startrgb,endrgb,text):
    changer = int((int(endrgb[0]) - int(startrgb[0]))/len(text))
    changeg = int((int(endrgb[1]) - int(startrgb[1]))/len(text))
    changeb = int((int(endrgb[2]) - int(startrgb[2]))/len(text))

    r = int(startrgb[0])
    g = int(startrgb[1])
    b = int(startrgb[2])

    for letter in text:
        print(f"\x1b[38;2;{r};{g};{b}m{letter}",end="")
        r+=changer
        g+=changeg
        b+=changeb

def validatergb(rgb):

    if not len(rgb) == 3:
        return False

    try:
        if 0 <= int(rgb[0]) <= 255 and 0 <= int(rgb[1]) <= 255 and 0 <= int(rgb[2]) <= 255:
            return True
        else:
            return False
    except ValueError:
        return False

def Main():
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("filename", type=str, help='The file to read from')
    parser.add_argument("color1",type=str,help='The first color of the gradiant')
    parser.add_argument("color2",type=str,help='The second color of the gradiant')
    args = parser.parse_args()

    color1 = args.color1.lower()
    color2 = args.color2.lower()

    if color1 in colors.keys():
        startcolor = colors.get(color1)
    elif validatergb(tuple(color1.split(','))):
        startcolor = tuple(color1.split(','))
    else:
        print('Invalid entry for color1. Use -h for help')
        exit(1)

    if color2 in colors.keys():
        endcolor = colors.get(color2)
    elif validatergb(tuple(color2.split(','))):
        endcolor = tuple(color2.split(','))
    else:
        print('Invalid entry for color2. Use -h for help')
        exit(1)

    if not path.exists(args.filename):
        print(f"Could not find file {args.filename}")
        exit(2)

    with open(args.filename, 'r', errors='replace') as f:
        for line in f.readlines():
            gradiant(startcolor,endcolor,line)
    print(clear)
if __name__ == '__main__':
    Main()
