from tkinter import *
from threads import Watcher
import connections
import configparser

# load and read config file
configfile = configparser.ConfigParser()
configfile.read('config.ini')
login_data = dict(configfile.items('LOGIN'))

# test connection for errors
testcon = connections.Rdsdb(login_data['user'], login_data['pass'])
errors = testcon.get_final_url()
if errors != 10 and errors != 20:
    watcherObj = Watcher()


# gui buttons functions


def stop_f(event):
    root.destroy()


def start_f(event):
    try:
        watcherObj.daemon = True
        watcherObj.start()
        label.config(text='Running...', fg='green')
        start_btn.config(text='Stop and exit')
        start_btn.bind("<Button-1>", stop_f)
    except:
        label.config(text='Login failed, check credentials or options in config file.', fg='red')
        start_btn.grid_forget()


# gui init

root = Tk()
root.title("TicketsWatcher")
root.minsize(250, 100)
root.resizable(False, False)
mainframe = Frame(root, width='250', height='100').grid()

label = Label(mainframe, text="Set credentials in config file and press start")
label.grid(row=0, column=0, sticky='W')

start_btn = Button(mainframe, text="Start")
start_btn.grid(row=0, column=1)

start_btn.bind("<Button-1>", start_f)

root.update()
root.mainloop()



