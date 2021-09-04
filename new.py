# # # import tkinter as tk
# # #
# # # class VerticalScrolledFrame(tk.Frame):
# # #     """A pure Tkinter scrollable frame that actually works!
# # #
# # #     * Use the 'interior' attribute to place widgets inside the scrollable frame
# # #     * Construct and pack/place/grid normally
# # #     * This frame only allows vertical scrolling
# # #     """
# # #     def __init__(self, parent, *args, **kw):
# # #         tk.Frame.__init__(self, parent, *args, **kw)
# # #
# # #         # create a canvas object and a vertical scrollbar for scrolling it
# # #         vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
# # #         vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
# # #         canvas = tk.Canvas(self, bd=0, highlightthickness=0,
# # #                         yscrollcommand=vscrollbar.set)
# # #         canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
# # #         vscrollbar.config(command=canvas.yview)
# # #
# # #         # reset the view
# # #         canvas.xview_moveto(0)
# # #         canvas.yview_moveto(0)
# # #
# # #         # create a frame inside the canvas which will be scrolled with it
# # #         self.interior = interior = tk.Frame(canvas)
# # #         interior_id = canvas.create_window(0, 0, window=interior,
# # #                                            anchor=tk.NW)
# # #
# # #         # track changes to the canvas and frame width and sync them,
# # #         # also updating the scrollbar
# # #         def _configure_interior(event):
# # #             # update the scrollbars to match the size of the inner frame
# # #             size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
# # #             canvas.config(scrollregion="0 0 %s %s" % size)
# # #             if interior.winfo_reqwidth() != canvas.winfo_width():
# # #                 # update the canvas's width to fit the inner frame
# # #                 canvas.config(width=interior.winfo_reqwidth())
# # #
# # #         interior.bind('<Configure>', _configure_interior)
# # #
# # #         def _configure_canvas(event):
# # #             if interior.winfo_reqwidth() != canvas.winfo_width():
# # #                 # update the inner frame's width to fill the canvas
# # #                 canvas.itemconfigure(interior_id, width=canvas.winfo_width())
# # #         canvas.bind('<Configure>', _configure_canvas)
# # #
# # #
# # # root = tk.Tk()
# # # root.title("Scrollable Frame Demo")
# # # root.configure(background="gray99")
# # #
# # # scframe = VerticalScrolledFrame(root)
# # # scframe.pack()
# # #
# # # lis = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# # # for i, x in enumerate(lis):
# # #     btn = tk.Button(scframe.interior, height=1, width=20, relief=tk.FLAT,
# # #         bg="gray99", fg="purple3",
# # #         font="Dosis", text='Button ' + lis[i],
# # #         command=lambda i=i,x=x: openlink(i))
# # #     btn.pack(padx=10, pady=5, side=tk.TOP)
# # #
# # # def openlink(i):
# # #     print (lis[i])
# # #
# # # root.mainloop()
# #
# # # from tkinter import *
# # # import time
# # # root = Tk()
# # # time1 = ''
# # # clock = Label(root, font=('times', 20, 'bold'), bg='green')
# # # clock.pack(fill=BOTH, expand=1)
# # # def tick():
# # #     global time1
# # #     # get the current local time from the PC
# # #     time2 = time.strftime('%H:%M:%S')
# # #     # if time string has changed, update it
# # #     if time2 != time1:
# # #         time1 = time2
# # #         clock.config(text=time2)
# # #     # calls itself every 200 milliseconds
# # #     # to update the time display as needed
# # #     # could use >200 ms, but display gets jerky
# # #     clock.after(200, tick)
# # # tick()
# # # root.mainloop(  )
# #
# # #
# # # import tkinter as tk
# # #
# # # class Page(tk.Frame):
# # #     def __init__(self, *args, **kwargs):
# # #         tk.Frame.__init__(self, *args, **kwargs)
# # #     def show(self):
# # #         self.lift()
# # #
# # # class Page1(Page):
# # #    def __init__(self, *args, **kwargs):
# # #        Page.__init__(self, *args, **kwargs)
# # #        label = tk.Label(self, text="This is page 1")
# # #        label.pack(side="top", fill="both", expand=True)
# # #
# # # class Page2(Page):
# # #    def __init__(self, *args, **kwargs):
# # #        Page.__init__(self, *args, **kwargs)
# # #        label = tk.Label(self, text="This is page 2")
# # #        label.pack(side="top", fill="both", expand=True)
# # #
# # # class Page3(Page):
# # #    def __init__(self, *args, **kwargs):
# # #        Page.__init__(self, *args, **kwargs)
# # #        label = tk.Label(self, text="This is page 3")
# # #        label.pack(side="top", fill="both", expand=True)
# # #
# # # class MainView(tk.Frame):
# # #     def __init__(self, *args, **kwargs):
# # #         tk.Frame.__init__(self, *args, **kwargs)
# # #         p1 = Page1(self)
# # #         p2 = Page2(self)
# # #         p3 = Page3(self)
# # #
# # #         buttonframe = tk.Frame(self)
# # #         container = tk.Frame(self)
# # #         buttonframe.pack(side="top", fill="x", expand=False)
# # #         container.pack(side="top", fill="both", expand=True)
# # #
# # #         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
# # #         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
# # #         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
# # #
# # #         b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
# # #         b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
# # #         b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
# # #
# # #         b1.pack(side="left")
# # #         b2.pack(side="left")
# # #         b3.pack(side="left")
# # #
# # #         p1.show()
# # #
# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     main = MainView(root)
# # #     main.pack(side="top", fill="both", expand=True)
# # #     root.wm_geometry("400x400")
# # #     root.mainloop()
# #
# #
# # # import tkinter as tk
# # # from tkinter import simpledialog
# # #
# # # application_window = tk.Tk()
# # #
# # # answer = simpledialog.askstring("Input", "What is your first name?",
# # #                                 parent=application_window)
# # #
# # # # asnswer = simpledialog.
# # # if answer is not None:
# # #     print("Your first name is ", answer)
# # # else:
# # #     print("You don't have a first name?")
# # #
# # # answer = simpledialog.askinteger("Input", "What is your age?",
# # #                                  parent=application_window,
# # #                                  minvalue=0, maxvalue=100)
# # # if answer is not None:
# # #     print("Your age is ", answer)
# # # else:
# # #     print("You don't have an age?")
# # #
# # # answer = simpledialog.askfloat("Input", "What is your salary?",
# # #                                parent=application_window,
# # #                                minvalue=0.0, maxvalue=100000.0)
# # # if answer is not None:
# # #     print("Your salary is ", answer)
# # # else:
# # #     print("You don't have a salary?")
# #
# #
# # #
# # # from tkinter import *
# # #
# # # def getpwd():
# # #     password = ''
# # #     root = Tk()
# # #     root.geometry("400x300")
# # #     namebox = Entry(root)
# # #     pwdbox = Entry(root, show = '*')
# # #
# # #     newnamebox = Entry(root)
# # #     newpwdbox = Entry(root, show = '*')
# #
# #     # pwdbox.configure()
# # #     def onpwdentry(evt):
# # #          password = pwdbox.get()
# # #          print(password)
# # #
# # #          root.destroy()
# # #     def onokclick():
# # #          password = pwdbox.get()
# # #          print(password)
# # #
# # #          root.destroy()
# # #
# # #     Label(root, text = 'Enter current User Name',font=("Times New Roman",15,"normal")).pack(side = 'top')
# # #     namebox.pack(side = 'top')
# # #     Label(root, text = 'Enter current Password',font=("Times New Roman",15,"normal")).pack(side = 'top')
# # #     pwdbox.pack(side = 'top')
# # #     Label(root, text='Enter new User Name', font=("Times New Roman", 15, "normal")).pack(side='top')
# # #     newnamebox.pack(side = 'top')
# # #     Label(root, text = 'Enter new Password',font=("Times New Roman",15,"normal")).pack(side = 'top')
# # #     newpwdbox.pack(side = 'top')
# # #     newpwdbox.bind('<Return>', onpwdentry)
# # #
# # #     Button(root, command=(onokclick,onpwdentry), text = 'OK',width = 11).pack(side = 'top')
# # #     root.mainloop()
# # #     return password
# # #
# # # getpwd()
# # #
# # #
# from escpos.connections import getUSBPrinter
# # import escpos.commandset
# #
# # # import subprocess
# # # lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
# # # # b = bytearray("hello")
# # # lpr.stdin.write(0x01)
# #
# # # lp = open("/dev/lp0", "w")
# # # lp.write("l")
# # #
# # printer = getUSBPrinter(commandSet='Generic')(idVendor=0x04e8,  # USB vendor and product Ids for Bixolon SRP-350plus
# #                           idProduct=0x330f,  # printer
# #                           inputEndPoint=0x81,
# # #                           outputEndPoint=0x02)
# # # commandSet
# # # import usb.core
# # #
# # # # find our device
# # # dev = usb.core.find(idVendor=0x04e8, idProduct=0x330f)
# # #
# # # # was it found?
# # # if dev is None:
# # #     raise ValueError('Device not found')
# # # printer.text("Hello World")
# # # printer.lf()
# # # from escpos import *
# # from escpos import printer
# #
# # Epson = printer.Usb(0x04e8,0x330f,in_ep=0x81,out_ep=0x02)
# # Epson.text("Hello World55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555\n")
# # # Print image
# # # Epson.image("logo.gif")
# # # Print QR Code
# # # Epson.qr("You can readme from your smartphone")
# # # Print barcode
# # # Epson.barcode('1324354657687','EAN13',64,2,'','')
# # # Cut paper
# # # Epson.cut()# Epson.
# # # from escpos.connections import getUSBPrinter
# # # printer = getUSBPrinter()(idVendor=0x04e8,
# # #                           idProduct=0x330f,
# # #                           inputEndPoint=0x81,
# # #                           outputEndPoint=0x02) # Create the printer object with the connection params
# # # from escpos import printer
# # # p = printer.Serial()  # adapt this to your printer model
# # #
# # # file = open("binary-blob.bin", "rb")  # read in the file containing your commands in binary-mode
# # # data = file.read()
# # # file.close()
# # #
# # # p._raw(data)
# # from escpos import printer
#from escpos.printer import Usb ,Dummy
#
# """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
#p = Usb(0x04e8, 0x330f, 0, profile="TM-T88III",out_ep=0x02)
# Generic = printer.Usb(0x04e8,0x330f,0,0x81,0x02)
# # d = Dummy()
#p.text("hey!!")
# # p._raw(d.output)
# p.text("Hello World\n")
# # p.text("Hello World\n")
# # p.text("Hello World\n")
# # p.text("Hello World\n")
# # p.text("Hello World\n")
# # p.text("Hello World\n")
# # # from escpos import config
# # # c = config.Config()
# # # printer = c.printer()
# # # c.load()
#import os
#import os, sys, win32
import win32print
printers = win32print.EnumPrinters(5)
print (printers)

# with open("Header") as f:
#     with open("Bill", "wt") as f1:
#         for line in f:
#             f1.write(line)
#
# # with open("Bill")
#
# with open("Footer") as f:
#     with open("Bill", "at") as f1:
#         for line in f:
#             f1.write(line)

# os.system("lpr -P CUPS-BRF-Printer header")
#os.system("lpr -P Samsung-ML-2160-Series header")
"""p = win32print.OpenPrinter ("Samsung-ML-2160-Series")
job = win32print.StartDocPrinter (p, 1, ("test of raw data", None, "RAW"))
win32print.StartPagePrinter (p)
win32print.WritePrinter (p, "data to print")
win32print.EndPagePrinter (p)
"""


#os.startfile("Samsung-ML-2160-Series","header")
