import streamlit as st

# Title and text
st.title("Welcome to My Streamlit App")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("Here is some regular text.")

# Divider
st.divider()

# Columns for side-by-side content
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")


# Image
st.image("https://static.streamlit.io/examples/cat.jpg", caption="A cute cat")

# Button
if st.button("Click me!", use_container_width=True):
    st.success("Button clicked!")

# Expander for collapsible content
with st.expander("See more details"):
    st.write("Here is some more information inside an expander.")


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)