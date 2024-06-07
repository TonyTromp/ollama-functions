# plugin_interface.py
class PluginInterface:
    def get_schema(self) -> object:
        raise NotImplementedError("Plugins must implement the 'get_schema' method")
    def get_plugin_name(self) -> str:
        raise NotImplementedError("Plugins must implement the 'get_plugin_name' method")    
    def get_plugin_description(self) -> str:
        raise NotImplementedError("Plugins must implement the 'get_plugin_description' method")
    def execute(self):
        raise NotImplementedError("Plugins must implement the 'execute' method")
