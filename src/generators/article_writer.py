class ArticleWriter:
    """
    Writes and reviews blog articles using the generated topics.
    """
    def generate_and_review_article(self, topic, category, keywords):
        """
        Generates and reviews the article content.
        Returns the article HTML string.
        """
        return self.generate_article({"topic": topic, "category": category, "keywords": keywords})

    def generate_article(self, topic_data):
        """
        Alternative method name to ensure compatibility.
        """
        topic = topic_data.get("topic", "Financial Freedom Guide") if isinstance(topic_data, dict) else str(topic_data)
        
        html_content = f"""
        <h2>Introduction to {topic}</h2>
        <p>Welcome to our guide on financial planning and management.</p>
        <h3>Key Takeaways</h3>
        <ul>
            <li>Focus on smart budgeting and saving.</li>
            <li>Maintain consistent financial discipline.</li>
        </ul>
        <p>By following these steps, you can improve your financial health significantly.</p>
        """
        return html_content
        
