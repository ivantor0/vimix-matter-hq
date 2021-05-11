if [ -d "/boot/grub" ]; then
    if [ -d "/boot/grub/themes/Matter" ]; then
        cp -rn Matter /boot/grub/themes
        cp Matter/theme.txt Matter/background.jpg Matter/font.pf2 /boot/grub/themes/Matter/
    else 
        mv Matter/theme.txt tmptheme.txt
        ./matter.py -i $* -hl 83B81A -fg FFFFFF -bg 282629
        mv tmptheme.txt Matter/theme.txt
        cp -r Matter /boot/grub/themes
    fi
    ./matter.py --seticons -i $*
    update-grub
elif [ -d "/boot/grub2" ]; then
    if [ -d "/boot/grub2/themes/Matter" ]; then
        cp -rn Matter /boot/grub2/themes
        cp Matter/theme.txt Matter/background.jpg Matter/font.pf2 /boot/grub2/themes/Matter/
    else 
        mv Matter/theme.txt tmptheme.txt
        ./matter.py -i $* -hl 83B81A -fg FFFFFF -bg 282629
        mv tmptheme.txt Matter/theme.txt
        cp -r Matter /boot/grub2/themes
    fi
    ./matter.py --seticons -i $*
    update-grub
else 
    echo "No /boot/grub nor /boot/grub2 found on your system!"
    echo "Check whether you have GRUB installed and where is it located at."
    exit 1
fi

