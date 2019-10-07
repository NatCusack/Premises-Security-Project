# Premises-Security-Project
FYP: Security Project using ANPR

<h1>Premises security system using Automatic Number Plate Recognition</h1>

For my final year project, I will be designing a home security system using Automatic Number Plate recognition (ANPR). This project will be designed to run on a Raspberry Pi Model 4, with Pi Camera, using Open CV and Python for ANPR and Pin out on the Raspberry Pi, C++ for data parsing and python for a web page.

<h3>Description</h3>
Then concept of my project is that the raspberry pi will continuously scan for licence plates of vehicles. When a number plate is detected, a picture will be sent to server, and the owner of the house will be notified. If the number plate matches an approved set of number plates (curated by the homeowner) then the system will open the set of electric gates and allow the vehicle to enter.  Other features of the system include:

<ul>
	<li>Notifying the homeowner when a known number plate is detected</li>
	<li>A user interface that give ability to add/remove known number plates to the system</li>
	<li>Database of pictures with relevant information (Date, time, number plate, accuracy)</li>
	<li>Homeowner granting access to premise remotely</li>
	<li>If a vehicle is detected for more than 1 minute, the system will record video and alert the homeowner</li>
	<li>A keypad to enter a pin to allow access</li>
</ul>

<h3>Project Break Down</h3>
<h4>Software</h4>
For this project, I plan mainly to use python with Open CV for the ANPR and the electric gates. The system will run on a Raspbian, a Linux based OS designed for the raspberry pi. The web server will be designed using HTML, JavaScript and CSS and will also run using python. 
<h4>Hardware</h4>
I plan to use the latest release of the Raspberry Pi model 4 with 4GB of Ram, as well as the newest Pi Camera which offers 1080p resolution at 30 frames per second. 
For the electric gates I planned to create a scaled version using my 3D printer and 2 servo motor and a keypad directly connected to the Raspberry Pi

<img src="https://westeurope1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=jpeg&cs=fFNQTw&docid=https%3A%2F%2Fgalwaymayoinstitute-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!WV4pOYfQP0uy-482zorbsWlKn6EeF7ZLoFkbxDDDleX9SC-VfbUgTJIYFOw5gWtC%2Fitems%2F01SP5L7KBZEWFCD3FPXRGYJK5VO4FFQYRA%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZ2Fsd2F5bWF5b2luc3RpdHV0ZS1teS5zaGFyZXBvaW50LmNvbUA4ZjA2Y2ZhZS0yMmQ1LTRjODQtYTQ2ZC0zZGJlM2M5MzU1OGQiLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNTcwNDYxMDkyIiwiZXhwIjoiMTU3MDQ4MjY5MiIsImVuZHBvaW50dXJsIjoiNXdpeVBHMGUwbmVNVUUvUGw4VTg1T3MxRHREM1ljRnVKKzZBblFjN3VLTT0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyOSIsImlzbG9vcGJhY2siOiJUcnVlIiwiY2lkIjoiTXpVNFpqQmlPV1l0TlRCbVl5MDVNREF3TFRkbE1UVXROakkyTVdNeVlXWmhNVFUyIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik16a3lPVFZsTlRrdFpEQTROeTAwWWpObUxXSXlabUl0T0dZek5tTmxPR0ZrWW1JeCIsIm5hbWVpZCI6IjAjLmZ8bWVtYmVyc2hpcHxnMDAzMzgzMDZAZ21pdC5pZSIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDM3ZmZlOTM5MTJhNzJAbGl2ZS5jb20iLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMiJ9.QVcrb2VWNkhqaXZCTUNUYXZTWFg5RWFpbG4wVDljQlZ1MTdYRzJIUzFwTT0&encodeFailures=1&srcWidth=&srcHeight=&width=1280&height=873&action=Access">
