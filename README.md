# Ai web scraper

## Overview

This project is designed to leverage the power of Streamlit, Langchain, Selenium, and BeautifulSoup to build a web application for data processing and visualization. The application uses advanced techniques for web scraping and natural language processing, enabling users to interact with data seamlessly.

## Features

- Web scraping capabilities using Selenium and BeautifulSoup.
- Natural Language Processing (NLP) functionalities powered by Langchain.
- User-friendly web interface built with Streamlit.
- Configurable environment settings via `.env` file.

## Requirements

This project requires the following Python packages:

- `streamlit`
- `langchain` 
- `langchain_ollama`
- `selenium`
- `beautifulsoup4`
- `lxml`
- `html5lib`
- `python-dotenv`
  
## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:JoniMustaniemi/ai-webscraper.git
   cd ai-webscraper
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   You can install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the packages individually:

   ```bash
   pip install streamlit langchain langchain_ollama selenium beautifulsoup4 lxml html5lib python-dotenv
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root directory and add your environment-specific variables.

   ```plaintext
   VARIABLE_NAME=value
   ANOTHER_VARIABLE_NAME=another_value
   ```

## Usage

To run the application, use the following command:

```bash
streamlit run main.py
```

