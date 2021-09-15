#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 31, 2019 04:59:03 PM PKT  platform: Linux

import sys
import datetime
import sqlite3
import time
from sqlite3 import Error
from threading import Thread
from tkinter import messagebox, simpledialog
import Main

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

# import Customer_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    # Customer_support.init(root, top)
    root.mainloop()

w = None
root = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    # Customer_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    parent = None
    top = None
    cursor = None

    def __init__(self, top=None, Name=None, Phone=None, balance=0,cursor=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Sans} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 20 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        customized_font = "-family {Calibri} -size 15 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=customized_font)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        top.geometry("880x753+640+142")
        top.title("New Toplevel")

        self.Name = ttk.Entry(top)
        self.Name.place(relx=0.159, rely=0.133, relheight=0.041, relwidth=0.232)
        self.Name.configure(width=204)
        self.Name.configure(takefocus="")
        self.Name.configure(cursor="xterm",font = font9)

        self.PhoneNumber = ttk.Entry(top)
        self.PhoneNumber.place(relx=0.477, rely=0.133, relheight=0.041, relwidth=0.232)
        self.PhoneNumber.configure(width=204)
        self.PhoneNumber.configure(takefocus="")
        self.PhoneNumber.configure(cursor="xterm",font = font9)

        self.Address = ttk.Entry(top)
        self.Address.place(relx=0.159, rely=0.193, relheight=0.041, relwidth=0.55)
        self.Address.configure(width=484)
        self.Address.configure(takefocus="")
        self.Address.configure(cursor="xterm",font = font9)

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.085, rely=0.133, height=29, width=61)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=customized_font)
        self.TLabel1.configure(relief='flat')
        self.TLabel1.configure(text='''Name''')
        self.TLabel1.configure(width=61)

        self.TLabel1_1 = ttk.Label(top)
        self.TLabel1_1.place(relx=0.403, rely=0.133, height=19, width=62)
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font=customized_font)
        self.TLabel1_1.configure(relief='flat')
        self.TLabel1_1.configure(text='''Phone#''')
        self.TLabel1_1.configure(width=62)

        self.TLabel1_3 = ttk.Label(top)
        self.TLabel1_3.place(relx=0.01, rely=0.199, height=29, width=132)
        self.TLabel1_3.configure(background="#d9d9d9")
        self.TLabel1_3.configure(foreground="#000000")
        self.TLabel1_3.configure(font=customized_font)
        self.TLabel1_3.configure(relief='flat')
        self.TLabel1_3.configure(text='''Shop Address''')
        self.TLabel1_3.configure(width=102)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.AddCustomerBtn = ttk.Button(top)
        self.AddCustomerBtn.place(relx=0.79, rely=0.2, height=28, width=130)
        self.AddCustomerBtn.configure(takefocus="")
        self.AddCustomerBtn.configure(text='''Add Customer''')
        self.AddCustomerBtn.configure(command = self.AddCustomer)

        self.style.configure('mystyle.Treeview.Heading',font=('Calibri',16,"bold"))
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                             font=('Calibri', 15),rowheight=40)  # Modify the font of the body
        self.Scrolledtreeview1 = ScrolledTreeView(top, style="mystyle.Treeview", columns=('Due Amount', 'PhoneNum','Address'))
        self.Scrolledtreeview1.place(relx=0.057, rely=0.372, relheight=0.546
                , relwidth=0.898)
        self.Scrolledtreeview1.tag_configure('odd', background='#E8E8E8')
        self.Scrolledtreeview1.tag_configure('even', background='#DFDFDF')
        # self.tree = ttk.Treeview(self.parent, columns=('Dose', 'Modification date'))
        self.Scrolledtreeview1.heading('#0', text='Name')
        self.Scrolledtreeview1.heading('#1', text='Balance')
        self.Scrolledtreeview1.heading('#2', text='Phone #')
        self.Scrolledtreeview1.heading('#3', text='Address', anchor='n')
        self.Scrolledtreeview1.column('#0')  # , stretch=tk.YES
        self.Scrolledtreeview1.column('#1',width=150)  # , stretch=tk.YES
        self.Scrolledtreeview1.column('#2',width=150)  # , stretch=tk.YES
        self.Scrolledtreeview1.column('#3', width=400)  # , stretch=tk.YES
        self.Scrolledtreeview1.bind("<Return>", self.updateBalance)
        self.Scrolledtreeview1.bind("<Delete>", self.deleteCustomer)


        self.tree_iterator = 0

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.028, rely=0.027, height=49, width=232)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font10)
        self.TLabel2.configure(relief='flat')
        self.TLabel2.configure(text='''Customers''')
        self.TLabel2.configure(width=232)

        self.customer_name_Entry = ttk.Entry(top)
        self.customer_name_Entry.place(relx=0.2, rely=0.305, relheight=0.050, relwidth=0.532)
        self.customer_name_Entry.configure(takefocus="")
        self.customer_name_Entry.configure(cursor="xterm", font = font9)




        self.TLabel1_1 = ttk.Label(top)
        self.TLabel1_1.place(relx=0.720, rely=0.133, relheight=0.041, relwidth=0.232)
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font=customized_font)
        self.TLabel1_1.configure(relief='flat')
        self.TLabel1_1.configure(text='''Balance:''')
        self.TLabel1_1.configure(width=62)

        self.customer_balance = ttk.Entry(top)
        self.customer_balance.place(relx=0.800, rely=0.133, relheight=0.041, relwidth=0.125)
        self.customer_balance.configure(width=204)
        self.customer_balance.configure(takefocus="")
        self.customer_balance.configure(cursor="xterm",font = font9)

        self.TLabel1_2 = ttk.Label(top)
        self.TLabel1_2.place(relx=0.050, rely=0.315, height=19, width=132)
        self.TLabel1_2.configure(background="#d9d9d9")
        self.TLabel1_2.configure(foreground="#000000")
        self.TLabel1_2.configure(font=customized_font)
        self.TLabel1_2.configure(relief='flat')
        self.TLabel1_2.configure(text='''Customer Name''')
        self.TLabel1_2.configure(width=132)

        self.TButton1_3 = ttk.Button(top)
        self.TButton1_3.place(relx=0.759, rely=0.310, height=28, width=130)
        self.TButton1_3.configure(takefocus="")
        self.TButton1_3.configure(text='''Get Customer''')
        self.TButton1_3.configure(command = self.getCustomer)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.006, rely=0.266, relwidth=0.989)

        if Phone != None:
            self.cursor = cursor
            self.PhoneNumber.insert(0, Phone)
            self.customer_balance.insert(0,balance)
            self.parent = Phone
            self.top = top
        if Name is not None:
            self.Name.insert(0,Name)


    def __del__(self):
        if self.cursor == None:
            Main.LaunchWindow()

    def refresh_Table(self,where_clause=''):
        pass
    def updateBalance(self, event=None):
        global root
        date = datetime.datetime.now()
        date=date.strftime("%Y-%m-%d")
        print(date)
        curItem = self.Scrolledtreeview1.focus()
        item = self.Scrolledtreeview1.item(curItem)
        name = item['text']
        old_balance = item['values'][0]
        phone_number = "0"+str(item['values'][1])

        received = simpledialog.askstring("Input","Enter Received Amount",
                                        parent=root)
        Note = simpledialog.askstring("Input", "Here you can type any Note or Reminder",
                                          parent=root)

        new_balance = int(old_balance) - int(received)
        print(new_balance)
        print(phone_number)
        global conn
        try:
            conn = sqlite3.connect("MyDataBase.db")
            c = conn.cursor()
            c.execute(f'UPDATE Customers SET Due_Amount = {new_balance} WHERE PhoneNumber = "{phone_number}"')
            c.execute(f'INSERT INTO Ledger(customerName,receivingDate,ReceivedAmount,Due_Amount,Note)VALUES ("{name}","{date}","{received}","{new_balance}","{Note}")')
            conn.commit()
            self.getCustomer()

        except Error as e:
            print(e)

    def deleteCustomer(self,event=None):
        curItem = self.Scrolledtreeview1.focus()
        item = self.Scrolledtreeview1.item(curItem)
        phone_number = "0" + str(item['values'][1])
        name = item['text']
        print(name)
        choice = messagebox.askyesno("confirmation", "Do you want to Delete this Customer?")
        if choice:
            global conn
            try:
                conn = sqlite3.connect("MyDataBase.db")
                c = conn.cursor()

                c.execute(f'DELETE FROM Customers WHERE C_Name = "{name}"')
                c.execute(f'DELETE FROM Ledger WHERE customerName = "{name}"')
                self.Scrolledtreeview1.delete(curItem)
                conn.commit()



            except Error as e:
                print(e)

    def AddCustomer(self,event = None):
        Name = self.Name.get().lower()
        Phn = self.PhoneNumber.get()
        blnc = int(self.customer_balance.get())
        Addr = self.Address.get()
        if self.parent != None:
            self.cursor.execute(f'INSERT INTO Customers(C_Name,Due_Amount,PhoneNumber,Address)VALUES ("{Name}",{blnc},"{Phn}","{Addr}")')
            self.top.destroy()
            return

        global conn
        try:
            conn = sqlite3.connect("MyDataBase.db")
            c = conn.cursor()
            c.execute(f'INSERT INTO Customers(C_Name,Due_Amount,PhoneNumber,Address)VALUES ("{Name}",{blnc},"{Phn}","{Addr}")')
            conn.commit()
            self.Name.delete(0,'end')
            self.PhoneNumber.delete(0,'end')
            self.Address.delete(0,'end')
            self.customer_balance.delete(0,'end')
            messagebox.showinfo("Done", "Customer added...!")

        except Error as e:
            if "UNIQUE" in e.__str__():
                messagebox.showinfo("Error","Some customer with this number already added...!")

    def getCustomer(self):
        for i in self.Scrolledtreeview1.get_children():
            self.Scrolledtreeview1.delete(i)
        customer_name = self.customer_name_Entry.get().lower()
        global conn
        try:
            conn = sqlite3.connect("MyDataBase.db")
            c = conn.cursor()
            c.execute(f'SELECT * FROM Customers WHERE C_Name like "{customer_name}%"')
            rows = c.fetchall()
            tag_list = ['odd', 'even']
            for row in rows:
                # print(row)
                self.Scrolledtreeview1.insert('', 'end', text=row[0],
                                              values=(row[1], row[2],row[3]),tags=(tag_list[self.tree_iterator%2],))  #
                # Increment counter
                self.tree_iterator = self.tree_iterator + 1
                found = True

        except Error as e:
            print(e)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()


def launchWindow():
    vp_start_gui()

