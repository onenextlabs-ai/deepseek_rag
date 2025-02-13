
# Document Intelligence

## Overview

Document Intelligence is an intelligent document assistant that helps you analyze and query PDF documents. It uses advanced natural language processing techniques to provide concise and factual answers to your queries based on the content of the uploaded documents.

## Features

- Upload and analyze PDF documents
- Split documents into smaller chunks for efficient processing
- Index document chunks into a vector store for quick retrieval
- Generate answers to user queries based on the context of the documents
- Professional and user-friendly UI

## Configuration

The application uses a configuration file (`config.py`) to store all configurable parameters for the UI and application settings. This makes it easy to customize the application according to your needs.

### UI Configuration

The `UI_CONFIG` dictionary in `config.py` contains parameters for customizing the appearance of the application, such as background colors, text colors, font family, and more.

### Application Configuration

The `APP_CONFIG` dictionary in `config.py` contains parameters for the application's functionality, such as the prompt template, PDF storage path, embedding model, and language model.

## Installation

1. Clone the repository:

   ```sh

   ```

git clone https://github.com/yourusername/deepseek_rag.git

    ```

2. Navigate to the project directory:

   ```sh

   ```

cd deepseek_rag

    ```

3. Install the dependencies using Pipenv:

   ```sh

   ```

pipenv install

    ```

4. Activate the virtual environment:

   ```sh

   ```

pipenv shell

    ```

## Usage

1. Run the Streamlit application:

   ```sh

   ```

streamlit run deep.py

    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.
3. Upload a PDF document using the file uploader.
4. Ask questions about the document using the chat input.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
