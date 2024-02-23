





!#/bin/bash
#VARIABLE
clear
blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'


echo -e "$red░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗"
echo -e "$red██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝"
echo -e "$red███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░"
echo -e "$red██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░"
echo -e "$red██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗"
echo -e "$red╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"

echo -e "$white░██╗░░░░░░░██╗███████╗██████╗░"
echo -e "$white░██║░░██╗░░██║██╔════╝██╔══██╗"
echo -e "$white░╚██╗████╗██╔╝█████╗░░██████╦╝"
echo -e "$white░░████╔═████║░██╔══╝░░██╔══██╗"
echo -e "$white░░╚██╔╝░╚██╔╝░███████╗██████╦╝"
echo -e "$white░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░"
echo -e ""
echo -e "$red[$green~$red] Author :$white Dimax66"
echo -e "$red[$green~$red] Team :$white Padang Sistem Error"
echo -e "$red[$green~$red] Tools :$white Attacker Web"
echo -e "$red[$green~$red] Telegram :$white https://t.me/PadangSystemError"
echo -e "$red[$green~$red] github :$white https://github.com/EscobarPadang"
echo ""

echo -e "$red[$green 01 $red]$green Cracked Cpanel+Checker"
echo -e "$red[$green 02 $red]$green Shell Finder+Checker Shell"
echo -e "$red[$green 03 $red]$green DDOS"
echo -e "$red[$green 04 $red]$green Wordpress Brute Force Multi CMS"
echo -e "$red[$green 05 $red]$green AutoXploit"
echo -e "$red[$green 06 $red]$green Scanner Login WordPress"
echo -e "$red[$green 07 $red]$green Proxy Checker"
echo -e "$red[$green 08 $red]$green Laravel"
echo -e "$red[$green 09 $red]$green Get SMTP"
echo -e "$white"
read -p "MENU :" act;

if [ $act = 1 ] || [ $act = 01 ]
then
clear
sleep 3

apt install python
cd asset
cd cpanel
python karma.py

fi

if [ $act = 2 ] || [ $act = 02 ]
then
clear
sleep 3

echo -e "$red[$green C $red]$green FIND"
echo -e "$red[$green B $red]$green CHECKER SHELL"
echo -e "$white"
read -p "MENU :" ac;

fi

if [ $ac = a ] || [ $ac = A ]
then
clear
sleep 3

cd asset
cd shell
apt install python
python SFind.py

fi

if [ $ac = b ] || [ $ac = B ]
then
clear
sleep 3

cd asset
cd shell
apt install python
python shell_checker.py

fi

if [ $act = 3 ] || [ $act = 03 ]
then
clear
sleep 3

cd asset
cd pandora
apt install python
python ddos.py

fi

if [ $act = 4 ] || [ $act = 04 ]
then
clear
sleep 3

cd asset
cd wp
apt install python
python multi.py

fi

if [ $act = 5 ] || [ $act = 05 ]   
then                                                              
clear
sleep 3                                    
cd asset
cd exploit
apt install python
python exploit.py

fi

if [ $act = 6 ] || [ $act = 06 ]
then
clear
sleep 3
cd asset
cd exploit
apt install python
python scanner.py

fi

if [ $act = 7 ] || [ $act = 07 ]
then
clear
sleep 3
cd asset
cd exploit
apt install python
python proxy.py

fi

if [ $act = 8 ] || [ $act = 08 ]
then
clear
sleep 3
cd asset
cd exploit
apt install python
python laravel.py

fi

if [ $act = 9 ] || [ $act = 09 ]
then
clear
sleep 3
cd asset
cd get
apt install python
python GetSMTP.py

fi
