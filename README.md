Positive Message Bot
===================

A bot that makes a random positive commit to your GitHub repository every 24 hours.

Features
--------
- Generates truly random positive messages using the ZenQuotes API.
- Automatically commits and pushes changes to the repository.

Requirements
------------
- Python 3.x
- requests library 
- Git

Usage
-----
1. Clone this repository:
   ```bash
   git clone https://github.com/hhussain04/positivemessagebot.git
   cd positivemessagebot
   ```

2. Run the script manually:
   ```bash
   python3 commit_bot.py
   ```

3. Automate it using:
   - Cron (Linux/Mac)
   - Task Scheduler (Windows)

File Details
------------
- `commit_bot.py`: Main script that fetches a random message, updates a file, and commits to the repository.
- `positive_message.md`: Log of all positive messages added.

Credits
-------
- ZenQuotes API (https://zenquotes.io/) for random positive quotes.
