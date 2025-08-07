News-Headlines Scraper

1) Objective:

- Automate data collection from a public news website
- Extract and store top headlines (from `<h1>`, `<h2>`, and `<h3>` tags)
- Save the results to a local `.txt` file (`headlines.txt`)
2) Overview:The project can be broken down into the following steps:

- **Step 1** – Choose the news website (e.g., BBC News)
- **Step 2** – Fetch the HTML content from the selected website using `requests`
- **Step 3** – Parse the HTML using the `BeautifulSoup` library
- **Step 4** – Find all headline tags (`<h1>`, `<h2>`, `<h3>`)
- **Step 5** – Extract and clean the text from those tags
- **Step 6** – Save the extracted headlines into a `.txt` file (`headlines.txt`)
3) Tools & Technologies Used:

- **Python 3**
- [requests](https://pypi.org/project/requests/) – For sending HTTP requests
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) – For parsing and extracting data from HTML
4) Folder Structure:
  
    tasks3 Folder - Day 3 Folder - headlines.txt File - scrape_headlines.py File

  Notes:

- Make sure you have `requests` and `beautifulsoup4` installed:
  pip install requests beautifulsoup4
