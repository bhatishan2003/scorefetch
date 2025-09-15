import requests
from bs4 import BeautifulSoup

# The URL you want to scrape
url = "https://www.cricbuzz.com/cricket-match/live-scores"

# Send a GET request to the URL
try:
    response = requests.get(url)
    # Check if the request was successful
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print the prettified HTML for readability
    print(soup.prettify())

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")