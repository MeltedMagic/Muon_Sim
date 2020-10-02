from tkinter import *
from AI_Remote import *
import datetime, os, math

#Save residual Plots Option
#Make residual PLots a part of chamber plot's figure
#Labels for each plot





window = Tk()
window.title("Muon Simulator")

time1 = ''
clock = Label(window, font=('times', 20, 'bold'), bg='green')
#print(len(axs), len(axss))
menubar = Menu(window)
optionmenu = Menu(menubar, tearoff = 0)
datamenu = Menu(menubar, tearoff = 0)

optionmenu.add_command(label = "Show Text Log", command = lambda: showLog())
optionmenu.add_command(label = "Show Plot", command = lambda: showPlots())
optionmenu.add_command(label = "Show Spread Sheet", command = lambda: showSpreadSheet())
optionmenu.add_separator()

datamenu.add_command(label = "Sort by Time", command = lambda: sortByTime())
datamenu.add_command(label = "Sort by nIterations", command = lambda: sortByIterations())

menubar.add_cascade(label = "Options", menu = optionmenu)
menubar.add_cascade(label = "Data Options", menu = datamenu)
AI_remote = AI_Remote()
X, Y, Phi = 0,0,0
Dx, Dy, dPhi = 0,0,0
count = 0
momentum = 0

designPosLabel = Label(window, text="Enter Design Pos:").grid(row=3, column=0)
actualPosLabel =Label(window, text="Enter Actual Range:").grid(row=5, column=0)
blank1 = Label(window,text="").grid(row=6,column=3)

xLabel = Label(window,text="X").grid(row=2,column=1)
yLabel = Label(window,text="Y").grid(row=2,column=2)
phiLabel = Label(window,text="Phi").grid(row=2,column=4)

DXLabel = Label(window,text="DX").grid(row=4,column=1)
DYLabel = Label(window,text="DY").grid(row=4,column=2)
DPhiLabel = Label(window,text="DPhi").grid(row=4,column=4)

runsLabel = Label(window, text = 'nRuns').grid(row=0, column=0)
accuracyLabel = Label(window, text="Accuracy").grid(row = 0, column = 1)
momentumLabel = Label(window, text="Momentum").grid(row=0, column=2)
lengthLabel = Label(window, text="Length").grid(row=0, column=4)
blank = Label(window,text="").grid(row=8,column=3)

runsEntry = Entry(window, width=12, bd = 2)
runsEntry.grid(row = 1, column = 0)
runsEntry.insert(0, '1')
accuracyEntry = Entry(window, width=12, bd = 2)
accuracyEntry.grid(row=1, column=1)
accuracyEntry.insert(0, "0.000001")
momentumEntry = Entry(window, width=12, bd = 2)
momentumEntry.grid(row=1, column=2)
momentumEntry.insert(0, "AUTO")
lengthEntry = Entry(window, width=12, bd = 2)
lengthEntry.grid(row=1, column = 4)
lengthEntry.insert(0, "100")
blankLabel = Label(window, text='      ').grid(row = 0, column = 3)
blankLabelTwo = Label(window, text='     ').grid(row=0, column=5)
xEntry = Entry(window, width=12, bd = 2)
xEntry.grid(row=3,column=1)
xEntry.insert(0, "50")
yEntry = Entry(window, width=12, bd = 2)
yEntry.grid(row=3,column=2)
yEntry.insert(0, "0")
phiEntry = Entry(window, width=12, bd = 2)
phiEntry.grid(row=3,column=4)
phiEntry.insert(0, "90")
phiEntry.config(state='readonly')

dxEntry = Entry(window, width=12, bd = 2)
dxEntry.grid(row=5,column=1)
dxEntry.insert(0, "5,5,1")
dyEntry = Entry(window, width=12, bd = 2)
dyEntry.grid(row=5,column=2)
dyEntry.insert(0, "0,0,0")
dPhiEntry = Entry(window, width=12, bd = 2)
dPhiEntry.grid(row=5,column=4)
dPhiEntry.insert(0, "0,0,0")
completionString = StringVar()
completionString.set("0 jobs complete out of: 0")
StartBtn = Button(window,text="Start", command=lambda: start()).grid(row=7, column=0)
completionLabel = Label(window, textvariable=completionString).grid(row =7, column = 1)

def start():
	nRuns = int(runsEntry.get())
	momentum = momentumEntry.get()
	dxValues = str(dxEntry.get()).split(',')
	dyValues = str(dyEntry.get()).split(',')
	dpValues = str(dPhiEntry.get()).split(',')
	xI, xF, xB = float(dxValues[0]), float(dxValues[1]), float(dxValues[2])
	yI, yF, yB = float(dyValues[0]), float(dyValues[1]), float(dyValues[2])
	pI, pF, pB = float(dpValues[0]), float(dpValues[1]), float(dpValues[2])

	#AI_DATA = [X,Y,PHI,DX,DY,DPHI,XI,XF,XB,YI,YF,YB,PI,PF,PB,LENGTH,ACCURACY,MOMENTUM,NRUNS]

	AI_DATA = [float(xEntry.get()), float(yEntry.get()), float(phiEntry.get())*(math.pi/180), xI, xF, xB, yI, yF, yB, pI, pF, pB, int(lengthEntry.get()), float(accuracyEntry.get()), momentum, nRuns]

	AI_remote.start(AI_DATA)

def showLog():
	AI_remote.showLog()
	#e.msgbox('Cannot open Log', 'wait until program is finished')
def showSpreadSheet():
	AI_remote.showSpreadSheet()
def showPlots():
	AI_remote.showPlots()
def sortByTime():
	AI_remote.setSortingFilter("time")
def sortByIterations():
	AI_remote.setSortingFilter("iterations")


window.config(menu=menubar)

window.mainloop()

