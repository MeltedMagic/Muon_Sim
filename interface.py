import numpy as np
import os
import math
from datetime import datetime
from GraphicMultpleScattering import *
from multpleScattering import *
from logWriter import *
import pandas as pd
'''
This is named Interface as this is an interface from main.py
to the rest of the codebase
'''


class Interface:
    def __init__(self):
        self.date = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.txtFilename = "log_" + self.date + "_.txt"
        self.csvFilename = "log_" + self.date + "_.csv"
        self.log = logWriter(self.txtFilename)
        self.count = 0
        self.nJobs = 0
        self.nIterations = []
        self.nMomenta = []
        self.SortByTime = False
        self.SortByIterations = True

    def start(self, AI_DATA):
        #self.progressWindow = progressWindow()
        ## For the sake of readability, I am going to expand out the assignment
        self.x = AI_DATA[0]
        self.y = AI_DATA[1]
        self.phi = AI_DATA[2]

        self.xI = int(AI_DATA[3])  #start
        self.xF = int(AI_DATA[4])  #stop
        self.xB = int(AI_DATA[5])  #jobs

        self.yI = int(AI_DATA[6])  #start
        self.yF = int(AI_DATA[7])  #stop
        self.yB = int(AI_DATA[8])  #jobs

        self.pI = AI_DATA[9]  #start
        self.pF = AI_DATA[10]  #stop
        self.pB = AI_DATA[11]  #jobs

        self.Length = AI_DATA[12]
        self.Accuracy = AI_DATA[13]
        self.momentum = AI_DATA[14]
        self.nRuns = AI_DATA[15]

        self.DxRange = np.linspace(self.xI, self.xF, self.xB, endpoint=True)
        self.DyRange = np.linspace(self.yI, self.yF, self.yB, endpoint=True)
        self.DpRange = np.linspace(int(self.pI),
                                   int(self.pF),
                                   int(self.pB),
                                   endpoint=True)

        self.times, self.xPos, self.yPos, self.phiPos = [], [], [], []
        self.DxPos, self.DyPos, self.DphiPos = [], [], []

        if self.xB == 0 and not (self.yB == 0 and self.pB == 0):
            ## runs when chambers are created in y, phi, and not x
            print("\n\n\n Code Block 1 in interface.py is executing.")
            print(f"xB: {self.xB},\t yB: {self.yB},\t pB: {self.pB} \n")
            if self.nRuns == 1:
                print("This code block is running")
                for dy in range(len(self.DyRange)):
                    for dp in range(len(self.DpRange)):
                        ## iterates through chambers generated in y and phi
                        DxValue = int(self.xF)  #stop position in x
                        DyValue = int(self.DyRange[dy])
                        DpValue = int(self.DpRange[dp])
                        program = multpleScattering(self.x, self.y, self.phi,
                                                    DxValue, DyValue, DpValue,
                                                    self.Length, self.Accuracy,
                                                    self.momentum)
                        self.count += 1  # number of jobs
                        print(
                            "\n--------------------------------------------------------------"
                        )
                        print("Job Number: ", self.count, " |", " Time: ",
                              program.returnTime(), "|", "nIterations: ",
                              program.returnNumberOfIterations())
                        print(
                            "--------------------------------------------------------------\n"
                        )
                        self.times.append(program.returnTime())
                        self.DxPos.append(DxValue)
                        self.DyPos.append(DyValue)
                        self.DphiPos.append(DpValue)
                        self.xPos.append(self.x)
                        self.yPos.append(self.y)
                        self.phiPos.append(self.phi)
                        self.nIterations.append(
                            program.returnNumberOfIterations())
                        self.nMomenta.append(program.returnMomentum())
            if self.nRuns > 1:
                for i in range(self.nRuns):
                    print("Run Number: ", i, "\n")
                    for dy in range(len(self.DyRange)):
                        for dp in range(len(self.DpRange)):
                            DxValue = int(self.xF)
                            DyValue = int(self.DyRange[dy])
                            DpValue = int(self.DpRange[dp])
                            program = multpleScattering(
                                self.x, self.y, self.phi, DxValue, DyValue,
                                DpValue, self.Length, self.Accuracy,
                                self.momentum)
                            self.count += 1
                            print(
                                "\n--------------------------------------------------------------"
                            )
                            print("Job Number: ", self.count, " |", " Time: ",
                                  program.returnTime(), "|", "nIterations: ",
                                  program.returnNumberOfIterations())
                            print(
                                "--------------------------------------------------------------\n"
                            )
                            self.times.append(program.returnTime())
                            self.DxPos.append(DxValue)
                            self.DyPos.append(DyValue)
                            self.DphiPos.append(DpValue)
                            self.xPos.append(self.x)
                            self.yPos.append(self.y)
                            self.phiPos.append(self.phi)
                            self.nIterations.append(
                                program.returnNumberOfIterations())
                            self.nMomenta.append(program.returnMomentum())

        if self.yB == 0 and not (self.xB == 0 or self.pB == 0):
            print("\n\n\n Code Block 2 in interface.py is executing.\n")
            if self.nRuns == 1:
                for dx in range(len(self.DxRange)):
                    for dp in range(len(self.DpRange)):
                        #print(dx, dy, dp)
                        DxValue = int(self.DxRange[dx])
                        DyValue = int(self.yF)
                        DpValue = int(self.DpRange[dp])
                        # print(DxValue)
                        program = multpleScattering(self.x, self.y, self.phi,
                                                    DxValue, DyValue, DpValue,
                                                    self.Length, self.Accuracy,
                                                    self.momentum)
                        self.count += 1
                        print(
                            "\n--------------------------------------------------------------"
                        )
                        print("Job Number: ", self.count, " |", " Time: ",
                              program.returnTime(), "|", "nIterations: ",
                              program.returnNumberOfIterations())
                        print(
                            "--------------------------------------------------------------\n"
                        )
                        self.times.append(program.returnTime())
                        self.DxPos.append(DxValue)
                        self.DyPos.append(DyValue)
                        self.DphiPos.append(DpValue)
                        self.xPos.append(self.x)
                        self.yPos.append(self.y)
                        self.phiPos.append(self.phi)
                        self.nIterations.append(
                            program.returnNumberOfIterations())
                        self.nMomenta.append(program.returnMomentum())

            if self.nRuns > 1:
                for i in range(self.nRuns):
                    print("Run Number: ", i, "\n")
                    for dx in range(len(self.DxRange)):
                        for dp in range(len(self.DpRange)):
                            #print(dx, dy, dp)
                            DxValue = int(self.DxRange[dx])
                            DyValue = int(self.yF)
                            DpValue = int(self.DpRange[dp])
                            # print(DxValue)
                            program = multpleScattering(
                                self.x, self.y, self.phi, DxValue, DyValue,
                                DpValue, self.Length, self.Accuracy,
                                self.momentum)
                            self.count += 1
                            print(
                                "\n--------------------------------------------------------------"
                            )
                            print("Job Number: ", self.count, " |", " Time: ",
                                  program.returnTime(), "|", "nIterations: ",
                                  program.returnNumberOfIterations())
                            print(
                                "--------------------------------------------------------------\n"
                            )
                            self.times.append(program.returnTime())
                            self.DxPos.append(DxValue)
                            self.DyPos.append(DyValue)
                            self.DphiPos.append(DpValue)
                            self.xPos.append(self.x)
                            self.yPos.append(self.y)
                            self.phiPos.append(self.phi)
                            self.nIterations.append(
                                program.returnNumberOfIterations())
                            self.nMomenta.append(program.returnMomentum())

        if self.pB == 0 and not (self.xB == 0 or self.yB == 0):
            print("\n\n\n Code Block 3 in interface.py is executing.\n")
            if self.nRuns == 1:
                for dx in range(len(self.DxRange)):
                    for dy in range(len(self.DyRange)):
                        DxValue = int(self.DxRange[dx])
                        DyValue = int(self.DyRange[dy])
                        DpValue = int(pF)
                        program = multpleScattering(self.x, self.y, self.phi,
                                                    DxValue, DyValue, DpValue,
                                                    self.Length, self.Accuracy,
                                                    self.momentum)
                        self.count += 1
                        print(
                            "\n--------------------------------------------------------------"
                        )
                        print("Job Number: ", self.count, " |", " Time: ",
                              program.returnTime(), "|", "nIterations: ",
                              program.returnNumberOfIterations())
                        print(
                            "--------------------------------------------------------------\n"
                        )
                        self.times.append(program.returnTime())
                        self.DxPos.append(DxValue)
                        self.DyPos.append(DyValue)
                        self.DphiPos.append(DpValue)
                        self.xPos.append(self.x)
                        self.yPos.append(self.y)
                        self.phiPos.append(self.phi)
                        self.nIterations.append(
                            program.returnNumberOfIterations())
                        self.nMomenta.append(program.returnMomentum())

            if self.nRuns > 1:
                for i in range(self.nRuns):
                    print("Run Number: ", i, "\n")
                    for dx in range(len(self.DxRange)):
                        for dy in range(len(self.DyRange)):
                            DxValue = int(self.DxRange[dx])
                            DyValue = int(self.DyRange[dy])
                            DpValue = int(pF)
                            program = multpleScattering(
                                self.x, self.y, self.phi, DxValue, DyValue,
                                DpValue, self.Length, self.Accuracy,
                                self.momentum)
                            self.count += 1
                            print(
                                "\n--------------------------------------------------------------"
                            )
                            print("Job Number: ", self.count, " |", " Time: ",
                                  program.returnTime(), "|", "nIterations: ",
                                  program.returnNumberOfIterations())
                            print(
                                "--------------------------------------------------------------\n"
                            )
                            self.times.append(program.returnTime())
                            self.DxPos.append(DxValue)
                            self.DyPos.append(DyValue)
                            self.DphiPos.append(DpValue)
                            self.xPos.append(self.x)
                            self.yPos.append(self.y)
                            self.phiPos.append(self.phi)
                            self.nIterations.append(
                                program.returnNumberOfIterations())
                            self.nMomenta.append(program.returnMomentum())
        if self.xB == 0 and self.yB == 0 and not (self.pB == 0):
            print("\n\n\n Code Block 4 in interface.py is executing.\n")
            if self.nRuns == 1:
                for dp in range(len(self.DpRange)):
                    DxValue = int(self.xF)
                    DyValue = int(self.yF)
                    DpValue = int(self.DpRange[dp])
                    program = multpleScattering(self.x, self.y, self.phi,
                                                DxValue, DyValue, DpValue,
                                                self.Length, self.Accuracy,
                                                self.momentum)
                    self.count += 1
                    print(
                        "\n--------------------------------------------------------------"
                    )
                    print("Job Number: ", self.count, " |", " Time: ",
                          program.returnTime(), "|", "nIterations: ",
                          program.returnNumberOfIterations())
                    print(
                        "--------------------------------------------------------------\n"
                    )
                    self.times.append(program.returnTime())
                    self.DxPos.append(DxValue)
                    self.DyPos.append(DyValue)
                    self.DphiPos.append(DpValue)
                    self.xPos.append(self.x)
                    self.yPos.append(self.y)
                    self.phiPos.append(self.phi)
                    self.nIterations.append(program.returnNumberOfIterations())
                    self.nMomenta.append(program.returnMomentum())

            if self.nRuns > 1:
                for i in range(self.nRuns):
                    print("Run Number: ", i, "\n")
                    for dp in range(len(self.DpRange)):
                        DxValue = int(self.xF)
                        DyValue = int(self.yF)
                        DpValue = int(self.DpRange[dp])
                        program = multpleScattering(self.x, self.y, self.phi,
                                                    DxValue, DyValue, DpValue,
                                                    self.Length, self.Accuracy,
                                                    self.momentum)
                        self.count += 1
                        print(
                            "\n--------------------------------------------------------------"
                        )
                        print("Job Number: ", self.count, " |", " Time: ",
                              program.returnTime(), "|", "nIterations: ",
                              program.returnNumberOfIterations())
                        print(
                            "--------------------------------------------------------------\n"
                        )
                        self.times.append(program.returnTime())
                        self.DxPos.append(DxValue)
                        self.DyPos.append(DyValue)
                        self.DphiPos.append(DpValue)
                        self.xPos.append(self.x)
                        self.yPos.append(self.y)
                        self.phiPos.append(self.phi)
                        self.nIterations.append(
                            program.returnNumberOfIterations())
                        self.nMomenta.append(program.returnMomentum())
        if self.yB == 0 and self.pB == 0 and not (self.xB == 0):
            print("\n\n\n Code Block 5 in interface.py is executing. \n")
            if self.nRuns == 1:
                for dx in range(len(self.DxRange)):
                    DxValue = int(self.DxRange[dx])
                    DyValue = int(self.yF)
                    DpValue = int(self.pF)
                    program = multpleScattering(self.x, self.y, self.phi,
                                                DxValue, DyValue, DpValue,
                                                self.Length, self.Accuracy,
                                                self.momentum)
                    self.count += 1
                    print(
                        "\n--------------------------------------------------------------"
                    )
                    print("Job Number: ", self.count, " |", " Time: ",
                          program.returnTime(), "|", "nIterations: ",
                          program.returnNumberOfIterations())
                    print(
                        "--------------------------------------------------------------\n"
                    )
                    self.times.append(program.returnTime())
                    self.DxPos.append(DxValue)
                    self.DyPos.append(DyValue)
                    self.DphiPos.append(DpValue)
                    self.xPos.append(self.x)
                    self.yPos.append(self.y)
                    self.phiPos.append(self.phi)
                    self.nIterations.append(program.returnNumberOfIterations())
                    self.nMomenta.append(program.returnMomentum())

            if self.nRuns > 1:
                for i in range(self.nRuns):
                    print("Run Number: ", i, "\n")
                    for dx in range(len(self.DxRange)):
                        DxValue = int(self.DxRange[dx])
                        DyValue = int(self.yF)
                        DpValue = int(self.pF)
                        program = multpleScattering(self.x, self.y, self.phi,
                                                    DxValue, DyValue, DpValue,
                                                    self.Length, self.Accuracy,
                                                    self.momentum)
                        self.count += 1
                        print(
                            "\n--------------------------------------------------------------"
                        )
                        print("Job Number: ", self.count, " |", " Time: ",
                              program.returnTime(), "|", "nIterations: ",
                              program.returnNumberOfIterations())
                        print(
                            "--------------------------------------------------------------\n"
                        )
                        self.times.append(program.returnTime())
                        self.DxPos.append(DxValue)
                        self.DyPos.append(DyValue)
                        self.DphiPos.append(DpValue)
                        self.xPos.append(self.x)
                        self.yPos.append(self.y)
                        self.phiPos.append(self.phi)
                        self.nIterations.append(
                            program.returnNumberOfIterations())
                        self.nMomenta.append(program.returnMomentum())

        if self.xB == 0 and self.pB == 0 and not (self.yB == 0):
            print("\n\n\n Code Block 6 in interface.py is executing. \n")
            if self.nRuns == 1:
                for dy in range(len(self.DyRange)):
                    print(f"max-value: {len(self.DyRange)}")
                    DxValue = int(self.xF)
                    DyValue = int(self.DyRange[dy])
                    DpValue = int(self.pF)
                    program = multpleScattering(self.x, self.y, self.phi,
                                                DxValue, DyValue, DpValue,
                                                self.Length, self.Accuracy,
                                                self.momentum)
                    self.count += 1
                    print(
                        "\n--------------------------------------------------------------"
                    )
                    print("Job Number: ", self.count, " |", " Time: ",
                          program.returnTime(), "|", "nIterations: ",
                          program.returnNumberOfIterations())
                    print(
                        "--------------------------------------------------------------\n"
                    )
                    self.times.append(program.returnTime())
                    self.DxPos.append(DxValue)
                    self.DyPos.append(DyValue)
                    self.DphiPos.append(DpValue)
                    self.xPos.append(self.x)
                    self.yPos.append(self.y)
                    self.phiPos.append(self.phi)
                    self.nIterations.append(program.returnNumberOfIterations())
                    self.nMomenta.append(program.returnMomentum())
            if self.nRuns > 1:
                for i in range(self.nRuns):
                    print("Run Number: ", i, "\n")
                    for dy in range(len(self.DyRange)):
                        DxValue = int(self.xF)
                        DyValue = int(self.DyRange[dy])
                        DpValue = int(self.pF)
                        program = multpleScattering(self.x, self.y, self.phi,
                                                    DxValue, DyValue, DpValue,
                                                    self.Length, self.Accuracy,
                                                    self.momentum)
                        self.count += 1
                        print(
                            "\n--------------------------------------------------------------"
                        )
                        print("Job Number: ", self.count, " |", " Time: ",
                              program.returnTime(), "|", "nIterations: ",
                              program.returnNumberOfIterations())
                        print(
                            "--------------------------------------------------------------\n"
                        )
                        self.times.append(program.returnTime())
                        self.DxPos.append(DxValue)
                        self.DyPos.append(DyValue)
                        self.DphiPos.append(DpValue)
                        self.xPos.append(self.x)
                        self.yPos.append(self.y)
                        self.phiPos.append(self.phi)
                        self.nIterations.append(
                            program.returnNumberOfIterations())
                        self.nMomenta.append(program.returnMomentum())

        else:
            print("\n\n\n Code Block 7 in interface.py is executing. \n")
            if self.nRuns == 1:
                print("all directions")
                for dx in range(len(self.DxRange)):
                    for dy in range(len(self.DyRange)):
                        for dp in range(len(self.DpRange)):
                            DxValue = int(self.DxRange[dx])
                            DyValue = int(self.DyRange[dy])
                            DpValue = int(self.DpRange[dp])
                            program = multpleScattering(
                                self.x, self.y, self.phi, DxValue, DyValue,
                                DpValue, self.Length, self.Accuracy,
                                self.momentum)
                            self.count += 1
                            print(
                                "\n--------------------------------------------------------------"
                            )
                            print("Job Number: ", self.count, " |", " Time: ",
                                  program.returnTime(), "|", "nIterations: ",
                                  program.returnNumberOfIterations())
                            print(
                                "--------------------------------------------------------------\n"
                            )
                            self.times.append(program.returnTime())
                            self.DxPos.append(DxValue)
                            self.DyPos.append(DyValue)
                            self.DphiPos.append(DpValue)
                            self.xPos.append(self.x)
                            self.yPos.append(self.y)
                            self.phiPos.append(self.phi)
                            self.nIterations.append(
                                program.returnNumberOfIterations())
                            self.nMomenta.append(program.returnMomentum())
            if self.nRuns > 1:
                for i in range(self.nRuns):
                    print("Run Number: ", i, "\n")
                    for dx in range(len(self.DxRange)):
                        for dy in range(len(self.DyRange)):
                            for dp in range(len(self.DpRange)):
                                DxValue = int(self.DxRange[dx])
                                DyValue = int(self.DyRange[dy])
                                DpValue = int(self.DpRange[dp])
                                program = multpleScattering(
                                    self.x, self.y, self.phi, DxValue, DyValue,
                                    DpValue, self.Length, self.Accuracy,
                                    self.momentum)
                                self.count += 1
                                print(
                                    "\n--------------------------------------------------------------"
                                )
                                print("Job Number: ", self.count, " |",
                                      " Time: ", program.returnTime(), "|",
                                      "nIterations: ",
                                      program.returnNumberOfIterations())
                                print(
                                    "--------------------------------------------------------------\n"
                                )
                                self.times.append(program.returnTime())
                                self.DxPos.append(DxValue)
                                self.DyPos.append(DyValue)
                                self.DphiPos.append(DpValue)
                                self.xPos.append(self.x)
                                self.yPos.append(self.y)
                                self.phiPos.append(self.phi)
                                self.nIterations.append(
                                    program.returnNumberOfIterations())
                                self.nMomenta.append(program.returnMomentum())

        ### variables are being initialized
        minTimeOne = 100
        minTimeTwo = 100
        minTimeThree = 100

        minCoordinatesOne = []
        minCoordinatesTwo = []
        minCoordinatesThree = []

        self.minTimeOneIndex = 0
        self.minTimeTwoIndex = 0
        self.minTimeThreeIndex = 0

        self.nJobs = self.xB + self.yB + self.pB

        if self.nJobs > 3 or self.nJobs == 3:  ### Try replacing with >= and see what happens

            # looking for the 3 fastest jobs
            minTimeOne = min(self.times)  ### Where is the min function from?
            ### min() function is built-in function
            ### to find the smallest value in the array.
            ### self.times is an array.
            self.minTimeOneIndex = self.times.index(minTimeOne)
            minTimeTwo = sorted(
                self.times)[-2]  ### Where is the sorted function from?
            self.minTimeTwoIndex = self.times.index(minTimeTwo)
            minTimeThree = sorted(self.times)[-3]
            self.minTimeThreeIndex = self.times.index(minTimeThree)
            minTimeIndices = [minTimeOne, minTimeTwo, minTimeThree]
            minCoordinates = []
            # organizing data for 3  fastest jobs:
            # Design Position first job
            minCoordinates.append(self.xPos[self.minTimeOneIndex])
            minCoordinates.append(self.yPos[self.minTimeOneIndex])
            minCoordinates.append(self.phiPos[self.minTimeOneIndex])
            # Actual Position first job
            minCoordinates.append(self.xPos[self.minTimeOneIndex] +
                                  self.DxPos[self.minTimeOneIndex])
            minCoordinates.append(self.yPos[self.minTimeOneIndex] +
                                  self.DyPos[self.minTimeOneIndex])
            minCoordinates.append(self.phiPos[self.minTimeOneIndex] +
                                  self.DphiPos[self.minTimeOneIndex])

            # Design Position second job
            minCoordinates.append(self.xPos[self.minTimeTwoIndex])
            minCoordinates.append(self.yPos[self.minTimeTwoIndex])
            minCoordinates.append(self.phiPos[self.minTimeTwoIndex])
            # Actual Position second job
            minCoordinates.append(self.xPos[self.minTimeTwoIndex] +
                                  self.DxPos[self.minTimeTwoIndex])
            minCoordinates.append(self.yPos[self.minTimeTwoIndex] +
                                  self.DyPos[self.minTimeTwoIndex])
            minCoordinates.append(self.phiPos[self.minTimeTwoIndex] +
                                  self.DphiPos[self.minTimeTwoIndex])

            # Design Position third job
            minCoordinates.append(self.xPos[self.minTimeThreeIndex])
            minCoordinates.append(self.yPos[self.minTimeThreeIndex])
            minCoordinates.append(self.phiPos[self.minTimeThreeIndex])
            # Actual Position third job
            minCoordinates.append(self.xPos[self.minTimeThreeIndex] +
                                  self.DxPos[self.minTimeThreeIndex])
            minCoordinates.append(self.yPos[self.minTimeThreeIndex] +
                                  self.DyPos[self.minTimeThreeIndex])
            minCoordinates.append(self.phiPos[self.minTimeThreeIndex] +
                                  self.DphiPos[self.minTimeThreeIndex])
            minCoordinates.append(self.Accuracy)
            minCoordinates.append(self.Length)

            # writing data: -- make this another file
            #parameters = ['job_number  ', 'design_position  ', 'actual_position  ', 'time_rank  ', 'time_elapsed  ']
            if self.SortByTime:
                rankedTimes = sorted(self.times)
                rankedIndexes = []
                for i in range(len(rankedTimes)):
                    rankedIndexes.append(rankedTimes.index(self.times[i]))
                rankedIndices = sorted(rankedIndexes)
                parameters = [
                    "time_rank", "design_position", "actual_position",
                    "time_elapsed(seconds)", "momentum", "# of iterations",
                    "job_number"
                ]
                csvData = []
                csvData.append(parameters)
                for i in rankedIndices:
                    design_position = [
                        self.xPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]])
                    ]
                    actual_position = [
                        self.xPos[rankedIndices[i]] +
                        self.DxPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]] +
                        self.DyPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]] +
                                     self.DphiPos[rankedIndices[i]])
                    ]
                    momemtumString = str(self.momentum) + "/" + str(
                        self.nMomenta[rankedIndices[i]])
                    appendData = [
                        rankedIndices[i], design_position, actual_position,
                        self.times[rankedIndices[i]], momemtumString,
                        self.nIterations[rankedIndices[i]], rankedIndexes[i]
                    ]
                    csvData.append(appendData)

                self.log.writeCSV(csvData, self.csvFilename)
            if self.SortByIterations:
                rankedIterations = sorted(self.nIterations)
                rankedIndexes = []
                for i in range(len(rankedIterations)):
                    rankedIndexes.append(
                        rankedIterations.index(self.nIterations[i]))
                rankedIndices = sorted(rankedIndexes)
                parameters = [
                    "iteration_rank", "design_position", "actual_position",
                    "time_elapsed(seconds)", "momentum", "# of iterations",
                    "job_number"
                ]
                csvData = []
                csvData.append(parameters)
                for i in rankedIndices:
                    design_position = [
                        self.xPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]])
                    ]
                    actual_position = [
                        self.xPos[rankedIndices[i]] +
                        self.DxPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]] +
                        self.DyPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]] +
                                     self.DphiPos[rankedIndices[i]])
                    ]
                    momemtumString = str(self.momentum) + "/" + str(
                        self.nMomenta[rankedIndices[i]])

                    appendData = [
                        rankedIndices[i], design_position, actual_position,
                        self.times[rankedIndices[i]], momemtumString,
                        self.nIterations[rankedIndices[i]], rankedIndexes[i]
                    ]

                    csvData.append(appendData)

                self.log.writeCSV(csvData, self.csvFilename)

        if self.nJobs == 2:
            minTimeOne = min(self.times)
            self.minTimeOneIndex = self.times.index(minTimeOne)
            minTimeTwo = sorted(self.times)[-2]
            minTimeIndices = [minTimeOne, minTimeTwo]
            minCoordinates = []

            # sorting 2 fastest jobs:
            # Design Position first job
            minCoordinates.append(self.xPos[self.minTimeOneIndex])
            minCoordinates.append(self.yPos[self.minTimeOneIndex])
            minCoordinates.append(self.phiPos[self.minTimeOneIndex])
            # Actual Position first job
            minCoordinates.append(self.xPos[self.minTimeOneIndex] +
                                  self.DxPos[self.minTimeOneIndex])
            minCoordinates.append(self.yPos[self.minTimeOneIndex] +
                                  self.DyPos[self.minTimeOneIndex])
            minCoordinates.append(self.phiPos[self.minTimeOneIndex] +
                                  self.DphiPos[self.minTimeOneIndex])

            # Design Position second job
            minCoordinates.append(self.xPos[self.minTimeTwoIndex])
            minCoordinates.append(self.yPos[self.minTimeTwoIndex])
            minCoordinates.append(self.phiPos[self.minTimeTwoIndex])
            # Actual Position second job
            minCoordinates.append(self.xPos[self.minTimeTwoIndex] +
                                  self.DxPos[self.minTimeTwoIndex])
            minCoordinates.append(self.yPos[self.minTimeTwoIndex] +
                                  self.DyPos[self.minTimeTwoIndex])
            minCoordinates.append(self.phiPos[self.minTimeTwoIndex] +
                                  self.DphiPos[self.minTimeTwoIndex])
            minCoordinates.append(self.Accuracy)
            minCoordinates.append(self.Length)

            # printing data
            if self.SortByTime:
                rankedTimes = sorted(self.times)
                rankedIndexes = []
                for i in range(len(rankedTimes)):
                    rankedIndexes.append(rankedTimes.index(self.times[i]))
                rankedIndices = sorted(rankedIndexes)
                parameters = [
                    "time_rank", "design_position", "actual_position",
                    "time_elapsed(seconds)", "momentum", "# of iterations",
                    "job_number"
                ]
                csvData = []
                csvData.append(parameters)
                for i in rankedIndices:
                    design_position = [
                        self.xPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]])
                    ]
                    actual_position = [
                        self.xPos[rankedIndices[i]] +
                        self.DxPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]] +
                        self.DyPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]] +
                                     self.DphiPos[rankedIndices[i]])
                    ]
                    momemtumString = str(self.momentum) + "/" + str(
                        self.nMomenta[rankedIndices[i]])
                    appendData = [
                        rankedIndices[i], design_position, actual_position,
                        self.times[rankedIndices[i]], momemtumString,
                        self.nIterations[rankedIndices[i]], rankedIndexes[i]
                    ]
                    csvData.append(appendData)

                self.log.writeCSV(csvData, self.csvFilename)
            if self.SortByIterations:
                rankedIterations = sorted(self.nIterations)
                rankedIndexes = []
                for i in range(len(rankedIterations)):
                    rankedIndexes.append(
                        rankedIterations.index(self.nIterations[i]))
                rankedIndices = sorted(rankedIndexes)
                parameters = [
                    "iteration_rank", "design_position", "actual_position",
                    "time_elapsed(seconds)", "momentum", "# of iterations",
                    "job_number"
                ]
                csvData = []
                csvData.append(parameters)
                for i in rankedIndices:
                    design_position = [
                        self.xPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]])
                    ]
                    actual_position = [
                        self.xPos[rankedIndices[i]] +
                        self.DxPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]] +
                        self.DyPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]] +
                                     self.DphiPos[rankedIndices[i]])
                    ]
                    momemtumString = str(self.momentum) + "/" + str(
                        self.nMomenta[rankedIndices[i]])
                    appendData = [
                        rankedIndices[i], design_position, actual_position,
                        self.times[rankedIndices[i]], momemtumString,
                        self.nIterations[rankedIndices[i]], rankedIndexes[i]
                    ]

                    csvData.append(appendData)

                self.log.writeCSV(csvData, self.csvFilename)

        if self.nJobs == 1:
            minTimeOne = min(
                self.times)  ## Get the smallest value of the self.times array
            self.minTimeOneIndex = self.times.index(minTimeOne)
            minTimeIndices = [minTimeOne, minTimeTwo]
            minCoordinates = []

            # sorting 2 fastest jobs:
            # Design Position first job
            minCoordinates.append(self.xPos[self.minTimeOneIndex])
            minCoordinates.append(self.yPos[self.minTimeOneIndex])
            minCoordinates.append(self.phiPos[self.minTimeOneIndex])
            # Actual Position first job
            minCoordinates.append(self.xPos[self.minTimeOneIndex] +
                                  self.DxPos[self.minTimeOneIndex])
            minCoordinates.append(self.yPos[self.minTimeOneIndex] +
                                  self.DyPos[self.minTimeOneIndex])
            minCoordinates.append(self.phiPos[self.minTimeOneIndex] +
                                  self.DphiPos[self.minTimeOneIndex])
            minCoordinates.append(self.Accuracy)
            minCoordinates.append(self.Length)

            # printing data
            if self.SortByTime:
                rankedTimes = sorted(self.times)
                rankedIndexes = []
                for i in range(len(rankedTimes)):
                    rankedIndexes.append(rankedTimes.index(self.times[i]))
                rankedIndices = sorted(rankedIndexes)
                parameters = [
                    "time_rank", "design_position", "actual_position",
                    "time_elapsed(seconds)", "momentum", "# of iterations",
                    "job_number"
                ]
                csvData = []
                csvData.append(parameters)
                for i in rankedIndices:
                    design_position = [
                        self.xPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]])
                    ]
                    actual_position = [
                        self.xPos[rankedIndices[i]] +
                        self.DxPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]] +
                        self.DyPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]] +
                                     self.DphiPos[rankedIndices[i]])
                    ]
                    momemtumString = str(self.momentum) + "/" + str(
                        self.nMomenta[rankedIndices[i]])
                    appendData = [
                        rankedIndices[i], design_position, actual_position,
                        self.times[rankedIndices[i]], momemtumString,
                        self.nIterations[rankedIndices[i]], rankedIndexes[i]
                    ]

                    csvData.append(appendData)

                self.log.writeCSV(csvData, self.csvFilename)
            if self.SortByIterations:
                rankedIterations = sorted(self.nIterations)
                rankedIndexes = []
                for i in range(len(rankedIterations)):
                    rankedIndexes.append(
                        rankedIterations.index(self.nIterations[i]))
                rankedIndices = sorted(rankedIndexes)
                parameters = [
                    "iteration_rank", "design_position", "actual_position",
                    "time_elapsed(seconds)", "momentum", "# of iterations",
                    "job_number"
                ]
                csvData = []
                csvData.append(parameters)
                for i in rankedIndices:
                    design_position = [
                        self.xPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]])
                    ]
                    actual_position = [
                        self.xPos[rankedIndices[i]] +
                        self.DxPos[rankedIndices[i]],
                        self.yPos[rankedIndices[i]] +
                        self.DyPos[rankedIndices[i]],
                        math.degrees(self.phiPos[rankedIndices[i]] +
                                     self.DphiPos[rankedIndices[i]])
                    ]
                    momemtumString = str(self.momentum) + "/" + str(
                        self.nMomenta[rankedIndices[i]])

                    appendData = [
                        rankedIndices[i], design_position, actual_position,
                        self.times[rankedIndices[i]], momemtumString,
                        self.nIterations[rankedIndices[i]], rankedIndexes[i]
                    ]

                    csvData.append(appendData)

                self.log.writeCSV(csvData, self.csvFilename)

    def showPlots(self):

        chamberOneInfo = [
            self.xPos[self.minTimeOneIndex], self.yPos[self.minTimeOneIndex],
            self.phiPos[self.minTimeOneIndex],
            self.DxPos[self.minTimeOneIndex], self.DyPos[self.minTimeOneIndex],
            self.DphiPos[self.minTimeOneIndex],
            self.nMomenta[self.minTimeOneIndex]
        ]
        #chamberTwoInfo = [self.xPos[self.minTimeTwoIndex], self.yPos[self.minTimeTwoIndex], self.phiPos[self.minTimeTwoIndex], self.DxPos[self.minTimeTwoIndex], self.DyPos[self.minTimeTwoIndex], self.DphiPos[self.minTimeTwoIndex]]
        #chamberThreeInfo = [self.xPos[self.minTimeThreeIndex], self.yPos[self.minTimeThreeIndex], self.phiPos[self.minTimeThreeIndex], self.DxPos[self.minTimeThreeIndex], self.DyPos[self.minTimeThreeIndex], self.DphiPos[self.minTimeThreeIndex]]

        plot = GraphicMultpleScattering()
        plot.start(chamberOneInfo, self.Length, self.Accuracy,
                   self.nIterations[self.minTimeOneIndex])

    def showSpreadSheet(self):
        os.system(f"open {self.csvFilename}")

    def showLog(self):
        os.system(f"open {self.txtFilename}")

    def setSortingFilter(self, command):
        if command == "time":
            self.SortByTime = True
        if command == "iterations":
            self.SortByIterations = True
        else:
            print("idk")

    def returnJobNumber(self):
        return count

    def returnProgressString(self):
        completionString = (str(self.count) + " jobs complete out of: " +
                            str(self.nJobs))
        return completionString


#print("2 --- time: ", minTimeOne, "x: ", minCoordinatesOne[0], "y: ", minCoordinatesOne[2], "phi: ", minCoordinatesOne[2], file = log)
#print("2 --- time: ", minTimeTwo, "x: ", minCoordinatesTwo[0], "y: ", minCoordinatesTwo[1], "phi: ", minCoordinatesTwo[2], file = log)
#rint("1 --- time: ", minTimeThree, "x: ", minCoordinatesThree[0], "y: ", minCoordinatesThree[1], "phi: ", minCoordinatesThree[2], file = log)
