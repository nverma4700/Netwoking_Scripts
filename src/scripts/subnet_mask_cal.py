'''
Task: Write a Python script that takes a CIDR notation (e.g., /24) ]
as input and outputs the corresponding subnet mask.
'''
import ipaddress

def cidr_to_netmak(cidr):
    try:
        # Create IPv4 network object using CIDR notation
        network = ipaddress.IPv4Network(f"0.0.0.0/{cidr}", strict=False)
        return network.netmask # Extract subnet mask
    except Exception as e:
        return "Invalid CIDR"
    
if __name__ == "__main__":
    cidr = input("Enter CIDR notiation: ").strip('/')
    subnet_mask = cidr_to_netmak(cidr)
    print(f"Subnet mask for /{cidr}: {subnet_mask}")
    
     