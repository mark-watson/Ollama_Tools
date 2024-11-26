"""
File Directory Module
Provides functions for listing files in the current directory
"""

from typing import Dict, List, Any
from pathlib import Path
import os

def list_directory(pattern: str = "*") -> Dict[str, Any]:
  """
  Lists files and directories in the current working directory

  Args:
      pattern (str): Glob pattern for filtering files (default: "*")

  Returns:
      Dict[str, Any]: Dictionary containing:
          - 'files': List of file names
          - 'count': Number of files found
          - 'current_dir': Current working directory path
          - 'error': Error message if any, None otherwise
  """
  try:
      current_dir = Path.cwd()
      files = list(current_dir.glob(pattern))

      # Convert Path objects to strings and sort
      file_list = sorted([str(f.name) for f in files])

      return {
          'files': file_list,
          'count': len(file_list),
          'current_dir': str(current_dir),
          'error': None
      }

  except Exception as e:
      return {
          'files': [],
          'count': 0,
          'current_dir': str(Path.cwd()),
          'error': f"Error listing directory: {str(e)}"
      }

# Function metadata for Ollama integration
list_directory.metadata = {
  'name': 'list_directory',
  'description': 'Lists files and directories in the current working directory',
  'parameters': {
      'pattern': 'Glob pattern for filtering files (default: "*")'
  }
}

# Export the function
__all__ = ['list_directory']

