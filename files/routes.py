from files import app
from flask import redirect,render_template
from files.service import Service
from files.auditlog import AuditLog
from flask import request
import datetime
import json

@app.route('/')
@app.route('/home')
def home():
    now = datetime.datetime.now()
    service = Service( request.args.get('newservice', default=None) )
    auditLog = AuditLog( request.args.get('newevent', default=json.dumps({})) )
    return render_template("index.html", service=service, now=now, auditLog=auditLog)

