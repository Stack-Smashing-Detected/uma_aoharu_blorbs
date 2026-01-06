import argparse
import questionary

from prompt_toolkit.styles import Style
from pyfiglet import figlet_format
from app.bar_chart import BarChart
from app.save_and_load import save_to_json
from app.skill_collector import SkillCollector

def main():
    running = True
    f = Figlet(font='slant')
    welcome_message = "Welcome to Uma Aoharu Blorbs! The app that shows how rigged the skill explosion mechanic is"
    add_mode = "You are now in add mode. Please enter the skill name you wish to add: "
    file_mode = "You are now in file mode. Please enter the filename of the text file: "
    draw_msg = "Drawing Frequency ar Chart, waiting for wit check to succeed..."
    save_msg = "Skill frequency table saved successfully."
    quit_msg = "Exiting the application. Good Luck in your Runs!"
    
    style = Style([
        ("question", "#5eeadc"),
        ("pointer", "fg:#ff9d00 bold"),
        ("highlighted", "fg:#ff9d00"),
        ("selected", "bold #5eeadc"),
        ("separator", "fg:#6c6c6c"),
        ("instruction", ""),  # default
        ("text", ""),
        ("disabled", "fg:#858585 italic")
    ])
    
    # entering program loop here.
    skill_collector = SkillCollector()
    
    while(running):
        status = questionary.select(
        "Select an option:",
        choices=[
            "Add Skill",
            "Add Skills from File",
            "Draw Histogram",
            "Save Skill Frequencies",
            "Quit"
        ]).ask()
        
        match status:
            case "Add Skill":
                print(add_mode)
                break
            case"Add Skills from File":
                print(file_mode)     
                break   
            case "Draw Histogram":
                print(draw_msg)
                break
            case "Save Skill Frequencies":
                print(save_msg)
                save_to_json(skill_collector.aoharu_skill_frequency_table, "/saved_data/aoharu_skill_frequencies.json")
                break
            case "Quit":
                print(quit_msg)
                running = False;
                break
           
        
        while status == "Add Skill":
            skill_name = questionary.text("Enter Skill Name: ").ask()
            freq = 1
            result = skill_collector.add_skill(skill_name, freq)
            print(result)
            
            continue_adding = questionary.confirm("Do you want to add another skill?").ask()
            if not continue_adding:
                break       
        
        while status == "Add Skills from File":
            filename = questionary.text("Enter Filename: ").ask()
            fp_prefix = "/saved_data/"
            filepath = fp_prefix + filename
            result = skill_collector.add_skills_from_file(filepath)
            
            continue_adding = questionary.confirm("Do you want to add another file?").ask()
            if not continue_adding:
                break       
        
        
        while status == "Draw Histogram":
            graph_type = questionary.select(
                "Select Category:",
                choices=[
                    "Dirt",
                    "Sprint",
                    "Mile",
                    "Medium",
                    "Long",
                    "Front Runner",
                    "Pace Chaser",
                    "Late Surger",
                    "End Closer",
                    "Return to Main Menu"
                ]).ask()

            if graph_type == "Return to Main Menu":
                break
            else:
                bar_chart = BarChart(skill_collector.get_specific_category_data(graph_type), 
                                     title=f"{graph_type} Aoharu Blorbs")
        
                
                
            
        
        
    
    
    