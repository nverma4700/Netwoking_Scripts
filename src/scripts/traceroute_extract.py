'''
Write a Python script that runs a traceroute command to a given IP address 
and extracts the path taken by the packets.
Sample Output:
Enter target IP address: 8.8.8.8 
Hop 1: 192.168.1.1 
Hop 2: 10.10.10.1 
Hop 3: 8.8.8.8
'''
import subprocess
import re

def extract_hop(output): # match the first element of everyline in traceroute output to get the hop number
    hop = re.match(r"\d", output)
    return hop.group()

def extract_ip(output): # search through each line of tracerout to get the IP address
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    ip = re.search(ip_pattern, output)
    return ip.group()

def tracroute_output(target):
    try:
        output = subprocess.check_output(["traceroute", target], text=True)
    except Exception:
        return False
    else:
        return output

if __name__ == "__main__":
    target = input("Enter the IP address: ")
    if not tracroute_output(target):
        print("Ip address is not valid")
    else:
        trace_output = tracroute_output(target)
    for output in trace_output.splitlines():
        hop = extract_hop(output)
        ip_info = extract_ip(output)
        if ip_info:
            ip = extract_ip(output)
        else:
            ip = "Unreachable"
        print(f"Hop{hop}: {ip}")

