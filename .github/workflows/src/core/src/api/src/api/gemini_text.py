import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

class GeminiTextAPI:
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_TEXT_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_TEXT_API_KEY is missing[span_9](start_span)[span_9](end_span).")
        
        genai.configure(api_key=self.api_key)
        # Using Gemini 1.5 Pro for complex reasoning and editorial quality
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')

    def generate_content(self, prompt: str, temperature: float = 0.7) -> str:
        """Generates text content based on the provided prompt."""
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    top_p=0.9,
                )
            )
            return response.text
        except Exception as e:
            logger.error(f"Gemini Text API Error: {e}")
            raise e

    def write_finance_article(self, topic: str, category: str, keywords: list) -> str:
        """Generates a professional, human-like finance article[span_10](start_span)[span_10](end_span)."""
        prompt = f"""
        Act as a Professional Finance Writer. Write an SEO-optimized, highly engaging, and accurate article about '{topic}' for the category '{category}'.
        
        Requirements:
        - Target Audience: USA and English-speaking audiences[span_11](start_span)[span_11](end_span).
        - Tone: Natural, Fluent, Professional, Clear, Engaging[span_12](start_span)[span_12](end_span).
        - Include Keywords naturally: {', '.join(keywords)}[span_13](start_span)[span_13](end_span).
        - Format with HTML tags suitable for Blogger (<h2>, <h3>, <p>, <ul>, <li>, <strong>)[span_14](start_span)[span_14](end_span).
        - Structure: Introduction, Main Points (with H2/H3), Actionable Advice, Key Takeaways, Conclusion, and FAQ[span_15](start_span)[span_15](end_span).
        - Ensure sentences are of variable length and avoid generic AI phrasing[span_16](start_span)[span_16](end_span).
        - Do NOT include markdown blocks (```html), just output raw HTML.
        """
        return self.generate_content(prompt, temperature=0.6)

    def generate_seo_metadata(self, article_text: str) -> dict:
        """Analyzes article and generates SEO title, meta description, and labels[span_17](start_span)[span_17](end_span)."""
        prompt = f"""
        Analyze the following article and provide SEO metadata in STRICT JSON format.
        JSON format required:
        {{
            "seo_title": "Optimized Title under 60 chars",
            "meta_description": "Compelling description under 150 chars",
            "url_slug": "optimized-url-slug",
            "blogger_labels": ["Label1", "Label2"]
        }}
        
        Article:
        {article_text[:2000]}...
        """
        response_text = self.generate_content(prompt, temperature=0.2)
        # In production, add robust JSON parsing/cleaning here
        import json
        clean_json = response_text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
      
