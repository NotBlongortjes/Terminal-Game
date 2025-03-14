import time
import sys
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import threading


def show_popup():
    # Create a Tkinter window for the pop-up
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("WARNING", "THERE IS NO ESCAPE!")
    root.destroy()  # Close the pop-up window

def block_alt_f4():
    while True:
        try:
            pass  # Keeps running, your game logic continues
        except KeyboardInterrupt:
            show_popup()  # Triggers when Alt+F4 is pressed

alt_f4_thread = threading.Thread(target=block_alt_f4)
alt_f4_thread.daemon = True  # Allow the thread to exit when the main program ends
alt_f4_thread.start()

def open_fullscreen_terminal():
    # Check if the script is already running in the terminal
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        # Actual script logic starts here
        print("Running in full-screen mode!")
    else:
        # Launch a new full-screen terminal window
        subprocess.Popen(["powershell", "-Command", "Start-Process cmd -ArgumentList '/c python your_script.py run' -WindowStyle Maximized"])
        subprocess.Popen(["powershell", "-Command", "(new-object -com wscript.shell).SendKeys('{F11}')"])

if __name__ == "__main__":
    open_fullscreen_terminal()
os.system('cls' if os.name == 'nt' else 'clear')

# Corrected slow_print function with two parameters: text and delay
def slow_print(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print('')  # Move to the next line after printing

def check_input_Y(choice):
    choice = choice.lower()
    if choice == "y" or choice =="yes" or choice =='yuh uh' or choice=="ja" or choice=="yup" or choice=="ye":
        return True
    else:
        return False
    
def check_input_N(choice):
    choice = choice.lower()
    if choice == "n" or choice =="no" or choice =="nuh uh" or choice=="neh" or choice=="nah" or choice=="ne":
        return True
    else:
        return False
    
def check_input_A(choice):
    choice = choice.lower()
    if choice == "a":
        return True
    else:
        return False
    
def check_input_B(choice):
    choice = choice.lower()
    if choice == "b":
        return True
    else:
        return False
    
def check_input_C(choice):
    choice = choice.lower()
    if choice == "c":
        return True
    else:
        return False
    
def check_input_D(choice):
    choice = choice.lower()
    if choice == "d":
        return True
    else:
        return False
    

slow_print("Welcome. Before we start, i need to ask you a few questions...", 0.05)

finished = False
valid_answer = False
while not valid_answer and not finished:
    slow_print("Do you wish to proceed??? (Y/N)", 0.05)

    choice = input()
    if check_input_Y(choice) :
        valid_answer = True
        finished = True
    elif check_input_N(choice):
        slow_print("...", 0.75)
        sys.exit()
        valid_answer = False
    else:
        slow_print("Error, Error, try Again", 0.05)




valid_answer = False
finished = False
os.system('cls' if os.name == 'nt' else 'clear')
while not valid_answer and not finished:
    time.sleep(0.25)
    slow_print("WARNING: \nThis is not just a test. \nThe more you answer, the more you reveal about yourself. \nThe more you reveal, the harder it becomes to escape. \nYou will not be allowed to close this window until the test is complete. \nIf you feel uncomfortable at any time, you are not imagining it.", 0.010)
    time.sleep(1)
    slow_print("Do you really want to proceed??? (Y/N)", 0.05)

    choice = input()
    if check_input_Y(choice) :
        valid_answer = True
        finished = True
    elif check_input_N(choice):
        slow_print("...", 0.75)
        sys.exit()
        valid_answer = False
    else:
        slow_print("Error, Error, try Again", 0.05)
    
valid_answer = False
finished = False
os.system('cls' if os.name == 'nt' else 'clear')
while not valid_answer and not finished:
    time.sleep(0.5)
    slow_print("The Survey shall start in:", 0.05)
    slow_print("3", 0.05)
    time.sleep(1)
    slow_print("2", 0.05)
    time.sleep(1)
    slow_print("1", 0.05)
    time.sleep(1)

    slow_print("The survey has been started. There is no Escape", 0.05)
    valid_answer = True
    finished = True


valid_answer = False
finished = False
os.system('cls' if os.name == 'nt' else 'clear')
while not valid_answer and not finished:
    time.sleep(2)
    slow_print("Are you currently alone? (Y/N)", 0.05)

    choice = input()
    if check_input_Y(choice) :
        slow_print("Are you sure?", 0.01)
        valid_answer = True
        finished = True
    elif check_input_N(choice):
        slow_print("Yes, you aren't :)", 0.25)
        slow_print("I'm inside", 0.01)
        os.system('cls' if os.name == 'nt' else 'clear')
        valid_answer = True
        finished = True
    else:
        slow_print("Error, Error, try Again", 0.05)

valid_answer = False
finished = False
os.system('cls' if os.name == 'nt' else 'clear')
while not valid_answer and not finished:
    time.sleep(0.5)
    slow_print("What is your name?", 0.05)
    user_name = input()
    valid_answer = True
    finished = True

valid_answer = False
finished = False
os.system('cls' if os.name == 'nt' else 'clear')
while not valid_answer and not finished:
    time.sleep(0.5)
    slow_print(f"{user_name}, are you comfortable right now :)? (Y/N)", 0.05)
    slow_print("answer", 0.025)
    slow_print("answer", 0.025)
    slow_print("answer", 0.025)
    slow_print("answer", 0.025)
    slow_print("answer", 0.025)

    choice = input()
    if check_input_Y(choice) :
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        valid_answer = True
        finished = True
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(5)
        sys.exit()
    elif check_input_N(choice):
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("Don't make him see you...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        slow_print("...", 0.001)
        valid_answer = True
        finished = True
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(5)
        sys.exit()
    else:
        slow_print("Error, Error, try Again", 0.05)