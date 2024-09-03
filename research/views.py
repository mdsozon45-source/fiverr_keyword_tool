from rest_framework.response import Response
from rest_framework.decorators import api_view
from .fiverr_scraper import FiverrScraper,FiverrScraperTitle

@api_view(['GET'])
def fiverr_keyword_search(request, keyword):
    scraper = FiverrScraper()
    titles = scraper.get_keyword_data(keyword)
    
    if isinstance(titles, list):
        top_keywords = scraper.extract_top_keywords(titles)
        return Response({'top_keywords': top_keywords})
    else:
        return Response(titles, status=400)




@api_view(['GET'])
def keyword_research_and_title(request, keyword):
    scraper = FiverrScraperTitle()
    titles = scraper.get_keyword_data(keyword)
    
    if isinstance(titles, list):
        top_keywords = scraper.extract_top_keywords(titles)
        generated_title = scraper.generate_title(top_keywords)
        return Response({
            'top_keywords': top_keywords,
            'generated_title': generated_title
        })
    else:
        return Response(titles, status=400)

