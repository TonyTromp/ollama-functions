from plugin_interface import PluginInterface
import subprocess
import dirtyjson
import urllib.parse

class SearchEbayTool(PluginInterface):

    _schema = {
        "name": "ebay_search",
        "description": "Search eBay for a specific item",
        "parameters": {
            "properties": {
                "item": {
                    "description": "item or description to search for",
                    "type": "string"
                }
            }
        }
    }

    def launch_browser(self, url):
        chrome_command = ['open', '-a', 'Google Chrome', url]
        subprocess.Popen(chrome_command)
    
    def get_schema(self):
        return self._schema
    
    def get_plugin_name(self):
        return self._schema['name'] 
    
    def get_plugin_description(self) -> str:
        return self._schema['description'] 
    
    def execute(self, parameters: dict):
        #  print( f"execute plugin {self.get_plugin_name()}")
        #  Do your magic here
        if 'item' in parameters:
            item = urllib.parse.quote(parameters['item'])
            url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw={item}&_sacat=0"
            self.launch_browser(url)
