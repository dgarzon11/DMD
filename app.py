import streamlit as st

st.set_page_config(
    page_title="DMD Clinical Trials Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Welcome to the DMD Clinical Trials Dashboard")
st.markdown(
    """
    Use the menu on the left to navigate through the different sections of the dashboard:
    - **Overview**: Key metrics and general insights.
    - **Study Details**: Explore detailed data for current and historical studies.
    - **Historical Trends**: Analyze how clinical trials have evolved over time.
    - **Geographic Distribution**: Discover the geographic spread of clinical trials.
    - **Competitive Analysis**: Compare sponsors and their areas of focus.
    - **Download Reports**: Export datasets and visualizations.
    - **Insights & Recommendations**: Key findings and actionable strategies.
    """
)
