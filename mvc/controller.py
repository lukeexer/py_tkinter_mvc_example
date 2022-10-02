'''Controller class.'''

import tkinter as tk

from mvc.view.hello import HelloFrame

class Controller(tk.Tk):
    '''Controller class.'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Hello Tkinter')
        self.geometry('800x600')
        self.resizable(width=False, height=False)

        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set('Hello World')

        variables = {}
        variables['name'] = self.name
        variables['hello_string'] = self.hello_string

        callbacks = {}
        callbacks['on_change'] = self.on_change

        HelloFrame(self, variables, callbacks).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)

    def on_change(self):
        '''On change calback function.'''

        if self.name.get().strip():
            self.hello_string.set('Hello ' + self.name.get())
        else:
            self.hello_string.set('Hello World')
