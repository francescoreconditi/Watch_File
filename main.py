#
# fff Import
#

import os
import pathlib
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from py.xml_distinta import check_xml_distinta

#
# fff Costanti
#

STRUCT_XML: str = "_05806_"

CHECK_PATH = "c:\\temp\\origine"
XML_PATH = "c:\\temp\\origine\\xml"
GARBAGE_PATH = "c:\\temp\\origine\\garbage"

#
# fff Flusso
#


class MyHandler(FileSystemEventHandler):

    # ! La funzione sotto "scatta" quando viene modificato (quindi anche "creato") un file nella
    # ! directory "che deve tenere d' occhio"
    def on_modified(self, event):

        for filename in os.listdir(CHECK_PATH):

            # ! Path completo
            src = os.path.join(CHECK_PATH, filename)

            # ! Scarto le directory
            if pathlib.Path(src).is_dir():
                continue

            # ! Controllo se e' un ".xml", e se contiene la stringa STRUCT_XML
            file_extension = pathlib.Path(filename).suffix

            if (file_extension.upper() == ".XML") and (STRUCT_XML in filename):

                # ! Determinazione file origine e di destinazione
                dest = os.path.join(XML_PATH, filename)

                # ! lo muovo
                os.rename(src, dest)

                # ! Lo "analizzo"
                check_xml_distinta(dest)
            else:
                # ! Lo metto da un' altra parte
                dest = os.path.join(GARBAGE_PATH, filename)

                # ! lo muovo
                os.rename(src, dest)


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
