from tkinter import *
import ticketList
import time
import tkinter.messagebox
import threading


class Watcher(threading.Thread):
    group_tickets = ticketList.Tickets()

    def run(self):

        prev_tk_id = 0

        while True:
            self.group_tickets.pull_tickets()
            tks_list = self.group_tickets.get_tks_ids_list()
            tks_no = len(tks_list)

            if tks_no is 0:
                prev_tk_id = 0

            elif prev_tk_id is 0 and tks_no is 1:
                prev_tk_id = tks_list[0]
                self.alert()

            time.sleep(10)

    def alert(self):
        print("alert")


class Gui(threading.Thread):

    def run(self):
        whatcherObj = Watcher()
        whatcherObj.daemon = True
        root = Tk()
        root.title("TicketsWatcher")
        mainframe = Frame(root, width=250, height=100)
        mainframe.pack()
        start_btn = Button(mainframe, text="START", command=whatcherObj.start)
        start_btn.pack()
        root.mainloop()
