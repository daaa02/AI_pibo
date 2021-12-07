#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

echo "install openpibo os"
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1c7yACdRlR7aM87xkV0wY1ElHurEeKfhW' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1c7yACdRlR7aM87xkV0wY1ElHurEeKfhW" -O EOS_PIBO_211206_V2.7z && rm -rf /tmp/cookies.txt

echo "pip install openpibo"
sudo pip3 install openpibo-python

cd 
mkdir openpibo
cd openpibo

echo "install openpibo github"
git clone https://github.com/themakerrobot/themakerrobot.git
git clone https://github.com/themakerrobot/openpibo-python.git
git clone https://github.com/themakerrobot/openpibo-tools.git
git clone https://github.com/themakerrobot/openpibo-files.git
git clone https://github.com/themakerrobot/openpibo-examples.git

echo "reboot"
reboot

exit 0
