import logging
from src.api.gemini_text import GeminiTextAPI

logger = logging.getLogger(__name__)

class TopicGenerator:
    def __init__(self):
        self.ai = GeminiTextAPI()

    def check_trending_priority(self) -> dict:
        """Phase 16 & 17: Analyzes current breaking financial news for High Priority queue[span_14](start_span)[span_14](end_span)."""
        logger.info("Checking Trending Priority Queue...")
        
        prompt = """
        Analyze current real-world financial news. Is there any HIGH PRIORITY breaking financial event today (e.g., Fed Rate Hike, Major Bank Collapse, Huge Stock Market crash)?
        If YES, provide a topic and keywords in JSON.
        If NO, return {"trending": false}.
        
        Strict JSON format:
        {
            "trending": true/false,
            "topic": "Topic Name if true",
            "category": "Finance News",
            "priority": "HIGH",
            "keywords": ["keyword1", "keyword2"]
        }
        """
        
        response = self.ai.generate_content(prompt, temperature=0.1)
        
        import json
        try:
            clean_json = response.replace("```json", "").replace("```", "").strip()
            data = json.loads(clean_json)
            return data
        except json.JSONDecodeError:
            logger.error("Failed to parse trending data.")
            return {"trending": False}

    def generate_subtopic(self, category: str, used_subtopics: list) -> dict:
        """Phase 15: Generates a unique subtopic for a given category avoiding past ones[span_15](start_span)[span_15](end_span)."""
        used_str = ", ".join(used_subtopics)
        
        prompt = f"""
        You are a Finance Content Strategist. I need a highly engaging, specific blog post topic for the category '{category}'.
        Do NOT use these previously covered topics: {used_str}[span_16](start_span)[span_16](end_span).
        
        Return STRICT JSON format:
        {{
            "topic": "Specific Article Title/Topic",
            "primary_keyword": "main seo keyword",
            "secondary_keywords": ["kw1", "kw2", "kw3"]
        }}
        """
        response = self.ai.generate_content(prompt, temperature=0.7)
        
        import json
        try:
            clean_json = response.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_json)
        except json.JSONDecodeError:
            logger.error("Failed to parse subtopic data.")
            raise ValueError("Subtopic generation failed.")
          
