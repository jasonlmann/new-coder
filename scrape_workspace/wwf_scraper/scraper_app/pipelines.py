from sqlalchemy.orm import sessionmaker
from models import Articles, db_connect, create_articles_table


class WwfPipeline(object):
    """Working Waterfront pipeline for storing scraped items in the database"""
    def __init__(self):
        """Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_articles_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save articles in the database.
		This method is called for every item pipeline component.
		"""
		
        session = self.Session()
        article = Articles(**item)

        try:
            session.add(article)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
