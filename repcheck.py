import requests
import argparse
from datetime import datetime

# Function to check reputation
def check_reputation(websites, preset_list, specific_websites):
    results = {}
    
    # Read the preset list of websites
    with open(preset_list, 'r') as file:
        preset_websites = [line.strip() for line in file.readlines()]
    
    # Add specific websites to the preset list
    preset_websites.extend(specific_websites)
    
    # Check reputation for each website
    for website in websites:
        if website in preset_websites:
            results[website] = "Unsafe"
        else:
            results[website] = "Safe"
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Check the reputation of websites.")
    parser.add_argument("websites_file", type=str, help="Path to the file containing a list of websites.")
    parser.add_argument("preset_list", type=str, help="Path to the file containing the preset list of websites.")
    args = parser.parse_args()

    # List of specific websites
    specific_websites = [
        "example1.com",
        "example2.com",
        "example3.com"
    ]
    
    # Read the list of websites from the file
    with open(args.websites_file, 'r') as file:
        websites = [line.strip() for line in file.readlines()]
    
    # Call the function to check reputation
    results = check_reputation(websites, args.preset_list, specific_websites)

    # Get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print results with date and time
    for website, reputation in results.items():
        print(f"{current_datetime} - {website}: {reputation}")

if __name__ == "__main__":
    main()
