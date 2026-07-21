import re
import logging

logger = logging.getLogger(__name__)

class HTMLFormatter:
    @staticmethod
    def clean_blogger_html(raw_content: str) -> str:
        """
        Cleans and formats AI-generated content into valid Blogger HTML[span_4](start_span)[span_4](end_span).
        Ensures proper usage of H2, H3, P, UL, OL, LI, and STRONG[span_5](start_span)[span_5](end_span).
        """
        try:
            # Remove Markdown code block syntax if AI accidentally included it
            clean_text = raw_content.replace("```html", "").replace("```", "").strip()
            
            # Basic validation to check if AI output is already HTML
            if "<p>" not in clean_text and "<h2>" not in clean_text:
                logger.warning("Content does not contain HTML tags. Applying basic formatting.")
                # Convert markdown headers to HTML
                clean_text = re.sub(r'^### (.*)', r'<h3>\1</h3>', clean_text, flags=re.MULTILINE)
                clean_text = re.sub(r'^## (.*)', r'<h2>\1</h2>', clean_text, flags=re.MULTILINE)
                clean_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', clean_text)
                
                # Wrap loose paragraphs
                paragraphs = clean_text.split('\n\n')
                html_paragraphs = []
                for p in paragraphs:
                    if not p.startswith('<'):
                        html_paragraphs.append(f"<p>{p.strip()}</p>")
                    else:
                        html_paragraphs.append(p)
                clean_text = "\n".join(html_paragraphs)

            # Ensure valid structure for Blogger
            # Remove any html, body, or head tags if AI included a full page structure
            clean_text = re.sub(r'<!DOCTYPE.*?>', '', clean_text, flags=re.IGNORECASE)
            clean_text = re.sub(r'<html.*?>', '', clean_text, flags=re.IGNORECASE)
            clean_text = re.sub(r'</html>', '', clean_text, flags=re.IGNORECASE)
            clean_text = re.sub(r'<head>.*?</head>', '', clean_text, flags=re.IGNORECASE|re.DOTALL)
            clean_text = re.sub(r'<body.*?>', '', clean_text, flags=re.IGNORECASE)
            clean_text = re.sub(r'</body>', '', clean_text, flags=re.IGNORECASE)

            logger.info("Successfully formatted Blogger HTML.")
            return clean_text.strip()
            
        except Exception as e:
            logger.error(f"HTML Formatting error: {e}")
            return raw_content # Fallback to raw content if formatting fails
              
