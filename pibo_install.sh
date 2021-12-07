#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

echo "pip install openpibo"
sudo pip3 install openpibo-python

echo "install openpibo github"
cd ../openpibo
git clone https://github.com/themakerrobot/themakerrobot.git
git clone https://github.com/themakerrobot/openpibo-python.git
git clone https://github.com/themakerrobot/openpibo-tools.git
git clone https://github.com/themakerrobot/openpibo-files.git
git clone https://github.com/themakerrobot/openpibo-examples.git

echo "reboot"
reboot

exit 0
