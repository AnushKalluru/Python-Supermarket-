import matplotlib.pyplot as plt
class Supermarket:
    def __init__(self,total_money):
        # Initialize the Supermarket object with an empty products dictionary, total money, and a list to store daily earnings
        self.products={}
        self.total_money = 0
        self.days_amounts=[0]
        self.b='y' # Variable to control whether to open or close the supermarket for that day
    def addingitems(self):
        
        # Method to add items to the supermarket
        n='y' 
        while True:
            if n=='y':
                
                # Input product name, ensuring it starts with an alphabet
                while True:
                    try:
                        product = str(input("enter the product name : ")).lower()
                        if (ord(product[0]) >= 97 and ord(product[0]) <= 122):
                            break
                        else:
                            print("product name must start with alphabets") 
                    except IndexError:
                        print("invalid product name!")
                
                # Input the MRP  for the product  
                while True:        
                        try:
                            mrp = float(input(f"enter the Mrp of {product} : "))
                            break
                        except ValueError:
                            print("invalid mrp") 
                n = input("do you want to add another product ('y' or 'n'): ").lower()
                               
            elif n!='n':
                n = input("enter only ('y' or 'n') : ").lower()
            else:
                break
            
            # Add the product to the products dictionary   
            self.products[product] = mrp
            

    def taking_quantities(self):
        
        # Display the list of available product
        print("available products are : ")
        print("|s.no.\t|products\t|Mrp")
        for index,key in enumerate(self.products.keys()):
            print(f"|{index+1}\t|{key}\t|{(self.products[key]):,.2f}")
        
        # Method to take quantities of selected products
        k={index+1:key for index,key in enumerate(self.products.keys())}
        while True:
                try:
                    z=str(input("enter the selected product numbers seperated by comma's  : "))
                    z=z.split(',')
                    quantity = {k[int(i)] : int(input(f"quantity of {k[int(i)]} : ")) for i in z}
                    break

                except ValueError:
                    print("invalid quantity")
                except KeyError:
                    print("entered product number is not in the above list")
        
        # Calculate the total cost for each product and display the total bill 
        multiply = {k:self.products[k]*quantity[k] for k in quantity.keys()}
        print("Here is your total bill")
        bill = print("|s.no.\t|products\t|Mrp\t|Quantity\t|Each Total   ")
        for index,key in enumerate(quantity.keys()):
            print(f"|{index+1}\t|{key}\t|{self.products[key]:,.2f}\t|{quantity[key]}\t|{multiply[key]:,.2f} ")
        total_bill = 0
        for i in multiply.values():
            total_bill += i  
        return total_bill

    def billing(self):
                
                # Method to perform billing and apply discounts based on the total bill
                total_bill = self.taking_quantities()

                if total_bill >= 1000 and total_bill<=5000:
                        # Apply a 10% discount for bills between 1000 and 5000 Rupees
                        discount=0.1
                        total_bill -= discount*total_bill
                        print(f"discount applied for shopping bill more than 1000 Rupees is 10% ")
                        self.total_money += int(total_bill)
                        print(f"Total Bill is : {total_bill:,.2f} == {int(total_bill):,} ")
                        print(f"Todays total money so far is : {int(self.total_money):,} ")
                        
                elif total_bill >=5000:
                        # Apply a 25% discount for bills over 5000 Rupees
                        discount=0.25
                        total_bill -= discount*total_bill
                        print(f"discount applied for shopping bill more than 5000 Rupees is 25% ")
                        self.total_money += int(total_bill)
                        print(f"Total Bill is : {total_bill:,.2f} == {int(total_bill):,} ")
                        print(f"Todays total money so far is : {int(self.total_money):,} ")
                        
                else:   
                        # No discount for bills below 1000 Rupees 
                        self.total_money += int(total_bill)
                    
                        print(f"Total Bill is : {total_bill:,.2f} == {int(total_bill):,} ")
                        print(f"Todays total money so far is : {int(self.total_money):,} ")
        

    def openingandclosing(self):

        # Method to manage the supermarket's opening and closing, handle customer billing
        a='y'
        while True:
            if a !='e':
                if self.b == 'y':
                    self.addingitems()
                    self.billing()
                    a = input("press any key to bill for next customer (or) press 'e' to close the supermarket : ").lower()
                    if a!= 'e':
                        self.b = input("do you want to add another product ('y' or 'n'): ").lower()
                    
                elif self.b=='n':
                    
                    # Display the list of available products before billing
                    self.billing()
                    a = input("press any key to bill for next customer (or) press 'e' to close the supermarket : ").lower()
                    if a!= 'e':
                        self.b = input("do you want to add another product ('y' or 'n'): ").lower()
                else:
                    self.b = input("enter only ('y' or 'n') : ").lower()

            else:
                # Store the total money earned for the day in the days_amounts list
                self.days_amounts.append(self.total_money)
                break
                
        
    def display_total_money(self):
        # Display the total money earned for the day
        print((f"yours today's total money is : {self.total_money:,}").upper())

    def plot_money_perday(self):
        # Plot the total money earned per day
        days=[i for i in range(0,len(self.days_amounts))]
        plt.plot(days,self.days_amounts,marker='o')
        plt.title("Money per Day")
        plt.xlabel("Days")
        plt.ylabel("Money in Rupees")
        plt.show()
       
# Main program          
print(("Create Your Own Supermarket!").upper())
print(("Add your Product name and their mrps").upper())
supermarket=Supermarket(0)  # Initialize the supermarket object

f=None
while True:
    if f!='e':
        # Reset total money earned for the day before opening and closing
        supermarket.total_money = 0
        supermarket.openingandclosing()
        supermarket.display_total_money()
        f=input("press any key to open supermarket for the next day (or) press 'e' to see the average money per day : ").lower()
        if f!='e':
            supermarket.b = input("do you want to add another product ('y' or 'n'): ").lower()
    else:
        break

# Calculate and display overall earnings and average earnings per day
overall_money = 0
for i in supermarket.days_amounts:
    overall_money+=i
print((f"your earned {overall_money:,} ruppes money total").upper())
print((f"your average earning per day is {(overall_money/(len(supermarket.days_amounts)-1)):,} rupees ").upper())

# Plot the total money earned per day
supermarket.plot_money_perday()

# Display a closing message    
print(("Closed:)").upper())
     
                
            
        
