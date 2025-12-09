# code for information gathering

import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

try:
    # Fetch headers of the URL
    req = requests.get("https://" + sys.argv[1])
    print("\nHeaders:\n" + str(req.headers))
except requests.RequestException as e:
    print("Failed to retrieve headers:", e)
    sys.exit(1)

try:
    # Get the IP address of the host
    gethostby_ = socket.gethostbyname(sys.argv[1])
    print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby_ + "\n")
except socket.gaierror as e:
    print("Failed to get IP address:", e)
    sys.exit(1)

try:
    # Fetch IP information from ipinfo.io
    req_two = requests.get("http://ipinfo.io/" + gethostby_ + "/json")
    resp_ = req_two.json()  # Directly parse JSON response

    # Display location and region information
    print("Location: " + resp_.get("loc", "N/A"))
    print("Region: " + resp_.get("region", "N/A"))
    print("Country: " + resp_.get("country", "N/A"))
except requests.RequestException as e:
    print("Failed to retrieve IP information:", e)
except json.JSONDecodeError:
    print("Failed to parse JSON response.")
