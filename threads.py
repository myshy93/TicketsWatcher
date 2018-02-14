from tkinter import *
import ticketList
import time
import tkinter.messagebox
import threading


class Gui(threading.Thread):
    def run(self):
        root = Tk()
        root.mainloop()


class Watcher(threading.Thread):
    group_tickets = ticketList.Tickets()
    stop = 0
    def run(self):
        while self.stop == 0:
            self.group_tickets.pull_tickets()
            print(self.group_tickets.get_tks_ids_list())
            time.sleep(20)

