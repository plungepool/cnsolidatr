#LIBRARIES
# import tkinter as tk #import tk
from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
import subprocess

#FUNCTIONS
def loadConfig():
	global configLocation
	loadFile = filedialog.askopenfilename()
	configLocation = loadFile
	txt_sources.delete("1.0", END)
	with open(loadFile) as fp:
		line = fp.readline()
		dest = 0
		while line:
			if dest == 0:
				destinationDir.set(line)
				dest = 1
			else:
				line = fp.readline()
				txt_sources.insert(END, line)
		txt_sources.delete("end-5c", END)
		# options.set("B")
	return configLocation

def saveConfigAs():
	global configLocation
	configLocation = filedialog.asksaveasfilename()
	configFile = open(configLocation, "x")
	configFile.close()
	return configLocation

def selectDestination():
	directory = filedialog.askdirectory()
	destinationDir.set(directory)

def selectSource():
	directory = filedialog.askdirectory()
	txt_sources.insert(END, directory)
	txt_sources.insert(END, '\n')

def submitForm():
	if not ent_destination.get() or not txt_sources.get('1.0'):
		messagebox.showerror(title="Error", message="Please select destination folder and at least one source folder.")
	elif not configLocation:
		saveConfigAs()
	args = str(options.get())
	configFile = open(configLocation, "w")
	configFile.write(ent_destination.get())
	configFile.close()
	configFile = open(configLocation, "a")
	configFile.write(txt_sources.get("1.0","end-1c"))
	configFile.write("\n#end")
	configFile.close()
	subprocess.call(['./copyscript.sh', args, configLocation])
	exit()

#MAIN
root = Tk()
root.title('cnsolidtr') #sets window title
myFont = font.Font(
	family='Courier', 
	size='18')

bgColor = 'white'
textColor = 'black'
btntxtColor = 'black'
fieldColor = "#f0f0f0"

#VARS
global configLocation
configLocation = ''
destinationDir = StringVar()
destinationDir.set("")
sourceDir = StringVar()
options = IntVar(None, "1")

#Frame Setup
frame=Frame(root, background=bgColor)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)

grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=3, row=5, columnspan=1)
Grid.columnconfigure(frame, 0, weight=1)
Grid.columnconfigure(frame, 1, weight=1)
Grid.rowconfigure(frame, 0, weight=1)

# Responsive Frame
for x in range(2):
	Grid.columnconfigure(frame, x, weight=1)
for y in range(5):
	Grid.rowconfigure(frame, y, weight=1)

# Row 0 : Save/Load
btn_load = Button(
	master=frame,
	text='Load Config',
	height='2',
	width='20',
	highlightbackground=bgColor,
	fg=btntxtColor,
	command=loadConfig)
btn_saveAs = Button(
	master=frame,
	text='Save Config As...',
	height='2',
	width='20',
	highlightbackground=bgColor,
	fg=btntxtColor,
	command=saveConfigAs)
btn_load['font'] = myFont
btn_saveAs['font'] = myFont
btn_load.grid(column=0, row=0, padx=8, pady=1)
btn_saveAs.grid(column=1, row=0, padx=8, pady=1)

# Row 1 : Set Destination
lbl_destination = Label(
	master=frame,
	text='Select destination\nfolder:',
	bg=bgColor,
	fg=textColor)
btn_selectDestFolder = Button(
	master=frame,
	text='...',
	height='1',
	width='3',
	highlightbackground=bgColor,
	fg=btntxtColor,
	command=selectDestination)
ent_destination = Entry(
	master=frame,
	width='15',
	highlightbackground=bgColor,
	bg=fieldColor,
	fg=btntxtColor,
	textvariable=destinationDir)
lbl_destination['font'] = myFont
btn_selectDestFolder['font'] = myFont
ent_destination['font'] = myFont
lbl_destination.grid(column=0, row=1, padx=8, pady=1)
btn_selectDestFolder.grid(column=1, row=1, sticky=W, padx=8, pady=1)
ent_destination.grid(column=1, row=1, padx=8, pady=1)

# Row 2 - 3 : Sources 
lbl_sources = Label(
	master=frame,
	text='Copy newest files\nfrom these locations:',
	bg=bgColor,
	fg=textColor)
btn_selectSourceFolder = Button(
	master=frame,
	text=' Add source folder... ',
	height='2',
	highlightbackground=bgColor,
	fg=btntxtColor,
	command=selectSource)
txt_sources = Text(
	master=frame,
	height='4',
	width='25',
	highlightbackground=bgColor,
	bg=fieldColor,
	fg=btntxtColor)
lbl_sources['font'] = myFont
btn_selectSourceFolder['font'] = myFont
txt_sources['font'] = myFont
lbl_sources.grid(column=0, row=2, sticky=W, padx=8, pady=1)
btn_selectSourceFolder.grid(column=1, row=2, sticky=W, padx=8, pady=1)
txt_sources.grid(column=0, columnspan=2, row=3, sticky='nwse', padx=8, pady=8)

# Row 4 - 5 : Options
lbl_options = Label(
	master=frame,
	text='Options:',
	bg=bgColor,
	fg=textColor)
rdo_deleteOld = Radiobutton(
	master=frame,
	text='Delete old files\nin destination folder',
	bg=bgColor,
	fg=textColor,
	variable=options,
	value=1)
rdo_backupOld = Radiobutton(
	master=frame,
	text='Backup old files\nin destination folder',
	bg=bgColor,
	fg=textColor,
	variable=options,
	value=2)
lbl_options['font'] = myFont
rdo_deleteOld['font'] = myFont
rdo_backupOld['font'] = myFont
lbl_options.grid(column=0, row=4, padx=8, pady=1)
rdo_deleteOld.grid(column=1, row=4, padx=8, pady=1)
rdo_backupOld.grid(column=1, row=5, padx=8, pady=1)

# Row 6 : Submit
btn_submit = Button(
	master=frame,
	text='CNSOLIDAT',
	default='active',
	height='2',
	width='40',
	highlightbackground=bgColor,
	fg=btntxtColor,
	command=submitForm)
btn_submit['font'] = myFont
btn_submit.grid(column=0, columnspan=2, row=6, padx=8, pady=5)

root.mainloop() # waits for user input/events, any code after is blocked
									# until window is closed