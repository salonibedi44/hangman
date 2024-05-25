import os
from time import sleep

frame = ["\t\t\t\t\t     _______"]
frame += ["\t\t\t\t\t     |     |"]
frame += ["\t\t\t\t\t           |" for x in range(11)]
frame += ["\t\t\t\t\t        ___|___"]

def add_head():
    frame[1] = "\t\t\t\t\t    _|_    |"
    frame[2] = "\t\t\t\t\t   |   |   |"
    frame[3] = "\t\t\t\t\t   |   |   |"
    frame[4] = "\t\t\t\t\t    \_/    |"
def add_face():
    frame[2] = "\t\t\t\t\t   |o o|   |"
    frame[3] = "\t\t\t\t\t   |'_'|   |"

def add_torso():
    for x in range(5):
        frame[x + 5] = "\t\t\t\t\t     |     |"

def add_right_arm():
    frame[6] = "\t\t\t\t\t     | /   |"
    frame[7] = "\t\t\t\t\t     |/    |"

def add_left_arm():
    frame[6] = "\t\t\t\t\t   \ | /   |"
    frame[7] = "\t\t\t\t\t    \|/    |"

def add_right_leg():
    frame[10] = "\t\t\t\t\t      \    |"
    frame[11] = "\t\t\t\t\t       \   |"

def add_left_leg():
    frame[10] = "\t\t\t\t\t    / \    |"
    frame[11] = "\t\t\t\t\t   /   \   |"


operations = [add_head, add_face, add_torso, add_right_arm, add_left_arm, add_right_leg, add_left_leg]

guesses = []

word = "bellow"
found = ["_" for x in range(len(word))]
indices = {}
for ind, char in enumerate(word): 
    if char in indices: indices[char]+=[ind]
    else: indices[char] = [ind]

attempts = 0

won = False

while attempts < len(operations):

    os.system("clear")
    for line in frame: print(line, flush = True)
    print("\n\n\t\t\t\t\t   " + ' '.join(found) + "\n\n")

    char = input("What character do you guess? ")

    #handle the character

    if char in guesses: 
        print("You already guessed the letter " + char + "!")

    elif char in indices:
        for ind in indices[char]: found[ind] = char
        if '_' not in found: break

    else:
        attempts+=1
        operations[attempts - 1]()

    guesses+=[char]
    
os.system("clear")

if attempts < len(operations):
    print("Good job!! You got the word: " + word)
else:
    print("Do better...")
    frame[2] = "\t\t\t\t\t   |x x|   |"
    frame[3] = "\t\t\t\t\t   | 0 |   |"

    for line in frame: print(line, flush = True)

