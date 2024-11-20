import requests
import re
from bs4 import BeautifulSoup

url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs"

response = requests.get(url)
if response.status_code == 200:
    print("Its all good")
    content = response.text.splitlines()
    print(content)

search_time_start = "17/May/2015:10:05:03"

log_pattern = re.compile(
        r'(?P<ip>\S+) '                  # IP address
        r'\S+ \S+ '                      # Placeholder for two fields (usually '- -')
        r'\[(?P<timestamp>[^\]]+)\] '    # Timestamp inside square brackets
        r'"(?P<request>[^"]+)" '         # Request method and URL in quotes
        r'(?P<status>\d{3}) '            # Status code (3 digits)
        r'(?P<size>\S+)'                 # Size of the response
    )

    # Loop through each line and search for the timestamp
for line in content:
    if search_time_start in line:
        match = log_pattern.match(line)
        if match:
            log_data = match.groupdict()
                
            # Clean and print the output in a readable format
            print(f"IP Address: {log_data['ip']}")
            print(f"Timestamp: {log_data['timestamp']}")
            print(f"Request: {log_data['request']}")
            print(f"Status Code: {log_data['status']}")
            print(f"Size: {log_data['size']}")
            print("-" * 50)  # Separator for readability




# soup = BeautifulSoup(content, 'html.parser')
# links = soup.find_all("a")

# for link in links:
#     print(link.get("href"))

