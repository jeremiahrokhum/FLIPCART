import mysql.connector
from datetime import date,datetime

#Make sure that you use customer_id as 3 
#He's actually has orders

#ADD ORDERS AFTER 706

#Lists out the states and counts the number of customers from those states
connect = mysql.connector.connect(user='root', password='', host='localhost', database='FLIPCART')

cursor_ = connect.cursor()

def customer_creation():
    customer_id = int(input("Enter the id of the customer: "))
    customer_username = input("Enter the username of Customer: ")
    customer_password = input("Enter the password of Customer: ")
    customer_DOB = input("Enter the DOB of Customer: ")
    customer_phone1 = input("Enter the primary phone number of Customer: ")
    customer_phone2 = input("Enter the secondary phone number of Customer: ")
    customer_email_id = input("Enter the email of Customer: ")
    customer_city = input("Enter the city of Customer: ")
    customer_state = input("Enter the state of Customer: ")
    cursor2 = connect.cursor()
    query = "INSERT INTO customer(customer_id,customer_username,customer_password,DOB,customer_number,customer_number2,customer_email_id,customer_city,customer_state) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor2.execute(query,(customer_id,customer_username,customer_password,customer_DOB,customer_phone1,customer_phone2,customer_email_id,customer_city,customer_state))
    connect.commit()
    print("Customer added successfully")

def seller_creation():
    seller_id = int(input("Enter the id of the seller: "))
    seller_username = input("Enter the username of seller: ")
    seller_password = input("Enter the password of seller: ")
    seller_phone1 = input("Enter the primary phone number of seller: ")
    seller_phone2 = input("Enter the secondary phone number of seller: ")
    seller_email_id = input("Enter the email of seller: ")
    seller_city = input("Enter the city of seller: ")
    seller_state = input("Enter the state of seller: ")
    cursor2 = connect.cursor()
    query = "INSERT INTO seller(seller_id,seller_username,seller_password,seller_phone_number,seller_phone_number2,seller_email_id,seller_city,seller_state) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor2.execute(query,(seller_id,seller_username,seller_password,seller_phone1,seller_phone2,seller_email_id,seller_city,seller_state))
    connect.commit()
    print("Customer added successfully!!")

def agent_creation():
    agent_id = int(input("Enter the id of the agent: "))
    agent_username = input("Enter the username of agent: ")
    agent_password = input("Enter the password of agent: ")
    agent_phone1 = input("Enter the primary phone number of agent: ")
    agent_phone2 = input("Enter the secondary phone number of agent: ")
    agent_email_id = input("Enter the email of agent: ")
    e = int(input("Enter expected time of delivery"))
    cursor2 = connect.cursor()
    query = "Insert into delivery_agent(agent_id,agent_username,agent_password,contact_number,contact_number2,agent_email_id,expected_time_of_delivery) values(%s,%s,%s,%s,%s,%s,%s)"
    cursor2.execute(query,(agent_id,agent_username,agent_password,agent_phone1,agent_phone2,agent_email_id,e))
    connect.commit
    print("Agent added Succesfully!!")

def view_categories():
    cursor2 = connect.cursor()
    query = "SELECT DISTINCT category_name from category"
    cursor_.execute(query)
    result = cursor_.fetchall()
    print("Sl No --- Category Name ")
    counter = 1
    for i in result:
        print(counter, i[0])
        counter += 1

def view_products():
    cursor2 = connect.cursor()
    query = "SELECT product_id,product_name,category_id,brand_name,product_price,product_quantity,product_discount from product"
    cursor_.execute(query)
    result = cursor_.fetchall()
    for i in result:
        print("Product ID --- Product Name --- Category_id --- Brand_Name --- Product_Price --- Product_Quantity --- Product_Discount")

        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6])

def view_cart(id):
    cursor2 = connect.cursor()
    query = f"SELECT c.customer_id, p.product_id, p.product_name, p.product_price, c.quantity FROM Cart c JOIN Product p ON c.product_id = p.product_id WHERE c.customer_id = {id};"
    cursor2.execute(query)
    result = cursor2.fetchall()
    for i in result:
        print("Customer ID --- Product ID --- Product Name --- Product_Price --- Product_Quantity")

        print(i[0], i[1], i[2], i[3], i[4])

def add_to_cart(id):
    cursor2 = connect.cursor()
    product_id = int(input("Enter the product id: "))
    quantity = int(input("Enter the quantity: "))
    query = "INSERT INTO cart(customer_id,product_id,quantity) VALUES(%s,%s,%s)"
    cursor2.execute(query,(id,product_id,quantity))
    connect.commit()
    print("Product added to cart successfully")

def add_money(id):
    cursor2 = connect.cursor()
    amount = int(input("Enter the amount: "))
    query = f"UPDATE wallet SET wallet_amount = wallet_amount + {amount} WHERE customer_id = {id}"
    cursor2.execute(query)
    connect.commit()
    print("Money added to wallet successfully")

def check_wallet(id):
    cursor2 = connect.cursor()
    query = f"SELECT wallet_amount from wallet where customer_id = {id}"
    cursor2.execute(query)
    result = cursor2.fetchall()
    print("Wallet Balance: ",result[0][0])

def remove_from_cart(id):
    cursor2 = connect.cursor()
    product_id = int(input("Enter the product id: "))
    query = f"DELETE FROM cart WHERE customer_id = {id} AND product_id = {product_id}"
    cursor2.execute(query)
    connect.commit()
    print("Product removed from cart successfully")

def view_orders(id):
    cursor2 = connect.cursor()
    query = f"SELECT order_id,order_date,order_time,agent_id FROM order_ WHERE customer_id = {id}"
    cursor2.execute(query)
    result = cursor2.fetchall()
    for i in result:
        print("Order ID --- Order Date --- Order Time --- Agent ID")

        print(i[0], i[1], i[2], i[3])

def add_category():
    cursor2 = connect.cursor()
    category_id = int(input("Enter Category id :  "))
    category_name = input("Enter category name : ")
    query = "INSERT INTO Category(category_id,category_name) VALUES(%s,%s)"
    cursor2.execute(query,(category_id,category_name))
    connect.commit()
    print("Category Added Succesfully!!")

def add_product():
    cursor2 = connect.cursor()
    product_id = int(input("Enter product id :  "))
    product_name = input("Enter product name : ")
    category_id = int(input("Enter category_id : "))
    brand_name = input("Enter brand name : ")
    product_price = int(input("Enter product price : "))
    product_quantity = int(input("Enter product quantity : "))
    product_discount = int(input("Enter product discount : "))
    query = "INSERT INTO Product(product_id,product_name,category_id,brand_name,product_price,product_quantity,product_discount) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    cursor2.execute(query,(product_id,product_name,category_id,brand_name,product_price,product_quantity,product_discount))
    connect.commit()
    print("Product Added Succesfully!!")


def checkout(id):
    cursor2 = connect.cursor()
    query = f"SELECT c.customer_id, p.product_id, p.product_name, p.product_price, c.quantity FROM Cart c JOIN Product p ON c.product_id = p.product_id WHERE c.customer_id = {id};"
    cursor2.execute(query)
    result = cursor2.fetchall()
    total = 0
    product_id = []
    for i in result:
        product_id.append(i[1])
        total += i[3]*i[4]
    print("Total amount to be paid: ",total)
    query = f"SELECT wallet_amount from wallet where customer_id = {id}"
    cursor2.execute(query)
    result = cursor2.fetchall()
    if(result[0][0] >= total):
        query = f"UPDATE wallet SET wallet_amount = wallet_amount - {total} WHERE customer_id = {id}"
        cursor2.execute(query)
        connect.commit()
        print("Payment Successful")
        print("Order Placed")
        for i in product_id:
            query = f"UPDATE product SET product_quantity = product_quantity - 1 WHERE product_id = {i}"
            cursor2.execute(query)
            connect.commit()
            order_id = input("Enter the order id: ")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            order_date = date.today()
            order_time = current_time
            product_id = i
            customer_id = id
            seller_id = input("Enter the seller id: ")
            agent_id = input("Enter the agent id: ")
            query = "INSERT INTO order_(order_ID,order_date,order_time,product_id,customer_id,seller_id,agent_id) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cursor2.execute(query,(order_id,order_date,order_time,product_id,customer_id,seller_id,agent_id))
            connect.commit()
        query = f"DELETE FROM cart WHERE customer_id = {id}"
        cursor2.execute(query)
        connect.commit()
    else:
        print("Insufficient Balance")

def view_delivery_status(id):
    #first we need to get the agent id from the order table
    cursor2 = connect.cursor()
    query = f"SELECT agent_id FROM order_ WHERE customer_id = {id}"
    cursor2.execute(query)
    result = cursor2.fetchall()
    agent_id = result[0][0]
    #now we will have to use this agent id to get the expeceted delivery date from the delivery agent table
    query = f"SELECT expected_time_of_delivery FROM delivery_agent WHERE agent_id = {agent_id}"
    cursor2.execute(query)
    result = cursor2.fetchall()
    print("Expected Delivery Date: ",result[0][0],"Days")

def empty_cart(id):
    cursor2 = connect.cursor()
    query = f"DELETE FROM cart WHERE customer_id = {id}"
    cursor2.execute(query)
    connect.commit()
    print("Cart Emptied")

def view_product_reviews():
    cursor2 = connect.cursor()
    product_id = int(input("Enter the product id: "))
    query = f"SELECT p.product_name, p.brand_name, c.customer_username, f.product_feedback FROM feedback f JOIN product p ON f.product_id = p.product_id JOIN customer c ON f.customer_id = c.customer_id WHERE f.product_id = {product_id}"
    cursor2.execute(query)
    result = cursor2.fetchall()
    if(result == []):
        print("No reviews for this product")
    else:
        for i in result:
            print("Product_Nameß --- Brand_Name --- Customer_Name --- Product Feedback")
            print(i[0],"||", i[1],"||", i[2],"||", i[3])

def view_own_product_reviews(id):
    cursor2 = connect.cursor()
    query = f"SELECT p.product_name, p.brand_name, c.customer_username, f.product_feedback FROM feedback f JOIN product p ON f.product_id = p.product_id JOIN customer c ON f.customer_id = c.customer_id WHERE f.customer_id = {id}"
    cursor2.execute(query)
    result = cursor2.fetchall()
    if(result == []):
        print("No reviews for your products")
    else:
        for i in result:
            print("Product_Nameß --- Brand_Name --- Customer_Name --- Product Feedback")
            print(i[0],"||", i[1],"||", i[2],"||", i[3])

def add_review(id):
    cursor2 = connect.cursor()
    feedback_id = int(input("Enter the feedback id: "))
    product_id = int(input("Enter the product id: "))
    product_feedback = input("Enter your feedback: ")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    feedback_date = date.today()
    feedback_time = current_time
    query = "INSERT INTO feedback(feedback_id,product_id,customer_id,product_feedback,feedback_date,feedback_time) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor2.execute(query,(feedback_id,product_id,id,product_feedback,feedback_date,feedback_time))
    connect.commit()
    print("Feedback Added")

def remove_review(id):
    cursor2 = connect.cursor()
    query = f"DELETE FROM feedback where customer_id = {id}"
    cursor2.execute(query)
    connect.commit()
    print("Feedback Removed")

def view_wishlist(id):
    cursor2 = connect.cursor()
    query = f"SELECT customer_id, product_id from wishlist where customer_id = {id}"
    cursor2.execute(query)
    result = cursor2.fetchall()
    counter = 0
    if(result == []):
        print("No products in your wishlist")
    else:
        for i in result:
            counter+=1
            print(f"Customer ID --- Product ID {counter}")
            print(i[0],"||", i[1])

def add_to_wishlist(id):
    cursor2 = connect.cursor()
    product_id = int(input("Enter the product id: "))
    query = "INSERT INTO wishlist(product_id,customer_id) VALUES(%s,%s)"
    cursor2.execute(query,(product_id,id))
    connect.commit()
    print("Product added to wishlist")

def remove_from_wishlist(id):
    cursor2 = connect.cursor()
    product_id = int(input("Enter the product id: "))
    query = f"DELETE FROM wishlist WHERE product_id = {product_id} AND customer_id = {id}"
    cursor2.execute(query)
    connect.commit()
    print("Product removed from wishlist")

def clear_wishlist(id):
    cursor2 = connect.cursor()
    query = f"DELETE FROM wishlist WHERE customer_id = {id}"
    cursor2.execute(query)
    connect.commit()
    print("Wishlist cleared")

while(1):
    print("Submission for the Final Deadline of DBMS")
    print("Made by Jeremiah and Manshaa")
    print()
    print("Press 1 to continue")
    print("Press 0 to exit")
    a = int(input())
    while(1):
        if(a == 1):
            while(1):
                print("Press 1 if you want to enter as Customer")
                print("Press 2 if you want to enter as Seller")
                print("Press 3 if you want to enter as Delivery Agent")
                print("Press 0 to get to the Previous Menu")
                b = int(input())
                if(b == 1):
                    while(1):
                        print()
                        print("Welcome to the login/signup page of Customer")
                        print("Press 1 if you want to login")
                        print("Press 2 if you want to signup")
                        print("Press 0 to get to the Previous Menu")
                        c = int(input())
                        if(c == 1):
                            id = int(input("Enter the id of the customer: "))
                            customer_username = input("Enter the username of Customer: ")
                            customer_password = input("Enter the password of Customer: ")
                            query = "SELECT customer_username,customer_password from customer where customer_id = %s"
                            cursor_.execute(query,(id,))
                            result = cursor_.fetchall()
                            #example: customer id = 1
                            # customer username = jsimonian0
                            # customer password = T8QAyBTVguz
                            print(result)
                            if(customer_username == result[0][0] and customer_password == result[0][1]):
                                print("Welcome to Customer Menu")
                                print()
                                while(1):
                                    print()
                                    print("1. Change Personal Details")
                                    print("2. View Categories")
                                    print("3. View Products")
                                    print("4. View Cart")
                                    print("5. Add Products to Cart")
                                    print("6. Add Money to Wallet")
                                    print("7. Check Wallet Balance")
                                    print("8. Remove Product from Cart")
                                    print("9. View Orders")
                                    print("10. Checkout")
                                    print("11. View Delivery Status")
                                    print("12. Empty Cart")
                                    print("13. View Product Reviews")
                                    print("14. View your Product Reviews")
                                    print("15. Add Product Review")
                                    print("16. Remove Product Review")
                                    print("17. View Wishlist")
                                    print("18. Add Product to Wishlist")
                                    print("19. Remove Product from Wishlist")
                                    print("20. Clear Wishlist")
                                    print("0. Exit")
                                    
                                    choice = int(input("Enter your choice: "))
                                    if(choice == 1):
                                        while(1):
                                            print()
                                            print("1. Change Username")
                                            print("2. Change Password")
                                            print("3. Change DOB")
                                            print("4. Change Primary Phone Number")
                                            print("5. Change Secondary Phone Number")
                                            print("6. Change Email ID")
                                            print("7. Change City")
                                            print("8. Change State")
                                            print("0. Exit")
                                            d = int(input())
                                            if(d == 1):
                                                new_username = input("Enter the new username: ")
                                                query = "UPDATE customer SET customer_username = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_username,id))
                                                connect.commit()
                                                print("Username updated successfully")
                                            if(d == 2):
                                                new_password = input("Enter the new password: ")
                                                query = "UPDATE customer SET customer_password = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_password,id))
                                                connect.commit()
                                                print("Password updated successfully")
                                            if(d == 3):
                                                new_DOB = input("Enter the new DOB: ")
                                                query = "UPDATE customer SET DOB = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_DOB,id))
                                                connect.commit()
                                                print("DOB updated successfully")
                                            if(d == 4):
                                                new_number = input("Enter the new primary phone number: ")
                                                query = "UPDATE customer SET customer_number = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_number,id))
                                                connect.commit()
                                                print("Primary phone number updated successfully")
                                            if(d == 5):
                                                new_number2 = input("Enter the new secondary phone number: ")
                                                query = "UPDATE customer SET customer_number2 = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_number2,id))
                                                connect.commit()
                                                print("Secondary phone number updated successfully")
                                            if(d == 6):
                                                new_email = input("Enter the new email: ")
                                                query = "UPDATE customer SET customer_email_id = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_email,id))
                                                connect.commit()
                                                print("Email updated successfully")
                                            if(d == 7):
                                                new_city = input("Enter the new city: ")
                                                query = "UPDATE customer SET customer_city = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_city,id))
                                                connect.commit()
                                                print("City updated successfully")
                                            if(d == 8):
                                                new_state = input("Enter the new state: ")
                                                query = "UPDATE customer SET customer_state = %s WHERE customer_id = %s"
                                                cursor_.execute(query,(new_state,id))
                                                connect.commit()
                                                print("State updated successfully")
                                            if(d == 0):
                                                break
                                    if(choice == 2):
                                        #View categories
                                        view_categories()
                                    if(choice == 3):
                                        #View products
                                        view_products()
                                    if(choice == 4):
                                        #View cart
                                        view_cart(id)
                                    if(choice == 5):
                                        #Add products to cart
                                        add_to_cart(id)
                                    if(choice == 6):
                                        #Add money to wallet
                                        add_money(id)
                                    if(choice == 7):
                                        #Check wallet balance
                                        check_wallet(id)
                                    if(choice == 8):
                                        #Remove product from cart
                                        remove_from_cart(id)
                                    
                                    if(choice == 9):
                                        #View orders
                                        view_orders(id)
                                    if(choice == 10):
                                        #Checkout
                                        checkout(id)
                                    if(choice == 11):
                                        #View delivery status
                                        view_delivery_status(id)
                                    if(choice == 12):
                                        #Empty cart
                                        empty_cart(id)
                                    if(choice == 13):
                                        #View product reviews
                                        view_product_reviews()
                                    if(choice == 14):
                                        #View your own product review
                                        view_own_product_reviews(id)
                                    if(choice == 15):
                                        #Add Review
                                        add_review(id)
                                    if(choice == 16):
                                        #Remove Review
                                        remove_review(id)
                                    if(choice == 17):
                                        #View wishlist
                                        view_wishlist(id)
                                    if(choice == 18):
                                        #Add to wishlist
                                        add_to_wishlist(id)
                                    if(choice == 19):
                                        #Remove from wishlist
                                        remove_from_wishlist(id)
                                    if(choice == 20):
                                        #Clear wishlist
                                        clear_wishlist(id)
                                    if(choice == 0):
                                        break

                                    # break
                            else:
                                print("Wrong username or password")
                        if(c == 2):
                            customer_creation()
                        if(c == 0):
                            break
                    
                if(b == 2):
                    while(1):
                        print()
                        print("Welcome to the login/signup page of Seller")
                        print("Press 1 if you want to login")
                        print("Press 2 if you want to signup")
                        print("Press 0 to get to the Previous Menu")
                        d = int(input())
                        if(d==1):
                            id = int(input("Enter the id of the seller: "))
                            seller_username = input("Enter the username of Seller: ")
                            seller_password = input("Enter the password of Seller: ")
                            query = "SELECT seller_username,seller_password from seller where seller_id = %s"
                            cursor_.execute(query,(id,))
                            result = cursor_.fetchall()
                            # example id-2
                            # username - sturmel1
                            # password - T7gP9OtjwE
                            if(seller_username == result[0][0] and seller_password == result[0][1]):
                                print("Welcome to Seller Menu")
                                print()
                                while(1):
                                    print()
                                    print("1. Search Category")
                                    print("2. Search Product")
                                    print("3. Add Category")
                                    print("4. Add Product")
                                    print("5. Assign Delivery agent")
                                    print("6. Show all previous orders")
                                    print("7. show all running order")
                                    print("8. total revenue")
                                    print("To EXIT press 0")
                                    choice1 = int(input("Enter your choice : "))
                                    if(choice1 == 1):
                                        view_categories()
                                    if(choice1 == 2):
                                        view_products()
                                    if(choice1 == 3):
                                        add_category()
                                    if(choice1 == 4):
                                        add_product()
                                    if(choice1 == 5):
                                        order_id = int(input("Enter the order_id : "))
                                        agent_id = int(input("Enter delivery agent id : "))
                                        query = "UPDATE order_ SET agent_id = %s WHERE order_id = %s"
                                        cursor_.execute(query,(agent_id,order_id))
                                        connect.commit()
                                        print("Order Updated Successfully!!")
                                    if(choice1 == 6):
                                        #previous orders
                                        cursor2 = connect.cursor()
                                        query = f"Select order_id FROM Order_ where seller_id = {id} and agent_id in (SELECT agent_id from Delivery_Agent where expected_time_of_delivery = 0) ORDER BY Order_ID"
                                        cursor2.execute(query)
                                        result = cursor2.fetchall()
                                        for i in result:
                                            print(i)
                                    if(choice1 == 7):
                                        #running orders
                                        cursor2 = connect.cursor()
                                        query = f"Select order_id FROM Order_ where seller_id = {id} and agent_id in (SELECT agent_id from Delivery_Agent where expected_time_of_delivery > 0) ORDER BY Order_ID"
                                        cursor2.execute(query)
                                        result = cursor2.fetchall()
                                        for i in result:
                                            print(i)
                                        # connect.commit()
                                    if(choice1 == 8):
                                        # total revenue
                                        cursor2 = connect.cursor()
                                        query = f"SELECT Seller.seller_username, SUM(Product.product_price * Product.product_quantity) AS total_revenue, COUNT(Order_.order_ID) AS number_of_orders FROM Product INNER JOIN Order_ ON Product.product_id = Order_.product_ID INNER JOIN Seller ON Order_.seller_ID = Seller.seller_ID where seller.seller_id= {id} GROUP BY Seller.seller_username"
                                        cursor2.execute(query)
                                        result = cursor2.fetchall()
                                        for i in result:
                                            print(i)
                                        connect.commit()
                                    if(choice1 == 0):
                                        break
                            else:
                                print("Wrong username or Password!!")
                        if(d==2):
                            seller_creation()
                        if(d == 0):
                            break
                    # break

                if(b == 3):
                    while(1):
                        print()
                        print("Welcome to the login/signup page of Delivery Agents")
                        print("Press 1 if you want to login")
                        print("Press 2 if you want to signup")
                        print("Press 0 to get to the Previous Menu")
                        e = int(input())
                        if(e==1):
                            id = int(input("Enter the id of the agent: "))
                            agent_username = input("Enter the username of agent: ")
                            agent_password = input("Enter the password of agent: ")
                            query = "SELECT agent_username,agent_password from delivery_agent where agent_id = %s"
                            cursor_.execute(query,(id,))
                            result = cursor_.fetchall()
                            if(agent_username == result[0][0] and agent_password == result[0][1]):
                                while(1):
                                    print()
                                    print("1. show all running orders")
                                    print("2. show all previous orders")
                                    print("3. update delivery status")
                                    print("to EXIT press 0")
                                    choice2 = int(input("Entger your choice : "))
                                    if(choice2==1):
                                        cursor2 = connect.cursor()
                                        query = f"select order_id from order_ where agent_id in(select agent_id from delivery_agent where agent_id= {id} and expected_time_of_delivery>0);"
                                        cursor2.execute(query)
                                        result = cursor2.fetchall()
                                        for i in result:
                                            print(i)
                                    if(choice2 == 2):
                                        cursor2 = connect.cursor()
                                        query = f"select order_id from order_ where agent_id in(select agent_id from delivery_agent where agent_id={id} and expected_time_of_delivery>0);"
                                        cursor2.execute(query)
                                        result = cursor2.fetchall()
                                        for i in result:
                                            print(i)
                                    if(choice2 == 3):
                                        order_id = int(input("Enter the order_id : "))
                                        x = int(input("Enter new expected time of delivery: "))
                                        query = "UPDATE Delivery_agent SET expected_time_of_delivery = %s WHERE agent_id = %s"
                                        cursor_.execute(query,(x,id))
                                        connect.commit()
                                        print("Order Updated Successfully!!")
                                    if(choice2 == 0):
                                        break
                            else:
                                print("Wrong Username or Password!!")
                        if(e==2):
                            agent_creation()
                        if(e==0):
                            break

                        # break

                if(b == 0):
                    break
            break
        if(a == 0):
            break
    if(a == 0):
        break
        
# while(1):
#     print("Welcome to the Command Line Interface made by Jeremiah and Manshaa")
#     print("Press 1 if you want to continue")
#     print("Press 0 if you want to exit")
#     a = int(input())
#     if(a == 1):
#         while(1):
#             print("Press 1 if you want to run OLAP queries")
#             print("Press 2 if you want to embedded queries")
#             print("Press 3 if you want to run Trigger queries")
#             print("Press 0 if you want to go to the previous menu")
#             b = int(input())
#             if(b == 1):
#                 while(1):
#                     print("Press 1 if you want to retrieve the total sales by category")
#                     print("Press 2 if you want to retrieve the total revenue and number of orders by the seller ")
#                     print("Press 3 if you want to find the number of orders delieverd by each delivery agent in a particular month")
#                     print("Press 4 if you want to find the total orders delivered by an agent")
#                     print("Press 0 if you want to go to the previous menu")
#                     c = int(input())
#                     if(c == 1):
#                         sql_query = """ 
#     SELECT Category.category_name, SUM(Product.product_price * Product.product_quantity) AS total_sales
#     FROM Product
#     INNER JOIN Category ON Product.category_id = Category.category_ID
#     INNER JOIN Order_ ON Product.product_id = Order_.product_ID
#     WHERE Order_.order_date
#     GROUP BY Category.category_name WITH ROLLUP;
#             """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     if(c == 2):
#                         sql_query = """ 
#     SELECT Seller.seller_name, SUM(Product.product_price * Product.product_quantity) AS total_revenue, COUNT(Order_.order_ID) AS number_of_orders
#     FROM Product
#     INNER JOIN Order_ ON Product.product_id = Order_.product_ID
#     INNER JOIN Seller ON Order_.seller_ID = Seller.seller_ID
#     GROUP BY Seller.seller_name WITH ROLLUP;
#             """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     if(c == 3):
#                         sql_query = """ 
#     SELECT d.agent_name, COUNT(*) AS order_count
#     FROM Delivery_Agent d
#     JOIN Order_ o ON d.agent_ID = o.agent_id
#     WHERE MONTH(o.order_date) = 3
#     GROUP BY d.agent_name WITH ROLLUP;
#             """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     if(c == 4):
#                         sql_query = """ 
#     select agent_id, count(order_id) as 'Total Orders'
#     from Order_ 
#     group by agent_id with rollup;
#             """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     else:
#                         break
#             if(b == 2):
#                 while(1):
#                     print("Press 1 if you want to run the first embedded query")
#                     print("Press 2 if you want to run the second embedded query")
#                     print("Press 0 if you want to go back")
#                     c = int(input())
#                     if(c == 1):
#                         sql_query = """ 
#         SELECT customer_state ,COUNT(*) FROM customer GROUP BY customer_state; 
#         """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     if(c == 2):
#                         sql_query = """ 
#                                 SELECT C.category_name, COUNT(*) as num_products_sold
#                     FROM Order_ O
#                     JOIN Product P ON O.product_ID = P.product_ID
#                     JOIN Category C ON P.category_id = C.category_ID
#                     GROUP BY C.category_name
#                     ORDER BY num_products_sold DESC
#                     LIMIT 5;
#                                 """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print(result)
#                     else:
#                         break
#             if(b == 3):
#                 while(1):
#                     print("Press 1 if you want to run the first Trigger")
#                     print("Press 2 if you want to run the second Trigger")
#                     print("Press 0 if you want to go back")
#                     c = int(input())
#                     if(c == 1):
#                         sql_query = """ 
                        
# create trigger verify_discount
# before insert on Product
# for each row
# if new.product_discount>80 then set new.product_discount=0;
# end if;//


#                                 """
#                         cursor_.execute(sql_query)
#                     if(c == 2):
#                         sql_query = """ 
# create trigger update_quantity
# before update 
# on Product
# for each row
# IF new.product_quantity<0 then set new.product_quantity=0;
# end if; $$ 


#         """
#                         cursor_.execute(sql_query)
#                         result = cursor_.fetchall()
#                         print("result")
#                     else:
#                         break
#             else:
#                 break
#     else:
#         break
# print(result)
# cursor_.close()
# connect.close()

