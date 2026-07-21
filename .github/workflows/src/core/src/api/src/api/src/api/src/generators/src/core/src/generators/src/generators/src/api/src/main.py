import logging
from datetime import datetime
from src.core.state_manager import StateManager
from src.core.content_history import ContentHistoryManager
from src.generators.topic_generator import TopicGenerator
from src.generators.article_writer import ArticleWriter
from src.generators.seo_optimizer import SEOOptimizer
from src.api.gemini_image import GeminiImageAPI
from src.api.blogger_api import BloggerAPI
from src.api.search_console_api import SearchConsoleAPI

# Setup Logging for Action Runner
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_automation_pipeline():
    """Phase 52: The Complete Hourly Pipeline[span_19](start_span)[span_19](end_span)."""
    logger.info("Starting AI Finance Blog Automation Pipeline...")

    # Initialize Modules
    state_mgr = StateManager()
    history_mgr = ContentHistoryManager()
    topic_gen = TopicGenerator()
    writer = ArticleWriter()
    seo = SEOOptimizer()
    image_api = GeminiImageAPI()
    blogger = BloggerAPI()
    gsc = SearchConsoleAPI()

    # Step 1: Check Automation State
    current_state = state_mgr.get_automation_state()
    if current_state.get('automation_status') != "Active":
        logger.info("Automation is currently paused. Exiting.")
        return

    # Step 2: Check Trending Priority Queue (Phase 16, 17)[span_20](start_span)[span_20](end_span)
    trending_data = topic_gen.check_trending_priority()
    
    if trending_data.get('trending'):
        logger.info(f"HIGH PRIORITY TREND DETECTED: {trending_data['topic']}[span_21](start_span)[span_21](end_span)")
        category = trending_data['category']
        topic = trending_data['topic']
        keywords = trending_data['keywords']
        is_trending = True
    else:
        # Step 3: Normal Category Rotation (Phase 15, 53)[span_22](start_span)[span_22](end_span)
        category = state_mgr.get_next_category()
        logger.info(f"Normal Rotation Category Selected: {category}[span_23](start_span)[span_23](end_span)")
        
        # Step 4: Subtopic Generation
        subtopic_data = topic_gen.generate_subtopic(category, used_subtopics=[])
        topic = subtopic_data['topic']
        keywords = [subtopic_data['primary_keyword']] + subtopic_data['secondary_keywords']
        is_trending = False

    # Step 5: Duplicate Detection (Phase 12)[span_24](start_span)[span_24](end_span)
    if history_mgr.is_duplicate_topic(topic, keywords[0]):
        logger.warning("Duplicate topic detected. Aborting this run to maintain diversity[span_25](start_span)[span_25](end_span).")
        return

    # Step 6: Content Generation & Editorial Review (Phase 7, 8, 9)[span_26](start_span)[span_26](end_span)
    article_html = writer.generate_and_review_article(topic, category, keywords)

    # Step 7: SEO Optimization & FAQ (Phase 10)[span_27](start_span)[span_27](end_span)
    seo_data = seo.generate_schema_and_faq(topic, article_html)
    labels = [category, "Finance"]
    if is_trending:
        labels.append("Breaking News")

    # Step 8: Image Generation (Phase 28)[span_28](start_span)[span_28](end_span)
    # image_bytes = image_api.generate_featured_image(topic) 
    # (Implementation for uploading image to a host and getting URL goes here)

    # Step 9: Blogger API Publishing (Phase 4)[span_29](start_span)[span_29](end_span)
    publish_result = blogger.publish_post(
        title=topic,
        content_html=article_html,
        labels=labels,
        is_draft=False # True for testing, False for production[span_30](start_span)[span_30](end_span)
    )

    if publish_result['status'] == 'success':
        # Step 10: Update State and History (Phase 13)[span_31](start_span)[span_31](end_span)
        if not is_trending:
            state_mgr.update_last_category(category)
            
        history_mgr.save_history({
            "post_id": publish_result['post_id'],
            "title": topic,
            "topic": topic,
            "category": category,
            "primary_keyword": keywords[0],
            "url": publish_result['url'],
            "is_trending": is_trending,
            "published_at": datetime.utcnow().isoformat()
        })

        # Step 11: Search Console & Sitemap (Phase 19, 38)[span_32](start_span)[span_32](end_span)
        gsc.ping_sitemap()
        logger.info(f"Pipeline completed successfully. URL: {publish_result['url']}")
    else:
        logger.error(f"Pipeline failed at publishing stage: {publish_result['message']}")

if __name__ == "__main__":
    run_automation_pipeline()
  
