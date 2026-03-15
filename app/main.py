import streamlit as st
import os
import sys

# Add the root directory to the Python path so it can find the agents folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.swarm_roles import create_data_wrangler, create_ml_diagnostic

# --- UI Setup ---
st.set_page_config(page_title="DiaBot Analytics Forge", layout="wide")
st.title("🧬 DiaBot Analytics Forge")
st.subheader("Autonomous Data Swarm (Track B: Quantitative Forge)")

st.markdown("""
**Mission:** Autonomously ingest, clean, and model messy medical datasets. 
""")

# --- Swarm Execution ---
if st.button("Initialize Swarm Mission", type="primary"):
    st.divider()
    
    # Phase 1: DataWrangler
    st.write("### 🧹 Phase 1: DataWrangler Agent Execution")
    with st.spinner("DataWrangler is analyzing and cleaning the dataset... (Check terminal for live logs)"):
        wrangler = create_data_wrangler()
        success_1, output_1 = wrangler.execute_task("Load 'data/raw_diabetes_data.csv', handle missing values, and save to 'data/clean_diabetes_data.csv'.")
        
        if success_1:
            st.success("DataWrangler Execution Complete!")
            st.code(output_1, language="text")
        else:
            st.error("DataWrangler encountered a fatal error.")
            st.stop()
            
    st.divider()
    
    # Phase 2: MLDiagnostic
    st.write("### 🧠 Phase 2: MLDiagnostic Agent Execution")
    with st.spinner("MLDiagnostic is training the Random Forest model... (Check terminal for live logs)"):
        ml_agent = create_ml_diagnostic()
        success_2, output_2 = ml_agent.execute_task("Load 'data/clean_diabetes_data.csv', train a Random Forest model, and print the accuracy and classification report.")
        
        if success_2:
            st.success("MLDiagnostic Execution Complete!")
            st.code(output_2, language="text")
            st.balloons() # A little celebration for completing the run
        else:
            st.error("MLDiagnostic encountered a fatal error.")