'''
Main code which will accomplish the following goals:
    1) User Interface 
    2) Managing list of passwords
    3) Managing master password
    4) Allowing access to passwords
    5) Creating and deleting passwords
'''
from generate import gen
import hashlib
import sqlite3


class database:
    def __init__(self, master_hash):
        self.conn = sqlite3.connect("database.db")
        self.curr = self.conn.cursor()
        try: 
            self.curr.execute("CREATE TABLE passwords (website TEXT, pass TEXT)")
        except:
            print("Table already exists")
            return
        #adds master_hash as first entry in database
        self.curr.execute("INSERT INTO passwords VALUES ('master_hash',?)",(master_hash,),)
    def add(self, website, password):
        self.curr.execute("INSERT INTO passwords VALUES (?,?)",(website,password,),)    
    def delete(self, target):
        self.curr.execute("DELETE FROM passwords WHERE website = ?",(target,),) 
    def toString(self):
        rows = self.curr.execute("SELECT website, pass FROM passwords").fetchall()
        for i in range(1,len(rows)):
            print("Website:",rows[i][0])
            print("Password:",rows[i][1])
            print("")

def hashed(x):
#returns sha256 hashed hexadecimal of string input x
    return hashlib.sha256(bytes(x,"utf-8")).hexdigest()


if __name__ == "__main__":
    print("Welcome to your password vault")
    dynamic_salt = gen(10)

    master_hash = hashed(input("Select your master password: ")+dynamic_salt)

    #AUTHENTICATION
    #--------------------------------------------------------------------
    access_granted = False
    user_input = hashed(input("Enter your master password: ")+dynamic_salt)
    #print("\nMaster hash:", master_hash)
    #print("Input hash :", user_input)
    if (user_input == master_hash):
        print("\nACCESS_GRANTED")
        access_granted = True
    else:
        print("\nACCESS_DENIED")
    #--------------------------------------------------------------------
    #INITIALIZE DATABASE
    d = database(master_hash) 
    d.add("google.com","password1")
    d.add("facebook.com","PASSWORD")
    d.toString()

