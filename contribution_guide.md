# Contribution Guide

## About

Uma Aoharu Blorbs is a Python application designed to track and visualize skill frequencies from Uma Musume Pretty Derby's Aoharu mode. The project helps players analyze how the skill explosion mechanic works by collecting skill data, organizing it by categories (such as distance types and running styles), and generating frequency charts for visualization.

The application features:
- An interactive command-line interface for adding skills manually or from text files
- Skill frequency tracking organized by categories (Dirt, Sprint, Mile, Medium, Long, Front Runner, Pace Chaser, Late Surger, End Closer)
- Visual bar charts showing skill frequency distributions
- JSON-based data persistence for saving and loading skill frequency tables

## How to Install

For detailed installation instructions, including Python setup, virtual environment configuration, and dependency installation, please refer to the [README.md](README.md) file's Installation section.

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
