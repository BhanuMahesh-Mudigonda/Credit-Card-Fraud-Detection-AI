import streamlit as st

def stats_row():

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric("Transactions","284,807","+18%")

    with c2:
        st.metric("Frauds","492","-2%")

    with c3:
        st.metric("Accuracy","99.95%")

    with c4:
        st.metric("AI Status","ONLINE")