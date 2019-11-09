#!/bin/bash

# Bash Script to Install Open CV 3.4.7 on Raspbian Buster.
# Author: Nathan Cusack
# Date :  06/11/2019

check(){
	echo "WARNING!!!"
	echo "Have you Expanded Filesystem?"
	read ans

	case $ans in

		y)
			installOpenCV
			;;
		n)
			FileExpandInstruct
			;;
		*)
			echo -n "Error"
			;;
	esac
}

FileExpandInstruct(){
	echo "Please Expand Filesystem by doing the following"
	echo ""
	echo "	Run: sudo raspi-config"
	echo "	In the Config Menu go to '7 Advanced Options'"
	echo "	In Advanced Options select 'A1 Expand Filesystem'"
	echo "	Hit <Select>, then <Finish>"
	echo "	Then Reboot your Pi" 
}

installOpenCV(){

	echo "Reclaim Space for Pi"
	# Remove  Wolfram Engine and Libre softwares
	sudo apt-get purge wolfram-engine
	sudo apt-get purge libreoffice*
	sudo apt-get clean
	sudo apt-get autoremove

	echo "Update and Upgrade any existing Packages"
	sudo apt-get update && sudo apt-get upgrade

	echo"Installing Dependencies"
	sudo apt-get install build-essential cmake pkg-config
	sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
	sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
	sudo apt-get install libxvidcore-dev libx264-dev
	sudo apt-get install libfontconfig1-dev libcairo2-dev
	sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev
	sudo apt-get install libgtk2.0-dev libgtk-3-dev
	sudo apt-get install libatlas-base-dev gfortran
	sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
	sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
	# Install python3.7 Dev
	sudo apt-get install python3-dev
	wget https://bootstrap.pypa.io/get-pip.py
	sudo python get-pip.py
	sudo python3 get-pip.py
	sudo rm -rf ~/.cache/pip
	# Install Python
	sudo pip install virtualenv virtualenvwrapper
	

}

check
