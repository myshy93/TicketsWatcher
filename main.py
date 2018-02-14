import threads


main_window = threads.Gui()
main_window.start()  # porneste gui si continua codul
 # se conecteaza la db si pregateste url pentru a fi apelat prin pull_tickets
whatcherObj = threads.Watcher()
whatcherObj.daemon = True
whatcherObj.start()







