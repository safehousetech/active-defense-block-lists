
# Active Defense Block Lists

NOTE:

1. main.py scripts run automatically ignore # and update localhost ip and url into target files 
2. cron job run in every 2 hours to update localhost ip and url into target files and push the changes into github 

## Variable that contains url and file of host and taget file that need to update 

| url            | file                                                                |
| ----------------- | ------------------------------------------------------------------ |
| https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt| adaway.txt |
| https://someonewhocares.org/hosts/hosts |someonewhocares.txt|
| https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts | StevenBlack.txt|
| https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds-Ultra.txt |GoodbyeAds.txt|
| https://block.energized.pro/blu/formats/domains.txt |energized.txt|
| https://github.com/d3ward/toolz/blob/master/src/d3host.txt |d3host.txt|
| https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt |ads-and-tracking-extended.txt|

## Installation Dependencies

Install Dependencies
#!/bin/bash
python -m venv .venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 main.py


