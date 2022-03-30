#!/bin/bash
# install stuff for Little Assistant
######################################
# vars
######################################
first=$(echo "Would you like to install Assistant dependencies?") 
installing=$(echo "Installing needed stuff for Assistant...")
done_installing=$(echo "Needed stuff for Assistant installed.") 
updater=$(sudo apt update -y) 
materials=$(sudo apt install links2 python3 cowsay libnotify-bin -y)
sleep1=$(sleep 1) 
notify1=$(notify-send "Little Linux Assistant" "Assistant dependencies installed.")
notify2=$(notify-send "Little Linux Assistant" "Dependencies installation cancelled.")
cancelling=$(echo "Okay. Not installing.") 
cancelling2=$(echo "Invalid key pressed. Exiting.")
all_ops=$(echo "All operations finished.") 
######################################
# functions
######################################
function installingStuff() {
	$installing 
	$updater && $materials
	$done_installing & $notify1 
	$sleep1
	$all_ops
	$sleep1 
	echo "Exiting..." 
	$sleep1
	exit
}
function xxExit() {
	$cancelling & $notify2
	$sleep1
	exit
}
function invalid_Input() {
	$cancelling2 & $notify2 
	$sleep1
	exit 
}
######################
# script begins:
######################
$first 
read -p "Type 'Yes' if you want to install, or 'No' if you don't: " installYN
if [[ $installYN == "Yes" ]] || [[ $installYN == "yes" ]]
then
	installingStuff
elif [[ $installYN == "No" ]] || [[ $installYN == "no" ]] 
then 
	xxExit
else 
	invalid_Input
fi 