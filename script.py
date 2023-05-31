import requests
from bs4 import BeautifulSoup

def extract_tags(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting Global Site Tag (gtag.js)
    global_site_tag = soup.find_all('script', {'src':lambda x: x and 'gtag' in x})
    print("Global Site Tag (gtag.js):")
    for tag in global_site_tag:
        print(tag)

    # Extracting Google Analytics (analytics.js or ga.js)
    google_analytics = soup.find_all('script', {'src':lambda x: x and ('analytics.js' in x or 'ga.js' in x)})
    print("\nGoogle Analytics (analytics.js or ga.js):")
    for tag in google_analytics:
        print(tag)
        
    # Extracting Google Publisher Tag (googletag.js)
    google_publisher_tag = soup.find_all('script', {'src':lambda x: x and 'googletag' in x})
    print("\nGoogle Publisher Tag (googletag.js):")
    for tag in google_publisher_tag:
        print(tag)

    # Extracting Google Tag Manager (gtm.js)
    google_tag_manager = soup.find_all('script', {'src':lambda x: x and 'gtm.js' in x})
    print("\nGoogle Tag Manager (gtm.js):")
    for tag in google_tag_manager:
        print(tag)

    # Extracting Floodlight ID
    # Floodlight tags are usually embedded within a noscript tag or a script tag
    floodlight_id = soup.find_all(lambda tag:tag.name in ("noscript", "script") and 'fls.doubleclick.net' in str(tag))
    print("\nFloodlight ID:")
    for tag in floodlight_id:
        print(tag)

url = 'https://www.xda-developers.com/'
extract_tags(url)
