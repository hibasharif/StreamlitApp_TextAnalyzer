import streamlit as st
import re

# Custom CSS for better UI
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .main-container {
            background: #ffffff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .title {
            color: #222222;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 16px;
            color: #666666;
            margin-bottom: 20px;
        }
        .section {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            border-left: 5px solid #4CAF50;
        }
        .warning {
            background-color: #fff3cd;
            padding: 10px;
            border-radius: 5px;
            color: #856404;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div class='main-container'>
        <h1 class='title'>📝 Text Analyzer</h1>
        <p class='subtitle'>By Hiba Sharif</p>
    </div>
""", unsafe_allow_html=True)

# User Input
text = st.text_area("Enter the Paragraph:")

search_word = st.text_input("🔍 Enter a word to search for:")
replace_word = st.text_input("✍ Enter a word to replace it with:")

if st.button("Analyze Paragraph"):
    if text.strip():
        # Word and Character Count
        words = text.split()
        num_words = len(words)
        num_chars = len(text)
        
        # Vowel Count
        num_vowels = len(re.findall(r'[aeiouAEIOU]', text))
        
        # Consonant Count
        num_consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text))
        
        # Sentence Count
        num_sentences = len(re.findall(r'[.!?]', text))
        
        # Longest and Shortest Words
        longest_word = max(words, key=len) if words else "N/A"
        shortest_word = min(words, key=len) if words else "N/A"
        
        # Search and Replace
        modified_text = text.replace(search_word, replace_word) if search_word else text
        
        # Uppercase and Lowercase Conversion
        upper_text = text.upper()
        lower_text = text.lower()
        
        # Operators & Type Casting
        avg_word_length = round(num_chars / num_words, 2) if num_words > 0 else 0
        contains_python = "Yes" if "python" in text.lower() else "No"
        
        # Display Results
        st.markdown(f"<div class='section'><b>📖 Total Words:</b> {num_words}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>🔢 Total Characters:</b> {num_chars}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>🗣 Vowel Count:</b> {num_vowels}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>📝 Consonant Count:</b> {num_consonants}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>📜 Sentence Count:</b> {num_sentences}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>🔠 Longest Word:</b> {longest_word}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>🔡 Shortest Word:</b> {shortest_word}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>🐍 Contains 'Python'?</b> {contains_python}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>📏 Average Word Length:</b> {avg_word_length}</div>", unsafe_allow_html=True)
        
        st.markdown(f"<div class='section'><b>📝 Modified Text:</b><br>{modified_text}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>🔠 Uppercase:</b><br>{upper_text}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section'><b>🔡 Lowercase:</b><br>{lower_text}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='warning'>⚠️ Please enter a paragraph before submitting!</div>", unsafe_allow_html=True)
