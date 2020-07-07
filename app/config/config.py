import os
import json

def load_config():
    """
    Loads application settings from config file based on environment variable PY_ENV; defaults to dev
    """
    filename = 'config.dev.json'

    if 'PY_ENV' in os.environ:
        if os.environ['PY_ENV'].lower() == 'production':
            filename = 'config.prod.json'
       
    filepath =  os.path.dirname(__file__) +'/'+ filename
    print(filepath)
    with open(filepath) as json_file:
        data = json.load(json_file)
        
    return data
    
        
        