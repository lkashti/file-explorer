import tkinter as tk


class ButtonsView:
    """
    Buttons widget - copy,paste,delete and move view
    """
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root, bg="lavender")
        # Initializing parameters
        self.src_path = ""
        self.dst_path = ""
        self.file_name = ""
        # Initializing internal widgets - buttons and labels
        self.label = tk.Label(self.frame, text="Actions",
                              font="Arial 12 bold", anchor="w", padx=ButtonsView.MARGIN_X,
                              bg="lavender")
        self.label.pack(fill=tk.X)
        
        self.new_folder_btn = tk.Button(self.frame, text="✚", font="Arial 9 bold")
        self.new_folder_btn.pack(side=tk.LEFT,
                                 padx=(ButtonsView.MARGIN_X * 2, ButtonsView.MARGIN_X),
                                 pady=ButtonsView.MARGIN_X)
        self.copy_btn = tk.Button(self.frame, text="Copy", font="Arial 9 bold")
        self.copy_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X * 2, ButtonsView.MARGIN_X),
                           pady=ButtonsView.MARGIN_X)
        self.paste_btn = tk.Button(self.frame, text="Paste", font="Arial 9 bold")
        self.paste_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X),
                            pady=ButtonsView.MARGIN_X)
        self.move_btn = tk.Button(self.frame, text="Move", font="Arial 9 bold")
        self.move_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X),
                           pady=ButtonsView.MARGIN_X)
        self.delete_btn = tk.Button(self.frame, text="Delete", font="Arial 9 bold")
        self.delete_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X),
                             pady=ButtonsView.MARGIN_X)
        # Bind to functionality
        self.new_folder_btn.bind("<Button-1>", self.controller.handle_create_folder_event)
        self.copy_btn.bind("<Button-1>", self.controller.handle_copy_event)
        self.paste_btn.bind("<Button-1>", self.controller.handle_paste_event)
        self.move_btn.bind("<Button-1>", self.controller.handle_copy_event)
        self.move_btn.bind("<Button-3>", self.controller.handle_move_event)
        self.delete_btn.bind("<Button-1>", self.controller.handle_click_delete)
        self.delete_btn.bind("<Double-1>", self.controller.handle_delete_event)
        # Locate current frame in left's side frame grid
        self.frame.grid(row=2, column=0,
                        sticky=tk.NSEW,
                        padx=ButtonsView.MARGIN_X, pady=ButtonsView.MARGIN_Y)
