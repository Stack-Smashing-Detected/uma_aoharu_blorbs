import json as js


class SaveAndLoad:
    @staticmethod
    def save_to_json(data: dict, filename: str) -> None:
        '''
        Saves a dictionary to a JSON file.
        
        Parameters:
        data (dict): The data to be saved.
        filename (str): The name of the file where data will be saved.
        '''
        with open(filename, 'w') as f:
            js.dump(data, f, indent=4)
    
    @staticmethod
    def load_from_json(filename: str) -> dict:
        '''
        Loads a dictionary from a JSON file.
        
        Parameters:
        filename (str): The name of the file to load data from.
        
        Returns:
        dict: The loaded data.
        '''
        with open(filename, 'r') as f:
            data = js.load(f)
        return data