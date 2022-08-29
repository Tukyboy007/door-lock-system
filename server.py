import os
import time
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO

led = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)

def res(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Command running: %s' % command
    if command == '/unlock':   
        bot.sendMessage(chat_id, 'Door unlocked')
        GPIO.output(led, GPIO.HIGH)
    if command == '/lock':
        bot.sendMessage(chat_id, 'Door locked')
        GPIO.output(led, GPIO.LOW)

bot = telepot.Bot('5465140429:AAEtNIMPQMZ40tdMqbWdtEnMeHDOUAaBGSA')
MessageLoop(bot, res).run_as_thread()
print 'Lock system started'
while 1:
    time.sleep(10)
