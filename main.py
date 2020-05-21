#main.py

from flask import Flask, g, request, render_template, redirect, url_for, session, jsonify, abort
from flask_wtf.csrf import CSRFProtect

from components.config import Config
from components.functions.login import loginFunction, passwordError, checkIfLocked, deleteLock

application = Flask(__name__)
application.config.from_object(Config)
csrf = CSRFProtect(application)

@application.route('/')
def root():
    return render_template("index.html")

@application.route('/login', methods = ['POST', 'GET'])
def login():
    if 'loggedin' in session:
        return redirect(url_for('success'))
    else:
        if request.method == "GET":
            return render_template("login.html", title = "Login")
        elif request.method == "POST":
            if checkIfLocked(request.form["username"]) == False:
                result = loginFunction(request.form["username"], request.form["password"])
                if result == "usernameError":
                    return render_template("login.html", resultLogin = "Username or password is wrong.")
                elif result == True:
                    session['loggedin'] = True
                    deleteLock(request.form["username"])
                    return redirect(url_for('root'))
                elif result == "passwordError":
                    if passwordError(request.form["username"], request.remote_addr) == "locked":
                        return render_template("login.html", resultLogin = "Your account is blocked, try again in 5 minutes.")
                    else:
                        return render_template("login.html", resultLogin = "Username or password is wrong.")
                elif result == "emptyError":
                    return render_template("login.html", resultLogin = "No credentials filled in.")
            else:
                return render_template("login.html", resultLogin = "Your account is temporary blocked. Come back later.")

@application.route('/success', methods = ['GET'])
def success():
    if 'loggedin' in session:
        if request.method == "GET":
            return render_template("success.html", title = "Success")
        else:
            return redirect(url_for('login'))
    else:   
        return redirect(url_for('login'))

@application.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    application.debug = True
    application.run()
