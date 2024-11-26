"""
LLM Tools Library
Provides a collection of utility functions for working with LLMs via Ollama
"""

from typing import List, Callable
from .file_contents import read_file_contents, write_file_contents
from .file_dir import list_directory, create_directory
from .Internet Access import search_web

def tools() -> List[Callable]:
  """
  Returns a list of available tool functions that can be used with Ollama

  Returns:
      List[Callable]: List of tool functions ready to use with Ollama
  """
  return [
      read_file_contents,
      write_file_contents,
      list_directory,
      create_directory,
      search_web
  ]

# Make commonly used functions available at package level
__all__ = [
  'read_file_contents',
  'write_file_contents', 
  'list_directory',
  'create_directory',
  'search_web',
  'tools'
]


