#!/bin/bash
# Shellbie installer.
# Currently assumes an Arch Linux-based system.
SCRIPT="Shellbie Installation Helper"
PKGS="mpg123 python python-pip links2 cowsay"
GTTS="gtts"
_error () {
    ERR_MSG="Oops, something went wrong. Please check logs."
    ERR_MSG2="Now exiting the Shellbie installation script - please correct errors and try again."
    echo "$ERR_MSG"
    sleep 1
    echo "$ERR_MSG2"
    sleep 1 && exit
}
download_pkgs () {
    # downloads the required packages for Shellbie
    echo "Installing needed packages for Shellbie..."
    sudo pacman -Sy $PKGS --noconfirm
    pip install $GTTS
    echo "Packages installed successfully."
    sleep 1
}
make_Shellbie_executable () {
    shellbie="shellbie.py"
    shellbie_exec_location="/usr/bin/shellbie"
    echo "Making Shellbie executable globally..."
    sleep 1
    chmod +x $shellbie
    sudo cp $shellbie $shellbie_exec_location
    echo "Done." && sleep 1
}
send_notification () {
    n_title="$SCRIPT"
    n_desc="Shellbie installation has finished."
    notify-send "$n_title" "$n_desc"
}
# Script begins here.
echo "$SCRIPT"
sleep 1
download_pkgs || _error
make_Shellbie_executable || _error
send_notification
echo "Script finished. You can now run Shellbie by invoking 'shellbie' in your terminal."
sleep 1 && exit
