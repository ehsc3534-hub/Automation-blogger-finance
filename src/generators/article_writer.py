class ArticleWriter:
    """
    Writes blog articles using the generated topics.
    """
    def generate_article(self, topic_data):
        """
        Generates the article content based on the topic data.
        Returns a dictionary containing the title and content.
        """
        return {
            "title": topic_data.get("topic", "Financial Freedom Guide"),
            "content": "<h2>Introduction</h2><p>Managing your finances effectively is crucial for long-term success.</p>"
        }
      
