import socket

# ASCII art for the anonymous mask icon
ANONYMOUS_MASK = """
───▄█▌─▄─▄─▐█▄
───██▌▀▀▄▀▀▐██
───██▌─▄▄▄─▐██
───▀██▌▐█▌▐██▀
▄██████─▀─██████▄
GIT:DEV.OMORI
╔══╗▒▒▒▒▒▒╔═╗╔═╦═╗╔═╗╔═╗╔══╗
╚╗╗╠═╦═╦═╗║║║║║║║║║║║║╬║╚║║╝
╔╩╝║╩╬╗║╔╬╣║║║║║║║║║║║╗╣╔║║╗
╚══╩═╝╚═╝╚╩═╝╚╩═╩╝╚═╝╚╩╝╚══╝

"""
#discord:omoriam
#IRAN
def scan_port(ip, port):
    """
    Scan a specific port on an IP address.

    Args:
    - ip (str): IP address to scan
    - port (int): Port number to scan

    Returns:
    - bool: True if port is open, False otherwise
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout to 1 second
    try:
        sock.connect((ip, port))
        sock.close()
        return True
    except socket.error:
        return False

def scan_ip_range(start_ip, end_ip, port):
    """
    Scan a range of IP addresses on a specific port.

    Args:
    - start_ip (str): Starting IP address (e.g., '192.168.0.1')
    - end_ip (str): Ending IP address (e.g., '192.168.0.10')
    - port (int): Port number to scan

    Returns:
    - list: List of IP addresses where the specified port is open
    """
    ip_range = generate_ip_range(start_ip, end_ip)
    open_ips = []
    for ip in ip_range:
        if scan_port(ip, port):
            open_ips.append(ip)
            print(f"Port {port} is open on {ip}")
            print(ANONYMOUS_MASK)
    return open_ips

def generate_ip_range(start_ip, end_ip):
    """
    Generate IP addresses within a specified range.

    Args:
    - start_ip (str): Starting IP address (e.g., '192.168.0.1')
    - end_ip (str): Ending IP address (e.g., '192.168.0.10')

    Returns:
    - list: List of IP addresses as strings within the range
    """
    start = ip_to_int(start_ip)
    end = ip_to_int(end_ip)

    ip_range = []
    while start <= end:
        ip_range.append(int_to_ip(start))
        start += 1

    return ip_range

def ip_to_int(ip):
    parts = ip.split('.')
    return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])

def int_to_ip(num):
    return '.'.join([str((num >> 24) & 255), str((num >> 16) & 255), str((num >> 8) & 255), str(num & 255)])

# Example usage:
start_ip = '192.168.0.1'
end_ip = '192.168.0.10'
port_to_scan = 80

print(f"Scanning IP range from {start_ip} to {end_ip} on port {port_to_scan}:")
open_ips = scan_ip_range(start_ip, end_ip, port_to_scan)
print("Open IPs:", open_ips)
