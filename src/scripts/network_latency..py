'''
Task: Write a Python script that pings a list of devices and calculates their average 
latency over a given number of pings.
Sample Output:
Enter device IPs (comma-separated): 192.168.1.1,192.168.1.2
Pinging each device 4 times…
192.168.1.1 average latency: 5ms
192.168.1.2 average latency: 8ms
'''

import subprocess
import re


def ping_output(ip, count=4):
    try:
        output = subprocess.check_output(["ping", "-c", str(count), ip], text=True)
    except Exception as e:
        return False
    else:
        return output


def average_latency(output):
    pattern = r"time=(\d+\.?\d*) ms"
    latency_list = re.findall(pattern, output)
    avg_latency = sum(list(map(float, latency_list))) / len(latency_list)
    return round(avg_latency, 3)


if __name__ == "__main__":
    ip_list = input().replace(' ', '').split(',')
    for ip in ip_list:
        output = ping_output(ip)
        if output:
            latency = average_latency(output)
            print(f"Average latency towards IP {ip} = {latency} ms")
        else:
            print(f"{ip} is not reachable")
    