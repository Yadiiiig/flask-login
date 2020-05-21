#login.py

from components.database.db import dbQuery, dbReturn
from passlib.hash import sha256_crypt
import datetime

def addTime(now, mins):
    fulldate = datetime.datetime.now()
    fulldate = fulldate + datetime.timedelta(minutes = mins)
    return fulldate

def loginFunction(username, password):
    if username and password:
        query = "SELECT * FROM logusers WHERE username = %s"
        data = (username, )
        result = dbReturn(query, data)
        if result == []:
            return "usernameError"
        else:
            if sha256_crypt.verify(password, result[0][2]):
                return True
            else:
                return "passwordError"
    else:
        return "emptyError"

def passwordError(username, ip):
    query = "SELECT * FROM failed_logins WHERE username = %s"
    data = (username, )
    result = dbReturn(query, data)

    if result == []:
        query = "INSERT INTO failed_logins (username, tryip, amountTries) VALUES (%s, %s, %s)"
        data = (username, ip, 1)
        dbQuery(query, data)
    else:
        if result[0][3] < 4:
            query = "UPDATE failed_logins SET amountTries = %s, tryip = %s WHERE username = %s"
            newValue = result[0][3] + 1
            data = (newValue, ip, username)
            dbQuery(query, data)
        elif result[0][3] == 4:
            query = "UPDATE failed_logins SET amountTries = %s, tryip = %s, lockedTill = %s WHERE username = %s"
            newValue = result[0][3] + 1
            lockedTill = addTime(datetime.datetime.now().time(), 5)
            data = (newValue, ip, lockedTill, username)
            dbQuery(query, data)
            return "locked"


def checkIfLocked(username):
    query = "SELECT lockedTill FROM failed_logins WHERE username = %s"
    data = (username, )
    result = dbReturn(query, data)
    if result == []:
        return False
    else:
        if result[0][0] == None:
            return False
        else: 
            if result[0][0] < datetime.datetime.now():
                query = "UPDATE failed_logins SET amountTries = %s WHERE username = %s"
                data = (4, username)
                dbQuery(query, data)
                return False
            else:
                return True

def deleteLock(username):
    query = "SELECT * FROM failed_logins WHERE username = %s"
    data = (username, )
    result = dbReturn(query, data)
    if result != []:
        query = "DELETE FROM failed_logins WHERE username = %s"
        data = (username, )
        dbQuery(query, data)
    else:
        pass
