from flask_script import Manager
from server_user import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()