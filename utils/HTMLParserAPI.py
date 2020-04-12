# We import requests to perform requests to urls and get the HTML
import requests
# We import BeautifulSoup to parse the result of requests as HTML
from bs4 import BeautifulSoup
# We import webdriver to get the source code of the page to parse it
import selenium.webdriver as webdriver


def get_from_url(url: str) -> BeautifulSoup:
    """
    This methods uses the parameter 'url' to make a request using 'requests', gets the text and parses that string
    to parse as a HTML
    :param url: A string that contains the URL of the page where we want to parse its HTML
    :return: BeautifulSoup object that contains the HTML parser
    """
    # We use our url to make a request
    req = requests.get(url)
    # If the request was granted (code 200)
    if req.status_code == 200:
        # We use BeautifulSoup to parse the html of our request
        html = BeautifulSoup(req.text, "html.parser")
        # We return our BeautifulSoup html parser
        return html
    else:
        raise Exception("Request status code was not 200, so it was not returned correctly")


def get_from_web_driver(driver: webdriver) -> BeautifulSoup:
    """
    This method use the instance of webdriver we were using to perform automatic tests, gets the source code
    of the current page and parses it as HTML and returns the BeautifulSoup object for this parser
    :param driver: Webdriver from which we will get the source code
    :return: BeautifulSoup object that contains our HTML parser
    """
    # We get the source code of the current page we are automating with webdriver
    source = driver.page_source
    # We use BeautifulSoup to parse our HTML source code that is a string as HTML code
    html = BeautifulSoup(source, "html.parser")
    # We return this HTML parser (which is a BeautifulSoup object)
    return html
