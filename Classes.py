

#****************************************************************************
class person:
    Name ="Sample"
    Phone = "03461398093"
    Address = "575 E-block"
    # def __init__(self,name,phone,address):
    #     self.Name = name
    #     self.Phone = phone
    #     self.Address = address

    def __int__(self):
        name = "Udharia"
        #do nothing

    def getName(self):
        return self.Name

    def setName(self,name):
        self.Name = name


    def getPhone(self):
        return self.Phone

    def setPhone(self, phone):
        self.phone = phone

    def getAddress(self):
        return self.Address

    def setAddress(self,address):
        self.Address = address

#****************************************************************************
class Customer(person):

    Associated_bills =[]
    Balance = 0
    Date_of_return = "some date"


    def __int__(self):
        self.Balance = 0

    # def __init__(self, name, phone, address,billList,balance,date_of_return):
    #     super().__init__(name, phone, address)
    #     self.Date_of_return = date_of_return
    #     self.Balance = balance
    #     self.Associated_bills = billList

#****************************************************************************
class Dealer(person):

    Bill = []
    Paid = 0
    Balance = 0

    def __int__(self):
        self.Balance = 0

    # def __init__(self, name, phone, address,bill,paid,balance):
    #     super().__init__(name, phone, address)
    #     self.Bill = bill
    #     self.Paid = paid
    #     self.Balance = balance

#****************************************************************************
class Bill:
    Bill_id = 0
    Date = " "
    List_of_Item = []
    Total = 0
    No_of_item = 0
    discount = 0
    udhar = 0

    customer = Customer()

    def __init__(self):
        self.udhar = 0
#****************************************************************************
class Sales:

    List_of_Bills = []
    Profit = 0
    Sale = 0

    def __init__(self):
        self.sale = 0

    def AddBill(self,bill):
        self.List_of_Bills.append(bill)


#****************************************************************************

class item:
    id = 0
    Name  = ""
    Quantity = 0
    BarCode = []
    Picture = []
    Buying_Price = 0
    Selling_Price = 0
    item_Profit = 0

    def __init__(self):
        self.item_Profit = 0


#****************************************************************************
class Stock:
    List_of_Items = []

    def __init__(self) -> None:
        super().__init__()


#****************************************************************************
class Record:
    ListofBills = []
    ListofCustomer = []
    ListofDealers = []

    def __init__(self) -> None:
        super().__init__()


#****************************************************************************
