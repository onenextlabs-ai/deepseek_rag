
# UI Configuration
UI_CONFIG = {
    "background_color": "#0E1117",
    "text_color": "#FFFFFF",
    "font_family": "Arial, sans-serif",
    "chat_input_bg_color": "#1E1E1E",
    "chat_input_text_color": "#FFFFFF",
    "chat_input_border_color": "#3A3A3A",
    "chat_input_border_radius": "5px",
    "chat_input_padding": "10px",
    "user_message_bg_color": "#1E1E1E",
    "user_message_border_color": "#3A3A3A",
    "user_message_text_color": "#E0E0E0",
    "user_message_border_radius": "10px",
    "user_message_padding": "15px",
    "user_message_margin": "10px 0",
    "assistant_message_bg_color": "#2A2A2A",
    "assistant_message_border_color": "#404040",
    "assistant_message_text_color": "#F0F0F0",
    "assistant_message_border_radius": "10px",
    "assistant_message_padding": "15px",
    "assistant_message_margin": "10px 0",
    "avatar_bg_color": "#00FFAA",
    "avatar_text_color": "#000000",
    "avatar_border_radius": "50%",
    "avatar_padding": "5px",
    "file_uploader_bg_color": "#1E1E1E",
    "file_uploader_border_color": "#3A3A3A",
    "file_uploader_border_radius": "5px",
    "file_uploader_padding": "15px",
    "header_color": "#00FFAA",
    "button_bg_color": "#00FFAA",
    "button_text_color": "#000000",
    "button_border_radius": "5px",
    "button_padding": "10px 20px",
    "button_font_size": "16px",
    "button_hover_bg_color": "#00CC88"
}

# Application Configuration
APP_CONFIG = {
    "prompt_template": """
        You are an expert research assistant. Use the provided context to answer the query. 
        If unsure, state that you don't know. Be concise and factual (max 3 sentences).

        Query: {user_query} 
        Context: {document_context} 
        Answer:
    """,
    "pdf_storage_path": 'document_store/pdfs/',
    "embedding_model": "deepseek-r1:1.5b",
    "language_model": "deepseek-r1:1.5b"
}
