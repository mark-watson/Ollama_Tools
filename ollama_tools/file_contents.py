"""
File Contents Module
Provides functions for reading and writing file contents with proper error handling
"""

from typing import Optional, Dict, Any
from pathlib import Path
import json

def read_file_contents(file_path: str, encoding: str = 'utf-8') -> Dict[str, Any]:
  """
  Reads contents from a file and returns them along with metadata

  Args:
      file_path (str): Path to the file to read
      encoding (str): File encoding to use (default: utf-8)

  Returns:
      Dict[str, Any]: Dictionary containing:
          - 'content': File contents as string
          - 'size': File size in bytes
          - 'exists': Boolean indicating if file exists
          - 'error': Error message if any, None otherwise
  """
  try:
      path = Path(file_path)
      if not path.exists():
          return {
              'content': None,
              'size': 0,
              'exists': False,
              'error': f"File not found: {file_path}"
          }

      with path.open('r', encoding=encoding) as f:
          content = f.read()

      return {
          'content': content,
          'size': path.stat().st_size,
          'exists': True,
          'error': None
      }

  except Exception as e:
      return {
          'content': None,
          'size': 0,
          'exists': True,
          'error': f"Error reading file: {str(e)}"
      }

def write_file_contents(
  file_path: str, 
  content: str, 
  encoding: str = 'utf-8', 
  mode: str = 'w'
) -> Dict[str, Any]:
  """
  Writes content to a file and returns operation status

  Args:
      file_path (str): Path to the file to write
      content (str): Content to write to the file
      encoding (str): File encoding to use (default: utf-8)
      mode (str): Write mode ('w' for write, 'a' for append)

  Returns:
      Dict[str, Any]: Dictionary containing:
          - 'success': Boolean indicating if write was successful
          - 'bytes_written': Number of bytes written
          - 'error': Error message if any, None otherwise
  """
  try:
      path = Path(file_path)

      # Create parent directories if they don't exist
      path.parent.mkdir(parents=True, exist_ok=True)

      with path.open(mode, encoding=encoding) as f:
          bytes_written = f.write(content)

      return {
          'success': True,
          'bytes_written': bytes_written,
          'error': None
      }

  except Exception as e:
      return {
          'success': False,
          'bytes_written': 0,
          'error': f"Error writing file: {str(e)}"
      }

# Function metadata for Ollama integration
read_file_contents.metadata = {
  'name': 'read_file_contents',
  'description': 'Reads contents from a file and returns them with metadata',
  'parameters': {
      'file_path': 'Path to the file to read',
      'encoding': 'File encoding (default: utf-8)'
  }
}

write_file_contents.metadata = {
  'name': 'write_file_contents',
  'description': 'Writes content to a file and returns operation status',
  'parameters': {
      'file_path': 'Path to the file to write',
      'content': 'Content to write to the file',
      'encoding': 'File encoding (default: utf-8)',
      'mode': 'Write mode ("w" for write, "a" for append)'
  }
}

# Export the functions
__all__ = ['read_file_contents', 'write_file_contents']

