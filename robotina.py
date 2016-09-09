""" A simple Telegram bot to get photos from a camera """

import cv2
import telepot
import time

TOKEN = "PUT HERE YOUR TELEGRAM TOKEN"
PHOTO = 'test.png'
CAM_PORT = 0

bot = telepot.Bot(TOKEN)

def take_photo():
    camera = cv2.VideoCapture(CAM_PORT)
    # Wait some time to get ligth in the camera
    time.sleep(0.5)
    rc, image = camera.read()
    if rc:
        cv2.imwrite(PHOTO, image)
    del(camera)

    return rc      

def send_photo(chat_id, photo_path, caption):
    with open(photo_path, 'rb') as photo:
        bot.sendPhoto(chat_id, photo, caption)

def handle_messages(msg):
    """ The entry point to the message reception """
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        text = msg['text']
        if text == '/getphoto':
            if take_photo():
                send_photo(chat_id, PHOTO, 'This is a test caption')
            else:
                bot.SendMessage(chat_id, 'A problem occurred taking the photo')
        else:
            error_msg = "No se de que me hablas!"
            # error_msg = "I don't know what are you talking about!"
            bot.sendMessage(chat_id, error_msg)

bot.message_loop(handle_messages)
print('Listen messages...')

while True:
    time.sleep(5)
