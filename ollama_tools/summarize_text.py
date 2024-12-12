"""
Summarize text
"""

from typing import Optional, Dict, Any
from pathlib import Path
import json

from ollama import chat
from ollama import ChatResponse

def summarize_text(text: str, encoding: str = 'utf-8') -> str:
  """
  Summarizes text

  Args:
      text (str): text to summarize

  Returns:
      a string os summarized text
  """
  print(f"\n\n**** summarize input text:\n\n{text}\n\n")
  summary : ChatResponse = chat(
    model="llama3.2:latest",
    messages=[
        {"role": "system",
         "content":
         "You are an expert at summarizing an input string. The only thing you return is the summarized text."},
        {"role": "user", "content": text}
    ])
  return summary['message']['content']

# Function metadata for Ollama integration
summarize_text.metadata = {
  'name': 'summarize_text',
  'description': 'Summarizes input text',
  'parameters': {
    'text': 'string of text to summarize'
  }
}

# Export the functions
__all__ = ['summarize_text']
