import mysql.connector as mysql 
mycon=mysql.connect(user='root',password='mysql',host='localho
st',database='Store') 
myc=mycon.cursor() 
o="y" 
while(o=="y" or o=="Y"): 
   m = """     
   **Shop bill management receipt** 
   ---- Tax invoice ---- 
   """ 
   print(m) 
   print("==================================================") 
   print('press S for generating stationary bill') 
   print('press C for generating clothing bill') 
   print('press E for generating electrical appliances bill') 
   print('press G for generating grocery bill') 
   print('press X to exit from program') 
   print("==================================================") 
   c = input("enter your choice(S or C or E or G or X):") 
   if(c=="S" or c=="s"): 
      print("----STATIONARY BILL----") 
      date=input("Invoice date:") 
      impt=int(input("Number of items purchased :")) 
      print("Details of customer") 
      customer=str(input("Customer's name:Mr./Miss :")) 
      address=str(input("Customer's address :")) 
      city=str(input("Customer's city :")) 
      state=str(input("Customer's state :")) 
      mobilenumber=int(input("Customer's mobile number : ")) 
      total=0 
      maxitem=60 # maximum  number of items can be purchased 
at a time 
      if(impt<=maxitem): 
         for a in range(1,impt+1): 
            print("Bill no :",a) 
            i=str(input("Item :")) 
            rate=float(input("Price of item in rupees :")) 



            qty=int(input("Quantity of item purchased :")) 
            value=qty*rate # total  price of product with no. 
of quantity  
            print("Total price:",value)  # total  amount of 
particular product 
            total=total+value # total  amount of all products 
            sql="insert into 
STATIONARY(item_name,price,quantity) 
values('{}',{},{})".format(i,rate,qty) 
            myc.execute(sql) 
            mycon.commit() 
         print("Items Purchased Till Now:") 
         myc.execute('SELECT * FROM STATIONARY ') 
         data=myc.fetchall() 
         
print("=====================================================") 
         print("Bill No",",","Product 
Name",",","Price",",","Quantity") 
         
print("=====================================================") 
         for b, c, d, e in data: 
            print(b, ",", end="") 
            print(c, ",", end="") 
            print(d, ",", end="") 
            print(e) 
 
         print("Total Amount:",total) 
         gst=18/100 
         gtax=total*gst #gst taxed amount 
         price=total+gtax # total amount of all products after 
adding gst  
         if(total<100): 
            print("Final price inclusive of taxes and 
potential discounts :",price) 
         elif(total>=100 and total<=800): 
            discount=5/100 
            dprice=total*discount # discount amount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>800 and total<=5000): 
            discount=15/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 



         elif(total>5000 and total<=14000): 
            discount=20/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>14000): 
            discount=25/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
      else: 
         print(" Sorry You Can Only Buy 60 Items At A Time") 
      print("STATIONARY BILL") 
   elif(c=="C" or c=="c"): 
      date=input("Invoice date:") 
      impt=int(input("Number of items purchased :")) 
      print("Details of customer") 
      customer=str(input("Customer's name:Mr./Miss :")) 
      address=str(input("Customer's address :")) 
      city=str(input("Customer's city :")) 
      state=str(input("Customer's state :")) 
      mobilenumber=int(input("Customer's mobile number : ")) 
      total=0 
      maxitem=60 # maximum  number of items can be purchased 
at a time 
      if(impt<=maxitem): 
         for a in range(1,impt+1): 
            print("Bill no :",a) 
            i=str(input("Item :")) 
            rate=float(input("Price of item in rupees :")) 
            qty=int(input("Quantity of item purchased :")) 
            value=qty*rate # total  price of product with no. 
of quantity 
            print("Total price:",value)  # total  amount of 
particular product 
            total=total+value # total  amount of all products 
            sql="insert into 
CLOTHING(item_name,price,quantity) 
values('{}',{},{})".format(i,rate,qty) 
            myc.execute(sql) 
            mycon.commit() 
         print("Items Purchased Till Now :") 
         myc.execute('SELECT * FROM CLOTHING') 
         data=myc.fetchall() 



         
print("=====================================================") 
         print("Bill No",",","Product 
Name",",","Price",",","Quantity") 
         
print("=====================================================") 
         for f, g, h, i in data: 
            print(f, ",", end="") 
            print(g, ",", end="") 
            print(h, ",", end="") 
            print(i) 
 
         print("Total Amount :",total) 
         gst=12/100 
         gtax=total*gst #gst taxed amount 
         price=total+gtax # total amount of all products after 
adding gst  
         if(total<800): 
            print("Final price inclusive of taxes and 
potential discounts :",price) 
         elif(total>=800 and total<=6000): 
            discount=5/100 
            dprice=total*discount # discount amount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>6000 and total<=11000): 
            discount=15/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>11000 and total<=15000): 
            discount=20/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>15000): 
            discount=25/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
      else: 
         print(" Sorry You Can Only Buy 60 Items At A Time ") 
      print("CLOTHING BILL") 
   elif(c=="E" or c=="e"): 



      print("----ELECTRICAL APPLIANCES BILL----") 
      date=input("Invoice date:") 
      impt=int(input("Number of items purchased :")) 
      print("Details of customer") 
      customer=str(input("Customer's name:Mr./Miss :")) 
      address=str(input("Customer's address :")) 
      city=str(input("Customer's city :")) 
      state=str(input("Customer's state :")) 
      mobilenumber=int(input("Customer's mobile number : ")) 
      total=0 
      maxitem=60 # maximum  number of items can be purchased 
at a time 
      if(impt<=maxitem): 
         for a in range(1,impt+1): 
            print("Bill no :",a) 
            i=str(input("Item :")) 
            rate=float(input("Price of item in rupees :")) 
            qty=int(input("Quantity of item purchased :")) 
            value=qty*rate # total  price of product with no. 
of quantity 
            print("Total price:",value)  # total  amount of 
particular product 
            total=total+value # total  amount of all products 
            sql="insert into 
ELECTRONICS(item_name,price,quantity) 
values('{}',{},{})".format(i,rate,qty) 
            myc.execute(sql) 
            mycon.commit() 
 
         print("Items Purchased Till Now :") 
         myc.execute('SELECT * FROM ELECTRONICS') 
         data=myc.fetchall() 
         
print("=====================================================") 
         print("Bill No",",","Product 
Name",",","Price",",","Quantity") 
         
print("=====================================================") 
         for j, k, l, m in data: 
            print(j,",", end="") 
            print(k,",", end="") 
            print(l,",", end="") 
            print(m) 
 



         print("Total Amount :",total) 
         gst=18/100 
         gtax=total*gst #gst taxed amount 
         price=total+gtax # total amount of all products after 
adding gst  
         if(total<1200): 
            print("Final price inclusive of taxes and 
potential discounts :",price) 
         elif(total>=1200 and total<=4000): 
            discount=5/100 
            dprice=total*discount # discount amount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>4000 and total<=7000): 
            discount=15/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>7000 and total<=12000): 
            discount=20/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>12000): 
            discount=25/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
possible discounts :",price-dprice) 
      else: 
         print(" Sorry You Can Only Buy 60 Items At A Time") 
      print("ELECTRICAL APPLINCES BILL") 
   elif(c=="G" or c=="g"): 
      print("----GROCERY BILL----") 
      date=input("Invoice date:") 
      impt=int(input("Number of items purchased :")) 
      print("Details of customer") 
      customer=str(input("Customer's name:Mr./Miss :")) 
      address=str(input("Customer's address :")) 
      city=str(input("Customer's city :")) 
      state=str(input("Customer's state :")) 
      mobilenumber=int(input("Customer's mobile number : ")) 
      total=0 
      maxitem=60 # maximum  number of items can be purchased 
at a time 



      if(impt<=maxitem): 
         for a in range(1,impt+1): 
            print("Bill no :",a) 
            i=str(input("Item :")) 
            rate=float(input("Price of item in rupees :")) 
            qty=int(input("Quantity of item purchased :")) 
            value=qty*rate # total  price of product with no. 
of quantity 
            print("Total price:",value)  # total  amount of 
particular product 
            total=total+value # total  amount of all products 
            sql="insert into GROCERY(item_name,price,quantity) 
values('{}',{},{})".format(i,rate,qty) 
            myc.execute(sql) 
            mycon.commit() 
 
         print("Items Purchased Till Now:") 
         myc.execute('SELECT * FROM GROCERY') 
         data=myc.fetchall() 
         
print("=====================================================") 
         print("Bill No",",","Product 
Name",",","Price",",","Quantity") 
         
print("=====================================================") 
         for o, p, q, r in data: 
            print(o, ",", end="") 
            print(p, ",", end="") 
            print(q, ",", end="") 
            print(r) 
 
         print("Total Amount :",total) 
         gst=12/100 
         gtax=total*gst #gst taxed amount 
         price=total+gtax # total amount of all products after 
adding gst  
         if(total<200): 
            print("Final price inclusive of taxes and 
potential discounts :",price) 
         elif(total>=200 and total<=500): 
            discount=5/100 
            dprice=total*discount # discount amount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 



         elif(total>500 and total<=900): 
            discount=15/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>900 and total<=15000): 
            discount=20/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice) 
         elif(total>15000): 
            discount=25/100 
            dprice=total*discount 
            print("Final price inclusive of taxes and 
potential discounts :",price-dprice)#final price is calculated 
after adding gst 
      else: 
         print(" Sorry You Can Only Buy 60 Items At A Time ") 
      print("GROCERY BILL") 
   elif(c=="x" or c=="X"): 
      exit() 
   else: 
      print("PLEASE ENTER A VALID PRODUCT CATEGORY") 
      print("  S for generating stationary bill") 
      print("  C for generating clothing bill") 
      print("  E for generating electrical appliances bill") 
      print("  G for generating grocery bill") 
   t = """    
   -----THANK YOU----- 
   -----VISIT US AGAIN----- 
   """ 
   print(t) 
   o=input("want to run again y/n or Y/N :")
