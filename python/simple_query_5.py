import psycopg2
import sys
import csv

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n') 
    #description
    print("This query shows all the items and quantities that were bought")
    print("Example input: uid:eileen")
       

def print_rows(rows):
    for row in rows:
        print(row)
    
def showItemsAndQuantity():
    #main function
    heading("Show age and gender")    
    uid = input("User id: ")
    showItemsAndQuantityHelper(uid)

def showItemsAndQuantityHelper(uid):
    #actually doing the queries
    tmpl = '''
    SELECT gs.name, gs.price, b.quantity, sum(gs.price*b.quantity)
      FROM Goods_Services as gs
      JOIN Bought as b
        ON gs.item_id = b.item_id
      JOIN P2B_Transactions as pb
        ON b.transaction_id = pb.transaction_id
      JOIN Personal_Users as p
        ON pb.user_id_personal = p.user_id
     WHERE p.user_id = %s
    GROUP BY gs.item_id, gs.name, gs.price, b.quantity

    '''
    cmd = cur.mogrify(tmpl, [uid])
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        name, price, quantity, sum = row
        print("Name: %s " % (name))
        print("Price: %s " % (price))
        print("Quantity Bought: %s " % (quantity))
        print("Total Cost: %s " % (sum))
        
        
    print("Done!")
    
    #description
    print("This query shows all the items and quantities that were bought")
if __name__ == '__main__':
    try:
        db, user = 'venmo', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        showItemsAndQuantity()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))