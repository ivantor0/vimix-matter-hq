import re
import sys

from os.path import exists
from shutil import move
from matter import PALETTE


def main():
    if len(sys.argv) not in (3, 4):
        raise AttributeError("Please check if you have entered font and its name in hyphens or color and two color names.")
    
    if sys.argv[1] == "font":
        
        if len(sys.argv) != 3:
            raise AttributeError("Please put your font name into hyphens.")
        
        if not exists("font.pf2"):
            raise FileNotFoundError("Please check that you have converted the font first and saved the result as font.pf2.")
        
        font_name = sys.argv[2]
        
        with open("Matter/theme.txt", "r") as f:
            t = f.read()
        
        t = re.sub(r'font = ".*?"', 'font = "' + font_name + '"', t)
        
        with open("Matter/theme.txt", "w") as f:
            f.write(t)
        
        move("font.pf2", "./Matter/font.pf2")
    
    elif sys.argv[1] == "color":
        
        if len(sys.argv) != 4:
            raise AttributeError("Please check if you have entered general_color and selection_color.")
        
        regular_color = PALETTE[sys.argv[2]] if sys.argv[2] in PALETTE else sys.argv[2].upper()
        selected_color = PALETTE[sys.argv[3]] if sys.argv[3] in PALETTE else sys.argv[3].upper()
        
        if not re.search(r"^[0-9A-F]{6}$", regular_color):
            raise AttributeError("Please check if you have entered a valid general_color name or HEX signature.")
        
        if not re.search(r"^[0-9A-F]{6}$", selected_color):
            raise AttributeError("Please check if you have entered a valid selection_color name or HEX signature.")
        
        with open("Matter/theme.txt", "r") as f:
            t = f.read()
        
        t = re.sub(r'item_color = ".*?"', 'item_color = "' + regular_color + '"', t)
        t = re.sub(r'selected_item_color = ".*?"', 'selected_item_color = "' + selected_color + '"', t)
        
        with open("Matter/theme.txt", "w") as f:
            f.write(t)
    
    else:
        raise NotImplementedError("Either you have mistyped the attributes, or this option is not implemented (yet?)")


if __name__ == "__main__":
    main()

