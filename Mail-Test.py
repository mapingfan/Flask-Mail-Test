# This program is used for testing flask-mail extension .
# something wrong in my app, so I must learn how to use this extension .
# password nwntuhwdkrrbbbbe

from flask import Flask
from flask_mail import Mail, Message
from flask_script import Manager
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = '25'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = '80551xx'
app.config['MAIL_PASSWORD'] = 'nwntuhwdkrrbbbbe'
app.config['FLASKY_MAIL_SENDER'] = "80551xx@qq.com"

mail = Mail(app)
manager = Manager(app)


@app.route('/')
def index():
    msg = Message('subject', sender=app.config['FLASKY_MAIL_SENDER'], recipients=['228787xx@qq.com'])
    msg.body = 'body'
    msg.html = '<b>HTML</b> body'
    mail.send(msg)

    return '<h1>Sent successfully</h1>'

if __name__ == "__main__":
    app.run(debug=True)




