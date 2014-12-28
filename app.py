#! usr/bin/python
# -*- coding: utf-8 -*-

############################# Application Imports #########################
from flask import Flask, request, render_template, json, Response, session, redirect, url_for, Markup
from werkzeug import secure_filename
import os

###############app settings######################
app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(25)

###############App routes##################
@app.route('/')
def index():
    return render_template('code.html')

################flask server################
if __name__ == "__main__":
    app.run(debug=True)
