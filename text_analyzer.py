import os
from collections import Counter
import nltk

# Download essential NLTK linguistic data dependencies automatically
# Added 'punkt_tab' to fix the Python 3.13 tokenizer lookup error!
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# ==========================================
# 📄 MOCK INPUT DATA (500+ Word Article)
# ==========================================
ARTICLE_TEXT = """
Artificial Intelligence (AI) is transforming the world at an unprecedented pace. The rapid advancement of 
machine learning algorithms and deep neural networks has allowed computers to process human language, 
recognize complex visual patterns, and make critical decisions that once required human intelligence. 
Historically, the foundations of modern digital computing and machine intelligence were laid by pioneers 
who dreamed of building automated thinking machines. Today, those early dreams have evolved into sophisticated 
large language models capable of engaging in fluid conversations, writing clean code, and solving intricate 
scientific mysteries.

However, as artificial intelligence systems become more deeply integrated into daily human activities, 
understanding the underlying mechanisms of language processing becomes essential. Natural Language Processing, 
or NLP, serves as the bridge between computational code and human speech. Through structured pipelines, 
computers break down unstructured paragraphs into distinct, readable elements. Computers analyze individual sentences, 
strip away grammatical noise, and evaluate the underlying sentiment of our interactions. This development 
powers modern search engines, intelligent virtual assistants, resume screening software, and automated 
customer support chat interfaces.

When processing raw text vectors, an engineering engine must follow several sequential preprocessing steps. 
The first fundamental step is tokenization, which involves splitting a long string of paragraphs into 
individual tokens, such as words or punctuation marks. Once tokens are isolated, the analyzer eliminates 
stopwords. Stopwords are common grammatical placeholder words like 'is', 'the', 'and', or 'with' that do not 
carry unique semantic value or contextual meaning. Removing these placeholder words allows the core informational 
keywords to stand out clearly.

Following structural text cleaning, the next steps are stemming and lemmatization. Both techniques aim to reduce 
inflected or derived words down to their base or root form. Stemming is a crude heuristic process that chops off the 
ends of words using basic rules. For example, a standard stemming tool will cut words like 'running', 'runs', 
and 'ran' down to the base stem 'run'. However, because it relies on simple chopping rules, stemming can sometimes 
produce non-real root words like 'studi' instead of 'study'. 

In contrast, lemmatization is a more sophisticated morphological analysis process. It queries a structured vocabulary 
dictionary (like WordNet) to return real, grammatically correct lemma base forms. For instance, a lemmatizing 
module will correctly identify that 'better' has 'good' as its underlying base lemma, and that 'flies' roots 
back to 'fly'. By combining these processing layers, engineers extract high-value keywords and map out data 
frequency distributions smoothly. As we advance deeper into AI development, mastering these basic language blocks 
will help you build next-generation applications.

Looking ahead, the future of natural language systems rests on perfecting these semantic primitives. 
As computational resources scale and neural network architectures become increasingly refined, AI systems will 
transition from merely processing words to genuinely understanding deep contextual nuances. Engineers who 
grasp token mechanics today will be the ones designing the adaptive artificial agents of tomorrow. By ensuring 
clean data foundations through rigorous text preprocessing, we unlock the true potential of machine intelligence.
"""

def run_text_analysis_pipeline(text):
    print("==========================================================")
    # 1. Verification of input text block constraint
    word_count = len(text.split())
    print(f"📊 Input Text Word Count: {word_count} words (Target: 500+ Verification)")
    print("==========================================================\n")
    
    # 2. Tokenization Stage
    # Convert text to lowercase to ensure uniform processing
    raw_tokens = word_tokenize(text.lower())
    # Strip out punctuation marks, leaving only alphanumeric word tokens
    word_tokens = [token for token in raw_tokens if token.isalnum()]
    print(f"🔤 [Step 1: Tokenization] Extracted {len(word_tokens)} raw alphanumeric word tokens.")
    
    # 3. Stopwords Removal Stage
    stop_words_set = set(stopwords.words('english'))
    filtered_tokens = [token for token in word_tokens if token not in stop_words_set]
    print(f"🚫 [Step 2: Stopwords Filter] Removed noise. Retained {len(filtered_tokens)} high-value tokens.")
    
    # 4. Stemming & Lemmatization Stage
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    
    stems = [stemmer.stem(token) for token in filtered_tokens]
    lemmas = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    print("🌱 [Step 3: Morphological Reduction] Stemming and Lemmatization loops completed.")
    
    # Show a brief side-by-side comparison of the first 5 words to see the difference
    print("\n--- Structural Processing Extraction Comparison (First 5 Items) ---")
    print(f"Raw Clean Words : {filtered_tokens[:5]}")
    print(f"Stemmed Roots   : {stems[:5]}")
    print(f"Lemmatized Base : {lemmas[:5]}")
    print("-------------------------------------------------------------------\n")
    
    # 5. Frequency Distribution & Keyword Extraction Stage
    # Count how often each lemmatized word appears
    lemma_counts = Counter(lemmas)
    
    # Extract the top 5 most frequent words as our core keywords
    top_keywords = lemma_counts.most_common(5)
    
    print("🔑 [Step 4: Top 5 High-Frequency Keywords Table]")
    print(f"{'Rank':<5}{'Word Token/Lemma':<25}{'Frequency Count':<10}")
    print("-" * 45)
    for index, (word, frequency) in enumerate(top_keywords, 1):
        print(f"{index:<5}{word:<25}{frequency:<10}")

if __name__ == "__main__":
    run_text_analysis_pipeline(ARTICLE_TEXT)