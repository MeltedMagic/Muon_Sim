#https://www.cs.uct.ac.za/mit_notes/python/Introduction_to_GUI_Programming.html
from numba import jit
import math, random, time
from geometry import *
from constants import *
from iterateMuon import iterateMuon
from circleIntersectLine import circleIntersectLine
from propagateMuon import propagateMuon
from chamber import *
import numpy as np
from plotter import *
random.seed(1.0)

class GraphicMultpleScattering:
		
	def start(self, chamberInfoOne, Length, Accuracy, nIterations):

		residualLeavingBounds = []
		self.OneX, self.OneY, self.OnePhi, self.OneDX, self.OneDY, self.OneDPhi = float(chamberInfoOne[0]), float(chamberInfoOne[1]), float(chamberInfoOne[2]), float(chamberInfoOne[3]), float(chamberInfoOne[4]), float(chamberInfoOne[5])
		#self.TwoX, self.TwoY, self.TwoPhi, self.TwoDX, self.TwoDY, self.TwoDPhi = float(chamberInfoTwo[0]), float(chamberInfoTwo[1]), float(chamberInfoTwo[2]), float(chamberInfoTwo[3]), float(chamberInfoTwo[4]), float(chamberInfoTwo[5])
		#self.ThreeX, self.ThreeY, self.ThreePhi, self.ThreeDX, self.ThreeDY, self.ThreeDPhi = float(chamberInfoThree[0]), float(chamberInfoThree[1]), float(chamberInfoThree[2]), float(chamberInfoThree[3]), float(chamberInfoThree[4]), float(chamberInfoThree[5])
		self.nIterations = nIterations

		self.momentum = chamberInfoOne[6]
		if self.momentum == 'AUTO':
			self.momentum = (OneX+OneDX)/30
		self.xinit, self.xfinal = 0, 50
		self.plotter = plotter(self.xinit, self.xfinal, float(self.momentum), self.nIterations)
		self.stepSizes = self.plotter.returnStepSizes()


		self.chamber1 = chamber(1, Length, self.OneX, self.OneY, self.OnePhi, self.OneX+self.OneDX, self.OneY+self.OneDY, self.OnePhi+self.OneDPhi, Accuracy, self.stepSizes )
		#self.chamber2 = chamber(1, Length, self.TwoX, self.TwoY, self.TwoPhi, self.TwoX+self.TwoDX, self.TwoY+self.TwoDY, self.TwoPhi+self.TwoDPhi, Accuracy, self.stepSizes )
		#self.chamber3 = chamber(1, Length, self.ThreeX, self.ThreeY, self.ThreePhi, self.ThreeX+self.ThreeDX, self.ThreeY+self.ThreeDY, self.ThreePhi+self.ThreeDPhi, Accuracy, self.stepSizes )
		#self.chamber1.plotChamber(self.sub1,self.sub2,self.sub3)
		for i in range(400):
			if self.chamber1.isDone(): #and self.chamber2.isDone() and self.chamber3.isDone()
				break
			self.actualEndpoints = self.chamber1.actualEndpoints
			self.designEndpoints = self.chamber1.designEndpoints
			self.plotter.updateEndpoints(self.actualEndpoints, self.designEndpoints)
			self.plotter.updateResidualPlot(self.chamber1.returnResidual())
			self.plotter.updateLinePlots(self.chamber1.countX, self.chamber1.countY, self.chamber1.countZ)
			
			shootMuons(self.chamber1, self.plotter)

			self.chamber1.align()
			self.chamber1.resetData()

			self.plotter.resetEndpoints()
			self.plotter.resetLinePlot()

	def returnTime(self):
		return self.time

def shootMuons(chamber1, plotter):
	for i in range(nEvents):

		if i%1000==0: i*1.0/nEvents

		#set up inital state of muon
		angleInitial = 1
		speedInitial = 1000

		angleInitial = random.random()-.5

		charge = random.random()
		if charge > .5: charge = 1
		else: charge = -1


		xInitial = 0
		yInitial = 0
		muonPath = []
		muonTrack = []
		#create muon track
		#if verbose > 5: print("start  angle {} speed {} charge {} x {} y {}".format( angleInitial, speedInitial, charge, xInitial, yInitial))
		muonTrack, muonPath = propagateMuon(angleInitial, speedInitial, charge, xInitial, yInitial)
		#muonTrackTwo, muonPathTwo = propagateMuon(angleInitial, speedInitial, charge, xInitial, yInitial)
		#muonTrackThree, muonPathThree = propagateMuon(angleInitial, speedInitial, charge, xInitial, yInitial)
		
		chamber1.getResiduals(muonTrack, muonPath)
		#chamber2.getResiduals(muonTrackTwo, muonPathTwo)
		#chamber3.getResiduals(muonTrackThree, muonPathThree)

		# note the y and x axis are not to scale, meaning things are stretched. A tilted chamber will look shorter
		if i%10000==0:
			#plt.clf()
			#trackPathsOne = sub1.plot(muonTrackOne[0],muonTrackOne[1], color='orange', label="track")
			#muonPathsOne = sub1.plot(muonPathOne[0],muonPathOne[1], marker = 'o', color='red', label="actual path")
			plotter.updateMuonPath(muonTrack, muonPath)
			#trackPathsTwo = sub2.plot(muonTrackTwo[0],muonTrackTwo[1], color='orange', label="track")
			#muonPathsTwo = sub2.plot(muonPathTwo[0],muonPathTwo[1], marker = 'o', color='red', label="actual path")

			#trackPathsThree = sub3.plot(muonTrackThree[0],muonTrackThree[1], color='orange', label="track")
			#muonPathsThree = sub3.plot(muonPathThree[0],muonPathThree[1], marker = 'o', color='red', label="actual path")
		
			plotter.resetMuonPaths()
