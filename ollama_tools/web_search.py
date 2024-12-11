"""
Web Search Module
Provides functions for web searching and HTML to Markdown conversion
and for returning the contents of a URI as plain text (with minimal markdown)
"""

from typing import Dict, Any
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import html

def uri_to_markdown(a_uri: str) -> Dict[str, Any]:
  """
  Fetches content from a URI and converts HTML to markdown-style text

  Args:
      a_uri (str): URI to fetch and convert

  Returns:
      web page text converted converted markdown content
  """
  try:
      # Validate URI
      parsed = urlparse(a_uri)
      if not all([parsed.scheme, parsed.netloc]):
          return f"Invalid URI: {a_uri}"

      # Fetch content
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
      response = requests.get(a_uri, headers=headers, timeout=10)
      response.raise_for_status()

      # Parse HTML
      soup = BeautifulSoup(response.text, 'html.parser')

      # Get title
      title = soup.title.string if soup.title else ''

      # Remove script and style elements
      for element in soup(['script', 'style', 'head']):
          element.decompose()

      # Convert headers
      for i in range(1, 7):
          for header in soup.find_all(f'h{i}'):
              header_text = header.get_text().strip()
              header.replace_with(f"{'#' * i} {header_text}\n\n")

      # Process paragraphs and line breaks
      for p in soup.find_all('p'):
          p.replace_with(f"\n{p.get_text().strip()}\n")

      for br in soup.find_all('br'):
          br.replace_with('\n')

      # Get text and clean up
      text = soup.get_text()

      # Clean up the text
      text = re.sub(r'\n\s*\n', '\n\n', text)  # Remove multiple blank lines
      text = re.sub(r' +', ' ', text)  # Remove multiple spaces
      text = html.unescape(text)  # Convert HTML entities
      text = text.strip()

      return f"Contents of URI {a_uri} is:\n{text}\n"

  except requests.RequestException as e:
      return f"Network error: {str(e)}"

  except Exception as e:
      return f"Error processing URI: {str(e)}"


def search_web(query: str, max_results: int = 5) -> Dict[str, Any]:
  """
  Performs a web search and returns results
  Note: This is a placeholder. Implement with your preferred search API.

  Args:
      query (str): Search query
      max_results (int): Maximum number of results to return

  Returns:
      Dict[str, Any]: Dictionary containing:
          - 'results': List of search results
          - 'count': Number of results found
          - 'error': Error message if any, None otherwise
  """
  # Placeholder for search implementation
  return {
      'results': [],
      'count': 0,
      'error': 'Web search not implemented. Please implement with your preferred search API.'
  }

# Function metadata for Ollama integration
uri_to_markdown.metadata = {
  'name': 'uri_to_markdown',
  'description': 'Converts web page content to markdown-style text',
  'parameters': {
      'a_uri': 'URI of the web page to convert'
  }
}

search_web.metadata = {
  'name': 'search_web',
  'description': 'Performs a web search and returns results',
  'parameters': {
      'query': 'Search query',
      'max_results': 'Maximum number of results to return'
  }
}

# Export the functions
__all__ = ['uri_to_markdown', 'search_web']


