import argparse
import os
import questionary
import six

from prompt_toolkit.styles import Style
from pyfiglet import figlet_format
from rich.text import Text
from rich.console import Console
from app.bar_chart import BarChart
from app.save_and_load import SaveAndLoad
from app.skill_collector import SkillCollector


def figlet_print(text: str, hex_color="#ffffff"):
    figlet_text = figlet_format(text, font="slant")
    styled_text = Text(figlet_text, style=f"{hex_color}")
    console = Console()
    console.print(styled_text)


def main():
    running = True
    
    welcome_message = Text("Welcome to Umaskill Umascam Umawatch! The app that reminds you that gamemode skill hints are cooked", style="#dceb24")
    add_mode = "You are now in add mode. Please enter the skill name you wish to add: "
    file_mode = "You are now in file mode. Please enter the filename of the text file: "
    draw_msg = "Drawing Frequency Chart, waiting for wit check to succeed..."
    save_msg = "Skill frequency table saved successfully."
    quit_msg = "Exiting the application. Good Luck in your Runs!"
    current_mode = "Aoharu Hai"
    mode_select_msg = "Select a Scenario"
    file_path = "./saved_data/aoharu_skill_frequencies.json" # default scenario for this program is Aoharu Hai.
    
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
    print(figlet_print("Umaskill Umascam Umawatch", "bold #40babf"))
    print(welcome_message)
    
    active_table = skill_collector.get_active_frequency_table(current_mode)
    while(running):
        # figure out how to show a select mode screen. 
        print(f"Current Gamemode: {current_mode}")
        status = questionary.select(
        "Select an option:",
        choices=[
            "Select Gamemode",
            "Add Skill",
            "Add Skills From File",
            "Draw Frequency Chart",
            "Save Skill Frequencies",
            "Quit"
        ],
        style=style
        ).ask()
        
        match status:
            case "Select Gamemode":
                print(mode_select_msg)
            case "Add Skill":
                print(add_mode)
            case"Add Skills from File":
                print(file_mode)        
            case "Draw Frequency Chart":
                print(draw_msg)
            case "Save Skill Frequencies":
                print(save_msg)
                SaveAndLoad.save_to_json(skill_collector.aoharu_skill_frequency_table, "./saved_data/aoharu_skill_frequencies.json")
            case "Quit":
                print(quit_msg)
                running = False;
                
        while status == "Select Gamemode":
            gamemode = questionary.select(
                "Select Gamemode:",
                choices=[
                    "Aoharu Hai",
                    "Make a New Track",
                    "Return to Main Menu"
                ],
                style=style
                ).ask()
            
            if gamemode == current_mode:
                print(f"You are already in {current_mode} mode. Please select a different gamemode.")
                continue
            
            
            match gamemode:
                case "Aoharu Hai":
                    current_mode = "Aoharu Hai"
                    filepath = "./saved_data/aoharu_skill_frequencies.json"

                case "Make a New Track":
                    current_mode = "Make a New Track"
                    filepath = "./saved_data/mant_rival_race_skill_frequencies.json"
                
                case "Return to Main Menu":
                    break
            
            
        while status == "Add Skill":
            skill_name = questionary.text("Enter Skill Name: ").ask()
            result = skill_collector.add_skill(skill_name, active_table)
            print(result)

            continue_adding = questionary.confirm("Do you want to add another skill?").ask()
            if not continue_adding:
                save_now = questionary.confirm("Do you want to save skill frequencies now?").ask()
                if save_now:
                    SaveAndLoad.save_to_json(skill_collector.aoharu_skill_frequency_table, "./saved_data/aoharu_skill_frequencies.json")
                    print(save_msg)
                break       
        
        while status == "Add Skills From File":
            filename = questionary.text("Enter Filename: ").ask()
            print(filename)
            fp_prefix = "./skill_textfiles/"
            filepath = fp_prefix + filename
            print(filepath)
            result = skill_collector.add_skills_from_file(filepath)
            print(result)

            save_now = questionary.confirm("Do you want to save skill frequencies now?").ask()
            if save_now:
                SaveAndLoad.save_to_json(skill_collector.aoharu_skill_frequency_table, "./saved_data/aoharu_skill_frequencies.json")
                print(save_msg)

            continue_adding = questionary.confirm("Do you want to add another file?").ask()
            if not continue_adding:
                break       


        while status == "Draw Frequency Chart":
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
                ],
                style=style
                ).ask()

            if graph_type == "Return to Main Menu":
                break
            else:
                graph_name = skill_collector.translate_choice_to_category(graph_type)
                bar_chart = BarChart(skill_collector.get_specific_category_table(graph_name),"Aoharu Blorbs", graph_type)
                bar_chart.plot_chart()
                
                
if __name__ == "__main__":
    main()
            
        
    
    
    