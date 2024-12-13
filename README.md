# Ollama_Tools

My personal Python code to use as Ollama tools

Ollama function calling docs:

    https://ollama.com/blog/functions-as-tools

## Notes on nested use of LLMs

There are currently two tool functions that also internally use LLMs:

- summararize_text.py: summarize_text(text: str, context: str = '') -> str that uses an LLM to summarize a block of text
- web_search.py: search_web(query: str, max_results: int = 5) -> str that uses an LLM to filter search results based on the original query and format the output as markdown for easy use by another LLM or tool
	
## Changing design notes

For the first iteration tools return something like this:

```
Output of list_directory: {'files': ['.git', '.gitignore', 'LICENSE', ...

Output of read_file_contents: {'content': 'git+https://github.com/mark-watso ...

Output of uri_to_markdown: {'content': 'Read My Blog on Blogspot ...
```

The problem with this is that this does allow chaining tools, calling a tool,
evaluating tool results with the original prompt fragment that triggered the tool, etc.

## Ollama's "new" JSON output support

https://ollama.com/blog/structured-outputs

