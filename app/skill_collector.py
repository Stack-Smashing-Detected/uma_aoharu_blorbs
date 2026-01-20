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
        self.existing_data = self.check_saved_data_exists("./saved_data")
        self.aoharu_skill_frequency_table = {}
        
        if self.existing_data:
            print("Existing data found, loading skill frequency table...")
            self.load_existing_frequency_table("./saved_data/aoharu_skill_frequencies.json")
        else:
            self.create_new_frequency_table()

    
    @property
    def skill_frequency_table(self):
        return self.aoharu_skill_frequency_table

    @skill_frequency_table.setter
    def skill_frequency_table(self, new_table: dict):
        self.aoharu_skill_frequency_table = new_table

    def create_new_frequency_table(self):
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
        self.skill_frequency_table = new_frequency_table
        
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
    
    def add_skill(self, skill_name) -> str:
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
            self.aoharu_skill_frequency_table[category][skill_name] += 1
            return f"Skill '{skill_name}' added to {category} category."
        
        elif "distance_type" in skill_conditions:
            category = DISTANCE_TYPES.get(skill_conditions["distance_type"])
            self.aoharu_skill_frequency_table[category][skill_name] += 1
            return f"Skill '{skill_name}' added to {category} category."

        elif "running_style" in skill_conditions:
            category = RUNNING_STYLES.get(skill_conditions["running_style"])
            self.aoharu_skill_frequency_table[category][skill_name] += 1
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
    
    def check_saved_data_exists(self, path: str):
        with os.scandir(path) as entries:
            for entry in entries:
                return True
        return False
    
    