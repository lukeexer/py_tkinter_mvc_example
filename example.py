# pylint: disable=W0703
'''Tkinter program entry point.'''

import traceback

from mvc.controller import Controller

if __name__ == '__main__':

    try:
        app = Controller()
        app.mainloop()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
