import app
from app import mail
from flask import render_template, current_app
from flask_mail import Message
import threading


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    t = threading.Thread(target=send_async_email, args=[current_app._get_current_object(), msg])
    t.start()
    return t
    # mail.send(msg)