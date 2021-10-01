import sys

# Colors will not be diplayed in windows or macOS machines
colors = True
platf = sys.platform
if platf.lower().startswith(("os", "win", "darwin","ios")): 
    colors = False

if not colors:
	red = white = reset = yellow = ""

else:                                                 
    white = "\033[97m"
    red = "\033[31;1m"
    yellow = "\033[93m"
    reset = "\033[0m"
