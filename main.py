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
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.curr = sqliteConnection.cursor()
    def addData(self, target):
        #TODO
    def deleteData(self, target):
        #TODO
    def toString(self):
        #TODO


def hashed(x):
#returns sha256 hashed hexadecimal of string input x
    return hashlib.sha256(bytes(x,"utf-8")).hexdigest()


if __name__ == "__main__":
    print("Welcome to your password vault")
    dynamic_salt = gen(10)

    master_hash = hashed(input("Select your master password: ")+dynamic_salt)

    #authenticaion-------------------------------------------------------
    access_granted = False
    user_input = hashed(input("Enter your master password: ")+dynamic_salt)
    print("\nMaster hash:", master_hash)
    print("Input hash :", user_input)
    if (user_input == master_hash):
        print("\nACCESS_GRANTED")
        access_granted = True
    else:
        print("\nACCESS_DENIED")
    #--------------------------------------------------------------------

