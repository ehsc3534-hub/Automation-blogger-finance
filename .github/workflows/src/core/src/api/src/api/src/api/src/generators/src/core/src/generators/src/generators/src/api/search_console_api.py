import os
import logging
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class SearchConsoleAPI:
    def __init__(self):
        # Reusing the OAuth credentials created for Blogger, ensuring GSC scope is added during auth[span_10](start_span)[span_10](end_span).
        self.client_id = os.environ.get("GOOGLE_CLIENT_ID")
        self.client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
        self.refresh_token = os.environ.get("GOOGLE_REFRESH_TOKEN")
        self.site_url = os.environ.get("WEBSITE_URL") # E.g., https://www.yourfinanceblog.com
        
        if self.refresh_token:
            self.credentials = Credentials(
                token=None,
                refresh_token=self.refresh_token,
                client_id=self.client_id,
                client_secret=self.client_secret,
                token_uri="https://oauth2.googleapis.com/token"
            )
            self.service = build('searchconsole', 'v1', credentials=self.credentials)

    def ping_sitemap(self):
        """Phase 19: Pings Google to refresh the XML/Atom feed Sitemap after publishing[span_11](start_span)[span_11](end_span)."""
        import requests
        sitemap_url = f"{self.site_url}/sitemap.xml"
        ping_url = f"https://www.google.com/ping?sitemap={sitemap_url}"
        try:
            response = requests.get(ping_url)
            if response.status_code == 200:
                logger.info("Successfully pinged Google regarding sitemap update[span_12](start_span)[span_12](end_span).")
            else:
                logger.warning(f"Sitemap ping returned status: {response.status_code}")
        except Exception as e:
            logger.error(f"Error pinging sitemap: {e}")

    def request_indexing(self, url: str):
        """Phase 20: Note that Google Indexing API is strict for regular blogs. 
        This is a placeholder for standard Search Console URL Inspection integration[span_13](start_span)[span_13](end_span)."""
        logger.info(f"Tracking indexing status for: {url}[span_14](start_span)[span_14](end_span).")
        # Direct indexing requests for standard articles are not supported by the Indexing API for non-news/job sites[span_15](start_span)[span_15](end_span).
        # We rely on the sitemap ping and organic crawl[span_16](start_span)[span_16](end_span).
        self.ping_sitemap()
        return "Monitoring via Sitemap"
      
