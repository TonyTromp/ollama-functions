import os
import importlib.util
from plugin_interface import PluginInterface
import dirtyjson

class PluginLoader:
    def __init__(self, plugin_directory):
        self.plugin_directory = plugin_directory
        self.plugins = []
        self._load()

    def _load(self):
        for subdir in os.listdir(self.plugin_directory):
            subdir_path = os.path.join(self.plugin_directory, subdir)
            if os.path.isdir(subdir_path):
                init_file = os.path.join(subdir_path, "__init__.py")
                plugin_file = os.path.join(subdir_path, "plugin.py")
                if os.path.isfile(init_file) and os.path.isfile(plugin_file):
                    print( f"loading plugin: {subdir}", subdir)
                    module_name = f"{subdir}.plugin"
                    spec = importlib.util.spec_from_file_location(module_name, plugin_file)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    self._register_plugins(module)

    def _register_plugins(self, module):
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, type) and issubclass(attribute, PluginInterface) and attribute is not PluginInterface:
                self.plugins.append(attribute())
    
    def list_plugins(self):
        return self.plugins 
    
    def get_plugin_by_name(self, plugin_name):
        for plugin in self.plugins:
            if plugin.get_plugin_name() == plugin_name:
                return plugin
        return None


class FunctionUtils:
    FUNC_PREFIX="<functioncall>"

    @staticmethod
    def is_function(message):
        return message.startswith(FunctionUtils.FUNC_PREFIX)

    @staticmethod
    def parse_function_call(message):
        if message.startswith(FunctionUtils.FUNC_PREFIX):        
            func_data = dirtyjson.loads(message[len(FunctionUtils.FUNC_PREFIX):])
            return func_data['name'], func_data['arguments']
        return None, None
    
    @staticmethod
    def invoke(plugins: PluginLoader, str_message):
        plugin_name, arguments = FunctionUtils.parse_function_call(str_message)
        if plugin_name is not None:
            plugin = plugins.get_plugin_by_name(plugin_name)
            plugin.execute(arguments)


if __name__ == "__main__":
    loader = PluginLoader("plugins")
