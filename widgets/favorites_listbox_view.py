import tkinter as tk


class ListBox:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.frame, width=40,
                                  yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.pack(fill=tk.BOTH)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.frame.grid(row=5, column=0, sticky="nsew",
                        padx=ListBox.MARGIN_X)

    def on_select(self, event):
        # Note here that Tkinter passes an event object to onselect()
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        path = value[3:]
        self.controller.on_favorite_click(path)
