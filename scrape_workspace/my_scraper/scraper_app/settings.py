BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['scraper_app.spiders']

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'jmann',
	'password': '',
	'database': 'scrape'
}

ITEM_PIPELINES = ['scrape_app.pipelines.LivingSocialPipeline']