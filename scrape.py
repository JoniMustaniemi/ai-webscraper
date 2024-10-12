import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup


def scrape_website(website):
    """
    Scrapes the HTML content of the specified website.

    Args:
        website (str): The URL of the website to scrape.

    Returns:
        str: The HTML content of the website.
    """
    print("Launching Chrome browser...")

    # Path to the ChromeDriver executable.
    chrome_driver_path = "./chromedriver.exe"

    # Chrome browser options.
    options = webdriver.ChromeOptions()

    # Create a Chrome driver instance with the specified service and options.
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # Navigate to the given website URL and wait for it to load.
        driver.get(website)
        time.sleep(5)  # Adjust the sleep time as necessary for page load
        print("Page loaded successfully.")

        # Return the HTML content of the loaded webpage.
        return driver.page_source
    except Exception as e:
        print(f"An error occurred while scraping the website: {e}")
        return ""
    finally:
        driver.quit()  # Ensure the driver quits regardless of success or failure


def extract_body_content(html_content):
    """
    Extracts the body content from the provided HTML.

    Args:
        html_content (str): The HTML content to parse.

    Returns:
        str: The extracted body content or an empty string if not found.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body

    return str(body_content) if body_content else ""


def clean_body_content(body_content):
    """
    Cleans the extracted body content by removing scripts and styles.

    Args:
        body_content (str): The body content to clean.

    Returns:
        str: The cleaned text content without scripts and styles.
    """
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove script and style elements.
    for element in soup(["script", "style"]):
        element.extract()

    # Get cleaned text content, stripping excess whitespace.
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    """
    Splits the DOM content into manageable chunks.

    Args:
        dom_content (str): The content to split.
        max_length (int): The maximum length of each chunk.

    Returns:
        list of str: A list of content chunks.
    """
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
