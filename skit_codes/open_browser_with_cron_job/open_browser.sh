#!/bin/bash
# Set the display for the GUI applications
export DISPLAY=:0

# To know your system display numbe, run: `echo $DISPLAY`

# Navigate to directory where the script is:
cd /home/usman/Desktop

python3 -c "import webbrowser; webbrowser.open('https://www.google.nl/maps/search/saudia')"
python3 -c "import webbrowser; webbrowser.open('https://www.google.com/search?q=cloud computing')"

# Run python script
python3 /home/usman/Desktop/open_browser_with_cron_job/open_browser.py
