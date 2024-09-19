'''
Task: Write a Python script that takes a MAC address in any format (e.g., 00-1B-63-84-45-E6, 00:1B:63:84:45:E6, 
or 001B.6384.45E6) and normalizes it to the format 00:1B:63:84:45:E6.
Sample Output:
Enter MAC address: 00-1B-63-84-45-E6
Normalized MAC: 00:1B:63:84:45:E6
'''
import re

def normalize_mac(mac_address):
    pattern = r"[^0-9A-Fa-f]" 
    # match anything that doesn't matches 0-9, A-F or a-f and replace it with empty string
    clean_mac = re.sub(pattern, '', mac_address)
    if len(clean_mac) != 12: 
        return "Invaling MAC"
    else:
        clean_mac_list = []
        for i in range(0, 12, 2):
            clean_mac_list.append(clean_mac[i:i+2])
    normalize_mac_address = ':'.join(clean_mac_list)
    return normalize_mac_address

if __name__ == "__main__":
    mac_address = input("Enter MAC address: ")
    normalize_mac_address = normalize_mac(mac_address)
    print(normalize_mac_address)