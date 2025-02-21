import os 
import time 

print("Welcome to the PigOS python installer!") 
answer = input('Start installer? [y/n]:') 
if answer == "n":
    exit()
if answer == "y":
    browserchoose = input('Install Firefox? [y/n]:') 
    if browserchoose == "y":
            os.system('sudo pacman -S --noconfirm firefox') 
            if browserchoose == "n":
                browserchoose2 = input('Install Chromium? [y/n]:') 
                if browserchoose2 == "y":
                    os.system('sudo pacman -S --noconfirm chromium')
xorginstall = input('Install Xorg? [y/n]:')
if xorginstall == "y":
    os.system ('sudo pacman -S --noconfirm xorg xorg-xinit mesa sddm sddm-kcm')
    os.system('sudo systemctl enable sddm')
    cinnamoninstall = input('Install Cinnamon? [y/n]:')
    if cinnamoninstall == "y":
        os.system('sudo pacman -S --noconfirm cinnamon')
baseutils = input('Install basic utils? [y/n]:')
if baseutils == "y":
    os.system('sudo pacman -S --noconfirm xed eog vim gnome-terminal nemo mpv ffmpeg mpg123 ncdu zip unzip wget curl jdk-openjdk')
multimedia = input('Install multimedia programs? [y/n]:') 
if multimedia == "y": 
    os.system('sudo pacman -S --noconfirm obs-studio gimp kdenlive')
virtual = input('Install VirtualBox? [y/n]:')
if virtual == "y":
    os.system('sudo pacman -S --noconfirm virtualbox')
    os.system('modprobe vboxdrv')
time.sleep(3)
print("The installation of the custom components is complete. Move on to system configuration...") 
os.system('sudo localectl set-x11-keymap --no-convert us,ru pc105 "" grp:alt_shift_toggle')
os.system('sudo localectl set-locale ru_RU.UTF-8')
os.system('echo "FONT=cyr-sun16" > /etc/vconsole.conf') 
os.system('sudo systemctl restart vconsole')

print("Installation complete")
print("now rebooting pc")
os.system('sudo reboot') 
