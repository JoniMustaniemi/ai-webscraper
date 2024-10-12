import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
)
from parse import parse_with_ollama


# Scraping logic.
def scrape_and_display_content(url):
    # Show progress message
    st.write("Scraping the website...")

    # Scrape the website and process the result.
    raw_html = scrape_website(url)
    body_content = extract_body_content(raw_html)
    cleaned_content = clean_body_content(body_content)

    # Store the cleaned content in session state.
    st.session_state["cleaned_dom_content"] = cleaned_content

    # Display the cleaned content in an expander.
    with st.expander("View Scraped DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)


# Parsing logic.
def parse_dom_content(parse_description):
    st.write("Parsing the content...")

    # Split the DOM content into manageable chunks.
    dom_chunks = split_dom_content(st.session_state["cleaned_dom_content"])

    # Perform parsing using the specified description.
    parsed_result = parse_with_ollama(dom_chunks, parse_description)

    # Display the parsed result.
    st.write(parsed_result)


# Title.
st.title("AI Web Scraper")

# Input for website URL.
url = st.text_input("Enter a Website URL:")

# Scrape site button logic.
if st.button("Scrape Site"):
    if url:
        scrape_and_display_content(url)
    else:
        st.error("Please enter a valid URL.")

# Display parsing options if content has been scraped.
if "cleaned_dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want me to do with the data: ")

    if st.button("Parse Content"):
        if parse_description:
            parse_dom_content(parse_description)
        else:
            st.error("Please enter a description for parsing.")
