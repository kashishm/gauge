# -*- coding: utf-8 -*-
import pyrebase

db = None


def init():
    config = {
        "apiKey": "AIzaSyAGTGrZCbaSYvCyTK3lSdJVDWCqRXwvEvo",
        "authDomain": "gauge-97536.firebaseapp.com",
        "databaseURL": "https://gauge-97536.firebaseio.com",
        "storageBucket": "gauge-97536.appspot.com",
        "serviceAccount": "firebase/fb.json"
    }

    global db
    db = pyrebase.initialize_app(config).database()


def query(q):
    db.child("queries").push(q)
