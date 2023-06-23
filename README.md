# Bitcoin Whitepages Web Scraper

## Summary of Skills and Concepts

* Use of Python Virtual Environment (venv)
* Use of pip and setuptools
* Package handling with requirements.txt
* Git and GitHub for version control and collaboration
* Gitignore implementation
* Web scraping with BeautifulSoup4, requests and lxml
* Data manipulation and export to CSV file
* Type hinting in Python
* Exception handling in Python with try-except blocks
* CSV data manipulation using \t as a delimiter

## Introduction

This project demonstrates the application of various Python programming, data scraping and data manipulation concepts. A web scraper has been developed to fetch headings from the Bitcoin Whitepages on bitcoin.com. The data is then written into a CSV file using \t as a delimiter.

## Setup and Installation

The project utilizes a Python virtual environment (venv), which isolates the Python interpreter and installed packages for the project. 

The `venv` is not tracked by Git due to an entry in the `.gitignore` file. However, a `requirements.txt` file was created using `pip freeze` in the virtual environment. This file lists all the Python packages used in the project and their versions, and it's tracked by Git. You can use this file to set up your own Python virtual environment with the required packages.

Here are the steps to setup and run the project:

1. Clone the repository.
```bash
git clone <repository_url>
```
2. Set up the Python virtual environment. Replace `<path_to_venv>` with your chosen directory.
```bash
python3 -m venv <path_to_venv>
```
3. Activate the virtual environment.
```bash
# Windows
<path_to_venv>\Scripts\activate

# Unix or MacOS
source <path_to_venv>/bin/activate
```
4. Install the required packages using pip and the provided `requirements.txt` file.
```bash
pip install -r requirements.txt
```
5. Run the Python script.
```bash
python <script_name.py>
```

## Web Scraper

The web scraper utilizes `requests` to make HTTP requests to bitcoin.com, `BeautifulSoup4` for parsing HTML and XML documents and `lxml` as the parser for BeautifulSoup4. 

This project makes good use of type hinting, ensuring that functions are used correctly and helping to prevent bugs. It also contains try-except blocks, demonstrating proper error handling.

## CSV File Creation

The scraped data is written to a CSV file using \t as a delimiter, demonstrating data manipulation and file handling in Python.

## Conclusion

This project showcases a range of important skills, from setting up isolated Python environments and using Git for version control, to web scraping and handling data in CSV format. It demonstrates good Python coding practices like type hinting and exception handling, making the code more robust and easier to maintain.

## Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

