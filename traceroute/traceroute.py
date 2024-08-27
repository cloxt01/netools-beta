import subprocess
import sys

def traceroute(host):
    subprocess.call(["traceroute", host])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python traceroute.py <hostname>")
    else:
        traceroute(sys.argv[1])
