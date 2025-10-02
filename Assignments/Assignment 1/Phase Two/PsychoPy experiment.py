 #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on June 14, 2022, at 19:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

""" 

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

#mylibs
from pathlib import Path
import numpy as np
from PIL import Image
from psychopy import core, event, visual
from psychopy.hardware import keyboard
import random
#                                                                               

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'task1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Narges\\Desktop\\ca1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

op2 = "/home/reza/University/Principles of Cognitive Science/Assignments/Assignment 1/Phase Two/BS_ca1/" 
op = op2 + "stimulus/"#########################################################################################################################

# Setup the Window

win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()
#welcome
ssBreak = True
while ssBreak:
    
    imagee_namee = 'welcome.png'
    geez_path1 = op2 + imagee_namee
    ppath1 = Path(geez_path1)
    image = visual.ImageStim(
        win=win,
        name=imagee_namee, 
        image=ppath1, mask=None,
        ori=0.0, pos=(0, 0), size=(1, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    keysBreak = event.getKeys()
    if keysBreak:
        if 'space' in keysBreak:
            ssBreak = False
    
    image.draw()
    win.flip()

##training
##identity

##end_of_training

##instruction2
#ssBreak = True
#while ssBreak:
#    
#    imagee_namee = 'instruction2.png'
#    geez_path1 = op2 + imagee_namee
#    ppath1 = Path(geez_path1)
#    image = visual.ImageStim(
#        win=win,
#        name=imagee_namee, 
#        image=ppath1, mask=None,
#        ori=0.0, pos=(0, 0), size=(1, 1),
#        color=[1,1,1], colorSpace='rgb', opacity=None,
#        flipHoriz=False, flipVert=False,
#        texRes=128.0, interpolate=True, depth=0.0)
#    
#    keysBreak = event.getKeys()
#    if keysBreak:
#        if 'space' in keysBreak:
#            ssBreak = False
#    
#    image.draw()
#    win.flip()

# creating training images
training_images = [
    (('app/f_1/ 0', 'Akbar'), ('app/f_1/ 99', 'Leila')),
    (('app/f_11/ 0', 'Mahdi'), ('app/f_11/ 99', 'Sara')), 
    (('sha/f_1/ 0', 'Ali'), ('sha/f_1/ 99', 'Ava')),
    (('sha/f_11/ 0', 'Fatemeh'), ('sha/f_11/ 99', 'Mohammad'))
]

# creating trials
stimul1 = []
stimul2 = []

for feature in [1,11]:
    stimul = []
    for rep in range(1,11):
        for n in [0,11,22,33,44,55,66,77,88,99]:
            im = 'app/f_' + str(feature) + '/ ' + str(n)
            stimul.append(im)
    random.shuffle(stimul)
    stimul1 = stimul1 + stimul

for feature in [1,11]:
    stimul = []
    for rep in range(1,11):
        for n in  [0,11,22,33,44,55,66,77,88,99]:
            im = 'sha/f_' + str(feature) + '/ ' + str(n)
            stimul.append(im)
    random.shuffle(stimul)
    stimul2 = stimul2 + stimul
#
images = stimul1 + stimul2
#
trialClock = core.Clock()
tri = 0
for rond in range(len(images)):
    # training
    if rond % 100 == 0:
        block_num = rond // 100

        ssBreak = True
        while ssBreak:
            image_1, name_1 = training_images[block_num][0]
            geez_path1 = op + image_1.split()[0] + image_1.split()[1] +'.png'
            ppath1 = Path(geez_path1)
            image1 = visual.ImageStim(
                win=win,
                name=image_1, 
                image=ppath1, mask=None,
                ori=0.0, pos=(-0.4, 0), size=(0.5, 0.5),
                color=[1,1,1], colorSpace='rgb', opacity=None,
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)

            image_2, name_2 = training_images[block_num][1]
            geez_path2 = op + image_2.split()[0] + image_2.split()[1] +'.png'
            ppath2 = Path(geez_path2)
            image2 = visual.ImageStim(
                win=win,
                name=image_2, 
                image=ppath2, mask=None,
                ori=0.0, pos=(0.4, 0), size=(0.5, 0.5),
                color=[1,1,1], colorSpace='rgb', opacity=None,
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)

            image_name1 = visual.TextStim(
                win=win,
                text=name_1,
                pos=(-0.4, -0.3),
                height=0.05,
                color='black'
            )

            image_name2 = visual.TextStim(
                win=win,
                text=name_2,
                pos=(0.4, -0.3),
                height=0.05,
                color='black'
            )

            keysBreak = event.getKeys()
            if keysBreak:
                if 'space' in keysBreak:
                    ssBreak = False
    
            image1.draw()
            image2.draw()
            image_name1.draw()
            image_name2.draw()
            win.flip()

    #break
    if tri == 100:
        tri = 0
        ssBreak = True
        while ssBreak:
            imagee_namee = 'break.png'
            geez_path1 = op2 + imagee_namee
            ppath1 = Path(geez_path1)
            image = visual.ImageStim(
                win=win,
                name=imagee_namee, 
                image=ppath1, mask=None,
                ori=0.0, pos=(0, 0), size=(1, 1),
                color=[1,1,1], colorSpace='rgb', opacity=None,
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)
    
            keysBreak = event.getKeys()
            if keysBreak:
                if 'space' in keysBreak:
                    ssBreak = False
    
            image.draw()
            win.flip()
    
    tri = tri + 1
    
    image_name = images[rond]
    geez_path = op + image_name.split()[0] + image_name.split()[1] +'.png'
    PATH = Path(geez_path)
    imaaaaaaaaaage = visual.ImageStim(
        win=win,
        name=image_name, 
        image=PATH, mask=None,
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)

    choices = (training_images[block_num][0][1], training_images[block_num][1][1])
    ans = visual.TextStim(
        win=win,
        text=f"Who do you prefer?\n\n{choices[0]} <                            > {choices[1]}",
        pos=(0, 0),
        height=0.05,
        color='black'
    )

    fixation = visual.ImageStim(
        win=win,
        name='fixation', 
        image=op2+"fixation.png", mask=None,
        ori=0.0, pos=(0, 0), size=(1,1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    Keeeeeeeeeeeeeeeeeeeeey = keyboard.Keyboard()
        # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
#    routineTimer.add(0.300000)
    # update component parameters for each repeat
    Keeeeeeeeeeeeeeeeeeeeey.keys = []
    Keeeeeeeeeeeeeeeeeeeeey.rt = []
    _Keeeeeeeeeeeeeeeeeeeeey_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation, imaaaaaaaaaage, ans, Keeeeeeeeeeeeeeeeeeeeey]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
    
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 0.200-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)

        # *image* updates
        if imaaaaaaaaaage.status == NOT_STARTED and tThisFlip >= 0.200-frameTolerance:
            # keep track of start time/frame for later
            imaaaaaaaaaage.frameNStart = frameN  # exact frame index
            imaaaaaaaaaage.tStart = t  # local t and not account for scr refresh
            imaaaaaaaaaage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imaaaaaaaaaage, 'tStartRefresh')  # time at next scr refresh
            imaaaaaaaaaage.setAutoDraw(True)
        if imaaaaaaaaaage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imaaaaaaaaaage.tStartRefresh + 0.500-frameTolerance:
                # keep track of stop time/frame for later
                imaaaaaaaaaage.tStop = t  # not accounting for scr refresh
                imaaaaaaaaaage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imaaaaaaaaaage, 'tStopRefresh')  # time at next scr refresh
                imaaaaaaaaaage.setAutoDraw(False)
        
        # *im1* updates
        if ans.status == NOT_STARTED and tThisFlip >= 0.700-frameTolerance:
            # keep track of start time/frame for later
            ans.frameNStart = frameN  # exact frame index
            ans.tStart = t  # local t and not account for scr refresh
            ans.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ans, 'tStartRefresh')  # time at next scr refresh
            ans.setAutoDraw(True)

        # *Keeeeeeeeeeeeeeeeeeeeey* updates
        waitOnFlip = False
        if Keeeeeeeeeeeeeeeeeeeeey.status == NOT_STARTED and tThisFlip >= 0.700-frameTolerance:
            # keep track of start time/frame for later
            Keeeeeeeeeeeeeeeeeeeeey.frameNStart = frameN  # exact frame index
            Keeeeeeeeeeeeeeeeeeeeey.tStart = t  # local t and not account for scr refresh
            Keeeeeeeeeeeeeeeeeeeeey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Keeeeeeeeeeeeeeeeeeeeey, 'tStartRefresh')  # time at next scr refresh
            Keeeeeeeeeeeeeeeeeeeeey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Keeeeeeeeeeeeeeeeeeeeey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Keeeeeeeeeeeeeeeeeeeeey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Keeeeeeeeeeeeeeeeeeeeey.status == STARTED and not waitOnFlip:
            theseKeys = Keeeeeeeeeeeeeeeeeeeeey.getKeys(keyList=['left', 'right'], waitRelease=False)#######################################################################
            _Keeeeeeeeeeeeeeeeeeeeey_allKeys.extend(theseKeys)
            if len(_Keeeeeeeeeeeeeeeeeeeeey_allKeys):
                Keeeeeeeeeeeeeeeeeeeeey.keys = _Keeeeeeeeeeeeeeeeeeeeey_allKeys[-1].name  # just the last key pressed
                Keeeeeeeeeeeeeeeeeeeeey.rt = _Keeeeeeeeeeeeeeeeeeeeey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        thisExp.addData('Feature Type', image_name.split()[0][:3])
        thisExp.addData('Feature Number', image_name.split()[0][6:-1])
        thisExp.addData('Morph Level', image_name.split()[1])
        # check responses
        if Keeeeeeeeeeeeeeeeeeeeey.keys in ['', [], None]:  # No response was made
            Keeeeeeeeeeeeeeeeeeeeey.keys = None
        else :  # we had a response
            thisExp.addData('Key',Keeeeeeeeeeeeeeeeeeeeey.keys)
            thisExp.addData('Response Time', Keeeeeeeeeeeeeeeeeeeeey.rt)
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    thisExp.nextEntry()
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
