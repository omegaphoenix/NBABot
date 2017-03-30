"""Imports the monkeyrunner modules used by this program"""
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

SHOT_TIME = 0.54
PAUSE = 1.97

def shoot():
    """Shoot a shot"""
    MonkeyRunner.sleep(PAUSE)
    start = (1850, 750)
    DEVICE.drag(start, start, SHOT_TIME)

def shoot_rack():
    """Shoot 5 shots"""
    for _ in xrange(5):
        shoot()

def shoot_round():
    """Shoot 25 shots"""
    for _ in xrange(5):
        shoot_rack()

print "Waiting for device!"
# Connects to the current device, returning a MonkeyDevice object
DEVICE = MonkeyRunner.waitForConnection()
print "Connected to device!"
DEVICE.touch(1850, 750, 'DOWN_AND_UP')
MonkeyRunner.sleep(1.1)
print "Begin Shooting!"
shoot_round()
