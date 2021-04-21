#LIBRARIES
import tkinter as tk #import tk

#FUNCTIONS
def submitForm():
	#ent_destination.get()
	exit()

#MAIN
window = tk.Tk() #creates window
window.title('cnsolidtr') #sets window title

frame1 = tk.Frame(master=window, height=100)
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
btn_load = tk.Button(
	master=frame1,
	text='Load Config',
	height='1',
	width='20')
lbl_OR = tk.Label(
	master=frame1,
	text='-OR-',
	height='1',
	width='5')
btn_saveAs = tk.Button(
	master=frame1,
	text='Save Config As...',
	height='1',
	width='20')
btn_load.grid(column=0, row=0, padx=5, pady=2)
lbl_OR.grid(column=1, row=0, padx=5, pady=2)
btn_saveAs.grid(column=2, row=0, padx=5, pady=2)

frame2 = tk.Frame(master=window, width=200, height=100)
frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
lbl_destination = tk.Label(
	master=frame2,
	text='Select destination folder:')
btn_selectDestFolder = tk.Button(
	master=frame2,
	text='...',
	height='1',
	width='2')
ent_destination = tk.Entry(
	master=frame2,
	width='25')
lbl_destination.grid(column=0, row=1, padx=5, pady=2)
btn_selectDestFolder.grid(column=1, row=1, pady=2)
ent_destination.grid(column=2, row=1, padx=1, pady=2)

frame3 = tk.Frame(master=window, width=200, height=100)
frame3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
lbl_rules = tk.Label(
	master=frame3,
	text='Copy:')
chk_newestFiles = tk.Checkbutton(
	master=frame3,
	text='newest files ')
chk_otherOption = tk.Checkbutton(
	master=frame3,
	text='other option')
lbl_rules.grid(column=0, row=2, padx=5, pady=2)
chk_newestFiles.grid(column=1, row=2, padx=5, pady=2)
chk_otherOption.grid(column=2, row=2, padx=5, pady=2)

lbl_extension = tk.Label(
	master=frame3,
	text='Ending with')
ent_extension = tk.Entry(
	master=frame3,
	width='2')
#buttons that fill in some suggested extensions?
lbl_extension.grid(column=3, row=2, padx=0, pady=2)
ent_extension.grid(column=4, row=2, padx=0, pady=2)

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