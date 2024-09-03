from sklearn.feature_extraction.text import TfidfVectorizer
import requests
from bs4 import BeautifulSoup

class FiverrScraper:
    def __init__(self):
        self.base_url = 'https://www.fiverr.com/search/gigs?query='

    def get_keyword_data(self, keyword):
        url = f"{self.base_url}{keyword.replace(' ', '%20')}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {e}"}

        soup = BeautifulSoup(response.content, 'html.parser')
        titles = []
        gigs = soup.find_all('div', class_='gig-card-layout')

        for gig in gigs:
            title_element = gig.find('p', class_='QTdEgIS')  # Adjust class as necessary
            title = title_element.text.strip() if title_element else 'No title found'
            titles.append(title)

        return titles

    def extract_top_keywords(self, titles, num_keywords=5):
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        X = vectorizer.fit_transform(titles)
        
        feature_names = vectorizer.get_feature_names_out()
        tfidf_scores = X.sum(axis=0).A1
        keyword_scores = dict(zip(feature_names, tfidf_scores))
        
        sorted_keywords = sorted(keyword_scores.items(), key=lambda x: x[1], reverse=True)
        
        top_keywords = [keyword for keyword, score in sorted_keywords[:num_keywords]]
        
        return top_keywords




class FiverrScraperTitle:

    def __init__(self):
        self.base_url = 'https://www.fiverr.com/search/gigs?query='

    def get_keyword_data(self, keyword):
        url = f"{self.base_url}{keyword.replace(' ', '%20')}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {e}"}

        soup = BeautifulSoup(response.content, 'html.parser')
        titles = []
        gigs = soup.find_all('div', class_='gig-card-layout')

        for gig in gigs:
            title_element = gig.find('p', class_='QTdEgIS')
            title = title_element.text.strip() if title_element else 'No title found'
            titles.append(title)

        return titles

    def extract_top_keywords(self, titles, num_keywords=5):
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        X = vectorizer.fit_transform(titles)
        
        feature_names = vectorizer.get_feature_names_out()
        tfidf_scores = X.sum(axis=0).A1
        keyword_scores = dict(zip(feature_names, tfidf_scores))
        
        sorted_keywords = sorted(keyword_scores.items(), key=lambda x: x[1], reverse=True)
        
        top_keywords = [keyword for keyword, score in sorted_keywords[:num_keywords]]
        
        return top_keywords

    def generate_title(self, top_keywords):
        base_action = "I will"
        keywords_phrase = ' & '.join(top_keywords[:3])  # Use up to top 3 keywords
        
        if 'django' in top_keywords and 'python' in top_keywords:
            action = "create"
            description = "web applications"
        elif 'react' in top_keywords:
            action = "build"
            description = "React apps"
        elif 'python' in top_keywords:
            action = "develop"
            description = "Python solutions"
        else:
            action = "offer"
            description = "expert services"

        # Create a title template
        generated_title = f"{base_action} {action} {description} using {keywords_phrase}"
        
        # Ensure the title is within 80 characters
        if len(generated_title) > 80:
            # Further refine the title to fit within 80 characters
            description = "apps" if len(description) > 4 else description
            generated_title = f"{base_action} {action} {description} with {keywords_phrase}"
            
            if len(generated_title) > 80:
                # Trim keywords if necessary
                keywords_phrase = ' & '.join(top_keywords[:2])
                generated_title = f"{base_action} {action} {description} with {keywords_phrase}"
        
        return generated_title


