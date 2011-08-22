import os
import inspect
from play.utils import *

MODULE = 'playboiler'

# Commands that are specific to your module

COMMANDS = ['playboiler:help', 'playboiler:init']

def execute(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "playboiler:help":
        print "~ This module copies the included HTML5Boilerplate files in to your application."
        print "~ You should run playboiler:init only once and on a new project as it will overwrite the public folder and the main.html file."

    elif command == "playboiler:init":
	module_dir = inspect.getfile(inspect.currentframe()).replace("commands.py", "")
        d = os.path.dirname(os.path.join(app.path, 'public/stylesheets/'))
        answer = raw_input('This command will completley remove and replace the main.html file and "public" folder in your application. Are you sure you want to continue?(y/n) ')

        if answer == 'y':
            public = os.path.join(app.path, 'public/')
            print 'Replacing folder: '+public
            if os.path.exists(public):
                shutil.rmtree(public)
            shutil.copytree(os.path.join(module_dir, 'public/'), public)

            main = os.path.join(app.path, 'app/views/', 'main.html')
            print 'Replacing file: '+ main
            shutil.copyfile(os.path.join(module_dir, 'main.html'), main)

        else:
            print 'You chose not to replace the files. Nothing was done.'


# This will be executed before any command (new, run...)
def before(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")



# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass



