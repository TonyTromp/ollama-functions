import os
import dirtyjson
from ollama import Client
from pprint import pprint
from simple_term_menu import TerminalMenu
from dotenv import load_dotenv
from plugin_loader import PluginLoader, FunctionUtils

load_dotenv()

tools = []
chat_messages = []

def get_system_prompt(tools):
    return f"""
    You are a helpful assistant with access to the following functions. Use them if required - {tools}
    """

def get_ollama_models(client: Client) -> list:
    models = client.list()['models']
    model_names = [model["name"] for model in models]
    return model_names

def select_model(client: Client) -> str:
    # Select LLM model to use
    print(f"\nSelect LLM model to use:\n")
    options = get_ollama_models(client)
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    return options[menu_entry_index]

def send_system_prompt(client: Client, model: str, system_prompt: str) -> str:
    chat_messages.append({'role': 'system', 'content': system_prompt })
    response = client.chat(model=model, messages=chat_messages, stream=False)
    return response['message']['content']

def send_chat_message(client: Client, model: str, message: str) -> str:
    chat_messages.append({ 'role': 'user','content': message })
    response = client.chat(model=model, messages=chat_messages, stream=False)
    chat_messages.append(response['message'])
    return response['message']['content']

def load_plugins(folder) -> list:
    plugins = PluginLoader(folder)
    schema = []

    for plugin in plugins.list_plugins():
        print(f"Plugin: {plugin.get_plugin_name()}")
        print(f"Description: {plugin.get_plugin_description()}")
        print(f"Parameters: {plugin.get_schema()['parameters']}")
        schema.append(plugin.get_schema())

    return plugins, schema



def main():
    plugins, schema = load_plugins("plugins")

    client = Client(host=os.getenv('OLLAMA_URL'))    

    model = os.getenv('OLLAMA_MODEL')
    if (not model or model is None):
        model = select_model(client)
    print(f"Using model {model}")

    print(f'\nSetting system prompt:')
    message = send_system_prompt(client, model,  get_system_prompt(schema))

    print(f'\nGet chat message:')
    message = send_chat_message(client, model, "What the weather in London?")
    if FunctionUtils.is_function(message):
        FunctionUtils.invoke(plugins, message)

    print(f'\nGet chat message:')
    message = send_chat_message(client, model, "Perform a nmap scan on 10.0.1.0/16")
    if FunctionUtils.is_function(message):
        FunctionUtils.invoke(plugins, message)

    print(f'\nGet chat message:')
    message = send_chat_message(client, model, "Perform a nmap scan on 10.0.1.0")
    if FunctionUtils.is_function(message):
        FunctionUtils.invoke(plugins, message)



if __name__ == "__main__":
    main()

