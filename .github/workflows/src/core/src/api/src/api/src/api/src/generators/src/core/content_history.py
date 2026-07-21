import os
import logging
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class ContentHistoryManager:
    def __init__(self):
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        if not url or not key:
            raise ValueError("Supabase credentials missing for Content History[span_10](start_span)[span_10](end_span).")
        self.supabase: Client = create_client(url, key)

    def is_duplicate_topic(self, topic: str, primary_keyword: str) -> bool:
        """Phase 12: Checks if the topic or keyword was recently used to ensure Content Diversity[span_11](start_span)[span_11](end_span)."""
        # Check by Title/Topic
        response_topic = self.supabase.table('content_history').select('*').ilike('topic', f"%{topic}%").execute()
        if len(response_topic.data) > 0:
            logger.warning(f"Duplicate detected based on topic: {topic}")
            return True
            
        # Check by Keyword
        response_keyword = self.supabase.table('content_history').select('*').ilike('primary_keyword', f"%{primary_keyword}%").execute()
        if len(response_keyword.data) > 0:
            logger.warning(f"Duplicate detected based on keyword: {primary_keyword}")
            return True

        return False

    def save_history(self, post_data: dict):
        """Phase 13: Saves the published article details to persistent storage[span_12](start_span)[span_12](end_span)."""
        try:
            # Expected post_data dict matches DB Schema
            self.supabase.table('content_history').insert(post_data).execute()
            logger.info(f"Successfully saved content history for post ID: {post_data.get('post_id')}")
        except Exception as e:
            logger.error(f"Failed to save content history: {e}")
          
