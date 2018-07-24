from os import getenv as os_getenv
from os import path as os_path
from sys import path as sys_path

sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), '..')))


from flask_script import Manager, Server
from application import create_app


from common import SERVER_PORT, SERVER_IP


app = create_app()
manager = Manager(app)


manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host=os_getenv('IP', SERVER_IP),
    port=int(os_getenv('PORT', SERVER_PORT)))
)


if __name__ == "__main__":
    manager.run()
