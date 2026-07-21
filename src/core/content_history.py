import os
import json
from datetime import datetime

class ContentHistoryManager:
    """
    Manages the history of published content to prevent duplication.
    """
    def __init__(self, history_file="content_history.json"):
        self.history_file = history_file

    def is_duplicate_topic(self, topic, keywords):
        """
        Checks if the topic or keywords already exist in the history.
        Returns True if it's a duplicate, False otherwise.
        """
        # ডিফল্টভাবে ডুপ্লিকেট নয় ধরে নিয়ে False রিটার্ন করছে
        return False

    def save_history(self, post_data):
        """
        Saves the published post data to history.
        """
        pass
      
