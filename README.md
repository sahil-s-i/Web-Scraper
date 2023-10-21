# Web-Scraper

Web Scraper is a basic Python web scraping script designed to extract product data from Amazon India. This project is intended for educational purposes and should be used responsibly while respecting Amazon's policies and terms of service.

## Contents

- [Important Note](#important-note)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [References](#references)

## Important Note
- **Rotating Proxies Recommended**: This script uses a local IP address for scraping. To avoid the risk of getting blocked by Amazon, it's highly recommended to use rotating proxies. Continuous scraping from a single IP address can lead to IP blocking.

- **Amazon URL**: The script is configured to scrape data from Amazon India. If you wish to scrape data from a different Amazon website, you can easily modify the URL in the code.

- **Basic Web Scraping:** Please note that this script is a very basic web scraping code. It provides a foundation for web scraping, and users are encouraged to explore and advance their web scraping skills for more complex projects.

- **Respect Website Policies:** Always ensure that your web scraping activities adhere to the policies and terms of service of the target website. Ethical and responsible scraping is essential.

## Prerequisites

Before using this script, ensure you have the following dependencies installed:

- Python 3
- Python libraries: requests, BeautifulSoup, pandas

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## Getting Started

1. Clone this repository to your local machine:
``` bash
git clone https://github.com/sahil-s-i/Web-Scraper.git
cd Web-Scraper
```
2. Run the script:
``` bash
python3 main.py
```

## Usage

- This script is designed to scrape product data from the Amazon India website.
- It adheres to Amazon's robots.txt guidelines and respects the terms of service.
- Customize the script to suit your specific scraping needs.

## Disclaimer
- This script is intended for educational and research purposes.
- Ensure that your use of this script complies with Amazon's policies and legal requirements.
- Use this code responsibly and ethically.

## References

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Documentation](https://docs.python.org/3/)
- [Oxylabs Proxies](https://oxylabs.io/)

