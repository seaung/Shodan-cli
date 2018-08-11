from flask_script import Manager, Server, Shell
from webapp import create_app

app = create_app()

'''
@manager.shell
def make_shell_context():
    return dict(app=app)
'''

def _make_context():
    return dict(app=app)


manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()

