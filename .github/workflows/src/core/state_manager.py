import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load variables for local testing
load_dotenv()

class StateManager:
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        if not url or not key:
            raise ValueError("Database credentials missing. Check GitHub Secrets.") # Error handling[span_57](start_span)[span_57](end_span)
        self.supabase: Client = create_client(url, key)
        self.categories = [
            "Finance News", 
            "Personal Finance", 
            "Credit Cards", 
            "Loans & Debt", 
            "Investing", 
            "Banking", 
            "Financial Book Summaries"
        ] # Normal Rotation[span_58](start_span)[span_58](end_span)

    def get_automation_state(self):
        """Fetches the current state of automation from persistent storage[span_59](start_span)[span_59](end_span)."""
        response = self.supabase.table('automation_state').select("*").eq('id', 1).execute()
        if not response.data:
            # Initialize if empty
            default_state = {"id": 1, "last_category_index": -1, "automation_status": "Active"}
            self.supabase.table('automation_state').insert(default_state).execute()
            return default_state
        return response.data[0]

    def get_next_category(self):
        """Calculates the next category avoiding consecutive duplicates[span_60](start_span)[span_60](end_span)."""
        state = self.get_automation_state()
        if state['automation_status'] != "Active":
            return None # Paused from Admin Dashboard[span_61](start_span)[span_61](end_span)

        next_index = (state['last_category_index'] + 1) % len(self.categories)
        return self.categories[next_index]

    def update_last_category(self, category_name):
        """Updates the rotation index after successful publish[span_62](start_span)[span_62](end_span)."""
        index = self.categories.index(category_name)
        self.supabase.table('automation_state').update(
            {"last_category_index": index}
        ).eq('id', 1).execute()

# Test the State Manager
if __name__ == "__main__":
    manager = StateManager()
    next_cat = manager.get_next_category()
    print(f"Next Category to Publish: {next_cat}")
      
