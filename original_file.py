#importing the python package SQLite3 as sql
import sqlite3 as sql
#created database as pharma
#created table name called PharmaPulse
con = sql.connect("PharmaPulse")
#print("Connection Created")
cur = con.cursor()
print("Pharma Pulse ")
print("Pulse of Precision, Heart of Healing")
#it is the operations which is performed by the user
print("1.Insert\n2.Update\n3.Search\n4.View\n5.Bill")
n = int(input("Enter the operations you want to perform :  "))
orders = {}
final_bill = 0
    #in this section you can insert the medicines multiple times as many as you can by giving the condition "Y"
if n==1:
    q = "insert into PharmaPulse values(?,?,?,?,?,?,?)"
    ch = 'y'
    while ch=='y':
        MedID = int(input("Enter the ProductID : "))
        cur.execute("SELECT MedID, MedName, SCost, ExpiryDate FROM PharmaPulse WHERE MedID = ?", (MedID,))
        result = cur.fetchone()
        if result:
            print(f"Entered ID is already exists in the database ")
        else:

            MedName = input("Enter the name of the Product : ")
            PCost = float(input("Enter the purchased price product cost : "))
            SCost = float(input("Enter the selling price of the product : "))
            Availability = int(input("Enter the quantity of the available in the storage : "))
            if Availability<0:
                print(f"Entered value {Availability} is in negative value ")
                continue
            elif Availability==0:
                print("Entered stock is empty")
            ExpiryDate = input("Enter the Expiry Date of the product : ")
            Profit = 0.0  # Hardcoded to 0 instead of input
            t1 = (MedID,MedName,PCost,SCost,Availability,ExpiryDate,Profit)
            cur.execute(q, t1)
            con.commit()
            print("Record Inserted")
            if Availability < 10:
                print(f"Stock for {MedName} (ID: {MedID}) is going to empty. Current availability: {Availability}")
            ch = input("Do yo want to continue (y/n) : ")
#Update operations like Cost , Availability , Delete
elif n==2:
    print("You have entered the update section ")
    print("201.Cost\n202.Availability\n203.Delete")
    m = int(input("Enter the operation you want to perform : "))
    if m>=201 and m<=203:
        if m==201:
            id = int(input("Enter the Medicine ID you want to update the cost :  "))
            cur.execute("select MedID from PharmaPulse where MedID = ?",(id,))
            result = cur.fetchone()
            if result:
                cost = float(input("Enter the price you want to update : "))
                cur.execute("update PharmaPulse set SCost = ? where MedID = ?",(cost,id))
                con.commit()
            else:
                print(f"No record found with the given id {id}")
                con.commit()
        if m==202:
            q = "update PharmaPulse set Availability = Availability + ? where MedID = ?"
            MedID = int(input("Enter the medicine  Id you want to update the Storage  : "))
            Availability = int(input("Enter the Medicines number you want to add : "))
            t1 = (Availability,MedID)
            cur.execute(q,t1)
            con.commit()
            print(f"the Entered Medicines quantity {Availability} is Updated")
            # Fetch updated availability for stock check
            cur.execute("SELECT Availability FROM PharmaPulse WHERE MedID = ?", (MedID,))
            new_availability = cur.fetchone()[0]
            if new_availability < 10:
                cur.execute("SELECT MedName FROM PharmaPulse WHERE MedID = ?", (MedID,))
                result = cur.fetchone()
                if result:
                    med_name = result[0]
                    print(f"Stock for {med_name} (ID: {MedID}) is going to empty. Current availability: {new_availability}")
                else:
                    print(f"No record found to update the storage capacity of the given ID {MedID}")
        if m==203:
            id = int(input("Enter the medicine you want to delete : "))
            cur.execute("select MedID from PharmaPulse where MedID = ? ",(id,))
            result = cur.fetchone()
            if result:
                cur.execute("delete from PharmaPulse where MedID = ? ",(id,))
                con.commit()
                print(f"Selected Record {id} is Deleted")
            else:
                print("No record found with the given id to delete ")
                con.commit()
    else:
        print("Selected the operation is not available ")
#search for the medicine by using the Medicine ID // First Letter of the medicine // start and end range of the cost
elif n==3:
    print("You have entered the Search Section")
    print("301.Search by using the Medicine ID\n302.Search by using the Medicine name of first letter\n303.Search by using the cost range")
    n = int(input("Enter the type of search you want to perform : "))
    if n>=301 and n<=303:
        if n ==301 :
            id = int(input("Enter the id you want to search: "))
            cur.execute("SELECT MedID, MedName, SCost, ExpiryDate FROM PharmaPulse WHERE MedID = ?", (id,))
            result = cur.fetchone()
            if result:
                print(f"MedID: {result[0]}, MedName: {result[1]}, SCost: {result[2]}, ExpiryDate: {result[3]}")
            else:
                print("No record found with the given ID.")
            con.commit()
        elif n==302 :
            name = input("Enter the first letter of the medicine: ").strip()
            cur.execute("SELECT MedID, MedName, SCost, ExpiryDate FROM PharmaPulse WHERE MedName LIKE ?", (name + '%',))
            results = cur.fetchall()
            if results:
                for result in results:
                    print(f"MedID: {result[0]}, MedName: {result[1]}, SCost: {result[2]}, ExpiryDate: {result[3]}")
            else:
                print(f"No medicines starting with '{name}' found.")
        elif n==303:
            r1 = float(input("Enter the starting range of the cost : "))
            r2 = float(input("Enter the ending range of the cost : "))
            if r1 > r2:
                r1, r2 = r2, r1
            cur.execute("SELECT MedID, MedName, SCost, ExpiryDate FROM PharmaPulse WHERE SCost BETWEEN ? AND ?",(r1, r2))
            results = cur.fetchall()
            if results:
                print("Medicines found within the cost range:")
                for row in results:
                    print(f"MedID: {row[0]}, MedName: {row[1]}, SCost: {row[2]}, ExpiryDate: {row[3]}")
            else:  # Corrected indentation
                print(f"No medicines found between ₹{r1} and ₹{r2}.")
#displays the complete table format
elif n==4:
    q1 = "SELECT * FROM PharmaPulse"
    cur.execute(q1)
    orders = cur.fetchall()
    # Print column headers
    if orders:
        print("MedID\tMedName\tPCost\tSCost\tStock\tExpDate\tProfit")
    # Print rows
        for row in orders:
            for value in row:
                print(value, end='\t')  # Print each value separated by a tab
            print()  # Move to the next line after printing a row
    else:
        print("No records inserted yet ")
# printing the final BIll
elif n==5:
    ch = 'y'
    while ch =='y':
        id = int(input("Enter the Medicine ID you want to buy : "))
        cur.execute("SELECT MedName, SCost FROM PharmaPulse WHERE MedID= ?", (id,))
        result = cur.fetchone()
        if result:
            print(f"the Cost of the medicine of {id} is {result[1]}")
            q = int(input("Enter the quantity : "))
            if q <= 0:
                print("Quantity must be positive.")
                continue
            # Check stock
            cur.execute("SELECT Availability FROM PharmaPulse WHERE MedID = ?", (id,))
            current_availability = cur.fetchone()[0]
            if q > current_availability:
                print("Error: Not enough stock available.")
                continue
            data = result[1]
            bill = data * q
            final_bill += bill
            orders[id] = [result[0], q, data, bill]
            # Update Availability
            new_storage = current_availability - q
            cur.execute("UPDATE PharmaPulse SET Availability = ? WHERE MedID = ?", (new_storage, id))
            con.commit()  # Commit stock update
            print(f"The amount of {result[0]} is {bill}")
            # Check stock level after update
            if new_storage < 10:
                cur.execute("SELECT MedName FROM PharmaPulse WHERE MedID = ?", (id,))
                result_name = cur.fetchone()
                if result_name:
                    print(f"Stock for {result_name[0]} (ID: {id}) is going to empty. Current availability: {new_storage}")
                # Calculate Profit
            cur.execute("SELECT PCost, SCost FROM PharmaPulse WHERE MedID = ?", (id,))
            pc_sc = cur.fetchone()
            if pc_sc:
                purchased, sold = pc_sc
                profit_per_unit = sold - purchased
                total_profit = profit_per_unit * q
                # Update Profit by accumulating total profit
                cur.execute("UPDATE PharmaPulse SET Profit = Profit + ? WHERE MedID = ?", (total_profit, id))
                con.commit()  # Commit profit update
        else:
            print("No record found with the given ID")
        ch = input("Do you want to buy more medicine (y/n) : ").lower()
    print("your bill is :- ")
    print("MedID MedName   Qnt   Cost   Bill")
    print('-----------------------------------')
    for i,j in orders.items():
        print(i , end='\t')
        for k in j:
            print(k,end='\t')
        print()
    print("---------------------------------------")
    print("the total bill amount is : ",final_bill)
con.commit()
con.close()
print("connection closed")