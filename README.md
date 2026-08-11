## Auto Typer – Python Desktop Automation Tool ##
A simple and interactive desktop automation application built with Python that automatically types user-provided text into any active application.
The project uses Tkinter for the graphical user interface and PyAutoGUI / Keyboard for controlling keyboard input. It also uses multithreading so that the GUI remains responsive while the typing process is running.

#Overview#
Typing the same content repeatedly can be time-consuming and repetitive.
Auto Typer was created to automate this process by allowing users to:
Enter the required text
Set a typing speed
Configure a starting delay
Choose how many times the text should be repeated
Pause and resume typing
Stop the process whenever required
Monitor typing progress
The application provides a simple dark-themed GUI for controlling the entire process.

#Technologies Used#
Python
Tkinter – GUI development
PyAutoGUI – Automated keyboard/mouse interaction
Keyboard – Keyboard input and global hotkeys
Threading – Running the typing process without freezing the GUI
Time – Delays and typing intervals

#Installation#
1. Clone the Repository
git clone https://github.com/yourusername/auto-typer.git
2. Navigate to the Project Folder
cd auto-typer
3. Install Required Libraries
pip install pyautogui keyboard
Tkinter is normally included with standard Python installations.
4. Run the Application
python auto_typer.py

#Concepts Learned#
This project helped me practice several important Python concepts:
Object-Oriented Programming
Tkinter GUI development
Event-driven programming
Multithreading
Keyboard automation
Global keyboard shortcuts
User input validation
Exception handling
Progress tracking
Working with external Python libraries

#Important Note#
This application controls keyboard input at the system level. Before starting the typing process, make sure the correct target application and input field are selected.
Use the Stop option or the PyAutoGUI failsafe if you need to interrupt the automation.
