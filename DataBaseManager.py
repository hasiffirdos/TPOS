import sqlite3
from sqlite3 import Error

conn = 0


def createDataBase():
    """ create a database connection to a SQLite database """
    global conn
    try:
        conn = sqlite3.connect("MyDataBase.db")
        c= conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Stocks '
                  '(Item_Id INTEGER PRIMARY KEY AUTOINCREMENT,'
                  'Name text,'
                  'Quantity INTEGER,'
                  'Barcode text,'
                  'picture text,'
                  'buying_price INTEGER,'
                  'sale_price INTEGER,'
                  'profit INTEGER)')

        # c.execute('INSERT INTO Item VALUES (1,"Asif",5,"barcode","picture",10,20,10)')

        c.execute('CREATE TABLE IF NOT EXISTS Bills '
                  '(Bill_Id INTEGER PRIMARY KEY AUTOINCREMENT,'
                  'today_date Date ,'
                  'Profit INTEGER,'
                  'Sale_earn INTEGER,'
                  'Discount INTEGER,'
                  'Lended_amount INTEGER,'
                  'borrower_Id text,'
                  'Lend_date Date)')

        conn.execute('CREATE TABLE IF NOT EXISTS Sales '
                  '(Sale_Id INTEGER PRIMARY KEY AUTOINCREMENT,'
                  'Billid INTEGER,'
                  'Itemid INTEGER,'
                  'Item_quantitty INTEGER,'
                  'Item_total INTEGER,'
                  'Item_profit INTEGER,'
                  'Item_price INTEGER,'
                
                     'CONSTRAINT Sales_fk'
                     '  FOREIGN KEY(Itemid) REFERENCES Stocks(Item_Id)'
                     # '  FOREIGN KEY(Billid) REFERENCES Bills(Bill_Id)'
                     ')')
        conn.execute('CREATE TABLE IF NOT EXISTS Admin (UserName INTEGER ,Password text) ')
        conn.execute('CREATE TABLE IF NOT EXISTS Customers (C_Name text ,Due_Amount INTEGER,PhoneNumber text, Address text)')
        conn.execute('CREATE TABLE IF NOT EXISTS Dealers (D_Name text ,Due_Amount INTEGER,Spend_Amount INTEGER,PhoneNumber text, Address text)')
        conn.execute("INSERT INTO Bills(Bill_Id,today_date,Profit,Sale_earn) VALUES (0,'date',0,0)")
        conn.commit()


        c.close()
        # conn.close()
    except Error as e:
        print(e)
    finally:
        conn.close()

def GetConnection():
    global conn
    try:
        conn = sqlite3.connect("MyDataBase.db")
        c = conn.cursor()
        return conn,c
    except Error as e:
        print(e)

def AddData():
    global conn
    try:
        conn = sqlite3.connect("MyDataBase.db")
        c = conn.cursor()
        # conn.execute('CREATE TABLE IF NOT EXISTS Customers (C_Name text ,Due_Amount INTEGER,PhoneNumber text, Address text)')
        # conn.execute('CREATE TABLE IF NOT EXISTS Dealers (D_Name text ,Due_Amount INTEGER,Spend_Amount INTEGER,PhoneNumber text, Address text)')

        # row = c.fetchall()
        # c.execute('DROP TABLE IF EXISTS Bills')
        # c.execute('ALTER TABLE Bills ADD COLUMN Lend_date Date DEFAULT 0')
                  # 'borrower_Id INTEGER default 0')
        # c.execute('DROP TABLE IF EXISTS Sales')
        conn.commit()
        c.close()
        conn.close()
    except Error as e:
        print(e)
    finally:
        conn.close()


# createDataBase()


def print_stocks():
    global conn
    try:
        conn = sqlite3.connect("MyDataBase.db")
        c = conn.cursor()

        c.execute("Select * from Stocks")
        rows = c.fetchall()
        for row in rows:
            print(row)
        c.close()
        conn.close()
    except Error as e:
        print(e)
    finally:
        conn.close()

def print_bills():
    global conn
    try:
        conn = sqlite3.connect("MyDataBase.db")
        c = conn.cursor()
        # conn.execute("INSERT INTO Bills(Bill_Id,today_date,Profit,Sale_earn) VALUES (0,'date',0,0)")
        # conn.commit()
        # c.execute("Select * from Customers")  #
        c.execute("Select * from Bills ")  # WHERE borrower_Id != '0'
        # c.execute("Update Bills SET Sale_earn  = Sale_earn -310, Profit = Profit - 310 Where Bill_Id = 6")  #Select * from Bills
        # conn.commit()
        rows = c.fetchall()
        for row in rows:
            print(row)
        c.close()
        conn.close()
    except Error as e:
        print(e)
    finally:
        conn.close()

def print_sales():
    global conn
    try:
        conn = sqlite3.connect("MyDataBase.db")
        c = conn.cursor()
        # c.execute(f'SELECT Itemid, sum(Item_total),'
        #           f'sum(Item_profit)'
        #           f' from (SELECT * From Sales WHERE Billid IN (SELECT Bill_Id from Bills where today_date = date("2019-01-23"))) '
        #           # f'INNER JOIN Stocks ON Sales.Itemid = Stocks.Name'
        #           # f'WHERE Billid = (SELECT Bill_Id from Bills where today_date = date("2019-01-23"))'
        #           f'GROUP BY Itemid')
        # c.execute(f'SELECT Billid, Itemid,Name,sum(Item_total),'
        #           f'sum(Item_profit)'
        #           f' from Stocks'
        #           # f'(SELECT * From Sales WHERE Billid IN (SELECT Bill_Id from Bills where today_date = date("2019-01-23"))) '
        #           f' INNER JOIN (SELECT * From Sales WHERE Billid IN (SELECT Bill_Id from Bills where today_date = date("2019-01-23"))) ON Itemid = Item_Id'
        #           f' GROUP BY Itemid')
                  # f'WHERE Billid = (SELECT Bill_Id from Bills where today_date = date("2019-01-23"))')
                  # f'GROUP BY Item_Id')
        id = 3
        billNumber = 6
        # c.execute(f"Delete from Sales WHERE Itemid = {id} and Billid = {billNumber}")
        # c.execute(f'SELECT Stocks.Name,Sales.Item_quantitty,Sales.Item_total,Sales.Item_profit'
        #           f' from Sales, Stocks'
        #           f' WHERE Billid = {3} and Item_Id = Itemid')
        # c.execute(f"Select * from Sales Where Billid = {1}")

        # c.execute('SELECT Bill_Id FROM Bills WHERE today_date = date("2019-01-23")')
        # list = [3,4]
        c.execute(f'SELECT * From Customers ') #WHERE Billid IN (SELECT Bill_Id from Bills where today_date = date("2019-01-23"))
        rows = c.fetchall()
        for row in rows:
            print(row)
        c.close()
        conn.close()
    except Error as e:
        print(e)
    finally:
        conn.close()

def main():
        # AddData()
        createDataBase()
        # print_stocks()
        print_bills()
        print_sales()
        #  conn.commit()


main()