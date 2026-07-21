import streamlit as st
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Finance Blog Admin Dashboard", layout="wide")[span_8](start_span)[span_8](end_span)

@st.cache_resource
def init_db():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    return create_client(url, key)

supabase = init_db()

st.title("⚙️ AI Finance Blog Admin Dashboard")[span_9](start_span)[span_9](end_span)

# Section 1: Automation Status & Controls[span_10](start_span)[span_10](end_span)
st.header("Automation Controls")[span_11](start_span)[span_11](end_span)
state_res = supabase.table('automation_state').select('*').eq('id', 1).execute()
current_state = state_res.data[0] if state_res.data else None

if current_state:
    status = current_state['automation_status']
    st.metric(label="Current System Status", value=status)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Start/Resume Automation"):
            supabase.table('automation_state').update({"automation_status": "Active"}).eq('id', 1).execute()
            st.success("Automation Started!")
            st.rerun()
    with col2:
        if st.button("⏸️ Pause Automation"):
            supabase.table('automation_state').update({"automation_status": "Paused"}).eq('id', 1).execute()
            st.warning("Automation Paused!")
            st.rerun()

# Section 2: Content History & Published Posts[span_12](start_span)[span_12](end_span)
st.header("📚 Published Content History")[span_13](start_span)[span_13](end_span)
history_res = supabase.table('content_history').select('*').order('published_at', desc=True).limit(10).execute()

if history_res.data:
    st.dataframe(history_res.data, use_container_width=True)
else:
    st.info("No content published yet.")

# Section 3: Error Logs / Failed Posts (Mockup view for DB implementation)[span_14](start_span)[span_14](end_span)
st.header("⚠️ Error Logs & Retry Status")[span_15](start_span)[span_15](end_span)
st.text("Check GitHub Actions workflow logs for detailed tracebacks.[span_16](start_span)[span_16](end_span)")
  
