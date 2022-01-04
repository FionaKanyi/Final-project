#100432-Fiona Kanyi
import datetime

id_check=1234567
customer={1234567:{"name":"Maxwell Orwell","dob":"1993-5-5","phone":"0712345678","loyalty":10000}, 2432434:{"name":"Jane Mwikali","dob":"2000-5-12","phone":"071323343","loyalty":2000}}
customer[1234567]["dob"] = datetime.datetime(1993, 5, 5)
customer[2432434]["dob"] = datetime.datetime(2000, 5, 12)

bag_slots=["occupied","occupied","empty","empty"]
slot_assigned={1234567:1}

birthday="false"
payment="Visa"
goods_bought=7200
total=goods_bought
points_earned=0
cashless_discount=0
birthday_discount=0
redeemed_points=0

def customer_entry():
    global customer
    global id_check
    
    id_check=int(input("Enter Customer National ID number: "))
    if id_check in customer:
        print("\nWelcome",customer[id_check]["name"],". Continue shopping.")
    else:
        print("\nNew customer! Enter their details to proceed: ")
        
        customer[id_check]={"name":"null","dob":"null","phone":"null"}
        
        customer[id_check]["name"]=input("\nFull name: ")
        
        date_entry=input('\nDate of birth in YYYY-MM-DD format: ')
        year, month, day = map(int, date_entry.split('-'))
        customer[id_check]["dob"] = datetime.date(year, month, day)
        
        customer[id_check]["phone"]=input("\nPhone number: ")
        
        customer[id_check]["loyalty"]=0
        print("\nDetails registered successfully!Customer has been added to our loyalty program. Earn points and redeem points as you shop!")
        print("\nCustomer details:",customer[id_check]["name"],customer[id_check]["dob"],customer[id_check]["phone"],"Loyalty points:",customer[id_check]["loyalty"])     

        
def store_bag():
    global slot_assigned
    check_bag=input("\nDoes the customer have a bag that is not allowed in the supermarket? yes or no\n")
    
    if check_bag=="yes":
        counter=0
        while counter<=4:
            if counter==4:
                print("\nSorry, there are no empty slots available to store your bag. Please proceed with it.\n")
                break
            if bag_slots[counter]=="occupied":
                counter+=1
            else:
                slot_assigned[id_check]=counter+1
                print("\nThe customer has been assigned slot", slot_assigned[id_check],". Continue with shopping.\n")
                bag_slots[counter]="occupied"
                break
    elif check_bag=="no":
        print("\nContinue with shopping.\n")
    else:
        print("\nInvalid input! Please enter yes if the customer has bag that is not allowed inside the supermarket, or no of the customer does not have one.")
        store_bag()
        

def birthday_check():
    from datetime import date
    global birthday
    
    today=date.today()
    
    if today.month==customer[id_check]["dob"].month and today.day==customer[id_check]["dob"].day:
        birthday="true"
    
        
def calculate_points():
    global total
    global points_earned
    
    points_earned=round(total/100)
    if points_earned>50:
        points_earned=(points_earned-50)*1.5+50
        

def redeem_points():
    global customer
    global total
    global redeemed_points
    
    print("\nYou have",customer[id_check]["loyalty"],"points\n")
    if customer[id_check]["loyalty"]>0:
        check_redeem=input("Would you like to redeem your loyalty points? yes OR no?")
        if check_redeem=="yes":
            redeemed_points=float(input("\nHow many loyalty points would you like to redeem?"))
            if redeemed_points<=customer[id_check]["loyalty"]:
                if redeemed_points>total:
                    redeemed_points=total
                customer[id_check]["loyalty"]-=redeemed_points
                total-=redeemed_points
                print("\nYou have redeemed",redeemed_points,"loyalty points. You now have",customer[id_check]["loyalty"],"loyalty points left")
                print("\nNew total is",total)
            else:
                print("\nYou have less than",redeemed_points,"loyalty points.")
                print("You total loyalty points are",customer[id_check]["loyalty"],". Please redeem a valid number of loyalty points.")
                redeem_points()
        elif check_redeem=="no":
            print()
        else:
            print("\nInvalid input! Please enter yes if the customer wants to redeem points, or no if they do not")
            redeem_points()
            
        
def payment_method():
    global total
    global payment
    
    print("Your total is: ",total,"\n")
    print("What method is the customer using to pay?")
    print("Options:\tCash\n\t\tMpesa\n\t\tVisa\n")
    payment=input()
    
    if payment=="Mpesa" or payment=="Visa" or payment=="Cash":
        print()
    else:
        print("\nInvalid input! Please choose either Cash, Visa or Mpesa")
        payment_method()
    

def apply_discounts():
    global cashless_discount
    global birthday_discount
    global total
    
    if payment=="Mpesa" or payment=="Visa":
        cashless_discount=goods_bought*0.02
        total-=cashless_discount
        print("\nYou have received a 2% percent discount for using",payment)
    if birthday=="true":
        birthday_discount=goods_bought*0.1
        total-=birthday_discount
        print("\nHappy Birthday! You have received 10% discount because it is your birthday!")

        
def check_discounts():
    if payment=="Mpesa" or payment=="Visa" or birthday=="true" or redeemed_points>0:
        print("\nLess:")
        if cashless_discount>0:
            print("2% for cashless payment\t",f'{round(cashless_discount):,}')
        if birthday_discount>0:
            print("10% birthday discount\t",f'{round(birthday_discount):,}')
        if redeemed_points>0:
            print("Points redeemed\t\t",f'{round(redeemed_points):,}')
        
    
def print_receipt():
    global cashless_discount
    global birthday_discount
    global payment
    global total
    
    now = datetime.datetime.now()
    separator="-"*50
    highlight="*"*8
    
    print("\n\n\t Start of receipt")
    print(separator)
    print("\t ABC SuperMarket")
    print ("\t",now.strftime("%Y-%m-%d %H:%M:%S"))
    print("\t Customer name:",customer[id_check]["name"])
    if birthday=="true":
        print(highlight,"Happy Birthday!",highlight)
        
    print(separator)
    print("\t\t\t KShs")
    print("Goods bought\t\t",f'{round(goods_bought):,}')
    check_discounts()    
    print("\nTotal:\t\t\t", f'{round(total):,}',"\n")
    
    print(separator)
    customer[id_check]["loyalty"]+=points_earned
    print("Payment by:",payment)
    print("Loyalty points earned with this purchase:", f'{points_earned:,}')
    print("Loyalty points balance:", f'{customer[id_check]["loyalty"]:,}')
    
    print("\nThank you for shopping with ABC Supermarket!")
    
    print(separator)
    print("\tEnd of receipt")


def retrieve_bag():
    global slot_assigned
    
    if id_check in slot_assigned:
        bag_slots[slot_assigned[id_check]-1]="empty"
        print("\n\nBag has been retrieved. Slot",slot_assigned[id_check],"is now empty.")
        del slot_assigned[id_check]

        
customer_entry()
store_bag()
payment_method()
calculate_points()
birthday_check()
apply_discounts()
redeem_points()
print_receipt()
retrieve_bag()

 