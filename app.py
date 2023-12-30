from flask import Flask, Response, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

def scrape_user_agents():
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Open the website
    url = "https://www.useragents.me/"
    driver.get(url)

    # Wait for the content to load
    driver.implicitly_wait(5)

    # Get the page source
    page_source = driver.page_source

    # Close the WebDriver
    driver.quit()

    # Parse the HTML content
    soup = BeautifulSoup(page_source, "html.parser")

    # Extract user agents data
    user_agents = []
    table_rows = soup.select("tbody tr")
    for row in table_rows:
        if "Check out smartproxy’s residential rotating proxy servers." in row.text:
            continue  # Skip this entry
        columns = row.find_all("td")
        share = columns[0].text.strip()
        if len(columns) > 1:
            os_browser = columns[1].text.strip()
        else:
            # Handle the case where columns doesn't have enough elements
            os_browser = "N/A"
            # Or raise an exception, log an error, or take appropriate action

        if len(columns) > 2:
            user_agent_element = columns[2].select_one(".ua-textarea")

        if user_agent_element:
            user_agent = user_agent_element.text.strip()
        else:
            # Handle the case where the element with class ".ua-textarea" is not found
            user_agent = "N/A"
            # Or raise an exception, log an error, or take appropriate action


        user_agents.append({"share": share, "os_browser": os_browser, "user_agent": user_agent})

    return user_agents

@app.route('/json')
def json_route():
    # Scrape user agents
    user_agents = scrape_user_agents()

    # Return user agents data in JSON format
    return jsonify(user_agents)

@app.route('/tsv')
def tsv_route():
    # Scrape user agents
    user_agents = scrape_user_agents()

    # Convert user agents data to TSV format
    tsv_data = "\t".join(["share", "os_browser", "user_agent"]) + "\n"
    for ua in user_agents:
        tsv_data += "\t".join([ua["share"], ua["os_browser"], ua["user_agent"]]) + "\n"

    # Return TSV data with proper response headers
    response = Response(tsv_data, content_type='text/tsv')
    response.headers['Content-Disposition'] = 'attachment; filename=Desktop_user_agents.tsv'
    return response

if __name__ == '__main__':
    app.run(debug=True)