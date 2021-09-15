#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 21, 2019 08:05:09 PM PKT  platform: Linux

import sys
import os
from tkinter import messagebox
from datetime import  datetime
from sqlite3 import Error
import sqlite3

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

# import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    # unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    # unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def insert_data(self):
        """
        Insertion method.
        """
        self.Scrolledtreeview1.insert('', 'end', text="Item_" + str(self.tree_iterator),
                             values=(" mg", "gg"))
        # Increment counter
        self.tree_iterator = self.tree_iterator + 1


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.conn = sqlite3.connect("MyDataBase.db")
        self.c = self.conn.cursor()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Sans Mono} -size 15 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 30 -weight normal -slant "  \
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

        top.geometry("1150x687+450+199")
        top.title("AF Softwares")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.035, rely=0.044, height=61, width=304)
        self.Label1.configure(font=font9)
        self.Label1.configure(text='''Sale Summary''')
        self.Label1.configure(width=304)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.026, rely=0.131, relheight=0.24, relwidth=0.717)

        # self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(width=825)
        self.i = tk.IntVar()
        self.DateRB = tk.Radiobutton(self.Frame1)
        self.DateRB.place(relx=0.376, rely=0.03, relheight=0.139, relwidth=0.119)
        self.DateRB.configure(indicatoron="0")
        self.DateRB.configure(justify='left')
        self.DateRB.configure(text='''By Date''')
        self.DateRB.configure(value=1,variable=self.i)
        self.DateRB.configure(width=98)

        self.MonthRB = tk.Radiobutton(self.Frame1)
        self.MonthRB.place(relx=0.376, rely=0.455, relheight=0.139
                , relwidth=0.119)
        self.MonthRB.configure(activebackground="#f9f9f9")
        self.MonthRB.configure(indicatoron="0")
        self.MonthRB.configure(justify='left',variable=self.i)
        self.MonthRB.configure(text='''By Month''')
        self.MonthRB.configure(value=2)
        self.MonthRB.configure(width=98)

        self.yearRB = tk.Radiobutton(self.Frame1)
        self.yearRB.place(relx=0.376, rely=0.665, relheight=0.139
                , relwidth=0.119)
        self.yearRB.configure(activebackground="#f9f9f9")
        self.yearRB.configure(indicatoron="0")
        self.yearRB.configure(justify='left',variable=self.i)
        self.yearRB.configure(text='''By Year''')
        self.yearRB.configure(value=3)
        self.yearRB.configure(width=98)

        self.WeekRB = tk.Radiobutton(self.Frame1)
        self.WeekRB.place(relx=0.376, rely=0.252, relheight=0.139
                , relwidth=0.119)
        self.WeekRB.configure(activebackground="#f9f9f9")
        self.WeekRB.configure(indicatoron="0")
        self.WeekRB.configure(justify='left',variable=self.i)
        self.WeekRB.configure(text='''By Week''')
        self.WeekRB.configure(value=4)
        self.WeekRB.configure(width=98)

        self.DateEntry = tk.Entry(self.Frame1)
        self.DateEntry.place(relx=0.139, rely=0.061,height=33, relwidth=0.068)
        self.DateEntry.configure(background="white")
        self.DateEntry.configure(font=font10)
        self.DateEntry.configure(width=56)
        self.DateEntry.focus()


        self.MonthEnrty = tk.Entry(self.Frame1)
        self.MonthEnrty.place(relx=0.139, rely=0.364,height=33, relwidth=0.068)
        self.MonthEnrty.configure(background="white")
        self.MonthEnrty.configure(font=font10)
        self.MonthEnrty.configure(selectbackground="#c4c4c4")

        self.YearEntry = tk.Entry(self.Frame1)
        self.YearEntry.place(relx=0.139, rely=0.667,height=33, relwidth=0.068)
        self.YearEntry.configure(background="white")
        self.YearEntry.configure(font=font10)
        self.YearEntry.configure(selectbackground="#c4c4c4")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.048, rely=0.697, height=21, width=49)
        self.Label2.configure(text='''Year''')
        self.Label2.configure(width=49)

        self.Label2_6 = tk.Label(self.Frame1)
        self.Label2_6.place(relx=0.048, rely=0.121, height=21, width=39)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(text='''Date''')

        self.Label2_7 = tk.Label(self.Frame1)
        self.Label2_7.place(relx=0.036, rely=0.394, height=21, width=59)
        self.Label2_7.configure(activebackground="#f9f9f9")
        self.Label2_7.configure(text='''Month''')
        self.Label2_7.configure(width=59)

        self.WeekEntry = tk.Entry(self.Frame1)
        self.WeekEntry.place(relx=0.285, rely=0.333,height=33, relwidth=0.068)
        self.WeekEntry.configure(background="white")
        self.WeekEntry.configure(font=font10)
        self.WeekEntry.configure(selectbackground="#c4c4c4")

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.212, rely=0.394, height=21, width=56)
        self.Label3.configure(text='''Week #''')

        self.GetSummaryButton = tk.Button(top)
        self.GetSummaryButton.place(relx=0.8, rely=0.175, height=41, width=131)
        self.GetSummaryButton.configure(text='''Filter''')
        self.GetSummaryButton.configure(width=131)
        self.GetSummaryButton.configure(command=lambda :self.date_filtered_summary(Option=1))

        self.style.configure('mystyle.Treeview.Heading',  font=font10)
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 15))  # Modify the font of the body
        self.Scrolledtreeview1 = ScrolledTreeView(top,style = "mystyle.Treeview",columns =('Sale','Profit','item sold'))
        self.Scrolledtreeview1.place(relx=0.026, rely=0.422, relheight=0.54, relwidth=0.948)

        self.Scrolledtreeview1.tag_configure('odd', background='#E8E8E8')
        self.Scrolledtreeview1.tag_configure('even', background='#DFDFDF')
        # self.tree = ttk.Treeview(self.parent, columns=('Dose', 'Modification date'))
        self.Scrolledtreeview1.heading('#0', text='Name')
        self.Scrolledtreeview1.heading('#1', text='Sale')
        self.Scrolledtreeview1.heading('#2', text='Profit')
        self.Scrolledtreeview1.heading('#3', text='item sold')

        self.Scrolledtreeview1.column('#0')#, stretch=tk.YES
        self.Scrolledtreeview1.column('#1')#, stretch=tk.YES
        self.Scrolledtreeview1.column('#2')#, stretch=tk.YES
        self.Scrolledtreeview1.column('#3')#, stretch=tk.YES
        self.tree_iterator = 0


        self.GetSalesButton = tk.Button(top)
        self.GetSalesButton.place(relx=0.8, rely=0.275, height=41, width=131)
        self.GetSalesButton.configure(activebackground="#f9f9f9")
        self.GetSalesButton.configure(text='''Get All Sales''')
        self.GetSalesButton.configure(command=lambda :self.get_all_sales())

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.550, rely=0.242, height=21, width=200)
        self.Label4.configure(text='''Total Sale''')
        self.Label4.configure(font=("Calibri",15))

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.540, rely=0.576, height=21, width=200)
        self.Label5.configure(text='''Total Profit''')
        self.Label5.configure(font=("Calibri",15))

        self.SaleTextView = tk.Entry(self.Frame1)
        self.SaleTextView.place(relx=0.739, rely=0.182, relheight=0.233, relwidth = 0.165)
        self.SaleTextView.configure(background="white")
        self.SaleTextView.configure(font=font10)
        self.SaleTextView.configure(selectbackground="#c4c4c4")
        self.SaleTextView.configure(width=136)
        # self.SaleTextView.configure(wrap='word',state = "disabled")

        self.ProfitTextView = tk.Entry(self.Frame1)
        self.ProfitTextView.place(relx=0.739, rely=0.545, relheight=0.233, relwidth = 0.165)
        self.ProfitTextView.configure(background="white")
        self.ProfitTextView.configure(font=font10)
        self.ProfitTextView.configure(selectbackground="#c4c4c4")
        self.ProfitTextView.configure(width=136)
        # self.ProfitTextView.configure(state = "disabled")#wrap='word',
        # self.Scrolledtreeview1.grid(row=4, columnspan=4, sticky='nsew')

    def __del__(self):
        Main.LaunchWindow()

    # def print_Sales(self,event = None):
    #     global conn
    #     try:
    #         conn = sqlite3.connect("MyDataBase.db")
    #         c = conn.cursor()
    #
    #         c.execute(f'SELECT Billid, Itemid,Name,sum(Item_total),sum(Item_profit)'
    #                   f' from Stocks'
    #                   f' INNER JOIN (SELECT * From Sales WHERE Billid IN (SELECT Bill_Id from Bills where today_date = date("2019-01-23"))) ON Itemid = Item_Id'
    #                   f' GROUP BY Itemid')
    #         Sales_Data = c.fetchall()
    #         # c.execute(f'SELECT * from Stocks WHERE Billid = (SELECT Bill_Id from Bills where today_date = date("{e_date}"))')
    #         # Sales_Data = c.fetchall()
    #
    #         for row in Sales_Data:
    #             print(row)
    #         c.close()
    #         conn.close()
    #     except Error as e:
    #         print(e)
    #     finally:
    #         conn.close()
    def get_all_sales(self,event=None):
        global conn, c
        try:
            sale = 0
            profit = 0
            conn = sqlite3.connect("MyDataBase.db")
            c = conn.cursor()
            c.execute(f'SELECT ItemName,SUM(Item_total),SUM(Item_profit),SUM(Item_quantitty) FROM Sales group by ItemName')
            rows = c.fetchall()
            print(rows.__len__())
            for i in self.Scrolledtreeview1.get_children():
                self.Scrolledtreeview1.delete(i)
            for row in rows:
                profit += row[2]
                sale += row[1]
                tag_list = ['odd', 'even']
                tag = tag_list[self.tree_iterator % 2]

                self.Scrolledtreeview1.insert('', 'end', text=row[0],
                                              values=(row[1], row[2], row[3]),
                                              tags=(tag,))  #
                # Increment counter
                self.tree_iterator = self.tree_iterator + 1
                self.ProfitTextView.delete(0, 'end')
                self.SaleTextView.delete(0, 'end')
                self.ProfitTextView.insert(0, profit)
                self.SaleTextView.insert(0, sale)
            c.close()
            conn.close()
        except Error as e:
            print(e)
        finally:
            conn.close()
    def populate_treeview(self,row):
        pass
    def date_filtered_summary(self, event=None, Option=None):
        global conn, c
        try:
            sale = 0
            profit = 0
            conn = sqlite3.connect("MyDataBase.db")
            c = conn.cursor()
            day = self.DateEntry.get()
            month = self.MonthEnrty.get()
            year = self.YearEntry.get()
            e_date= year+'-'+month+'-'+day
            found = False

            if self.i.get() == 1:
                if len(day) ==0 or  len(month) == 0 or len(year) ==0 :
                    messagebox.showwarning("Invalid", "Please Fill All the fields")
                    return
                e_date = datetime.strptime(e_date, "%Y-%m-%d")
                # if Option == 2:
                #
                #     c.execute(f'SELECT ItemName,SUM(Item_total),SUM(Item_profit),SUM(Item_quantitty) FROM Sales group by ItemName')
                #     rows = c.fetchall()
                #     print(rows.__len__())
                #     for row in rows:
                #         self.Scrolledtreeview1.insert('', 'end', text=row[0],
                #                                       values=(row[1], row[2],row[3]))  #
                #         # Increment counter
                #         self.tree_iterator = self.tree_iterator + 1
                #         found = True
                # elif Option==1:
                if Option==1:
                    c.execute(f'SELECT * from Bills where today_date = date("{e_date}")')
                    rows = c.fetchall()
                    for row in rows:
                        profit += row[2]
                        sale += row[3]
                        print(row)
                        found = True

            elif self.i.get() == 2:
                if len(month)==0:
                    messagebox.showwarning("Invalid", "Please Fill the month field")
                    return
                if len(month)==1:

                    temp = "%-0"+month+"-%"
                else:
                    temp = "%-"+month+"-%"
                if Option == 2:
                    c.execute(f'SELECT Billid, Itemid,Name,sum(Item_total),sum(Item_profit)'
                              f' from Stocks'
                              f' INNER JOIN (SELECT * From Sales WHERE Billid IN (SELECT Bill_Id from Bills where today_date = date("{e_date}"))) ON Itemid = Item_Id'
                              f' GROUP BY Itemid')
                    rows = c.fetchall()
                    for row in rows:
                        # print(row)
                        self.Scrolledtreeview1.insert('', 'end', text=row[2],
                                                      values=(row[3], row[4]))  #
                        # Increment counter
                        self.tree_iterator = self.tree_iterator + 1
                        found = True
                elif Option == 1:
                    c.execute(f'SELECT * from Bills where today_date like "{temp}"')
                    rows = c.fetchall()
                    for row in rows:
                        profit += row[2]
                        sale += row[3]
                        found = True
            elif self.i.get() == 3:
                if len(year)==0:
                    messagebox.showwarning("Invalid", "Please Fill the year field")
                    return

                temp = year+"-%"
                print(temp)
                if Option == 2:
                    c.execute(f'SELECT Billid, Itemid,Name,sum(Item_total),sum(Item_profit)'
                              f' from Stocks'
                              f' INNER JOIN (SELECT * From Sales WHERE Billid IN (SELECT Bill_Id from Bills where today_date = date("{temp}"))) ON Itemid = Item_Id'
                              f' GROUP BY Itemid')
                    rows = c.fetchall()
                    for row in rows:
                        # print(row)
                        self.Scrolledtreeview1.insert('', 'end', text=row[2],
                                                      values=(row[3], row[4]))  #
                        # Increment counter
                        self.tree_iterator = self.tree_iterator + 1
                        found = True

                elif Option == 1:
                    c.execute(f'SELECT * from Bills where today_date like "{temp}"')
                    rows = c.fetchall()
                    for row in rows:
                        profit += row[2]
                        sale += row[3]
                        print(row)
                        found = True
            elif self.i.get() == 4:
                day1 =0
                day2 =0
                if len(day) ==0 or  len(month) == 0 or len(year) ==0 :
                    messagebox.showwarning("Invalid", "Please Fill All the fields")
                    return
                week = self.WeekEntry.get()
                if len(week) == 0:
                    messagebox.showwarning("Invalid", "Please Fill the week field")
                    return

                if len(month)==1:
                    month = "0"+month

                if week == '1':
                    day1 = '1'
                    day2 = '8'
                elif week =='2':
                    day1 = '9'
                    day2 = '16'
                elif week =='3':
                    day1 = '17'
                    day2 = '24'
                elif week =='4':
                    day1 = '25'
                    day2 = '31'
                e_date1 = year + '-' + month + '-' + day1
                e_date2 = year + '-' + month + '-' + day2

                print(e_date1)
                print(e_date2)
                if Option == 2:
                    c.execute(f'SELECT Billid, Itemid,Name,sum(Item_total),sum(Item_profit)'
                              f' from Stocks'
                              f' INNER JOIN (SELECT * From Sales WHERE Billid IN (SELECT Bill_Id from Bills where today_date BETWEEN date("{e_date1}") AND date("{e_date2}"))) ON Itemid = Item_Id'
                              f' GROUP BY Itemid')
                    rows = c.fetchall()
                    for row in rows:
                        # print(row)
                        self.Scrolledtreeview1.insert('', 'end', text=row[2],
                                                      values=(row[3], row[4]))  #
                        # Increment counter
                        self.tree_iterator = self.tree_iterator + 1
                        found = True
                elif Option == 1:

                    c.execute(f'SELECT * from Bills where today_date BETWEEN date("{e_date1}") AND date("{e_date2}")')
                    rows = c.fetchall()
                    for row in rows:
                        profit += row[2]
                        sale += row[3]
                        print(row)
                        found = True

            else:
                messagebox.showwarning("Missing", "Please Select one option")
                return


            if not found:
                messagebox.showinfo("Not Found", "No Record Found of this name")
            elif Option == 1:
                self.ProfitTextView.delete(0, 'end')
                self.SaleTextView.delete(0, 'end')
                self.ProfitTextView.insert(0, profit)
                self.SaleTextView.insert(0, sale)

            c.close()
            conn.close()
        except Error as e:
            print(e)
        finally:
            conn.close()

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

