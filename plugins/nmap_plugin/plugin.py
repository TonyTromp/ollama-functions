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

