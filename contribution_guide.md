# Contribution Guide

## About

Uma Aoharu Blorbs is a Python application designed to track and visualize skill frequencies from Uma Musume Pretty Derby's Aoharu mode. The project helps players analyze how the skill explosion mechanic works by collecting skill data, organizing it by categories (such as distance types and running styles), and generating frequency charts for visualization.

The application features:
- An interactive command-line interface for adding skills manually or from text files
- Skill frequency tracking organized by categories (Dirt, Sprint, Mile, Medium, Long, Front Runner, Pace Chaser, Late Surger, End Closer)
- Visual bar charts showing skill frequency distributions
- JSON-based data persistence for saving and loading skill frequency tables

## How to Install

### Installing Python

1. **Download Python**: Visit [python.org](https://www.python.org/downloads/) and download the latest stable version of Python 3 (Python 3.14 or higher recommended).

2. **Installation Steps**:
   - Run the downloaded installer
   - **Important**: Check the box that says "Add Python to PATH" during installation
   - Choose "Install Now" or customize the installation location if needed
   - Complete the installation

3. **Verify Installation**: Open your terminal or command prompt and run:
   ```bash
   python --version
   ```
   You should see the Python version number displayed.

### Setting Up a Virtual Environment

A virtual environment isolates your project dependencies from your system Python installation. This prevents conflicts between different projects.

1. **Navigate to the Project Directory**:
   ```bash
   cd path/to/uma_aoharu_blorbs
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
   This creates a new folder called `venv` in your project directory.

3. **Activate the Virtual Environment**:
   
   **On Windows**:
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

### Using requirements.txt

The `requirements.txt` file lists all the Python packages needed for this project. To install them:

1. **Make sure your virtual environment is activated** (you should see `(venv)` in your terminal).

2. **Install all dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   This command will automatically install all packages listed in `requirements.txt`, including:
   - matplotlib
   - pandas
   - pyfiglet
   - PyQt6
   - questionary
   - rich
   - and other dependencies

3. **Verify Installation**: You can check installed packages with:
   ```bash
   pip list
   ```

## Contribution Guide

### Committing the `aoharu_skill_frequencies.json` File

When contributing to this project, please note that **only the `aoharu_skill_frequencies.json` file** should be committed to version control. This file is located in the `saved_data/` directory and contains the collected skill frequency data.

**Important Guidelines**:

1. **Before Committing**: Make sure you've activated your virtual environment and are in the project root directory.

2. **Check Your Changes**:
   ```bash
   git status
   ```
   Review which files have been modified.

3. **Stage Only the JSON File**:
   ```bash
   git add saved_data/aoharu_skill_frequencies.json
   ```
   
   **Do NOT** commit other files unless explicitly requested or you've made code changes that require it.

4. **Commit with a Descriptive Message**:
   ```bash
   git commit -m "Update aoharu_skill_frequencies.json with new skill data"
   ```
   
   Use clear, descriptive commit messages that explain what data was added or updated.

5. **Push Your Changes**:
   ```bash
   git push
   ```
   
   Make sure you're pushing to the correct branch (typically your feature branch, not main/master).

**Note**: If you accidentally stage other files, you can unstage them using:
```bash
git reset HEAD <filename>
```

Or to unstage all files except the JSON file:
```bash
git reset
git add saved_data/aoharu_skill_frequencies.json
```

## Closing Statement

This tool is pretty much for those who are interested in what skills are most common, who knows maybe the game has a rarity system we do not know of or maybe its just "bad luck" but that's the fun in researching probability.

Happy skill tracking, and good luck with your runs!
