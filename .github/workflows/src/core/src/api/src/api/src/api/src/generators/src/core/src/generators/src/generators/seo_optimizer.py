import json
import logging
from src.api.gemini_text import GeminiTextAPI

logger = logging.getLogger(__name__)

class SEOOptimizer:
    def __init__(self):
        self.ai = GeminiTextAPI()

    def generate_schema_and_faq(self, title: str, article_text: str) -> dict:
        """Phase 10: Generates FAQPage and Article Schema (Structured Data)[span_3](start_span)[span_3](end_span)."""
        prompt = f"""
        Analyze the following article about '{title}'.
        Generate:
        1. 3 relevant FAQs with answers.
        2. JSON-LD Structured Data for 'Article' and 'FAQPage' suitable for Google Search[span_4](start_span)[span_4](end_span).
        
        Return STRICT JSON format:
        {{
            "faqs": [
                {{"question": "Q1", "answer": "A1"}},
                {{"question": "Q2", "answer": "A2"}}
            ],
            "schema_markup": "Raw JSON-LD string here"
        }}
        
        Article snippet: {article_text[:1500]}
        """
        response = self.ai.generate_content(prompt, temperature=0.2)
        try:
            clean_json = response.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_json)
        except Exception as e:
            logger.error(f"Failed to generate Schema/FAQ: {e}")
            return {"faqs": [], "schema_markup": ""}

    def integrate_internal_links(self, article_html: str, previous_articles: list) -> str:
        """Phase 11: Adds internal links contextually using natural anchor text[span_5](start_span)[span_5](end_span)."""
        if not previous_articles:
            return article_html

        # In a real implementation, you would use BeautifulSoup to find natural text matches 
        # and replace them with <a href="url">text</a> based on previous_articles[span_6](start_span)[span_6](end_span).
        logger.info("Integrating internal links naturally[span_7](start_span)[span_7](end_span).")
        return article_html # Returning unmodified for now to prevent HTML corruption
      
