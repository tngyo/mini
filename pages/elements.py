import streamlit as st
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.link_button("Open a new tab/window to view the source code here", "https://github.com/tngyo/mini/blob/main/main.py")

st.subheader("st.write's swiss knife prowess")
#st.write's swiss knife prowess
st.write("Hello World! with [Streamlit](https://www.streamlit.io) :smile: :wave: :100: :coffee:", 123, True, datetime.datetime.now().weekday())
st.write({"key":"value"})

st.subheader("Magic")
#Streamlit Magic
8 + 10 * 50 / 2.3
"Some text without explicit method call with Magic"
"This text instance is true" if True else "Then text instance is false"

st.subheader("st.markdown")
#Markdown is supported
st.markdown("**This is markdown bold text.**")

st.subheader("st.link_button st.code st.divider")
st.link_button("Go to gallery", "https://streamlit.io/gallery")

codes = """
    def hello_world():
        print('Hello, World!')
"""
st.code(codes, language="python")
st.code("print('Hello, World!')")

st.divider()

st.subheader("st.image")
st.image("static/TOC.jpg", width=250)

st.subheader("st.video")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.subheader("st.audio")
st.audio("https://www.sample-videos.com/audio/mp3/crowd-cheering.mp3")

st.subheader("st.dataframe st.data_editor st.table st.metric")
st.dataframe({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

edited_df = st.data_editor(df)

st.table(edited_df)

st.caption("Metric")
st.metric(label="Total rows", value=len(df))
st.metric(label="Total Age", value=df["Age"].sum())
st.metric(label="Average Age", value=round(df["Age"].mean(),1))

st.subheader("Json and dict")

sample_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "JavaScript", "HTML"]
    }

st.caption("Show dictionary with st.json")

st.json(sample_dict)

st.caption("Show dictionary with st.write (that's why it's a swiss knife) :smile:")

st.write(sample_dict)

st.subheader("st.title st.header st.subheader st.caption st.info st.success st.warning st.error")

st.title("Title")

st.header("Header")

st.subheader("Subheader")

st.caption("Caption")

st.info("This is an info message.")

st.success("This is a success message.")

st.warning("This is a warning message.")

st.error("This is an error message.")

st.subheader("st.button st.checkbox st.radio st.selectbox st.multiselect st.progress st.text_input st.number_input st.toast st.slider")

st.button("Click me!")

st.checkbox("Check this box")

st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])

st.selectbox("Select an item", ["Item 1", "Item 2", "Item 3"])

st.multiselect("Select multiple items", ["Item 1", "Item 2", "Item 3"])

st.progress(0.5)

st.text_input("Enter text", "Type here...")

st.number_input("Enter a number", 0)

st.toast("This is a toast message.")

st.slider("Slide me", 0, 100, 50)

st.subheader("st.date_input st.time_input st.color_picker st.file_uploader")

d = st.date_input("Enter a date", value=None)
st.write("Selected date is:", d)

t = st.time_input("Select a time", value=None)
st.write("Selected time is:", t)

c = st.color_picker("Pick a color", "#FF0000")
st.write("Selected color is:", c)

st.file_uploader("Upload a file")

st.subheader("st.area_chart, st.bar_chart, st.line_chart, st.scatter_chart")

chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["A", "B", "C"]
)

st.caption("Area Chart")
st.area_chart(chart_data)

st.caption("Bar Chart")
st.bar_chart(chart_data)

st.caption("Line Chart")
st.line_chart(chart_data)

scatter_data = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100)
})

st.caption("Scatter Chart")
st.scatter_chart(scatter_data)

st.subheader("st.map pyplot")

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], #coodinates around SF
    columns= ['latitude', 'longitude']
)

st.map(map_data)

fig, ax = plt.subplots()
ax.plot(chart_data["A"], label='A')
ax.plot(chart_data["B"], label='B')
ax.plot(chart_data["C"], label='C') 
ax.set_title('Pylot line chart')
ax.legend()
st.pyplot(fig)
