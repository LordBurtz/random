""" displayes the current time (what did you expect lol?)
    Synopsis: <trigger> <specification>
    contact me on discord Fingolfin#5731 if you got any questions..
"""
from albertv0 import *
from time import sleep
import datetime as dt

__iid__ = "PythonInterface/v0.1"
__version__ = "1.0"
__trigger__ = "time "
__author__ = "Fingolfin#5731"
__prettyname__ = "time"
__dependencies__ = ["python", "datetime"]
#iconPath = iconLookup('icon.png')

def initialize():
    pass

def finalize():
    pass


def handleQuery(query):
    if not query.isTriggered:
        return

    now = dt.datetime.now()

    if query.string.startswith("exact"):
        return Item(
            id = __prettyname__,
            text = str(dt.datetime.now()),
            subtext = "exact time",
            icon = "clock.png"
        )

    elif query.string.startswith("date"):
        return Item(
            id = __prettyname__,
            text = now.strftime('%Y-%m-%d %A'),
            subtext = "maybe its wednesday my dudes",
            icon = "clock.png"
        )

    else:
        #return dt.datetime.now()
        return Item(
            id = __prettyname__,
            text = now.strftime('%H:%M:%S on %A, %B the %dth, %Y'),
            subtext = now.strftime('%Y-%m-%d %H:%M:%S'),
            icon="clock.png"
        )
