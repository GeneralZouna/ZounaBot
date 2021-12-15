import sqlite3
import json


def get_Balance(userID):
    
    return balance


def set_Balance(userID,amount):
    pass


def transfer(fromID,toID,amount):
    fromBalance = get_Balance(fromID)
    if fromBalance >= amount:
        toBalance = getBalance(toID)
        
        set_Balance(toID,toBalance + amount)
        set_Balance(fromID, fromBalance + amount)
        
    return fromBalance >= amount

def pay(userID,amount):
    balance = get_Balance(userID)
    if balance >= amount:
        set_Balance(userID,balance - amount)
    return balance >= amount
