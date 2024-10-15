from crewai_tools import BaseTool
import requests
from bs4 import BeautifulSoup

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class Webscraper(BaseTool):
    
    name: str = "Webpage Scraper"
    description: str = """
    a tool to get all the content from a given webpage
    """

    def scrape_webpage(self, url):
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful

            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the webpage's textual content
            page_content = soup.get_text(separator="\n", strip=True)

            return page_content

        except requests.exceptions.RequestException as e:
            return f"An error occurred while fetching the webpage: {e}"



    def _run(self, url:str) -> str:
        return self.scrape_webpage(url)