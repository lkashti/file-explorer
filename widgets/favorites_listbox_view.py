import tkinter as tk


class ListBox:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10
    '''
    List box widget - the list of the favorites
    In a separate frame because of UI constrains  
    '''
    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        # Initializing internal widgets
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.frame, width=40,
                                  yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.pack(fill=tk.BOTH)
        # Bind to functionality
        self.listbox.bind('<<ListboxSelect>>', self.controller.on_list_view_select)
        # Locate current frame in left's side frame grid
        self.frame.grid(row=5, column=0, sticky="nsew",
                        padx=ListBox.MARGIN_X)