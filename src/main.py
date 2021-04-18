#LIBRARIES
import tkinter as tk #import tk

#FUNCTIONS
def submitForm():
	ent_destination.get()
	exit()

#MAIN
window = tk.Tk() #creates window

lbl_greeting = tk.Label(
	text="welcme 2 cnsolidtr",
	fg="white",
	bg="black")
lbl_greeting.pack() #pack function adds widgets to window and resizes to fit

lbl_Destination = tk.Label(
	text="Select destination folder:")
ent_destination = tk.Entry(
	width=30)
lbl_Destination.pack()
ent_destination.pack()

btn_submit = tk.Button(
	text='CNSOLIDAT',
	default="active",
	height="1",
	width="50",
	command=submitForm)
btn_submit.pack()

window.mainloop() #waits for user input/events, any code after is blocked
									#until window is closed

#Open the applet. 

#Create a new file that'll hold all your settings for a project or 
#load up an existing one.

#You'll select a destination folder, then a bunch of folders you 
#want to pull the latest files from.

#Peruse the additional options if you like and hit the CNSOLIDAT button.
#auto save config to destination folder and run from there

#The script will run and now you'll have all your most recent 
#exports in a folder that you can hand striaght to your client!

#Best of all, now that it's set up you can run the same process 
#from the saved project file you've created again and again.