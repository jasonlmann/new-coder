from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scrapy import Selector
#from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import WwfArticle

class WwfSpider(CrawlSpider):
    """
    Spider for Working Waterfront.com
    """
    name = "wwf"
    allowed_domains = ["workingwaterfront.com"]
    start_urls = ["http://www.workingwaterfront.com/Arts"]
    
    rules = (       
        # Extract links to follow from starting category page
        Rule(LinkExtractor(allow=('/articles/*'), allow_domains=('workingwaterfront.com'), restrict_xpaths=('//div[@class="hp_feature"]/h2/a', )), callback='parse_items'),
        
        #Extract links from bottom pagination links
        Rule(LinkExtractor(allow=('/Articles/*'), restrict_xpaths=('//div[@id="pagingcontrols"]/a[contains(text(), "Next")]'))),
        
    )

    main_article_xpath = '//div[@id="article_detail"]'
	
    item_fields = {
        'title': './/h1/text()',
        'sub_hed': './/h2/text()',
        'author': './/div[@class="credit"]/text()',
        'content': './/div[@id="article_body"]/p',
        'publish_date': './/span[@class="date"]/text()'
    }

    def parse_items(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link
        """
        selector = Selector(response)

        # iterate over articles
        for article in selector.xpath(self.main_article_xpath):
            loader = ItemLoader(WwfArticle(), selector=article)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
