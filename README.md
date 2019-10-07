# Premises-Security-Project
FYP: Security Project using ANPR

Premises security system using Automatic Number Plate Recognition

For my final year project, I will be designing a home security system using Automatic Number Plate recognition (ANPR). This project will be designed to run on a Raspberry Pi Model 4, with Pi Camera, using Open CV and Python for ANPR and Pin out on the Raspberry Pi, C++ for data parsing and python for a web page.

Description
Then concept of my project is that the raspberry pi will continuously scan for licence plates of vehicles. When a number plate is detected, a picture will be sent to server, and the owner of the house will be notified. If the number plate matches an approved set of number plates (curated by the homeowner) then the system will open the set of electric gates and allow the vehicle to enter.  Other features of the system include:
•	Notifying the homeowner when a known number plate is detected
•	A user interface that give ability to add/remove known number plates to the system
•	Database of pictures with relevant information (Date, time, number plate, accuracy)
•	Homeowner granting access to premise remotely
•	If a vehicle is detected for more than 1 minute, the system will record video and alert the homeowner.
•	A keypad to enter a pin to allow access.

Project Break Down
Software
For this project, I plan mainly to use python with Open CV for the ANPR and the electric gates. The system will run on a Raspbian, a Linux based OS designed for the raspberry pi. The web server will be designed using HTML, JavaScript and CSS and will also run using python. 
	Hardware
I plan to use the latest release of the Raspberry Pi model 4 with 4GB of Ram, as well as the newest Pi Camera which offers 1080p resolution at 30 frames per second. 
For the electric gates I planned to create a scaled version using my 3D printer and 2 servo motor and a keypad directly connected to the Raspberry Pi
