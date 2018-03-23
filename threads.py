import ticketList
import time
from tkinter import messagebox
import threading
import vlc



class Watcher(threading.Thread):

    # sound alert
    player = vlc.MediaPlayer("resources/beeps.mp3")

    bulk_tickets = ticketList.Tickets()
    stop = 0

    def run(self):

        self.stop = 0
        prev_tk_id = 0

        while True:

            self.bulk_tickets.pull_tickets()
            tks_list = self.bulk_tickets.get_tks_ids_list()
            tks_no = len(tks_list)

            if tks_no is 0:
                prev_tk_id = 0

            elif prev_tk_id is 0 and tks_no is 1:
                prev_tk_id = tks_list[0]
                self.alert()

            time.sleep(10)

    def alert(self):
        self.player.play()
        messagebox.showinfo('New ticket!', 'You have a new ticket in queue!')
        self.player.stop()




