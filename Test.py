# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

pause = 0.2

def tap(x, y):
    MonkeyRunner.sleep(pause)
    device.touch(x, y, 'DOWN_AND_UP')
    MonkeyRunner.sleep(pause)

def rapidTap(n, x, y):
    for i in xrange(1, n):
        tap(x, y)

def dragUp(y1, y2):
    start = (540, y1)
    end = (540, y2)
    duration = 0.4
    steps = 2
    # Swipe up to unlock
    device.drag(start, end, duration, steps)
    MonkeyRunner.sleep(pause)

def dragLeft(x1, x2):
    MonkeyRunner.sleep(pause)
    start = (x1, 1000)
    end = (x2, 1000)
    duration = 0.4
    steps = 2
    # Swipe up to unlock
    device.drag(start, end, duration, steps)
    MonkeyRunner.sleep(pause)

#Unlock device
def unlock():
    dragUp(1800, 200)
    x_left = 200
    x_mid = 550
    x_right = 850
    y_top = 850
    y_mid = 1050
    y_bot = 1300
    y_check = 1550
    # TODO
    tap(x_right, y_check)

def startNBA():
    MonkeyRunner.sleep(pause*3)
    tap(400, 1300)
    MonkeyRunner.sleep(pause*90)
    print "Finished waiting for app"
    dragUp(1800, 200)
    dragUp(1800, 200)
    MonkeyRunner.sleep(pause*40)
    print "Finished waiting for app"

def startQuickGame(RC=False):
    dragUp(1800, 200)
    dragUp(1800, 200)
    if RC:
        tap(500,780)
    else:
        tap(500, 1550)
    MonkeyRunner.sleep(pause*25)

def playQuickGame(RC=False):
    if RC:
        print "In Rival Clash"
        tap(500,1050)
        MonkeyRunner.sleep(pause*15)
        print "Starting RC Quick Game"
        tap(500,1650)
    else:
        tap(500, 1700)
    MonkeyRunner.sleep(pause*25)
    rapidTap(25, 500, 630)
    print "C"
    tap(830, 1800)
    rapidTap(25, 500, 630)
    print "SF"
    tap(510, 1800)
    rapidTap(25, 500, 630)
    print "PF"
    tap(670, 1800)
    rapidTap(25, 500, 630)
    print "SG"
    tap(350, 1800)
    rapidTap(25, 500, 630)
    print "PG"
    tap(970, 1870)
    tap(200, 1800)
    rapidTap(30, 555, 1370)
    print "Done playing"
    chooseWinnings()
    chooseWinnings()
    MonkeyRunner.sleep(pause*6)
    tap(555, 1370)
    print "Choosing second card"
    MonkeyRunner.sleep(pause*6)
    chooseWinnings()
    chooseWinnings()
    MonkeyRunner.sleep(pause*6)
    tap(555, 1370)
    MonkeyRunner.sleep(pause*6)
    tap(500, 1870)
    MonkeyRunner.sleep(pause*8)

def chooseWinnings():
    row1 = 340
    row2 = 580
    row3 = 840
    row4 = 1100
    row5 = 1330
    col1 = 130
    col2 = 340
    col3 = 540
    col4 = 750
    col5 = 960
    row = [340, 580, 840, 1100, 1330]
    col = [130, 340, 540, 750, 960]
    for x in col:
        for y in row:
            device.touch(x, y, 'DOWN_AND_UP')

    
def reset():
    dragUp(1919, 1000)
    tap(800, 1850)
    MonkeyRunner.sleep(pause*25)
    tap(915, 515)

print "Waiting for device!"
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
print "Connected to device!"
MonkeyRunner.sleep(pause)
#unlock()
while True:
    startQuickGame()
    for x in xrange(0,8):
        playQuickGame()
    reset()
    startNBA()
