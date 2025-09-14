##Streamlit doesn't require it because it runs the script top-to-bottom every time the user interacts with the UI.

import streamlit as st
import pandas as pd

from langgraph.graph import StateGraph, END
from langgraph_flow.state import initial_state
from langgraph_flow.graph import build_graph

st.set_page_config(page_title="Agentic AI Workflow - Automotive", layout="wide")
st.title("Agentic AI Workflow: EV Battery Health Monitoring")

st.sidebar.header("Battery Data Upload")
file = st.sidebar.file_uploader("battery_logs.csv", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("📊 Sample Battery Data")
    st.dataframe(df.head())

    #Initial shared state with CSV data
    state = initial_state()
    state["battery_data_csv"] = df

    #Run the workflow graph
    if st.button("🔁 Run Agentic AI Workflow"):
        final_state = build_graph(state)
        st.success("✅ Workflow Complete")
    
        if "service_plan" in final_state:
            st.subheader("🛠️ Service Plan")
            st.json(final_state["service_plan"])
        
        if "appointment" in final_state:
            st.subheader("📅 Scheduled Appointment")
            st.json(final_state["appointment"])
        
        if "user_message" in final_state:
            st.subheader("✉️ Communication Summary")
            st.write(final_state["user_message"])

else:
    st.info("Please upload the 'battery_logs.csv' file to proceed.")