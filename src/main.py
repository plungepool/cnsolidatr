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
		# txt_sources.delete("1.0", "2.0")
		txt_sources.delete("end-5c", END)
		txt_sources.insert(END, '\n')
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
	global configLocation
	args = str(options.get())
	configFile = open(configLocation, "w")
	configFile.write(ent_destination.get() + "\n")
	configFile.close()
	configFile = open(configLocation, "a")
	configFile.write(txt_sources.get("1.0","end-1c"))
	configFile.write("#end")
	configFile.close()
	subprocess.call(['./copyscript.sh', args, configLocation])
	exit()

#MAIN
root = Tk()
root.title('cnsolidtr') #sets window title
myFont = font.Font(family='Courier', size='12', weight='bold')

#VARS
global configLocation
destinationDir = StringVar()
destinationDir.set(" ")
sourceDir = StringVar()
options = IntVar(None, "1")

#Frame Setup
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)

grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=3, row=5, columnspan=1)

Grid.columnconfigure(frame, 0, weight=1)
Grid.columnconfigure(frame, 1, weight=1)
Grid.columnconfigure(frame, 2, weight=1)

Grid.rowconfigure(frame, 0, weight=1)

# Responsive Frame
for x in range(3):
	Grid.columnconfigure(frame, x, weight=1)
for y in range(5):
	Grid.rowconfigure(frame, y, weight=1)

# Row 0 : Save/Load
btn_load = Button(
	master=frame,
	text='Load Config',
	# fg='black',
	height='1',
	width='20',
	command=loadConfig)
lbl_OR = Label(
	master=frame,
	text='-OR-',
	height='1',
	width='5')
btn_saveAs = Button(
	master=frame,
	text='Save Config As...',
	height='1',
	width='20',
	command=saveConfigAs)
btn_load['font'] = myFont
lbl_OR['font'] = myFont
btn_saveAs['font'] = myFont
btn_load.grid(column=0, row=0)
lbl_OR.grid(column=1, row=0)
btn_saveAs.grid(column=2, row=0)

# Row 1 : Set Destination
lbl_destination = Label(
	master=frame,
	text='Select destination folder:')
btn_selectDestFolder = Button(
	master=frame,
	text='...',
	height='1',
	width='3',
	command=selectDestination)
ent_destination = Entry(
	master=frame,
	width='20',
	textvariable=destinationDir)
lbl_destination['font'] = myFont
btn_selectDestFolder['font'] = myFont
ent_destination['font'] = myFont
lbl_destination.grid(column=0, row=1)
btn_selectDestFolder.grid(column=1, row=1)
ent_destination.grid(column=2, columnspan=2, row=1)

# Row 2 - 3 : Sources 
lbl_sources = Label(
	master=frame,
	text='Copy newest files from these locations:')
btn_selectSourceFolder = Button(
	master=frame,
	text='Add source folder...',
	command=selectSource)
txt_sources = Text(
	master=frame,
	height='4',
	width='25')
lbl_sources['font'] = myFont
btn_selectSourceFolder['font'] = myFont
txt_sources['font'] = myFont
lbl_sources.grid(column=0, columnspan=2, row=2)
btn_selectSourceFolder.grid(column=2, row=2)
txt_sources.grid(column=0, columnspan=3, row=3, sticky='nwse', padx=5, pady=1)

# Row 4 - 5 : Options
lbl_options = Label(
	master=frame,
	text='Options:')
rdo_deleteOld = Radiobutton(
	master=frame,
	text='Delete old files in destination folder',
	variable=options,
	value=1)
rdo_backupOld = Radiobutton(
	master=frame,
	text='Backup old files in destination folder',
	variable=options,
	value=2)
lbl_options['font'] = myFont
rdo_deleteOld['font'] = myFont
rdo_backupOld['font'] = myFont
lbl_options.grid(column=0, row=4)
rdo_deleteOld.grid(column=1, columnspan=2, row=4)
rdo_backupOld.grid(column=1, columnspan=2, row=5)

# Row 6 : Submit
btn_submit = Button(
	master=frame,
	text='CNSOLIDAT',
	default='active',
	height='1',
	width='50',
	command=submitForm)
btn_submit['font'] = myFont
btn_submit.grid(column=0, columnspan=3, row=6, padx=5, pady=5)

root.mainloop() # waits for user input/events, any code after is blocked
									# until window is closed