import requests
import subprocess
import datetime

# Function to fetch a random positive message
def get_random_message():
    try:
        # Fetch a random quote from ZenQuotes API
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return data[0]["q"], data[0]["a"]
    except Exception as e:
        # Fallback message in case of error
        return "Keep going! The quote fetching may have failed but you haven't! Something amazing is coming your way!", "Grid"

# Fetch a truly random positive message
quote, author = get_random_message()

# Create/update a file with the commit timestamp and message
file_name = "positive_message.md"
with open(file_name, "a") as file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"**\"{quote}\"**  \n")
    file.write(f"— {author}  \n")
    file.write(f"*{timestamp}*  \n\n")

# Git commands to commit and push the changes
subprocess.run(["git", "add", file_name])
subprocess.run(["git", "commit", "-m", f"Added positive message: {quote}"])
subprocess.run(["git", "push"])
