import psycopg2
import sys
import csv

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')
    #printing description of the query
    print("\nThis query returns the demographics (age and gender) of the user with the user_id that has been inputted.\n")
    #Giving cues for the inputs
    print("Input: eileenmao\n")
    
def show_demographics():
    #asking user for user id to show input
    heading("Show demographics")    
    uid = input("User ID: ")
    show_demographics_helper(uid)

def show_demographics_helper(uid):
    #executing the query itself
    tmpl = '''
        SELECT age, gender
          FROM Personal_Users
         WHERE user_id = %s
    '''
    cmd = cur.mogrify(tmpl, [uid])
    cur.execute(cmd)
    rows = cur.fetchall()
    #print demographics
    for row in rows:
        print("Age: %s" % (row[0]))
        print("Gender: %s" % (row[1]))
    print("The demographics have been printed!")
 
        
if __name__ == '__main__': #main method
    try:
        db, user = 'venmo', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        show_demographics()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))