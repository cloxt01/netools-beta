import socket
import sys

def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open")
        s.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <hostname> <start_port> <end_port>")
    else:
        scan_ports(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
