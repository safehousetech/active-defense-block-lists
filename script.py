import requests
import ipaddress
import json


def is_valid_ip(ip_str):
    try:  
        ip_obj = ipaddress.ip_address(ip_str) 
        return True  
    except ValueError:  
        pass
    return False

with open('input.json') as file_object:
    list_of_data = json.load(file_object)
    for data in list_of_data:
        URL = data['url']
        OUTPUT_FILE = data['file']
        resp = requests.get(URL)
        #print(resp.text)
        content = resp.text
        split_data_by_new_line = content.split("\n")
        #print(split_data_by_new_line)
        exception_list = ['127.0.0.1  localhost','::1  localhost']

        output_file = open(OUTPUT_FILE,'r')
        file_parsed = []
        is_comment = False
        for line in output_file.readlines():
            if is_valid_ip(line.split(' ')[0]) and (line[:-1] not in exception_list):
                break
            file_parsed.append(line[:-1])
        output_file.close()

        # URL Data parsing logic
        url_parsed = []
        index = 0
        for x in split_data_by_new_line:
            if x=='':
                pass
            else:
                if '#'==x[0]:
                    pass
                else:
                    url_parsed.append(x)


        output_file = open(OUTPUT_FILE,"w")
        file_parsed.extend(url_parsed)
        for block in file_parsed:
                    output_file.write(block+"\n")
        output_file.close()
