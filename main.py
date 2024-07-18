import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime

c = datetime.now()

# Displays Time
current_time = c.strftime('%H:%M:%S')


# Function to extract email addresses from a webpage
def extract_emails(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Using regular expression to find email addresses
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = set(re.findall(pattern, soup.get_text()))
            return emails
        else:
            print(f"Failed to retrieve webpage: {response.status_code}")
            return set()
    except requests.exceptions.RequestException as e:
        print(f"Error during requests: {e}")
        return set()
    
def get_a_tag_values(url):
    try:
        filename = "facebook.txt" 
        response = requests.get(url)

        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            facebook_links = []
            
            # ADD DAte on Txt File
            
            with open(filename, 'a+') as file:                    
                date = str(c)
                file.write("\n"+"DATE : " + date + '\n')
                file.close()

            # Find all <a> tags and extract their href attribute
            i=0
            for tag in soup.find_all('a'):
                href = tag.get('href')
                if href and 'facebook' in href.lower():
                    i+=1
                    save = "0"
                    time.sleep(0.3)
                    with open(filename, 'a+') as file:
                        if href not in facebook_links:
                            facebook_links.append(href)
                            file.write(href + '\n')
                            file.close()
                            save = "done"
                    if save == "done":
                        print(f"{i} {href} {current_time}   Saved in {filename}")
                        save == "not"
                    else:
                        print(f"{i} {href} {current_time}")
            if facebook_links:
                print(F"\n"+"Link End"+'\n')
        else:
            print(f"Failed to retrieve webpage: {response.status_code}")
       
    
    except requests.exceptions.RequestException as e:
        print(f"Error during requests: {e}")


def save_emails_to_file(emails, filename):
    try:
        with open(filename, 'a+') as file:                    
            date = str(c)
            file.write("\n"+"DATE : " + date + '\n')
            file.close()
        i = 0
        for email in emails:
            i+=1
            save = "0"
            time.sleep(0.3)
            emailAll = []
            with open(filename, 'a+') as file:
                if email not in emailAll:
                    emailAll.append(email)
                    file.write(email + '\n')
                    file.close()
                    save = "done"
                    if save == "done":
                        print(f"{i} {email} {current_time}   Saved in {filename}")
                        save == "not"
                    else:
                        print(f"{i} {email} {current_time}")
    except IOError as e:
        print(f"Error writing to file: {e}")


    


# Example usage:
if __name__ == "__main__":
    url = str(input('Enter Site Url : '))
    output_file = 'emails.txt' 
    emails = extract_emails(url)
    fb = get_a_tag_values(url)

    if emails:
        save_emails_to_file(emails, output_file)
    else:
        print("No email addresses found on the webpage.")
