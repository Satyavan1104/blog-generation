import streamlit as st
import cohere

# Initialize Cohere API client (replace 'YOUR_API_KEY' with your Cohere API key)
cohere_client = cohere.Client('Mrh9BFF0YcKhl4jp5JC7ijKj0JwpQXdKFiz2aWm4')

## Function to get response from Cohere

def getCohereResponse(input_text, no_words, blog_style):
    # Generate the prompt
    template = f"""
        Write a blog for {blog_style} job profile on the topic "{input_text}" within {no_words} words.
    """
    
    # Generate text using Cohere
    response = cohere_client.generate(
        model='command-xlarge-nightly',
        prompt=template,
        max_tokens=int(no_words),  # Ensure the word count aligns with token limits
        temperature=0.7  # Adjust creativity level
    )
    
    # Extract and return the generated text
    return response.generations[0].text


st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

# Input for blog topic
input_text = st.text_input("Enter the Blog Topic")

# Creating two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words', value='250')  # Default value
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'),
                              index=0)

submit = st.button("Generate")

# Final response
if submit:
    if input_text and no_words.isdigit():
        with st.spinner("Generating blog..."):
            response = getCohereResponse(input_text, no_words, blog_style)
            st.markdown("### Generated Blog")
            st.write(response)
    else:
        st.error("Please provide a valid blog topic and a numeric word count!")
