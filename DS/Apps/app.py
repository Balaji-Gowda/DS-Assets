import streamlit as st
import requests
import pandas as pd
import altair as alt
import urllib3

# 🔕 Suppress SSL warnings (for ngrok)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 🖥️ Streamlit UI setup
st.set_page_config(page_title="Power BI DAX Chatbot", layout="wide")
st.title("🔍 Power BI DAX Chatbot")

query = st.text_input("Ask a question about your Power BI data:")

if st.button("Generate & Execute"):
    if query:
        with st.spinner("Generating DAX and querying Power BI..."):
            try:
                # 🔗 Call FastAPI backend via ngrok (SSL verify disabled)
                response = requests.post(
                    "https://4829165c0477.ngrok-free.app/query-and-execute",
                    json={"question": query},
                    verify=False  # 👈 disables SSL verification
                )

                if response.status_code == 200:
                    data = response.json()

                    # 🧠 Show generated DAX
                    st.subheader("🧠 Generated DAX Query")
                    st.code(data["dax_query"], language="DAX")

                    # 📊 Show result table
                    st.subheader("📊 Power BI Result")
                    rows = data["result"]["results"][0]["tables"][0]["rows"]
                    df = pd.DataFrame(rows)
                    st.dataframe(df)

                    # 📈 Chart options
                    numeric_cols = df.select_dtypes(include='number').columns
                    if not df.empty and len(numeric_cols) > 0:
                        st.subheader("📈 Chart")
                        chart_type = st.selectbox("Choose chart type", ["Bar", "Line", "Pie"])
                        x_col = st.selectbox("X-axis", df.columns)
                        y_col = st.selectbox("Y-axis", numeric_cols)

                        if chart_type == "Bar":
                            chart = alt.Chart(df).mark_bar().encode(x=x_col, y=y_col)
                        elif chart_type == "Line":
                            chart = alt.Chart(df).mark_line().encode(x=x_col, y=y_col)
                        elif chart_type == "Pie":
                            chart = alt.Chart(df).mark_arc().encode(theta=y_col, color=x_col)

                        st.altair_chart(chart, use_container_width=True)

                    # 📥 Export to CSV
                    st.subheader("📥 Export Result")
                    csv = df.to_csv(index=False).encode("utf-8")
                    st.download_button("Download CSV", csv, "result.csv", "text/csv")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Unexpected error: {e}")
