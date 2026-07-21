import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BloggerAPI:
    def __init__(self):
        self.blog_id = os.environ.get("BLOGGER_BLOG_ID")
        self.client_id = os.environ.get("GOOGLE_CLIENT_ID")
        self.client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
        self.refresh_token = os.environ.get("GOOGLE_REFRESH_TOKEN")
        
        if not all([self.blog_id, self.client_id, self.client_secret, self.refresh_token]):
            raise ValueError("Blogger API credentials missing in environment variables[span_5](start_span)[span_5](end_span).")

        self.credentials = Credentials(
            token=None,
            refresh_token=self.refresh_token,
            client_id=self.client_id,
            client_secret=self.client_secret,
            token_uri="https://oauth2.googleapis.com/token"
        )
        self.service = build('blogger', 'v3', credentials=self.credentials)

    def publish_post(self, title: str, content_html: str, labels: list, is_draft: bool = False):
        """Publishes a post to Blogger and returns the URL and Post ID[span_6](start_span)[span_6](end_span)."""
        try:
            body = {
                "kind": "blogger#post",
                "title": title,
                "content": content_html,
                "labels": labels
            }
            
            logger.info(f"Publishing post: {title}")
            request = self.service.posts().insert(
                blogId=self.blog_id, 
                body=body, 
                isDraft=is_draft
            )
            response = request.execute()
            
            logger.info(f"Successfully published: {response.get('url')}")
            return {
                "post_id": response.get("id"),
                "url": response.get("url"),
                "status": "success"
            }
            
        except HttpError as error:
            logger.error(f"An error occurred while publishing to Blogger: {error}")
            return {"status": "error", "message": str(error)}

# Testing the module
if __name__ == "__main__":
    blogger = BloggerAPI()
    test_result = blogger.publish_post(
        title="Test Finance Post",
        content_html="<h1>Test</h1><p>This is a test post for the AI Finance Blog.</p>",
        labels=["Finance News", "Test"],
        is_draft=True # Testing as draft first
    )
    print(test_result)
          
