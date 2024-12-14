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
    print("=" * 50)


def main():
    # Test file writing
    separator("Testing File Writing")
    test_content = """Hello, this is a test file!
It contains multiple lines
And some example content.
"""

    write_result = write_file_contents("test123.txt", test_content)
    print(f"Write file test:  {write_result}")

    # Test file reading
    separator("Testing File Reading")
    read_result = read_file_contents("test123.txt")
    print(f"Read file result: {read_result}")

    # Test directory listing
    separator("Testing Directory Listing")
    dir_result = list_directory()
    print(f"Results reading current directory: {dir_result}")

    # Test Python files only
    separator("Testing Python Files Listing")
    py_files = list_directory("*.py")
    print(f"Results listing Python file in current directory: {py_files}")

    # Test URI to Markdown conversion
    separator("Testing URI to Markdown Conversion")
    uri = "https://example.com"
    print(f"Converting {uri} to markdown...")
    md_result = uri_to_markdown(uri)
    print(f"Result of URI to markdown:\n{md_result}")


if __name__ == "__main__":
    main()
