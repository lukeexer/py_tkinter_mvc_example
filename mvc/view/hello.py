'''View classes.'''

import tkinter as tk

from tkinter import ttk

class HelloFrame(tk.Frame):
    '''A friendly little module.'''

    def __init__(self, parent, variables, callbacks, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        name_label = ttk.Label(self, text='Name:')
        name_entry = ttk.Entry(self, textvariable=variables['name'])
        ch_button = ttk.Button(self, text='Change', command=callbacks['on_change'])
        hello_label = ttk.Label(self, textvariable=variables['hello_string'],
            font=('TkDefaultFont', 64), wraplength=600)

        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)
        self.columnconfigure(1, weight=1)
