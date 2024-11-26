"""
Example script demonstrating the usage of LLM tools
"""

from ollama_tools import *

from ollama_tools.file_contents import read_file_contents, write_file_contents
from ollama_tools.file_dir import list_directory
from ollama_tools.web_search import uri_to_markdown

def separator(title: str):
  """Prints a section separator"""
  print(f"\n{'='*50}")
  print(f" {title}")
  print('='*50)

def main():
  # Test file writing
  separator("Testing File Writing")
  test_content = """Hello, this is a test file!
It contains multiple lines
And some example content.
"""

  write_result = write_file_contents("test123.txt", test_content)
  if write_result['success']:
      print(f"Successfully wrote {write_result['bytes_written']} bytes to test123.txt")
  else:
      print(f"Error writing file: {write_result['error']}")

  # Test file reading
  separator("Testing File Reading")
  read_result = read_file_contents("test123.txt")
  if read_result['error'] is None:
      print(f"File size: {read_result['size']} bytes")
      print("Content:")
      print(read_result['content'])
  else:
      print(f"Error reading file: {read_result['error']}")

  # Test directory listing
  separator("Testing Directory Listing")
  dir_result = list_directory()
  if dir_result['error'] is None:
      print(f"Current directory: {dir_result['current_dir']}")
      print(f"Found {dir_result['count']} files:")
      for file in dir_result['files']:
          print(f"  - {file}")
  else:
      print(f"Error listing directory: {dir_result['error']}")

  # Test Python files only
  separator("Testing Python Files Listing")
  py_files = list_directory("*.py")
  if py_files['error'] is None:
      print(f"Found {py_files['count']} Python files:")
      for file in py_files['files']:
          print(f"  - {file}")
  else:
      print(f"Error listing Python files: {py_files['error']}")

  # Test URI to Markdown conversion
  separator("Testing URI to Markdown Conversion")
  uri = "https://example.com"
  print(f"Converting {uri} to markdown...")
  md_result = uri_to_markdown(uri)
  if md_result['error'] is None:
      print(f"Title: {md_result['title']}")
      print("\nContent preview (first 500 chars):")
      print(md_result['content'][:500] + "...")
  else:
      print(f"Error converting URI: {md_result['error']}")

if __name__ == "__main__":
  try:
      main()
  except Exception as e:
      print(f"An error occurred: {str(e)}")

