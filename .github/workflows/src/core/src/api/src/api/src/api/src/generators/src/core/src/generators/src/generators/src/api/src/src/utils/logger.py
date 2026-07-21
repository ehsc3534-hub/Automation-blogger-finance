import time
import logging
from functools import wraps

# Setup robust logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("FinanceAutoBlog")

def retry_with_backoff(retries=3, backoff_in_seconds=2):
    """
    Decorator for Phase 24: Handles API Rate Limits, Network Errors, or Quota Limits
    with Exponential Backoff[span_3](start_span)[span_3](end_span).
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if x == retries:
                        logger.error(f"Failed after {retries} retries in {func.__name__}. Error: {str(e)}[span_4](start_span)[span_4](end_span)")
                        raise e
                    sleep_time = (backoff_in_seconds * 2 ** x)
                    logger.warning(f"Error in {func.__name__}: {str(e)}. Retrying in {sleep_time} seconds...[span_5](start_span)[span_5](end_span)")
                    time.sleep(sleep_time)
                    x += 1
        return wrapper
    return decorator
      
