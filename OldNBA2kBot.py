# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

PAUSE = 0.2

def tap(x, y):
    """Tap"""
    MonkeyRunner.sleep(PAUSE)
    device.touch(x, y, 'DOWN_AND_UP')
    MonkeyRunner.sleep(PAUSE)

def rapidTap(n, x, y):
    """Tap n times"""
    for i in xrange(1, n):
        tap(x, y)

def dragUp(y1, y2):
    """Unlock device"""
    start = (540, y1)
    end = (540, y2)
    duration = 0.4
    steps = 2
    # Swipe up to unlock
    device.drag(start, end, duration, steps)
    MonkeyRunner.sleep(PAUSE)

def dragLeft(x1, x2):
    """Swipe left"""
    MonkeyRunner.sleep(PAUSE)
    start = (x1, 1000)
    end = (x2, 1000)
    duration = 0.4
    steps = 2
    # Swipe up to unlock
    device.drag(start, end, duration, steps)
    MonkeyRunner.sleep(PAUSE)

def unlock():
    """Unlock device"""
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
    """Start NBA game"""
    MonkeyRunner.sleep(PAUSE*5)
    tap(400, 1300)
    MonkeyRunner.sleep(PAUSE*90)
    print "Finished waiting for app"
    dragUp(1800, 200)
    dragUp(1800, 200)
    MonkeyRunner.sleep(PAUSE*40)
    print "Finished waiting for app"

def startQuickGame(RC=False):
    """Start quick game"""
    dragUp(1800, 200)
    dragUp(1800, 200)
    if RC:
        tap(500,780)
    else:
        tap(500, 1550)
    MonkeyRunner.sleep(PAUSE*25)

def playRound(QG=False):
    """Grind round of quick game"""
    print "C"
    tap(830, 1800)
    rapidTap(25, 500, 630)
    print "PF"
    tap(670, 1800)
    rapidTap(25, 500, 630)
    print "SF"
    tap(510, 1800)
    rapidTap(25, 500, 630)
    print "PG"
    tap(200, 1800)
    rapidTap(25, 500, 630)
    print "SG"
    if QG:
        tap(970, 1870)
    tap(350, 1800)
    rapidTap(30, 555, 1370)

def startRTTC():
    """ Click on RTTC button"""
    MonkeyRunner.sleep(PAUSE*5)
    tap(500, 1700)
    MonkeyRunner.sleep(PAUSE*25)

def playRTTC(Greedy=True):
    """ Click Play """
    tap(500, 1350)
    #Click +7
    MonkeyRunner.sleep(PAUSE*20)
    tap(280, 900)
    MonkeyRunner.sleep(PAUSE*5)
    rapidTap(25, 500, 630)
    for x in xrange(0,4):
        playRound()
    print "Done playing"
    if Greedy:
        for x in xrange(0,8):
            chooseWinnings()
            chooseWinnings()
            MonkeyRunner.sleep(PAUSE*8)
            tap(555, 1370)
            MonkeyRunner.sleep(PAUSE*8)
        tap(500, 1870)
        MonkeyRunner.sleep(PAUSE*6)


def playQuickGame(RC=False):
    """Play quick game"""
    if RC:
        print "In Rival Clash"
        tap(500,1050)
        MonkeyRunner.sleep(PAUSE*15)
        print "Starting RC Quick Game"
        tap(500,1400)
    else:
        tap(500, 1700)
    MonkeyRunner.sleep(PAUSE*25)
    rapidTap(25, 500, 630)
    playRound(QG=True)
    print "Done playing"
    chooseWinnings()
    chooseWinnings()
    MonkeyRunner.sleep(PAUSE*6)
    tap(555, 1370)
    print "Choosing second card"
    MonkeyRunner.sleep(PAUSE*6)
    chooseWinnings()
    chooseWinnings()
    MonkeyRunner.sleep(PAUSE*6)
    tap(555, 1370)
    MonkeyRunner.sleep(PAUSE*6)
    tap(500, 1870)
    MonkeyRunner.sleep(PAUSE*8)

def chooseWinnings():
    """Click all the possible winnings"""
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
    """Reset game"""
    dragUp(1919, 1000)
    tap(800, 1850)
    MonkeyRunner.sleep(PAUSE*25)
    tap(915, 515)

def playRTTCevery15():
    """Play every 15 minutes"""
    MonkeyRunner.sleep(60*10)
    for x in xrange(0,12):
        print "Unlocking"
        device.wake()
        unlock()
        startNBA()
        startRTTC()
        playRTTC()
        reset()
        MonkeyRunner.sleep(60*5)
        print "5 minutes remaining"
        MonkeyRunner.sleep(60*5)
    while True:
        print "Unlocking"
        device.wake()
        unlock()
        startNBA()
        startRTTC()
        playRTTC(Greedy=False)
        reset()
        MonkeyRunner.sleep(60*5)
        print "5 minutes remaining"
        MonkeyRunner.sleep(60*5)

def playnRTTCGames(n=5):
    """Play every 15 minutes"""
    unlock()
    startNBA()
    startRTTC()
    for x in xrange(0,n):
        playRTTC()
    reset()
    playRTTCevery15()

def playnQuickGames(n=7):
    unlock()
    for x in xrange(0,n):
        startNBA()
        startQuickGame(RC=True)
        for y in xrange(0,8):
            playQuickGame(RC=True)
        print x
        reset()


print "Waiting for device!"
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
print "Connected to device!"
MonkeyRunner.sleep(PAUSE)
playnQuickGames()
