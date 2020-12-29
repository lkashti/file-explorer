import tkinter as tk
import widgets.TreeView as tv

class SelectView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller

        self.frame = tk.Frame(root)

        self.select_label = tk.Label(self.frame, text="Select",
                                     font="Arial 15 bold")
        self.select_label.pack()

        self.v = tk.IntVar()
        self.v.set(0)
        self.values = {"All": 0,
                       "None": 1,
                       "Costume": 2,
                       }
        for index, btn in enumerate(self.values):
            b = tk.Radiobutton(self.frame,
                               text=btn,
                               value=index,
                               variable=self.v,command=self.get_val)
            b.pack(side=tk.LEFT)
        # self.rb_all = tk.Radiobutton(self.frame,text="all",value=1,variable=self.v).pack(side=tk.LEFT)
        # self.rb_none = tk.Radiobutton(self.frame,text="none",value=2,variable=self.v).pack(side=tk.LEFT)
        # self.rb_costume = tk.Radiobutton(self.frame,text="costume",value=3,variable=self.v).pack(side=tk.LEFT)
        self.frame.grid(row=2, column=0,
                        sticky=tk.NSEW,
                        padx=SelectView.MARGIN_X,
                        pady=SelectView.MARGIN_Y)


    def get_val(self):
        self.controller.vv = self.v.get()
        # val = self.v.get()
        # return val

