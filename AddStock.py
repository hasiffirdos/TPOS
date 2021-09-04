#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 12, 2018 08:22:07 PM PKT  platform: Linux

# import sys
import os
import datetime
import Classes as obj
from sqlite3 import Error
import sqlite3
import Main


try:
    import Tkinter as tk

except ImportError:
    import tkinter as tk
    from tkinter import messagebox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import AddStock_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = AddStock (root)
    AddStock_support.init(root, top)
    root.mainloop()


w = None
def create_AddStock(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    print("create stock is calling...")
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = AddStock (w)
    AddStock_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_AddStock(root):
    print("some thing")
    root.destroy()
    Main.vp_start_gui()

class AddStock:
    CurrentItem = []
    name = ""
    def confirmUpdate(self,event = None):
        choice = messagebox.askyesno("confirmation", "Do you want to update this")
        curItem = self.Scrolledtreeview1.focus()
        item = self.Scrolledtreeview1.item(curItem,'values')

        if choice and curItem != '':
            self.AddNewButton.config(state = "disabled")
            self.NameEntry.delete(0,'end')
            self.NameEntry.insert(0,item[0])
            self.name = item[0]
            self.QuantityEntry.delete(0,'end')
            self.SellingPriceEntry.delete(0,'end')
            self.SellingPriceEntry.insert(0,item[3])
            self.BuyingPriceEntry.delete(0,'end')
            self.BuyingPriceEntry.insert(0,item[2])
            self.QuantityEntry.focus()
            # self.UpdatethisItem()


    def flush_fields(self):
        self.QuantityEntry.delete(0,'end')
        self.NameEntry.delete(0,'end')
        self.SellingPriceEntry.delete(0,'end')
        self.BuyingPriceEntry.delete(0,'end')
    def UpdatethisItem(self,event = None):

            global conn,c
            try:
                conn = sqlite3.connect("MyDataBase.db")
                c = conn.cursor()
                Name = self.NameEntry.get()
                quantity = self.QuantityEntry.get()
                bPrice = self.BuyingPriceEntry.get()
                sPrice = self.SellingPriceEntry.get()
                if quantity == "" or bPrice == "" or sPrice == "":
                    messagebox.showerror("Error", "Fill All the Fiels")
                    return

                # c.execute(f'-- UPDATE Stocks SET Quantity = Quantity +?,buying_price = ?,sale_price =? WHERE Name like "%s"'%Name,(quantity,bPrice,sPrice))
                c.execute(f"UPDATE Stocks SET Name = '{Name}', Quantity = Quantity + {quantity},buying_price = {bPrice},sale_price ={sPrice} WHERE Name = '{self.name}'")
                conn.commit()
                messagebox.showinfo("Done", "item Added Successfully")
                self.flush_fields()
                rows = c.fetchall()
                for row in rows:
                    self.ExsitedItemsListbox.insert(0, row)
                    # print(row)
                c.close()
                conn.close()
                self.AddNewButton.config(state="normal")



            # conn.close()
            except Error as e:
                print(e)
            finally:
                # c.close()
                conn.close()



    def SearchItemByName(self,event= None):

        global conn,c
        try:
            conn = sqlite3.connect("MyDataBase.db")
            c = conn.cursor()
            Name = self.SearchByNameEntry.get()
            temp = "%" + Name + "%"
            c.execute(f'SELECT * from Stocks WHERE Name like "{temp}"')
            rows = c.fetchall()
            found = False
            for i in self.Scrolledtreeview1.get_children():
                self.Scrolledtreeview1.delete(i)
            for row in rows:
                self.Scrolledtreeview1.insert('', 0, text=row[0],
                                              values=(row[1],row[2],row[5],row[6],row[7]))
                # Increment counter
                self.tree_iterator = self.tree_iterator + 1

                # self.ExsitedItemsListbox.insert(0,
                # f" id : {row[0]} | Name: {row[1]}       ||| Quantity: {row[2]} ||| buying_price: {row[5]} ||| Selling_price {row[6]} ||| Profit: {row[7]}")
                # # print(row)
                found = True
            if not found:
                messagebox.showinfo("Not Found", "No Record Found of this name")

            c.close()
            conn.close()


        # conn.close()
        except Error as e:
            print(e)
        finally:
            # c.close()
            conn.close()

    def ViewStocks(self):
        global conn
        try:
            conn = sqlite3.connect("MyDataBase.db")
            c = conn.cursor()
            c.execute("SELECT * FROM Stocks")
            rows = c.fetchall()
            found = True
            total = 0
            for i in self.Scrolledtreeview1.get_children():
                self.Scrolledtreeview1.delete(i)
            for row in rows:
                self.Scrolledtreeview1.insert('', 'end', text=row[0],
                                              values=(row[1], row[2], row[5], row[6], row[7]))
                # Increment counter
                total+=(row[2]*row[5])
                self.tree_iterator = self.tree_iterator + 1
                found = False

            self.GrandTotal.delete(0,'end')
            self.GrandTotal.insert(0,total)
        except Error as e:
            print(e)
    def AddStockToDataBase(self,event = None):
        global conn,c
        try:
            conn = sqlite3.connect("MyDataBase.db")
            c = conn.cursor()
            # name = str(name)
            name =self.NameEntry.get()
            quantity =self.QuantityEntry.get()
            bPrice = self.BuyingPriceEntry.get()
            sPrice = self.SellingPriceEntry.get()
            if len(name) > 0 and len(quantity) > 0 and len(bPrice) > 0 and len(sPrice) > 0 :

                data = name,quantity,"barcode","picture",bPrice,sPrice,int(0)
                c.execute('INSERT INTO Stocks(Name,Quantity,Barcode,picture,buying_price,sale_price,profit) VALUES (?,?,?,?,?,?,?)',data)
                conn.commit()
                messagebox.showinfo("Done","Add Successfully")
                self.NameEntry.delete(0, 'end')
                self.QuantityEntry.delete(0, 'end')
                self.BuyingPriceEntry.delete(0, 'end')
                self.SellingPriceEntry.delete(0, 'end')
                self.NameEntry.focus()

            else:
                messagebox.showerror("Error","Fill All the Fields")
            # c.execute('SELECT * from Stocks')
            # rows = c.fetchall()
            # for row in rows:
            #     print(row)
            c.close()
            conn.close()


        # conn.close()
        except Error as e:
            print(e)
        finally:
            conn.close()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font9 = "-family {DejaVu Sans} -size 36 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font10 = "-family {DejaVu Sans} -size 20 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()

        top.geometry("1098x747+405+168")
        top.title("Al-Ferooz Garments")  #New Toplevel



        self.NameEntry = tk.Entry(top)
        self.NameEntry.place(relx=0.128, rely=0.161,height=43, relwidth=0.179)
        self.NameEntry.configure(background="white")
        self.NameEntry.configure(font=font10)
        self.NameEntry.configure(width=196)
        self.NameEntry.focus()

        self.QuantityEntry = tk.Entry(top)
        self.QuantityEntry.place(relx=0.401, rely=0.161, height=43
                , relwidth=0.169)
        self.QuantityEntry.configure(background="white")
        self.QuantityEntry.configure(font=font10)
        self.QuantityEntry.configure(width=186)

        self.BuyingPriceEntry = tk.Entry(top)
        self.BuyingPriceEntry.place(relx=0.71, rely=0.161, height=43
                , relwidth=0.16)
        self.BuyingPriceEntry.configure(background="white")
        self.BuyingPriceEntry.configure(font=font10)
        self.BuyingPriceEntry.configure(width=176)

        self.SellingPriceEntry = tk.Entry(top)
        self.SellingPriceEntry.place(relx=0.128, rely=0.281, height=43
                , relwidth=0.179)
        self.SellingPriceEntry.configure(background="white")
        self.SellingPriceEntry.configure(font=font10)
        self.SellingPriceEntry.configure(width=196)

        self.AddNewButton = tk.Button(top)
        self.AddNewButton.place(relx=0.719, rely=0.361, height=41, width=110)
        self.AddNewButton.configure(text='''Add New''')
        self.AddNewButton.configure(width=110)
        self.AddNewButton.configure(command=self.AddStockToDataBase)

        self.GetStocks = tk.Button(top)
        self.GetStocks.place(relx=0.868, rely=0.522, height=41, width=95)
        self.GetStocks.configure(text='''View Stocks''')
        self.GetStocks.configure(width=110)
        self.GetStocks.configure(command=self.ViewStocks)

        self.UpdateButton = tk.Button(top)
        self.UpdateButton.place(relx=0.838, rely=0.361, height=41, width=95)
        self.UpdateButton.configure(text='''Update''')
        self.UpdateButton.configure(width=95, command=self.UpdatethisItem)
        self.UpdateButton.bind('<Return>',self.UpdatethisItem)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.064, rely=0.174, height=21, width=43)
        self.Label1.configure(text='''Name''')
        # self.Label1.configure(font=font10)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.337, rely=0.174, height=21, width=60)
        self.Label2.configure(text='''Quantity''')
        # self.Label2.configure(font=font10)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.601, rely=0.174, height=21, width=85)
        self.Label3.configure(text='''Buying Price''')
        # self.Label3.configure(font=font10)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.027, rely=0.295, height=21, width=84)
        self.Label4.configure(text='''Selling Price''')
        # self.Label4.configure(font=font10)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.064, rely=0.027, height=61, width=306)
        self.Label5.configure(font=font9)
        self.Label5.configure(text='''Add Stocks''')


        # self.ExsitedItemsListbox = tk.Listbox(top)
        # self.ExsitedItemsListbox.place(relx=0.055, rely=0.616, relheight=0.236
        #         , relwidth=0.887)
        # self.ExsitedItemsListbox.configure(background="white")
        # self.ExsitedItemsListbox.configure(font=font10)
        # self.ExsitedItemsListbox.configure(width=974,bg = "black",fg ="white")
        # self.ExsitedItemsListbox.bind("<Button-1>",self.confirmUpdate)


        self.style.configure('mystyle.Treeview.Heading', font=('Calibri', 12))
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                             font=('Calibri', 12))  # Modify the font of the bodySellin
        self.Scrolledtreeview1 = ScrolledTreeView(top, style="mystyle.Treeview", columns=('Name', 'Quantity','Buying price','Selling Price','profit'))
        self.Scrolledtreeview1.place(relx=0.055, rely=0.616, relheight=0.350
                , relwidth=0.887)
        self.Scrolledtreeview1.bind("<ButtonRelease-1>",self.confirmUpdate)
        self.Scrolledtreeview1.tag_configure('odd', background='#E8E8E8')
        self.Scrolledtreeview1.tag_configure('even', background='#DFDFDF')
        # self.tree = ttk.Treeview(self.parent, columns=('Dose', 'Modification date'))
        self.Scrolledtreeview1.heading('#0', text='ID')
        self.Scrolledtreeview1.heading('#1', text='Name')
        self.Scrolledtreeview1.heading('#2', text='Quantity')
        self.Scrolledtreeview1.heading('#3', text='Buying price')
        self.Scrolledtreeview1.heading('#4', text='Selling price')
        self.Scrolledtreeview1.heading('#5', text='profit')
        self.Scrolledtreeview1.column('#0',width = 100)  # , stretch=tk.YES
        self.Scrolledtreeview1.column('#1',width = 300)  # , stretch=tk.YES
        self.Scrolledtreeview1.column('#2',width = 100)  # , stretch=tk.YES
        self.Scrolledtreeview1.column('#3',width = 100)  # , stretch=tk.YES
        self.Scrolledtreeview1.column('#4',width = 100)  # , stretch=tk.YES
        self.Scrolledtreeview1.column('#5',width = 100)  # , stretch=tk.YES
        self.tree_iterator = 0

        self.SearchByNameEntry = tk.Entry(top)
        self.SearchByNameEntry.place(relx=0.173, rely=0.522, height=43
                , relwidth=0.279)
        self.SearchByNameEntry.configure(background="white")
        self.SearchByNameEntry.configure(font=font10)
        self.SearchByNameEntry.configure(width=306)
        self.SearchByNameEntry.bind("<Return>",self.SearchItemByName)

        self.GrandTotal = tk.Entry(top)
        self.GrandTotal.place(relx=0.700, rely=0.522, height=43
                                     , relwidth=0.150)
        self.GrandTotal.configure(background="white")
        self.GrandTotal.configure(font=font10)
        self.GrandTotal.configure(width=100)


        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.064, rely=0.529, height=21, width=111)
        self.Label6.configure(text='''Search by Name''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        # destroy_AddStock()

    def __del__(self):
        print("something to print")
        # destroy_AddStock(self.root)
        Main.LaunchWindow()
        self.c.close()
        self.conn.close()
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



