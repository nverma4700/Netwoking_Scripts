'''
Task: Write a Python script that extracts the Autonomous System (AS) path from BGP output. 
The script should take a BGP output as input and extract the AS numbers.
Sample Output:
Enter BGP output: "AS path: 65001 65002 65003"
AS Numbers: [65001, 65002, 65003]
'''
import re

def as_path_extract(asn_str):
    as_path_pattern = re.compile(r"AS path:\s*([\d\s]+)")
    match = as_path_pattern.findall(asn_str)
    return match

if __name__ == "__main__":
    asn_str = "AS path: 65001 65002 65003"
    asn_list = as_path_extract(asn_str)
    print(asn_list)