from scrapy.item import Item, Field

class WwfArticle(Item):
    """Working Waterfront container (dictionary-like object) for scraped data"""
    title = Field()
    sub_hed = Field()
    author = Field()
    content = Field()
    publish_date = Field()
	
