import threads


main_window = threads.Gui()
main_window.start()  # porneste gui si continua codul
whatcherObj = threads.Watcher()
whatcherObj.daemon = True
whatcherObj.start()







