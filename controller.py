from model import Model
from view import View
import tkinter as tk
import operator
import shutil
import errno
import time
import os


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        # Pass to view links on root frame and controller object
        self.view = View(self.root, self)
        self.root.deiconify()
        # initialization
        self.folder_details = []
        self.file_details = []
        self.results = []
        self.searched_path = ""
        self.update_all_views(self.model.get_home_path())
        self.view.center_frame.favorites_view.load_favorites()
        self.root.mainloop()

    #   Top Bar Functionality
    '''
    Home Button - jump to root folder and clear the history of 'Back' and 'Forward' buttons
    '''

    def handle_home_event(self, event):
        self.view.center_frame.log.log_text.config(text="-- Will be show here --")
        self.model.back_stack.clear_stack()
        self.model.forward_stack.clear_stack()
        self.update_all_views(self.model.get_home_path())

    '''
    Back Button - Display the previews folder, the parent of the current path, and push the current
                  path to 'forward_stack' in addition to use it when 'Forward' button will be clicked
    '''

    def handle_back_event(self, event):
        self.view.center_frame.log.log_text.config(text="-- Will be show here --")
        if len(self.model.back_stack.stack) > 0:
            self.model.forward_stack.push(self.view.navbar.path.get())
            self.update_all_views(self.model.back_stack.pop())

    '''
    Forward Button - Display the previews folder, the child of the current path, and push the current
                     path to 'Back_stack' in addition to use it when 'Back' button will be clicked
    '''

    def handle_forward_event(self, event):
        self.view.center_frame.log.log_text.config(text="-- Will be show here --")
        if len(self.model.forward_stack.stack) > 0:
            self.model.back_stack.push(self.view.navbar.path.get())
            self.update_all_views(self.model.forward_stack.pop())

    '''
    Display path inserted by the user
    If the path is not valid - an error will config under the 'Log' label
    '''

    def handle_enter_path(self, event):
        try:
            self.update_all_views(self.view.navbar.path.get())
            self.view.center_frame.log.log_text.config(text="-- Will be show here --")
        except FileNotFoundError as e:
            self.view.center_frame.log.log_text.config(text="Path is not valid")

    '''
    Handle search event by using two functions;
    find_all_files - use os.walk in addition to find an item recursively
    change_tree_view_cols - change the current tree into new tree
    '''

    def handle_search_path(self, event):
        exclude = ["#4", "#5"]
        try:
            self.results = self.find_all_files(self.view.navbar.search_field.get(),
                                               self.model.get_home_path())
        except FileNotFoundError:
            pass
        if len(self.results) > 1:
            self.change_tree_view_cols(exclude)

        #   Left side of center frame Functionality

    def handle_focus_in_search_bar(self, event):
        self.view.navbar.search_text.set("")
        self.view.center_frame.log.log_text.config(text="-- Will be show here --")

    '''
    Select all the elements in the tree view 
    Flag is using to handle an UI error after Disable the 'None' checkbox
    '''

    def select_all(self, event):
        if self.view.center_frame.select_view.all_var.get() == 0:
            self.view.center_frame.right_frame.tree.selection_set(
                self.view.center_frame.right_frame.tree.get_children())
        else:
            self.view.center_frame.right_frame.tree.selection_set()

    '''
    Display hidden files when 'Hidden' checkbox returns 0 value 
    Else they stay hidden
    '''

    def show_hidden(self, event):
        if self.view.center_frame.select_view.hidden_var.get() == 0:
            self.view.center_frame.select_view.hidden_flag = True
            self.update_all_views(self.view.navbar.path.get())
            self.view.center_frame.select_view.hidden_checkbox.config(text="Hide Hidden")
        if self.view.center_frame.select_view.hidden_var.get() == 1:
            self.view.center_frame.select_view.hidden_flag = False
            self.update_all_views(self.view.navbar.path.get())
            self.view.center_frame.select_view.hidden_checkbox.config(text="Show Hidden")

    '''
    Copy Button - set the source file for this action by taking the current path and add the file name,
                  than it update the user log 
    '''

    def handle_copy_event(self, event):
        self.view.center_frame.buttons_view.src_path = os.path.join(
            self.view.navbar.path.get(),
            self.view.center_frame.buttons_view.file_name
        )

        self.view.center_frame.log.log_text.config(
            text="{}".format("Source: " +
                             os.path.basename(
                                 os.path.normpath(
                                     self.view.center_frame.buttons_view.src_path)))
        )

    '''
    Paste Button - call to function that used by 'pate' and 'move' actions; will be detailed before
                   'cpy_src_dst()'
                   than it update the user log and the view in addition to see the new file in it new destination 
    '''

    def handle_paste_event(self, event):
        try:
            self.cpy_src_dst()
            self.update_all_views(self.view.navbar.path.get())
            self.view.center_frame.log.log_text.config(text="-- Will be show here --")
        except FileNotFoundError as e:
            print(e)

    '''            
    Move Button - call to function that used by 'pate' and 'move' actions; will be detailed before
                  ''cpy_src_dst()', remove the file from its source
                  than it update the user log and the view in addition to see the new file in it new destination 
    '''

    def handle_move_event(self, event):
        try:
            self.cpy_src_dst()
            try:
                if os.path.isfile(self.view.center_frame.buttons_view.src_path):
                    os.remove(self.view.center_frame.buttons_view.src_path)
                elif os.path.isdir(self.view.center_frame.buttons_view.src_path):
                    shutil.rmtree(self.view.center_frame.buttons_view.src_path)
            except PermissionError:
                self.view.center_frame.log.log_text.config(
                    text="-- Error: -- \nYou do not have Permissions\nFor this action")
            self.update_all_views(self.view.navbar.path.get())
            self.view.center_frame.log.log_text.config(text="-- Will be show here --")
        except FileNotFoundError as e:
            print(e.errno)

    '''
    Delete Button - One click - display a warning to the user  
    '''

    def handle_click_delete(self, event):
        self.view.center_frame.log.log_text.config(
            text="-- Warning: -- \nDelete will erase file from PC\nStill want to delete?\nDouble Click on 'Delete'")

    '''
    Delete Button - Double click - Erase the file from the system and update the tree view   
    '''

    def handle_delete_event(self, event):
        self.view.center_frame.buttons_view.src_path = os.path.join(
            self.view.navbar.path.get(),
            self.view.center_frame.buttons_view.file_name
        )
        if os.path.isfile(self.view.center_frame.buttons_view.src_path):
            os.remove(self.view.center_frame.buttons_view.src_path)
        if os.path.isdir(self.view.center_frame.buttons_view.src_path):
            shutil.rmtree(self.view.center_frame.buttons_view.src_path)
        self.update_all_views(self.view.navbar.path.get())

    '''
    Main functionality of 'Move' and 'Paste'
    Check if the user select a source file, set its path and copy to destination using 'shutil' package
    If user did not select a source file - an error will display under log        
    '''

    def cpy_src_dst(self):
        src_path = self.view.center_frame.buttons_view.src_path
        dst_path = self.view.navbar.path.get()
        if len(src_path) > 2:
            if os.path.isfile(self.view.center_frame.buttons_view.src_path):
                file_to_copy = os.path.basename(src_path)
                self.view.center_frame.buttons_view.dst_path = os.path.join(
                    dst_path, file_to_copy
                )
                shutil.copyfile(src_path, self.view.center_frame.buttons_view.dst_path)
            if os.path.isdir(self.view.center_frame.buttons_view.src_path):
                self.copy_tree(src_path, dst_path)
        else:
            self.view.center_frame.log.log_text.config(text="You Need To Choose a File")

    '''
    Copy source directory into destination directory recursively     
    '''

    def copy_tree(self, src, dst):
        try:
            dst = os.path.join(dst, os.path.basename(src))
            # if not os.path.exists(dst):
            os.makedirs(dst)
            contents = os.listdir(src)
            for item in contents:
                src = os.path.join(self.view.center_frame.buttons_view.src_path, item)
                self.view.center_frame.buttons_view.dst_path = os.path.join(dst, item)
                if os.path.isfile(src):
                    shutil.copyfile(src, self.view.center_frame.buttons_view.dst_path)
                elif os.path.isdir(src):
                    self.copy_tree(src, self.view.center_frame.buttons_view.dst_path)
        except (OSError, PermissionError, FileExistsError) as e:
            # If the error was caused because the source wasn't a directory
            if e.errno == errno.ENOTDIR:
                shutil.copytree(src, dst)
            else:
                print('Directory not copied. Error: %s' % e)

    '''
    Adding path to listbox named 'Favorites' and store its path in json file for future uses     
    '''

    def add_to_favorites(self, event):
        # show addition in the view
        favs = [item.get("path") for item in self.model.favorites.get()]
        if self.view.navbar.path.get() not in favs:
            fav_listbox = self.view.center_frame.favorites_lb_view.listbox
            fav_listbox.insert("end",
                               " ⭐ " + self.view.navbar.path.get())
            # store favorite object in json file
            self.model.favorites.store(self.view.navbar.path.get())

    '''
    Remove selected path from listbox named 'Favorites' and remove it from the json file     
    '''

    def rmv_from_favorites(self, event):
        # delete from view
        list_box = self.view.center_frame.favorites_lb_view.listbox
        selected = list_box.curselection()
        if selected is not ():
            # the split is used to dismiss the star icon
            selected_path = list_box.get(selected).split(" ", 2)[2]
            list_box.delete(selected)
            # remove from json file
            self.model.favorites.remove(selected_path)

    '''
    When selecting an element the text from the list view will be format
    into valid path and will be send to on favorite click
    '''

    def on_list_view_select(self, event):
        if self.view.center_frame.favorites_lb_view.listbox.size() > 0:
            try:
                w = event.widget
                index = int(w.curselection()[0])
                value = w.get(index)
                path = value[3:]
                self.on_favorite_click(path)
            except IndexError:
                pass

    '''
    When click an element the path will display in the tree view     
    '''

    def on_favorite_click(self, new_path):
        if os.path.isdir(new_path):
            self.model.back_stack.push(self.view.navbar.path.get())
            self.model.forward_stack.clear_stack()
            self.update_all_views(new_path)

    #   Right side - TreeView - of center frame Functionality
    '''
    Double click on tree item will display the clicked folder data and children
    '''

    def on_double_click(self, event):
        # get selected item
        try:
            item = self.view.center_frame.right_frame.tree.selection()[0]
            item_text = self.view.center_frame.right_frame.tree.item(item,
                                                                     "text")
        except IndexError:
            return
        # clear tree before update
        if os.path.isdir(os.path.join(self.view.navbar.path.get(), item_text)):
            new_path = os.path.join(self.view.navbar.path.get(), item_text)
            self.model.back_stack.push(self.view.navbar.path.get())
        elif os.path.isdir(os.path.dirname(self.searched_path)):
            new_path = os.path.dirname(self.searched_path)
        self.model.forward_stack.clear_stack()
        self.update_all_views(new_path)
        self.view.status_bar.item_label.config(text="None")

    '''
    Display the selected file name in the status bar
    '''

    def on_tree_select(self, event):
        index = self.view.center_frame.right_frame.tree.focus()
        line_tup = self.view.center_frame.right_frame.tree.item(index)
        self.view.center_frame.buttons_view.file_name = line_tup['text']
        self.view.status_bar.item_label.config(text=line_tup['text'])
        catch = self.view.center_frame.right_frame.tree.focus()
        try:
            self.searched_path = self.view.center_frame.right_frame.tree.item(catch)['values'][1]
        except IndexError:
            self.searched_path = ""

    '''
    Update children of the tree view be removing old children and inserting current path children    
    '''

    def update_treeview(self, path):
        exclude = ["#2"]
        self.change_tree_view_cols(exclude)
        self.change_tree_view_cols(exclude)
        self.view.center_frame.right_frame.tree.delete(
            *self.view.center_frame.right_frame.tree.get_children())
        self.folder_details, self.file_details = self.model.get_content_from_path(
            path, self.view.center_frame.select_view.hidden_flag)
        self.view.center_frame.show_folders_and_files(self.folder_details,
                                                      self.file_details)

    '''
    Sort a column from tree view by the index of the column    
    '''

    def sort_tree_view(self, index):
        self.view.center_frame.right_frame.tree.delete(
            *self.view.center_frame.right_frame.tree.get_children())
        self.folder_details.sort(key=operator.itemgetter(index))
        self.file_details.sort(key=operator.itemgetter(index))
        self.view.center_frame.show_folders_and_files(self.folder_details,
                                                      self.file_details)

    '''
    Update all views - tree, navigation bar, status bar items counter    
    '''

    def update_all_views(self, path):
        self.update_treeview(path)
        self.view.navbar.path.set(path)
        self.view.status_bar.item_count = self.model.get_folder_file_count(
            path, self.view.center_frame.select_view.hidden_flag)
        self.view.status_bar.item_count_label.config(text=self.view.status_bar.item_count)

    def find_all_files(self, name, path):
        result = []
        try:
            temp_time = time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(path)))
        except FileNotFoundError:
            temp_time = "No Permission"
        for root, dirs, files in os.walk(path):
            if name in files:
                result.append((name, os.path.join(root, name), temp_time))
            if name in dirs:
                result.append((name, os.path.join(root, name), temp_time))
        if not result:
            self.view.center_frame.log.log_text.config(text="-- File Not Found --")
        return result

    def change_tree_view_cols(self, excludes):
        displaycolumns = []
        self.view.center_frame.right_frame.tree.delete(
            *self.view.center_frame.right_frame.tree.get_children())
        self.view.center_frame.right_frame.exclusion_list.clear()
        for i in excludes:
            self.view.center_frame.right_frame.exclusion_list.append(i)
        for col in self.view.center_frame.right_frame.tree["columns"]:
            if not "%s" % col in self.view.center_frame.right_frame.exclusion_list:
                displaycolumns.append(col)
        self.view.center_frame.right_frame.tree["displaycolumns"] = displaycolumns
        for result in self.results:
            self.view.center_frame.right_frame.tree.insert("", index="end",
                                                           text=result[0],
                                                           values=result[0:])
