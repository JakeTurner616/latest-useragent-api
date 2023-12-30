# User Agent Scraper

Latest-useragent-api is a flask api that uses Selenium and BeautifulSoup to dynamically fetch the most up-to-date user agents from "https://www.useragents.me/" sorted by popularity. It offers two convenient routes for accessing the scraped data:

1. **JSON Route** (`/json`): Delivers the user agent data in JSON format as a response.
2. **TSV Route** (`/tsv`): Presents the user agent data in TSV (Tab-Separated Values) format as a direct download.

## Features

- Utilizes Selenium for navigating a headless Chrome browser, ensuring accurate and current user agent data.
- Sorts user agents by popularity, providing insights into commonly used configurations.
- Ignores entries containing the text "Check out smartproxy’s residential rotating proxy servers."
- Offers data retrieval in both JSON and downloadable TSV formats.

## Purpose

This user agent scraping api serves has the potential to serve a crucial purpose in the realm of web scraping and automated interactions with web servers. By retrieving the latest and most popular user agents from "https://www.useragents.me/", it provides a valuable resource for programs engaged in scraping activities that necessitate up-to-date user agents. Automated programs can utilize the latest user agents to avoid triggering basic bot detection mechanisms implemented by webservers. This proactive approach helps prevent the recording of anomalous patterns in browser usage, especially in scenarios where automated scraping pipelines may inadvertently use outdated or easily detectable user agents, thereby minimizing the risk of triggering primitive bot detection and ensuring a smoother interaction between automated systems and web servers.
