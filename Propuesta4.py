import requests
from bs4 import BeautifulSoup
import csv

def get_chiropractors(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    chiropractors = []
    
    for item in soup.find_all('div', class_='chiropractor'):
        name = item.find('h2', class_='name').text
        email = item.find('a', class_='email')['href'].replace('mailto:', '')
        phone = item.find('span', class_='phone').text
        practice = item.find('span', class_='practice').text
        location = item.find('span', class_='location').text
        
        chiropractors.append([name, email, phone, practice, location])
    
    return chiropractors

def save_to_csv(data, filename='chiropractors.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email', 'Phone', 'Practice', 'Location'])
        writer.writerows(data)

if __name__ == '__main__':
    url = 'https://example.com/chiropractors'
    chiropractors = get_chiropractors(url)
    save_to_csv(chiropractors)


"""
Note:

    Replace https://example.com/chiropractors with the actual URL from which you intend to scrape data.
    Ensure to comply with the website's terms of service and legal requirements related to web scraping.
    Enhance the code to handle pagination if the data spans multiple pages.
"""