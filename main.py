import requests
import ipaddress
import json
conf=[
    {"url":"https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt","file":"adaway.txt"},
    {"url":"https://someonewhocares.org/hosts/hosts","file":"someonewhocares.txt"},
    {"url":"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts","file":"StevenBlack.txt"},
    {"url":"https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds-Ultra.txt","file":"GoodbyeAds.txt"},
    {"url":"https://block.energized.pro/blu/formats/domains.txt","file":"energized.txt"},
    {"url":"https://github.com/d3ward/toolz/blob/master/src/d3host.txt","file":"d3host.txt"},
    {"url":"https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt","file":"ads-and-tracking-extended.txt"} 
]

def is_valid_ip(ip_str):
    try:  
        return ipaddress.ip_address(ip_str)  
    except ValueError:  
        return False

for item in conf:
    url = item['url']
    output_file = item['file']
    resp = requests.get(url)
    content = resp.text
    exception_list = ['127.0.0.1  localhost','::1  localhost']
    file_parsed = []
    is_comment = False
    with open(output_file,'r') as file:
        for line in file.readlines():
            # first word of the line is an ip address or items not in exception list
            if is_valid_ip(line.split(' ')[0]) and (line[:-1] not in exception_list):
                break
            file_parsed.append(line[:-1])

    url_parsed = [l for l in content.split("\n") if l and not l.startswith("#")]

    with open(output_file,"w") as file:
        file_parsed.extend(url_parsed)
        for block in file_parsed:
            file.write(block+"\n")

