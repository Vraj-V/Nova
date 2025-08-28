import eel
from backend.feature import *
from backend.command import *

# Play startup sound first
playAssistantSound()

# Point to the correct frontend folder (relative to main.py)
eel.init("front-end")

# Start eel (this will block the program)
eel.start(
    "index.html",
    mode="edge",
    host="localhost",
    block=True,
    port=5500,
    cmdline_args=["--app=http://localhost:5500/index.html"]
)
