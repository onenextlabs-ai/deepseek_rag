import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from config import UI_CONFIG, APP_CONFIG

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {UI_CONFIG['background_color']};
        color: {UI_CONFIG['text_color']};
        font-family: {UI_CONFIG['font_family']};
    }}
    
    /* Chat Input Styling */
    .stChatInput input {{
        background-color: {UI_CONFIG['chat_input_bg_color']} !important;
        color: {UI_CONFIG['chat_input_text_color']} !important;
        border: 1px solid {UI_CONFIG['chat_input_border_color']} !important;
        border-radius: {UI_CONFIG['chat_input_border_radius']} !important;
        padding: {UI_CONFIG['chat_input_padding']} !important;
    }}
    
    /* User Message Styling */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {{
        background-color: {UI_CONFIG['user_message_bg_color']} !important;
        border: 1px solid {UI_CONFIG['user_message_border_color']} !important;
        color: {UI_CONFIG['user_message_text_color']} !important;
        border-radius: {UI_CONFIG['user_message_border_radius']} !important;
        padding: {UI_CONFIG['user_message_padding']} !important;
        margin: {UI_CONFIG['user_message_margin']} !important;
    }}
    
    /* Assistant Message Styling */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {{
        background-color: {UI_CONFIG['assistant_message_bg_color']} !important;
        border: 1px solid {UI_CONFIG['assistant_message_border_color']} !important;
        color: {UI_CONFIG['assistant_message_text_color']} !important;
        border-radius: {UI_CONFIG['assistant_message_border_radius']} !important;
        padding: {UI_CONFIG['assistant_message_padding']} !important;
        margin: {UI_CONFIG['assistant_message_margin']} !important;
    }}
    
    /* Avatar Styling */
    .stChatMessage .avatar {{
        background-color: {UI_CONFIG['avatar_bg_color']} !important;
        color: {UI_CONFIG['avatar_text_color']} !important;
        border-radius: {UI_CONFIG['avatar_border_radius']} !important;
        padding: {UI_CONFIG['avatar_padding']} !important;
    }}
    
    /* Text Color Fix */
    .stChatMessage p, .stChatMessage div {{
        color: {UI_CONFIG['text_color']} !important;
    }}
    
    .stFileUploader {{
        background-color: {UI_CONFIG['file_uploader_bg_color']} !important;
        border: 1px solid {UI_CONFIG['file_uploader_border_color']} !important;
        border-radius: {UI_CONFIG['file_uploader_border_radius']} !important;
        padding: {UI_CONFIG['file_uploader_padding']} !important;
    }}
    
    h1, h2, h3 {{
        color: {UI_CONFIG['header_color']} !important;
        font-family: {UI_CONFIG['font_family']} !important;
    }}
    
    .stButton button {{
        background-color: {UI_CONFIG['button_bg_color']} !important;
        color: {UI_CONFIG['button_text_color']} !important;
        border: none !important;
        border-radius: {UI_CONFIG['button_border_radius']} !important;
        padding: {UI_CONFIG['button_padding']} !important;
        font-size: {UI_CONFIG['button_font_size']} !important;
    }}
    
    .stButton button:hover {{
        background-color: {UI_CONFIG['button_hover_bg_color']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

PROMPT_TEMPLATE = APP_CONFIG['prompt_template']
PDF_STORAGE_PATH = APP_CONFIG['pdf_storage_path']
EMBEDDING_MODEL = OllamaEmbeddings(model=APP_CONFIG['embedding_model'])
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
LANGUAGE_MODEL = OllamaLLM(model=APP_CONFIG['language_model'])


def save_uploaded_file(uploaded_file) -> str:
    """
    Saves the uploaded file to disk and returns its file path.
    """
    try:
        file_path = PDF_STORAGE_PATH + uploaded_file.name
        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return ""

def load_pdf_documents(file_path):
    """
    Loads PDF documents from the provided file path.
    Returns an empty list if loading fails.
    """
    try:
        document_loader = PDFPlumberLoader(file_path)
        return document_loader.load()
    except Exception as e:
        st.error(f"Failed to load PDF: {e}")
        return []

def chunk_documents(raw_documents):
    """
    Splits raw documents into smaller chunks for processing.
    """
    text_processor = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return text_processor.split_documents(raw_documents)

def index_documents(document_chunks):
    """
    Indexes the document chunks into the vector store.
    """
    DOCUMENT_VECTOR_DB.add_documents(document_chunks)

def find_related_documents(query):
    """
    Searches for documents related to the query in the vector store.
    """
    return DOCUMENT_VECTOR_DB.similarity_search(query)

def generate_answer(user_query, context_documents):
    """
    Generates an answer to the user's query based on the context documents.
    """
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    response_chain = conversation_prompt | LANGUAGE_MODEL
    return response_chain.invoke({"user_query": user_query, "document_context": context_text})


# UI Configuration


st.title("📘 Document Intelligence")
st.markdown("### Your Intelligent Document Assistant")
st.markdown("---")

# File Upload Section
uploaded_pdf = st.file_uploader(
    "Upload Research Document (PDF)",
    type="pdf",
    help="Select a PDF document for analysis",
    accept_multiple_files=False

)

if uploaded_pdf:
    saved_path = save_uploaded_file(uploaded_pdf)
    raw_docs = load_pdf_documents(saved_path)
    processed_chunks = chunk_documents(raw_docs)
    index_documents(processed_chunks)
    
    st.success("✅ Document processed successfully! Ask your questions below.")
    
    user_input = st.chat_input("Enter your question about the document...")
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.spinner("Analyzing document..."):
            relevant_docs = find_related_documents(user_input)
            ai_response = generate_answer(user_input, relevant_docs)
            
        with st.chat_message("assistant", avatar="🤖"):
            st.write(ai_response)