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
        return data[0]["q"] + " — " + data[0]["a"]
    except Exception as e:
        # Fallback message in case of error
        return "Keep going! Something amazing is coming your way!"

# Fetch a truly random positive message
message = get_random_message()

# Create/update a file with the commit timestamp and message
file_name = "positive_message.txt"
with open(file_name, "a") as file:
    file.write(f"{datetime.datetime.now()}: {message}\n")

# Git commands to commit and push the changes
subprocess.run(["git", "add", file_name])
subprocess.run(["git", "commit", "-m", message])
subprocess.run(["git", "push"])
