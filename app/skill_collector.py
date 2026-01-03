import json as js
import re

from .SaveAndLoad import save_to_json, load_from_json
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
    def __init__(self, existing_data=False):
        # check if the saved_data directory is not empty first, if empty initialize it
        self.existing_data = existing_data
        self.aoharu_skill_frequency_table = {}
           
    
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
                "medium": Counter(),
                "long": Counter(),
                "front_runner": Counter(),
                "pace_chaser": Counter(),
                "late_surger": Counter(),
                "end_closer": Counter(),
            }
        self.skill_frequency_table(new_frequency_table)
        
    def load_existing_frequency_table(self, filename: str):
        raw_table = load_from_json(filename)
        
        loaded_table = {category: Counter(data) for category, data in raw_table.items()}
        self.skill_frequency_table(loaded_table)
        
    def add_skill(self, skill_name) -> str:
        '''
        Gets a skill name then uses the data obtained from skill_meta.json to identify where the
        skill should be added to.
        
        Parameters:
        skill_name (str): The name of the skill to be collected.
        
        Returns: str: A message indicating the result of the operation.
        '''
        
        skills_data = js.load("/skill_data/skill_data.json")
        skill_names = js.load("/skill_data/skillnames.json")
        skill_id = ''
        
        # obtain the id of the skill from its name by iterating over "skill_names"
        for id in skill_names:
            if(skill_names[id] == skill_name):
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
        
        
    def parse_condition(self, condition: str) -> dict: 
        ''' The condition we are looking for will always be the first in the condition string'''
        
        conditions = {}
        for cond in condition.split("&"):
            match = re.match(r"(\w+)(==|>=|<=|!=|<|>)(\d+)", cond)
            if match:
                key, _, value = match.groups()
                conditions[key] = int(value)
        
        # The first condition will always define the style, distance or track type the skill is exclusive to.
        return conditions
    
    
    