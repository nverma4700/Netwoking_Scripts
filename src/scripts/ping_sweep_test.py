'''
Task: Create a Python script that performs a simple ping sweep over a given range 
of IP addresses and prints the reachable hosts.
'''

import os

def ping(ip):
    """
    Returns True if host (str) responds to a ping request.
    """
    response = os.system(f'ping -c 1 {ip}') # returns 0 for sucessful ping, else returns a number
    return response == 0 # bool logic 

def ping_ip_address(ip_list):
    reachable_ip = []
    for ip in ip_list:
        if ping(ip):
            reachable_ip.append(ip)
    return reachable_ip
            
if __name__ == "__main__":
    ip_addresses = [
        "8.8.8.8",  # Google DNS
        "192.168.1.1",  # Router IP
        "127.0.0.1",  # Localhost
        "10.255.255.1"  # Non-existent IP
    ]
    reachable_ips = ping_ip_address(ip_addresses)
    print(reachable_ips)