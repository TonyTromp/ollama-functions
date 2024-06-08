from plugin_interface import PluginInterface
import subprocess
import dirtyjson

class WebBrowserTool(PluginInterface):

    _schema = {
        "name": "web_browser",
        "description": "Open Chrome web browser and navigate to a given URL",
        "parameters": {
            "properties": {
                "url": {
                    "url": "url path starting with http:// or https://",
                    "type": "string"
                }
            }
        }
    }

    def launch_browser(self, url):
        # Command to open Google Chrome with the specified URL
        chrome_command = ['open', '-a', 'Google Chrome', url]
        # Spawn the Chrome process
        subprocess.Popen(chrome_command)
        print('Chrome browser has been opened with the specified URL')
    
    def get_schema(self):
        return self._schema
    
    def get_plugin_name(self):
        return self._schema['name'] 
    
    def get_plugin_description(self) -> str:
        return self._schema['description'] 
    
    def execute(self, parameters: dict):
        print( f"Hello from {self.get_plugin_name()}")
        if type(parameters)==str:
            parameters = eval(parameters)
        #  Do your magic here
        if 'url' in parameters:
            self.launch_browser(parameters['url'])
