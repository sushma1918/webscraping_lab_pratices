"""
generic_web_scraper.py

This module provides functions to perform web scraping on any given URL using the Requests library.
It demonstrates fetching the following information:
- HTML content (text)
- URL of the request
- HTTP status code
- Cookies
- Elapsed time for the request
- HTTP headers and their items

Functions:
- get_text(url)
- get_url(url)
- get_status_code(url)
- get_cookies(url)
- get_elapsed_time(url)
- get_headers(url)
- get_header_items(url)
- get_header_keys(url)
- get_header_key_value(url)

Author: Sushma Sharma
"""

import requests


def get_text(url):
    """
    Fetches the HTML content (text) of the given webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The HTML content of the webpage.
    """
    response = requests.get(url)
    return response.text

def get_url(url):
    """
    Fetches the URL of the request.

    Args:
        url (str): The URL of the webpage to request.

    Returns:
        str: The URL of the request.
    """
    response = requests.get(url)
    return response.url

def get_status_code(url):
    """
    Fetches the HTTP status code of the request.

    Args:
        url (str): The URL of the webpage to request.

    Returns:
        int: The HTTP status code of the request.
    """
    response = requests.get(url)
    return response.status_code

def get_cookies(url):
    """
    Fetches the cookies set by the server.

    Args:
        url (str): The URL of the webpage to request.

    Returns:
        RequestsCookieJar: Cookies returned by the server.
    """
    try:
        response = requests.get(url)
        return response.cookies
    except Exception as e:
        print(f"Error: {e}")
        return None     

def get_elapsed_time(url):
    """
    Fetches the time taken for the request.

    Args:
        url (str): The URL of the webpage to request.

    Returns:
        timedelta: Time taken to complete the request.
    """
    response = requests.get(url)
    return response.elapsed

def get_headers(url):
    """
    Fetches the HTTP headers of the response.

    Args:
        url (str): The URL of the webpage to request.

    Returns:
        dict: HTTP headers of the response.
    """
    response = requests.get(url)
    return response.headers

def get_header_items(url):
    """
    Fetches the HTTP header items as key-value pairs.

    Args:
        url (str): The URL of the webpage to request.

    Returns:
        list: List of key-value pairs of header items.
    """
    response = requests.get(url)
    return list(response.headers.items())

def get_header_keys(url):
    """
    Gets all the HTTP header keys from the response.

    Args:
        url (str): The URL of the webpage to request.

    Returns:
        list: List of header keys.
    """
    response = requests.get(url)
    return list(response.headers.keys())

def get_header_key_value(url):
    """
    Gets all HTTP header key-value pairs from the response.

    Args:
        url (str): The URL of the webpage to request.

    Returns:
        dict: Dictionary of key-value pairs of headers.
    """
    response = requests.get(url)
    return dict(response.headers.items())

# if __name__ == "__main__":
#     test_url = input("Enter the URL to scrape: ")

#     print("\n=== Fetching Text ===")
#     print(get_text(test_url))
    
#     print("\n=== Fetching URL ===")
#     print(get_url(test_url))
    
#     print("\n=== Fetching Status Code ===")
#     print(get_status_code(test_url))
    
#     print("\n=== Fetching Cookies ===")
#     print(get_cookies(test_url))
    
#     print("\n=== Fetching Elapsed Time ===")
#     print(get_elapsed_time(test_url))
    
#     print("\n=== Fetching Headers ===")
#     print(get_headers(test_url))
    
#     print("\n=== Fetching Header Items ===")
#     print(get_header_items(test_url))
    
#     print("\n=== Fetching Header Keys ===")
#     print(get_header_keys(test_url))
    
#     print("\n=== Fetching Header Key-Value Pairs ===")
#     print(get_header_key_value(test_url))
