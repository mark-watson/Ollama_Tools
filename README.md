# Ollama_Tools

My personal Python code to use as Ollama tools

Ollama function calling docs:

    https://ollama.com/blog/functions-as-tools
	
## Changing design notes

For the first iteration tools return something like this:

```
Output of list_directory: {'files': ['.git', '.gitignore', 'LICENSE', ...

Output of read_file_contents: {'content': 'git+https://github.com/mark-watso ...

Output of uri_to_markdown: {'content': 'Read My Blog on Blogspot ...
```

The problem with this is that this does allow chaining tools, calling a tool,
evaluating tool results with the original prompt fragment that triggered the tool, etc.

