import json as js
import os
import re

from app.save_and_load import SaveAndLoad
from collections import Counter



GROUND_TYPES = {
    1: "turf",
    2: "dirt",
}

DISTANCE_TYPES = {
    1: "sprint",
    2: "mile",
    3: "medium",
    4: "long",
}

RUNNING_STYLES = {
    1: "front_runner",
    2: "pace_chaser",
    3: "late_surger",
    4: "end_closer",
}


'''
This module collects the skill from the user input and places it inside one of 9 dictionaries
based on its strategy or distance attribute.
'''

class SkillCollector:
    def __init__(self):
        # check if the saved_data directory is not empty first, if empty initialize it
        self.aoharu_skill_frequency_table = {}
        self.mant_skill_frequency_table = {}
        
        if not self.check_json_not_empty("./saved_data/aoharu_skill_frequencies.json"):
            self.aoharu_skill_frequency_table = self.create_new_frequency_table()
        else:
            print("Loading Aoharu Hai Skill Frequency Table...")
            self.load_existing_frequency_table("./saved_data/aoharu_skill_frequencies.json")
            
        if not self.check_json_not_empty("./saved_data/mant_rival_race_skill_frequencies.json"):
            self.mant_skill_frequency_table = self.create_new_frequency_table()
        else:
            print("Loading Make a New Track Skill Frequency Table...")
            self.load_existing_frequency_table("./saved_data/mant_rival_race_skills_frequencies.json");                
        

    
    def get_active_frequency_table(self, mode: str) -> dict:
        match mode:
            case "Aoharu Hai":
                return self.aoharu_skill_frequency_table
            case "Make a New Track":
                return self.mant_skill_frequency_table
        
    def set_active_frequency_table(self, mode: str, new_table: dict):
        match mode:
            case "Aoharu Hai":
                self.aoharu_skill_frequency_table = new_table
            case "Make a New Track":
                self.mant_skill_frequency_table = new_table
        
    

    def create_new_frequency_table(self) -> dict:
        new_frequency_table = {
                "turf": Counter(),
                "dirt": Counter(),
                "sprint": Counter(),
                "mile": Counter(),
                "medium": Counter(),
                "long": Counter(),
                "front_runner": Counter(),
                "pace_chaser": Counter(),
                "late_surger": Counter(),
                "end_closer": Counter(),
            }
        return new_frequency_table
        
    def load_existing_frequency_table(self, filename: str):
        with open(filename, "r", encoding="utf-8"):
            raw_table = SaveAndLoad.load_from_json(filename)
        
            loaded_table = {category: Counter(data) for category, data in raw_table.items()}
            self.skill_frequency_table = loaded_table
        
    def get_specific_category_table(self, category: str) -> Counter:
        '''
        Returns the skill frequency table for a specific category.
        
        Parameters:
        category (str): The category for which the skill frequency table is requested.
        
        Returns:
        Counter: The skill frequency table for the specified category.
        '''
        return self.aoharu_skill_frequency_table.get(category, Counter())
    
    def add_skill(self, skill_name: str, active_table: dict) -> str:
        '''
        Gets a skill name then uses the data obtained from skill_meta.json to identify where the
        skill should be added to.
        
        Parameters:
        skill_name (str): The name of the skill to be collected.
        
        Returns: str: A message indicating the result of the operation.
        '''
        if "Corners" in skill_name or  "Straightaways" in skill_name or "Savvy" in skill_name:
            skill_name += " ○"
                            
        with open("./skill_data/skill_data.json", "r", encoding="utf-8") as data_file:
            skills_data = js.load(data_file)
        
        with open("./skill_data/skillnames.json") as name_file:
            skill_names = js.load(name_file)

        skill_id = ''
        
        # obtain the id of the skill from its name by iterating over "skill_names"
        for id in skill_names:
            if(skill_names[id][0] == skill_name):
                skill_id = id
                break
        
        skill_data = skills_data.get(skill_id, {})
        if not skill_data:
            return "No skill with this ID found"
        
        skill_conditions = self.parse_condition(skill_data['alternatives'][0]['condition']);
        if "ground_type" in skill_conditions:
            category = GROUND_TYPES.get(skill_conditions["ground_type"])
            active_table[category][skill_name] += 1
            return f"Skill '{skill_name}' added to {category} category."
        
        elif "distance_type" in skill_conditions:
            category = DISTANCE_TYPES.get(skill_conditions["distance_type"])
            active_table[category][skill_name] += 1
            return f"Skill '{skill_name}' added to {category} category."

        elif "running_style" in skill_conditions:
            category = RUNNING_STYLES.get(skill_conditions["running_style"])
            active_table[category][skill_name] += 1
            return f"Skill '{skill_name}' added to {category} category."
        
        else:
            return "Skill is non-category specific skill or does not exist in the game currently"
        
    
    def add_skills_from_file(self, filename: str) -> str:
        '''
        Reads skill names from a text file and adds them to the frequency table.
        
        Parameters:
        filename (str): The name of the text file containing skill names.
        
        Returns: str: A message indicating the result of the operation.
        '''
        
        skill_name = ''
        try:
            with open(filename, 'r') as file:
                for line in file.readlines():               
                    print(self.add_skill(line.strip()))
                    

            return f"Skills from '{filename}' added successfully."
        
        except FileNotFoundError:
            return f"File '{filename}' not found."
          
        
    def parse_condition(self, condition: str) -> dict: 
        ''' The condition we are looking for will always be the first in the condition string'''
        
        conditions = {}
        for cond in condition.split("&"):
            match = re.match(r"(\w+)(==|>=|<=|!=|<|>)(\d+)", cond.strip())
            if match:
                key, _, value = match.groups()
                conditions[key] = int(value)
        
        # The first condition will always define the style, distance or track type the skill is exclusive to.
        return conditions

    def translate_choice_to_category(self, choice: str) -> str:
        mapping = {
            "Turf": "turf",
            "Dirt": "dirt",
            "Sprint": "sprint",
            "Mile": "mile",
            "Medium": "medium",
            "Long": "long",
            "Front Runner": "front_runner",
            "Pace Chaser": "pace_chaser",
            "Late Surger": "late_surger",
            "End Closer": "end_closer",
        }
        return mapping.get(choice, "")
    
    def check_json_not_empty(self, filename:str) -> bool:
        with open(filename, "r", encoding="utf-8") as f:
            try :
                data = js.load(f)
                return bool(data)  # returns False if the JSON is empty, True otherwise
            except js.JSONDecodeError:
                return False