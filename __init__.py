"""
    bitwarden extension depending on the npm module
    bw <application>
    by Fingolfin#5731 or on github LordBurtz
"""

from albertv0 import *
from shutil import which
import tkinter as tk
import tkinter.simpledialog
import subprocess

__iid__ = "PythonInterface/v0.1"
__version__ = "1.0"
__trigger__ = "bw "
__author__ = "LordBurtz"
__prettyname__ = "bitwarden-pwd-manager"
__dependencies__ = ["bitwarden npm install", "tkinter", "subprocess"]


def initialize():
    if which("bw") is None:
        raise Exception("'bw' // the bitwarden npm module is not installed")

    global locked
    global session_key

    locked = True

    proc = subprocess.Popen("bw unlock --raw {}".format("sprintal!a!melody17"), stdout=subprocess.PIPE, shell=True,
                            encoding='utf-8')
    out, err = proc.communicate()
    session_key = out


def finalize():
    global locked
    global session_key

    locked = True
    session_key = "do not go gentle into that good night"
    session_key = str(session_key)


def handleQuery(query):
    global locked
    global session_key

    if not query.isTriggered:
        return

    proc = subprocess.Popen("bw unlock --raw {}".format("sprintal!a!melody17"), stdout=subprocess.PIPE, shell=True,
                            encoding='utf-8')
    out, err = proc.communicate()
    session_key = ''.join(out)

    if query.string.startswith("unlock"):
        return Item(
            id=__prettyname__,
            text="unlock your vault",
            subtext="input your password",
            actions=[FuncAction("open vault", ask4pwd())]
        )

    elif query.string.startswith("lock"):
        return Item(
            id=__prettyname__,
            text=str(query.string.strip()),
            subtext="masterpassword will be cleared"
        )

    else:
        items = []
        returned_usr = ""
        returned_pwd = ""
        quazzel = query.string

        returned_usr = subprocess.Popen("bw get username {} --raw --session {}".format(quazzel, session_key),
                                stdout=subprocess.PIPE, shell=True, encoding='utf-8').communicate()
        returned_pwd = subprocess.Popen("bw get password {} --raw --session {}".format(quazzel, session_key),
                                 stdout=subprocess.PIPE, shell=True, encoding='utf-8').communicate()

        user = ''.join(item for item in returned_usr if item)
        passw = ''.join(item for item in returned_pwd if item)

        if returned_usr:
            items.append(Item(
                id=__prettyname__,
                text="username",
                subtext="on enter it'll be copied to clipboard",
                actions=[ClipAction("copy to clipboard", user)]
            ))

        if returned_pwd:
            items.append(Item(
                id=__prettyname__,
                text="password",
                subtext="on enter it'll be copied to clipboard",
                actions=[ClipAction("copy to clipboard", passw)]
            ))

        return items


""""
def ask4pwd():
    global locked
    global session_key

    tk.Tk().withdraw()
    pwd = tkinter.simpledialog.askstring("Password for bitwarden", "Enter password:", show='*')
    session_key = subprocess.Popen("bw unlock --raw {}".format(pwd), stdout=subprocess.PIPE, shell=True, encoding='utf-8').communicate[0]
    time.sleep(1)

    if session_key != "Invalid master password.":
        locked = False

def closeall():
    global locked
    global session_key

    locked = True
    session_key  = "Do not go gentle in to that good night"
"""
