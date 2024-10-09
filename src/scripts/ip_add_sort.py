"""
Task:Given a list of IP addresses, sort them by their numerical value.
Sample Input: 
['192.168.1.3', '10.0.0.10', '172.16.0.0', '192.168.0.100']
Sample Output:
['10.0.0.1', '172.16.0.1', '192.168.0.100', '192.168.1.1']
"""

import ipaddress

def sort_ip_address(ip_list):
    '''
    Will take a ip_list and sort it out based on the integer value of the ip address
    '''
    sorted_ip_addresses = sorted(ip_list, key=lambda ip: int(ipaddress.IPv4Address(ip)))
    return sorted_ip_addresses


def sort_ip_last_octect(ip_list):
    '''
    Will take a ip_list and sort it out based on last octet value of the ip address
    '''
    sorted_ip_last_octet = sorted(ip_list, key=lambda ip: int(ip.split('.')[-1]))
    return sorted_ip_last_octet

if __name__ == '__main__':
    ip_addresses = ['192.168.1.3', '10.0.0.10', '172.16.0.0', '192.168.0.100']
    sorted_ips = sort_ip_address(ip_addresses)
    last_octet_sorted_ips = sort_ip_last_octect(ip_addresses)
    print(sorted_ips)
    print(last_octet_sorted_ips)