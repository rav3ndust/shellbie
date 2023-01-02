#!/bin/bash
set -euo pipefail 
# Shellbie installer - Ubuntu/Debian version. 
# Sets up Shellbie's operating environment, assumes ubuntu/debian linux environment. 
SCRIPT="Shellbie Installation Helper" 
PKGS="mpg123 python3 python3-pip links2 cowsay"
GTTS="gtts"
_error() {
    # error handling.
    ERR_MSG="Oops, something went wrong. Please check logs."
    ERR_MSG2="Now exiting the Shellbie installation script - please correct errors and try again."
    echo "$ERR_MSG"
    sleep 1
    echo "$ERR_MSG2"
    sleep 1 && exit 
}
download_pkgs() {
    # downloads the required pkgs for shellbie. 
    echo "Installing needed packages for Shellbie..."
    sudo apt-get install $PKGS -y 
    pip install $GTTS
    echo "Packages installed successfully." 
    sleep 1
}
make_Shellbie_executable() {
    # makes Shellbie able to be run globally. 
    run_shellbie="python3 shellbie/shellbie.py"
    shellbie="shellbie.py"
    shellbie_launch_script="shellbieproxy.sh"
    shellbie_exec_location="/usr/bin/shellbie"
    echo "Making Shellbie executable gloabally..."
    sleep 1
    touch $shellbie_launch_script
    echo "$run_shellbie" >> $shellbie_launch_script
    chmod +x $shellbie_launch_script
    sudo cp $shellbie_launch_script $shellbie_exec_location
    echo "Done." && sleep 1
}
send_notification() {
    n_title="$SCRIPT"
    n_desc="Shellbie installation has finished."
    notify-send "$n_title" "$n_desc"
}
# Script begins here.
echo "$SCRIPT"
sleep 1
download_pkgs || _error
make_shellbie_executable || _error 
send_notification
echo "Script finished. You can now run Shellbie by invoking 'shellbie' in your terminal."
sleep 1 && exit
