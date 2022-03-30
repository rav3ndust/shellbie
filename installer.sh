#!/bin/bash
#
# install stuff for Little Assistant
######################################
# vars
######################################
first="Would you like to install Assistant dependencies?" 
installing="Installing needed stuff for Assistant..."
done_installing="Needed stuff for Assistant installed." 
updater=$(sudo apt update -y) 
materials=$(sudo apt install links2 python3 cowsay -y)
sleep1=$(sleep 1) 
notify1=$(notify-send "Little Linux Assistant" "Assistant dependencies installed.")
notify2=$(notify-send "Little Linux Assistant" "Dependencies installation cancelled.")
cancelling="Okay. Not installing." 
cancelling2="Invalid key pressed. Exiting."
######################################
# functions
######################################
function installingStuff() {
	echo($installing) 
	$updater && $materials
	echo($done_installing) & $notify1 
	$sleep1
	echo "Exiting..." 
	$sleep1
	exit
}
function xxExit() {
	echo($cancelling) & $notify2
	$sleep1
	exit
}
function inValid() {
	echo($cancelling2) & $notify2 
	$sleep1
	exit 
}
######################
# script begins:
######################
echo($first) 
read -p "Type 'Yes' if you want to install, or 'No' if you don't: " installYN
if [[ $installYN == "Yes" ]] || [[ $installYN == "yes" ]]
then
	installingStuff
elif [[ $installYN == "No" ]] || [[ $installYN == "no" ]] 
then 
	xxExit
else 
	inValid
fi 