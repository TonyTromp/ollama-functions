# ollama-functions

## About

This boiler-plate project uses Ollama natively to invoke python function, and  similar to LangChain Tools (but using native Ollama API only).
it does this by leveraging the llm model called: calebfahlgren/natural-functions [calebfahlgren/natural-functions](https://ollama.com/calebfahlgren/natural-functions)

To make it flexible, i have opted for a runtime plugin system, which can be expanded to include your own functionality

Without any modifications you should use the llm model, since not all open llms are good enough to handle function invocation.

## How to use:

*Create venv and install requirements*
```
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

*Create .env file*
```
# .env
OLLAMA_URL=http://<your_ollama_ip>:11434
# If no model is specified, you will get a select box
OLLAMA_MODEL=calebfahlgren/natural-functions:latest

```