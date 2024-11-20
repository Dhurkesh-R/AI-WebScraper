import streamlit as st
from scrape import scrape_website, extract_body_content, split_dom_content, clean_body_content
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")
        st.write("URL provided:", url)
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)

        st.session_state.dom_content = cleaned_content

        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
    else:
        st.write("Please enter a valid URL.")

if "dom_content" in  st.session_state:
    parse_description  = st.text_area("Describe What you want to parse.")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)