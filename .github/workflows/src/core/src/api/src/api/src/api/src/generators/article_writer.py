import logging
from src.api.gemini_text import GeminiTextAPI

logger = logging.getLogger(__name__)

class ArticleWriter:
    def __init__(self):
        self.ai = GeminiTextAPI()

    def generate_and_review_article(self, topic: str, category: str, keywords: list) -> str:
        """Handles Phase 7, 8, and 9: Generation, Editorial Review, and Fact Checking[span_3](start_span)[span_3](end_span)."""
        
        # Step 1: Initial Content Generation (Phase 7)
        logger.info(f"Generating initial draft for: {topic}")
        initial_draft = self.ai.write_finance_article(topic, category, keywords)
        
        # Step 2 & 3: Editorial Review & Fact Checking (Phase 8 & 9)
        logger.info(f"Conducting Editorial Review and Fact Check for: {topic}")
        review_prompt = f"""
        You are a Senior Financial Editor. Review and refine the following finance article draft[span_4](start_span)[span_4](end_span).
        
        Tasks:
        1. Fact Check: Verify all financial concepts. Ensure it complies with YMYL (Your Money or Your Life) standards[span_5](start_span)[span_5](end_span). Add disclaimers if needed[span_6](start_span)[span_6](end_span).
        2. Editorial Review: Improve flow, transition, and professionalism. Remove generic AI phrases. Ensure human-like variability in sentence structure[span_7](start_span)[span_7](end_span).
        3. Formatting: Ensure clean HTML tags suitable for Blogger (H2, H3, P, UL, LI, STRONG)[span_8](start_span)[span_8](end_span). Do NOT use markdown code blocks.
        
        Draft:
        {initial_draft}
        """
        
        final_article = self.ai.generate_content(review_prompt, temperature=0.5)
        
        # Clean potential markdown artifacts
        final_article = final_article.replace("```html", "").replace("```", "").strip()
        
        return final_article
      
