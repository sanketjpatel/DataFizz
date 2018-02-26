from bs4 import BeautifulSoup
from bookparser import set_details_from
import os

def extract(n):
    """Extract books from n HTML files. Returns list of books."""
    data_dir = os.environ.get('DATA_DIR')
    books = []
    for i in range(1, n+1):
        # Parse HTML file
        html_doc = open('%s/book%d.html' % (data_dir, i))
        parsed_html = BeautifulSoup(html_doc, 'html.parser')
        book = set_details_from(parsed_html)    # Dictionary with key, value pairs of book details
        books.append(book)                      # List of dictionaries. List of books
    return books
