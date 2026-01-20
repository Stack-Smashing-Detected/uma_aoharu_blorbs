# Uma-Musume Scenario Skill Frequency Feature - Usage Guide

## About

Uma-Musume Scenario Skill Frequency Feature is a Python application designed to track and visualize skill frequencies from Uma Musume Pretty Derby's Aoharu Scenario. The project helps players analyze how the skill explosion mechanic works by collecting skill data, organizing it by categories (such as distance types and running styles), and generating frequency charts for visualization.

The application features:
- An interactive command-line interface for adding skills manually or from text files
- Skill frequency tracking organized by categories (Dirt, Sprint, Mile, Medium, Long, Front Runner, Pace Chaser, Late Surger, End Closer)
- Visual bar charts showing skill frequency distributions
- JSON-based data persistence for saving and loading skill frequency tables

## Installation

### Opening a terminal (so you can run the commands)

You’ll run the commands below in a terminal.

- **Windows (recommended: PowerShell)**:
  - Press the **Windows key**, type **PowerShell**, press **Enter**
  - Optional: in File Explorer, go to the project folder, then **Shift + Right Click** → **Open PowerShell window here**
- **Windows (Command Prompt)**:
  - Press the **Windows key**, type **cmd**, press **Enter**
- **macOS**:
  - Open **Applications → Utilities → Terminal**
- **Linux**:
  - Open your system’s **Terminal** app (often `Ctrl`+`Alt`+`T`)

When you see code blocks labeled `bash`, that just means “type these commands into your terminal”.

### Installing Python

1. **Download Python**: Visit [python.org](https://www.python.org/downloads/) and download the latest stable version of Python 3 (Python 3.8 or higher recommended).

2. **Installation Steps**:
   - Run the downloaded installer
   - **Important**: Check the box that says "Add Python to PATH" during installation
   - Choose "Install Now" or customize the installation location if needed
   - Complete the installation

3. **Verify Installation**: In your terminal, run:
   ```bash
   python --version
   ```
   You should see the Python version number displayed.

### Setting Up a Virtual Environment

A virtual environment isolates your project dependencies from your system Python installation. This prevents conflicts between different projects.

1. **Navigate to the Project Directory**:
   
   In your terminal, change directory to the folder where you cloned/downloaded this repo.
   
   ```bash
   cd path/to/uma_aoharu_blorbs
   ```

   - **Tip (Windows)**: you can copy the folder path from File Explorer and paste it after `cd`.

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
   This creates a new folder called `venv` in your project directory.

3. **Activate the Virtual Environment**:
   
   **On Windows (PowerShell or Command Prompt)**:
   ```bash
   venv\Scripts\activate
   ```
   
   **On macOS/Linux**:
   ```bash
   source venv/bin/activate
   ```
   
   When activated, you'll see `(venv)` at the beginning of your command prompt.

4. **Deactivate** (when you're done working):
   ```bash
   deactivate
   ```

### Setting Up pip

`pip` (Python Package Installer) comes bundled with Python 3.4+, so if you have Python installed, you likely already have pip.

1. **Verify pip Installation**:
   ```bash
   pip --version
   ```

2. **Upgrade pip** (recommended):
   ```bash
   python -m pip install --upgrade pip
   ```

### Installing Dependencies

The `requirements.txt` file lists all the Python packages needed for this project. To install them:

1. **Make sure your virtual environment is activated** (you should see `(venv)` in your terminal).

2. **Install all dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   This command will automatically install all packages listed in `requirements.txt`, including:
   - matplotlib (for chart visualization)
   - pandas (for data handling)
   - pyfiglet (for ASCII art)
   - PyQt6 (for GUI components)
   - questionary (for interactive menus)
   - rich (for styled terminal output)

3. **Verify Installation**: You can check installed packages with:
   ```bash
   pip list
   ```

## Running the Application

Once you have completed the installation steps:

1. **Activate your virtual environment** (if not already activated).

2. **Run the application**:
   ```bash
   python main.py
   ```

3. The application will display a welcome message and present you with an interactive menu.

## Windows: Build an Executable (.exe)

You can bundle this app into a single Windows executable using **PyInstaller**.

### 1) Install PyInstaller (in your venv)

```bash
pip install pyinstaller
```

### 2) Build

From the project root (same folder as `main.py`):

```bash
pyinstaller --onefile --name "UmaAoharuBlorbs" main.py
```

### 3) Find and run the executable

- The executable will be created at: `dist\UmaAoharuBlorbs.exe`
- Run it by double-clicking it in File Explorer, or from PowerShell:

```bash
.\dist\UmaAoharuBlorbs.exe
```

### Notes

- **You must build on Windows to get a Windows `.exe`** (PyInstaller does not cross-compile between OSes).
- **First build is slower**: PyInstaller analyzes imports and collects dependencies.
- **Data files**: This project reads JSON from `skill_data/` and writes to `saved_data/`. If you want the `.exe` to be runnable from anywhere, we can add a PyInstaller spec to bundle those folders and update paths in code to resolve relative-to-exe.

## macOS/Linux: Build an Executable

You can also bundle this app into a native executable for **macOS** or **Linux** using **PyInstaller**.

### 1) Install PyInstaller (in your venv)

```bash
pip install pyinstaller
```

### 2) Build

From the project root (same folder as `main.py`):

```bash
pyinstaller --onefile --name "UmaAoharuBlorbs" main.py
```

### 3) Find and run the executable

- The executable will be created at: `dist/UmaAoharuBlorbs`
- Run it from your terminal:

```bash
./dist/UmaAoharuBlorbs
```

### Notes

- **Build on the target OS**: build on Linux for Linux binaries, and on macOS for macOS binaries.
- **Data files**: Same note as Windows — this app expects `skill_data/` and `saved_data/` to be present relative to where it runs, unless we bundle those assets and adjust path resolution.

## Features

### Main Menu Interface

The application uses an interactive command-line interface with the following options:

- **Add Skill** - Manually add individual skills
- **Add Skills From File** - Import multiple skills from a text file
- **Draw Frequency Chart** - Generate visual charts by category
- **Save Skill Frequencies** - Save your collected data to a JSON file
- **Quit** - Exit the application

### Adding Skills

#### Add Skill (Manual Entry)

This option allows you to add skills one at a time.

1. Select **"Add Skill"** from the main menu.
2. Enter the exact skill name when prompted.
3. The application will automatically categorize the skill based on its attributes:
   - **Ground Type**: Turf or Dirt
   - **Distance Type**: Sprint, Mile, Medium, or Long
   - **Running Style**: Front Runner, Pace Chaser, Late Surger, or End Closer
4. You'll see a confirmation message indicating which category the skill was added to.
5. The app will ask if you want to add another skill. Continue adding or return to the main menu.

**Note**: Skills with special conditions (Corners, Straightaways, or Savvy) will automatically have an "○" symbol appended to their name.

#### Add Skills From File

This option allows you to import multiple skills from a text file.

1. **Prepare your text file**:
   - Create a text file with one skill name per line
   - Place the file in the `skill_textfiles/` directory (create this folder if it doesn't exist)
   - Example file content:
     ```
     Fine Weather Girl
     Fine Weather Girl
     Straightaway Ace ○
     Corner Artist ○
     ```

2. Select **"Add Skills From File"** from the main menu.

3. Enter the filename (without the path) when prompted.

4. The application will process each skill in the file and display confirmation messages.

5. You can add multiple files in one session.

**Important**: Make sure your text file uses the exact skill names as they appear in the game.

### Draw Frequency Chart

This feature generates visual bar charts showing the frequency distribution of skills for specific categories.

1. Select **"Draw Frequency Chart"** from the main menu.

2. Choose a category to visualize:
   - **Distance Categories**: Dirt, Sprint, Mile, Medium, Long
   - **Running Style Categories**: Front Runner, Pace Chaser, Late Surger, End Closer

3. A bar chart window will open displaying:
   - Skill names on the x-axis
   - Frequency counts on the y-axis
   - Title indicating the selected category

4. After viewing the chart, you'll return to the category selection menu.

5. Select **"Return to Main Menu"** when you're done viewing charts.

### Save Skill Frequencies

This feature saves your collected skill frequency data to a JSON file.

1. Select **"Save Skill Frequencies"** from the main menu.

2. The application will save the current state of all skill frequency tables to:
   ```
   saved_data/aoharu_skill_frequencies.json
   ```

3. You'll see a confirmation message when the save is successful.

**Note**: The application automatically loads existing data when you start it. If you have previously saved data, it will be loaded automatically at startup.

### Data Persistence

- Your skill frequency data is saved in `saved_data/aoharu_skill_frequencies.json`
- When you start the application, it automatically checks for existing data and loads it if available
- Each category maintains its own frequency counter, tracking how many times each skill appears
- The data persists between sessions, so you can continue collecting data over time

## Categories Explained

Skills are automatically categorized based on their conditions in the game:

- **Dirt** / **Turf**: Ground type restrictions
- **Sprint** / **Mile** / **Medium** / **Long**: Distance type restrictions  
- **Front Runner** / **Pace Chaser** / **Late Surger** / **End Closer**: Running style restrictions

Each skill can appear in multiple categories if it has multiple condition types. The frequency charts show how often skills appear in each category, helping you identify patterns in the skill explosion mechanic.

## Requirements

- Python 3.10 or higher (3.14 or higher recommended)
- All dependencies listed in `requirements.txt`:
  - matplotlib
  - pandas
  - pyfiglet
  - PyQt6
  - questionary
  - rich
  - six
  - click

## Tips for Best Results

1. **Accurate Skill Names**: Make sure to use the exact skill names as they appear in-game for accurate categorization.

2. **Regular Saves**: Save your data frequently to avoid losing your collected information.

3. **File Organization**: Keep your skill text files organized in the `skill_textfiles/` directory for easy access.

4. **Data Collection**: The more data you collect, the more reliable your frequency charts will be for identifying patterns.

Happy skill tracking, and good luck with your runs!