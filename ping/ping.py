
import os
import sys

def ping(host):
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        print(f"{host} is up!")
    else:
        print(f"{host} is down!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping.py <hostname>")
    else:
        ping(sys.argv[1])
