from bs4 import BeautifulSoup
import requests 

def run_algo():
    req = requests.get('https://hertie-scraping-website.vercel.app')
    soup = BeautifulSoup(req.content, 'html.parser')
    featured_article_text = soup.find_all('p', class_='text-base')
    html_str = str(soup)
    flags = []

    text_content= [item.text for item in featured_article_text]

    flags = []
    for text_content in text_content:  # replace 'your_list' with your actual list name
        if text_content.startswith('flag-'):
            flags.append(text_content)


    featured_article_text = soup.find_all('p', class_='text-base')

    for i in range(7,40):
        
        string = 'flag-' + str(i)
        div_info = soup.find('div', id=string)
        if div_info and div_info.get_text(strip=True):  
            flags.append(div_info.get('id'))

    
    featured_article_text = soup.find_all('div', class_='')
    for i in range(7, 40):
        class_name = f'flag-{i}'
        div_info = soup.find('div', class_=class_name)
        if div_info and div_info.get_text(strip=True):
            flags.append(class_name)
            
    return(flags)

if __name__ == "__main__":
    flags = run_algo()
    print(flags)
