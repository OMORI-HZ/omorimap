# omorimap
iprange and check openports
*I do not guarantee that it will not be used for negative and illegal activities, and all responsibility for using this tool rests with the user*

Explanation:
scan_port function: Attempts to connect to a specified port on a given IP address using a TCP socket (socket.SOCK_STREAM). If the connection is successful (socket.connect() doesn't throw an error), it indicates that the port is open.

scan_ip_range function: Iterates through a range of IP addresses (using generate_ip_range) and checks if the specified port is open on each IP address by calling scan_port. It collects and returns a list of IP addresses where the port is open.

generate_ip_range function: Generates a list of IP addresses between a starting and ending IP address, similar to the previous example.

Example Usage: Demonstrates how to use scan_ip_range to scan a range of IP addresses (start_ip to end_ip) on a specific port (port_to_scan).

Notes:
This example uses a timeout of 1 second (sock.settimeout(1)) for the socket connection. You can adjust this value based on your requirements.
Error handling in this example is minimal. In a production environment, you might want to add more robust error handling and logging.
For scanning larger IP ranges or multiple ports, consider threading or asynchronous programming to improve performance.

pls star and follow for more🎆
🤍🩶💛🤎💜🩵💙💚🧡🩷❤️🖤
