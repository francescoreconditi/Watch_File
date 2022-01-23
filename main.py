#
# fff Import
#

import json
import os
import time
from distutils.file_util import move_file

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#
# fff Costanti
#

PATH_TO_WATCH = "c:\\temp\\origine"
PATH_TO_PUT = "c:\\temp\\destinazione"

#
# fff Flusso
#


class MyHandler(FileSystemEventHandler):
    i = 1

    # ! La funzione sotto "scatta" quando viene modificato (quindi anche "creato") un file nella
    # ! directory "che deve tenere d' occhio"
    def on_modified(self, event):
        for filename in os.listdir(PATH_TO_WATCH):

            # ! File origine
            src = os.path.join(PATH_TO_WATCH, filename)

            # ! File Destinazione
            new_destination = os.path.join(PATH_TO_PUT, filename)

            print(f"Origine : {src}      Destinazione : {new_destination}")

            # ! lo muovo
            os.rename(src, new_destination)


# ! Creo l' "handler"
event_handler = MyHandler()

# ! Creo l' oggetto "osservatore" ...
observer = Observer()

# ! ... e gli associo l' "handler" sopra creato, passandogli la "dir da guardare"
observer.schedule(event_handler, PATH_TO_WATCH, recursive=False)    # ! True -> anche le sottodir.

# ! Avvio l' "osservatore"
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()    # ! per finire tutto
