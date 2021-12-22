import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]


# Gets message

def get_message():
    global x, y

    position = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 70, y - 40, duration=.5)
    pt.tripleClick()
    pt.hotkey('ctrl', 'c')
    whatsapp_message = pyperclip.paste()
    pt.click
    print("message received: " + whatsapp_message)

    return whatsapp_message

# Posts
def post_response(message):
    global x, y

    position1 = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


# Processes responce
def process_responce(message):
    random_no = random.randrange(3)
    if "?" in str(message).lower():
        return "Don't ask me any questions!"
    else:
        if random_no == 0:
            return "That's cool"
        elif random_no == 1:
             return "Remember to call me!"
        else:
             return "I want to eat something"


# Check for new messages
def check_for_new_messages():
    pt.moveTo(x + 78, y - 45, duration=.5)

    while True:
        # Continuosly checks for green dot and new messages
        try:
            position = pt.locateOnScreen("green_circle.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No new users with new messages located")

            if  pt.pixelMatchesColor(int(x + 78), int(y - 45), (255, 255, 255), tolerance=10):
                print("is_white")
                processed_message = process_responce(get_message())
                post_response(processed_message)
            else:
                print("No new messages yet...")
                sleep(5)




check_for_new_messages()

