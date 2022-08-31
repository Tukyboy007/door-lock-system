# door-lock-system

#Bot name && link

Door-locker

http://t.me/locker007_bot

Create Telegram Bot
 
@BotFather ->> Search on telegram. Create and manage bots.

# Create python script to communicate with the  bot from the PLC

$sudo apt-get install python-pip

$sudo pip install telepot

# Python script server code ->> "./server.py"

# Python script running with handle.
   $python server.py

#Python script as service through systemctl/systemd

    $sudo nano /etc/systemd/system/locksystem.service

#systemctl/systemd code ->> "./locksystem.service"

 $ sudo apt-get install -y systemd
 $ systemd --version --> show version

#service control on CLI

  $sudo systemctl daemon-reload
  $sudo systemctl enable locksystem.service
  $sudo systemctl start locksystem.service
# 
