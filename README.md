
# Active Defense Block Lists

NOTE:

1.Thi Python scripts run automatically and download block lists form the internet and update on files .
2.We have configured github action to run cron job in every to hours to update the files and push the changes into github as blob commit .
3. we have creted json files to get url and files as reference 

## Tech Stack

Python
Github Action
Bash Script

## URL and Files input.json Color Reference

| URL            | FILES                                                                |
| ----------------- | ------------------------------------------------------------------ |
| https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt| adaway.txt |
| https://someonewhocares.org/hosts/hosts |someonewhocares.txt|
| https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts | StevenBlack.txt|
| https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds-Ultra.txt |GoodbyeAds.txt|
| https://block.energized.pro/blu/formats/domains.txt |energized.txt|
|https://github.com/d3ward/toolz/blob/master/src/d3host.txt||d3host.txt|
|https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt||ads-and-tracking-extended.txt|


## Installation

Install dependency 

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python3 script.py


## Deployment

To sync the changes from host to target 

```bash
  python3 script.py
```

