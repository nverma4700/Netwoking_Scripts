"""
Task: Write a Python script that validates whether a given IP address is valid (IPv4 format). 
The script should check for proper structure and range (0-255 for each octet).
"""
import ipaddress
import re

#Way 1 --> using ipaddress module
def check_valid_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return f"{ip} is valid IP"
    except Exception as e: 
        return f"{ip} is invalid IP"
    

# Way 2 --> using regex
def validiate_ip_address(ip):
    '''
    First validiate if the number of octects in the IP address are correct
    '''
    octects = ip.split('.')
    if len(octects) != 4:
        return f'{ip} is an invalid IP'
    else: #Validate each octect:
        for octect in octects:
            if not octect.isdigit() or 0<=int(octect)<=255: 
                return f'{ip} is an invalid IP'
            elif len(octect) > 1 and octect[0] == "0":
                return f'{ip} is an invalid IP'
            else: 
                return f'{ip} is a valid IP'
            
                
if __name__ == '__main__':
    ip_list = ['192.168.300.3', '10.0.0.10', '172.260.0.0', '192.168.0.100']
    for ip in ip_list:
        print(validiate_ip_address(ip))