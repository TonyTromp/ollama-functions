![#f03c15](https://www.ollama.com/public/ollama.png)

# ollama-functions

## About

This boiler-plate project uses Ollama natively to invoke python function, and  similar to LangChain Tools (but using native Ollama API only).
it does this by leveraging the llm model called: calebfahlgren/natural-functions [calebfahlgren/natural-functions](https://ollama.com/calebfahlgren/natural-functions)

To make it flexible, i have opted for a runtime plugin system, which can be expanded to include your own functionality

Without any modifications you should use the llm model, since not all open llms are good enough to handle function invocation.

## How to use:

*Create venv and install requirements*
```bash
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

*Run it* 
```bash
source venv/bin/activate
python app.py
```

## Extending the functionality

The *plugin_loader* is a simple class that loads the plugins from the plugins folder. In the sample code it looks into the plugin/ folder for any plugin.

a function plugin consists of the following file structure

```bash
|-Plugins
|-- <YOUR_PLUGIN_FOLDER>
|---- __init__.py
|---- plugin.py
```

The plugin.py inherits from the base class *PluginInterface* and implements the following methods:
```python
from plugin_interface import PluginInterface

class nmap_scan_single_ip(PluginInterface):

    _schema =     {
      "name": "nmap_scan",
      "description": "Perform a nmap network scan on a single ip address.",
      "parameters": {
          "properties": {              
              "ipv4": "ipv4 or CIDR range",
              "description": "ipv4 or CIDR range address of scan target",
              "type": "string"
          }
      }
    }
    
    def get_schema(self):
        return self._schema
    
    def get_plugin_name(self):
        return self._schema['name'] 
    
    def get_plugin_description(self) -> str:
        return self._schema['description'] 
    
    def execute(self, parameters):
        print( f"Hello from {self.get_plugin_name()}")
        print(parameters)
        #  Do your magic here
```

In the schema you define how the LLM requires to call the Python method and its arguments you need to passthrough.
The generic 'execute' method is invoked passing the arguments extracted by the LLM from the schem.
During load, all schema's files are appended to the schema[] list and passed through as context for the LLM.

