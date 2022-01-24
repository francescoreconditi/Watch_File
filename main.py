#
# fff Import
#

import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#
# fff Costanti
#

CHECK_PATH = "c:\\temp\\origine"
DEST_PATH = "c:\\temp\\destinazione"

#
# fff Flusso
#


class MyHandler(FileSystemEventHandler):

    # ! La funzione sotto "scatta" quando viene modificato (quindi anche "creato") un file nella
    # ! directory "che deve tenere d' occhio"
    def on_modified(self, event):

        for filename in os.listdir(CHECK_PATH):

            # ! File origine
            src = os.path.join(CHECK_PATH, filename)

            # ! File Destinazione
            new_destination = os.path.join(DEST_PATH, filename)

            print(f"Origine : {src}   ->    Destinazione : {new_destination}")

            # ! lo muovo
            os.rename(src, new_destination)


if __name__ == "__main__":
    # ! Creo l' "handler"
    event_handler = MyHandler()

    # ! Creo l' oggetto "osservatore" ...
    observer = Observer()

    # ! ... e gli associo l' "handler" sopra creato, passandogli la "dir da guardare"
    observer.schedule(event_handler, CHECK_PATH, recursive=False)    # ! True -> anche le sottodir.

    # ! Avvio l' "osservatore"
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()    # ! per finire tutto
