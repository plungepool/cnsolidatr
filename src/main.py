#LIBRARIES
import tkinter as tk #import tk

#FUNCTIONS
def submitForm():
	#ent_destination.get()
	exit()

#MAIN
window = tk.Tk() #creates window
window.title('cnsolidtr') #sets window title

# lbl_greeting = tk.Label(
# 	text="welcme 2 cnsolidtr",
# 	fg="white",
# 	bg="black")
# lbl_greeting.pack() #pack function adds widgets to window and resizes to fit

btn_load = tk.Button(
	text='Load Config',
	height='1',
	width='20')
lbl_OR = tk.Label(
	text='-OR-',
	height='1',
	width='10')
btn_saveAs = tk.Button(
	text='Save Config As...',
	height='1',
	width='20')
btn_load.pack()
lbl_OR.pack()
btn_saveAs.pack()

lbl_destination = tk.Label(
	text='Select destination folder:')
btn_selectDestFolder = tk.Button(
	text='...',
	height='1',
	width='2')
ent_destination = tk.Entry(
	width='30')
lbl_destination.pack()
btn_selectDestFolder.pack()
ent_destination.pack()

lbl_rules = tk.Label(
	text='Copy:')
chk_newestFiles = tk.Checkbutton(
	text='newest files')
lbl_rules.pack()
chk_newestFiles.pack()

lbl_extension = tk.Label(
	text='Ending with')
ent_extension = tk.Entry(
	width='2')
#buttons that fill in some suggested extensions?
lbl_extension.pack()
ent_extension.pack()

lbl_sources = tk.Label(
	text='From these locations:')
btn_selectSourceFolder = tk.Button(
	text='Add source folder...')
txt_sources = tk.Text(
	height='8',
	width='40')
lbl_sources.pack()
btn_selectSourceFolder.pack()
txt_sources.pack()

lbl_options = tk.Label(
	text='Options:')
chk_deleteOld = tk.Checkbutton(
	text='Delete old files in destination folder')
chk_backupOld = tk.Checkbutton(
	text='Backup old files in destination folder')
lbl_options.pack()
chk_deleteOld.pack()
chk_backupOld.pack()

btn_submit = tk.Button(
	text='CNSOLIDAT',
	default='active',
	height='1',
	width='50',
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