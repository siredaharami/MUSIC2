import os
import importlib
from testing import app

def load_plugins():
    plugin_dir = "testing/modules"
    

    for file_name in os.listdir(plugin_dir):
        if file_name.endswith(".py") and not file_name.startswith("__"):
            module_name = file_name[:-3]  # Remove the .py extension
            importlib.import_module(f"{plugin_dir}.{module_name}")
            print(f"Successfully imported: {module_name}")


if __name__ == "__main__":
    print("Loading plugins...")
    load_plugins()
    print("All plugins imported successfully.")
    print("Bot is running...")
    app.run()
