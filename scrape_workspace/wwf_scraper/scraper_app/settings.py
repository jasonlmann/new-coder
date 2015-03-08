BOT_NAME = 'wwf'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = ['scraper_app.pipelines.WwfPipeline']

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'jmann',
	'password': '',
	'database': 'scrape'
}

