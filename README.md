Positive Message Bot
===================

A bot that makes a random positive commit to your GitHub repository every 24 hours.

Features
--------
- Generates truly random positive messages using the ZenQuotes API.
- Automatically commits and pushes changes to repository.

Requirements
------------
- Python 3.x
- requests library 
- Git

Usage
```bash
1. Clone this repository:
   git clone https://github.com/<your-username>/positive-commit-bot.git
   cd positive-commit-bot

2. Run the script manually:
   python3 commit_bot.py

3. Automate it using:
   - Cron (Linux/Mac)
   - Task Scheduler (Windows)#
```

File Details
------------
- commit_bot.py: Main script that fetches a random message, updates a file, and commits to the repository.
- positive_message.txt: Log of all positive messages added.

Credits
-------
- ZenQuotes API (https://zenquotes.io/) for random positive quotes.

