import os
from app import create_app, db
from app.models import User, Post
from flask_script import Shell, Manager, Server
from flask_migrate import MigrateCommand, Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host="127.0.0.1", port=5000, use_debugger=True))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()