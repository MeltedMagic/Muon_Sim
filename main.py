import tkinter as tk
import interface
import datetime
import os
import math

# Save residual Plots Option
# Make residual PLots a part of chamber plot's figure
# Labels for each plot

ai = interface.Interface()
window = tk.Tk()
window.title("Muon Simulator")

time1 = ''
clock = tk.Label(window, font=('times', 20, 'bold'), bg='green')
#print(len(axs), len(axss))
menubar = tk.Menu(window)
optionmenu = tk.Menu(menubar, tearoff=0)
datamenu = tk.Menu(menubar, tearoff=0)

# Menu Bar Options
optionmenu.add_command(label="Show Text Log", command=lambda: showLog())
optionmenu.add_command(label="Show Plot", command=lambda: showPlots())
optionmenu.add_command(label="Show Spread Sheet",
                       command=lambda: showSpreadSheet())
optionmenu.add_separator()
datamenu.add_command(label="Sort by Time", command=lambda: sortByTime())
datamenu.add_command(label="Sort by nIterations",
                     command=lambda: sortByIterations())
menubar.add_cascade(label="Options", menu=optionmenu)
menubar.add_cascade(label="Data Options", menu=datamenu)

X, Y, Phi = 0, 0, 0
Dx, Dy, dPhi = 0, 0, 0
count = 0
momentum = 0

designPosLabel = tk.Label(window, text="Enter Design Pos:").grid(row=3,
                                                                 column=0)
actualPosLabel = tk.Label(window, text="Enter Actual Range:").grid(row=5,
                                                                   column=0)
blank1 = tk.Label(window, text="").grid(row=6, column=3)

xLabel = tk.Label(window, text="X").grid(row=2, column=1)
yLabel = tk.Label(window, text="Y").grid(row=2, column=2)
phiLabel = tk.Label(window, text="Phi").grid(row=2, column=4)

DXLabel = tk.Label(window, text="DX").grid(row=4, column=1)
DYLabel = tk.Label(window, text="DY").grid(row=4, column=2)
DPhiLabel = tk.Label(window, text="DPhi").grid(row=4, column=4)

runsLabel = tk.Label(window, text='nRuns').grid(row=0, column=0)
accuracyLabel = tk.Label(window, text="Accuracy").grid(row=0, column=1)
momentumLabel = tk.Label(window, text="Momentum").grid(row=0, column=2)
lengthLabel = tk.Label(window, text="Length").grid(row=0, column=4)
blank = tk.Label(window, text="").grid(row=8, column=3)

runsEntry = tk.Entry(window, width=12, bd=2)
runsEntry.grid(row=1, column=0)
runsEntry.insert(0, '1')

accuracyEntry = tk.Entry(window, width=12, bd=2)
accuracyEntry.grid(row=1, column=1)
accuracyEntry.insert(0, "0.000001")

momentumEntry = tk.Entry(window, width=12, bd=2)
momentumEntry.grid(row=1, column=2)
momentumEntry.insert(0, "AUTO")

lengthEntry = tk.Entry(window, width=12, bd=2)
lengthEntry.grid(row=1, column=4)
lengthEntry.insert(0, "100")

blankLabel = tk.Label(window, text='      ').grid(row=0, column=3)
blankLabelTwo = tk.Label(window, text='     ').grid(row=0, column=5)

xEntry = tk.Entry(window, width=12, bd=2)
xEntry.grid(row=3, column=1)
xEntry.insert(0, "50")

yEntry = tk.Entry(window, width=12, bd=2)
yEntry.grid(row=3, column=2)
yEntry.insert(0, "0")

phiEntry = tk.Entry(window, width=12, bd=2)
phiEntry.grid(row=3, column=4)
phiEntry.insert(0, "90")
phiEntry.config(state='readonly')

dxEntry = tk.Entry(window, width=12, bd=2)
dxEntry.grid(row=5, column=1)
dxEntry.insert(0, "5,5,1")

dyEntry = tk.Entry(window, width=12, bd=2)
dyEntry.grid(row=5, column=2)
dyEntry.insert(0, "0,0,0")

dPhiEntry = tk.Entry(window, width=12, bd=2)
dPhiEntry.grid(row=5, column=4)
dPhiEntry.insert(0, "0,0,0")

completionString = tk.StringVar()
completionString.set("0 jobs complete out of: 0")
StartBtn = tk.Button(window, text="Start",
                     command=lambda: start()).grid(row=7, column=0)
completionLabel = tk.Label(window,
                           textvariable=completionString).grid(row=7, column=1)


# ---------------------------------------------------------
def start():
    nRuns = int(runsEntry.get())
    momentum = momentumEntry.get()
    accuracy = accuracyEntry.get()
    dxValues = str(dxEntry.get()).split(',')
    dyValues = str(dyEntry.get()).split(',')
    dpValues = str(dPhiEntry.get()).split(',')
    xI, xF, xB = int(dxValues[0]), int(dxValues[1]), int(dxValues[2])
    yI, yF, yB = int(dyValues[0]), int(dyValues[1]), int(dyValues[2])
    pI, pF, pB = int(dpValues[0]), int(dpValues[1]), int(dpValues[2])

    #AI_DATA = [X,Y,PHI,XI,XF,XB,YI,YF,YB,PI,PF,PB,LENGTH,ACCURACY,MOMENTUM,NRUNS]

    dataBundle = [
        float(xEntry.get()),
        float(yEntry.get()),
        float(phiEntry.get()) * (math.pi / 180), xI, xF, xB, yI, yF, yB, pI,
        pF, pB,
        int(lengthEntry.get()),
        float(accuracy), momentum, nRuns
    ]
    ai.start(dataBundle)


def showLog():
    ai.showLog()
    #e.msgbox('Cannot open Log', 'wait until program is finished')


def showSpreadSheet():
    ai.showSpreadSheet()


def showPlots():
    ai.showPlots()


def sortByTime():
    ai.setSortingFilter("time")


def sortByIterations():
    ai.setSortingFilter("iterations")


window.config(menu=menubar)
window.mainloop()
