import tkinter as tk


class NewFolderWindow:
    """Create a new folder"""
    PAD = 5

    def __init__(self, root, controller):
        self.controller = controller
        self.window = tk.Toplevel(root)
        self.window.title("New Folder")
        self.window.geometry("300x100+500+400")
        self.window.resizable(0,0)
        self.window.wm_attributes("-topmost", 1)

        self.name_label = tk.Label(self.window, text="Name:", font="Arial 12 bold")
        self.name_label.pack(pady=NewFolderWindow.PAD)

        self.name_entry = tk.Entry(self.window, width=30)
        self.name_entry.focus()
        self.name_entry.pack(pady=NewFolderWindow.PAD)

        self.create_btn = tk.Button(self.window, text="Create")
        self.create_btn.pack(pady=NewFolderWindow.PAD)

        # binds
        self.name_entry.bind("<Return>",
                             lambda e: self.controller.create_new_folder(
                                 self.name_entry.get(),
                                 self.window
                             ))
        self.create_btn.bind("<Button-1>",
                             lambda e: self.controller.create_new_folder(
                                 self.name_entry.get(),
                                 self.window
                             ))

        self.window.mainloop()
