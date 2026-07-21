import os
import json

class StateManager:
    """
    Manages the automation state and category rotation for the finance blog.
    """
    def __init__(self, state_file="automation_state.json"):
        self.state_file = state_file

    def get_automation_state(self):
        """
        Retrieves the current automation state.
        Returns a dictionary containing the state status.
        """
        # ডিফল্টভাবে স্টেট 'Active' রিটার্ন করছে, প্রয়োজনে ফাইল থেকে রিড করতে পারেন
        return {"automation_status": "Active"}

    def get_next_category(self):
        """
        Returns the next content category for rotation.
        """
        categories = ["Personal Finance", "Investing", "Cryptocurrency", "Real Estate", "Taxes"]
        # সহজ উদাহরণের জন্য প্রথম ক্যাটাগরি রিটার্ন করা হচ্ছে
        return categories[0]

    def update_last_category(self, category):
        """
        Updates the record of the last used category.
        """
        pass
      
