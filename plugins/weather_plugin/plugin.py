from plugin_interface import PluginInterface

class WeatherTool(PluginInterface):

    _schema = {
        "name": "weather",
        "description": "Get the weather forecast for a given location.",
        "parameters": {
            "properties": {
                "location": {
                    "description": "The location to get the weather forecast for.",
                    "type": "string"
                }
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
