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
#AES stuff
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class database:
    def __init__(self, master_hash=None,salt=None):
        if (master_hash and salt):
            self.conn = sqlite3.connect("database.db")
            self.curr = self.conn.cursor()
            try: 
                self.curr.execute("CREATE TABLE passwords (website TEXT, username TEXT, pass TEXT)")
            except:
                print("Table already exists")
                return
            #adds master_hash as first entry in database
            values = ("master",master_hash,salt)
            self.curr.execute("INSERT INTO passwords VALUES(?,?,?);", values)
            self.conn.commit()
        else:
            try:
                self.conn = sqlite3.connect("database.db")
                self.curr = self.conn.cursor()
            except:
                print("Cannot connect to database.db")
                return

    def add(self, website,password):
        self.curr.execute(f"INSERT INTO passwords VALUES(?,?,?); ('{website}','{username}','{password}')")    

    def delete(self, target):
        self.curr.execute("DELETE FROM passwords WHERE website = ?",(target,),) 

    def deleteALL(self):
        self.curr.execute("DELETE FROM passwords")

    def toString(self):
        rows = self.curr.execute("SELECT website, pass FROM passwords").fetchall()
        print(len(rows))
        for i in range(0,len(rows)):
            print(rows[i])
            '''
            print("Website:",rows[i][0])
            print("Username:",rows[i][1])
            print("Password:",rows[i][2])
            '''
            print("")

def hashed(x):
#returns sha256 hashed hexadecimal of string input x
    return hashlib.sha256(bytes(x,"utf-8")).hexdigest()

def authenticate(salt):
        #AUTHENTICATION
        #--------------------------------------------------------------------
        user_input = hashed(input("Enter your master password: ")+salt)
        #print("\nMaster hash:", master_hash)
        #print("Input hash :", user_input)
        if (user_input == master_hash):
            print("\nACCESS_GRANTED")
            return True
        else:
            print("\nACCESS_DENIED")
            return False
        #--------------------------------------------------------------------

if __name__ == "__main__":
    print("Welcome to your password vault")
    
    mode = input('''
                 Select your option:
                    1)Create new Password List
                    2)Use Existing Password List
                 ''')
    if(mode == "1"):
        salt = gen(10)
        master_hash = hashed(input("Select your master password: ")+salt)
        db = database(master_hash,salt)
        db.toString()
    elif (mode == "2"):
        db = database()
        db.toString()
        db.add("protonmail.com","jsmith1","testingtesting123")
        db.toString() 
