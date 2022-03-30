#!/bin/bash
#
# install stuff for Little Assistant
first="Would you like to install Assistant dependencies?" 
installing="Installing needed stuff for Assistant..."
done_installing="Needed stuff for Assistant installed." 
updater=$(sudo apt update -y) 
materials=$(sudo apt install links2 python3 cowsay -y)
sleep1=$(sleep 1) 
function installingStuff() {
	echo($installing) 
	$updater && $materials
	echo($done_installing) 
	$sleep1
	echo "Exiting..." 
	$sleep1
	exit
}
function xxExit() {
	echo "Okay. Not installing." 
	$sleep1
	exit
}
function inValid() {
	echo "Invalid key pressed. Exiting." 
	$sleep1
	exit 
}
######################
# script begins:
######################
echo($first) 
read -p "Type 'Yes' if you want to install, or 'No' if you don't: " installYN
if [[ $installYN == "Yes" ]]
then
	installingStuff
elif [[ $installYN == "No" ]]
then 
	xxExit
else 
	inValid
fi 