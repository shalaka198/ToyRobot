import os
import json

def load_config():
    """
    Loads application settings from config file
    """
    filepath =  os.path.dirname(__file__) +'/'+ 'config.json'
    print(filepath)
    with open(filepath) as json_file:
        data = json.load(json_file)
        
    return data
    
        
        