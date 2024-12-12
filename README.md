# Image Tagger

This project is an image tagging and searching application that leverages the power of open-source local multimodal LLM like Llama 3.2 Vision and vector database like ChromaDB to provide a seamless image management experience.

## Features

-   **Folder Selection and Image Discovery**: On first launch, the application prompts users to select a folder by inputting the full path of a folder. It then recursively scans this folder and its subfolders to discover images (supports `png`, `jpg`, `jpeg`, and `webp` formats).
-   **Image Indexing**: Initializes a JSON-based index to track images within the selected folder. This index is updated dynamically to reflect new or deleted images.
-   **Intelligent Tagging**: Utilizes Llama 3.2 Vision with Ollama to generate descriptive tags for each image. This includes identifying elements/styles, creating a short description, and extracting any text present within the images.
-   **Vector Database Storage**: Stores image metadata (path, tags, description, text content) in a ChromaDB vector database for efficient retrieval. *Note: Vector search integration is planned for future updates.*
-   **Natural Language Search**: Enables users to search images using natural language queries. The application performs a full-text search on the stored metadata to find relevant images. *Note: Vector search integration is planned for future updates.*
-   **User Interface**: Provides a user-friendly web interface built with Tailwind CSS and Vue3 for browsing and interacting with images.
    -   **Image Grid**: Displays images in a responsive grid layout.
    -   **Image Modal**: On clicking a thumbnail, a modal opens, displaying the image along with its tags, description, and extracted text.
    -   **Progress Tracking**: Shows real-time progress during batch processing of images, including the number of processed and failed images.

## Prerequisites

-   **Python 3.7+**: Ensure Python is installed on your system.
-   **Ollama**: Install Ollama to run the Llama model. Follow the instructions on the [Ollama website](https://ollama.com/).
-   **ChromaDB**: ChromaDB will be installed as a Python package via pip.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Troyanovsky/llama-vision-image-tagger
    cd llama-vision-image-tagger
    ```

2. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Pull and Start the Ollama model:**

    Ensure the Llama 3.2 Vision model is running in Ollama. You may need to pull and start the model using Ollama's command-line interface. 

    Download the installer from [here](https://github.com/ollama/ollama) and install Ollama.

    Pull and run the Llama 3.2 Vision model:

    ```bash
    ollama run llama3.2-vision # For 11B model
    ```

## Usage

1. **Run the FastAPI backend:**

    ```bash
    uvicorn main:app --host 127.0.0.1 --port 8000
    ```

    This will start the server on `http://127.0.0.1:8000`.

2. **Access the web interface:**

    Open your web browser and navigate to `http://127.0.0.1:8000`.

3. **Select a folder:**

    Enter the path to the folder containing your images and click "Open Folder". The application will scan the folder and display the found images.

4. **Process images:**

    -   **Process All**: Click the "Process All" button to start tagging all unprocessed images. The progress will be displayed on the screen.
    -   **Process Individual Images**: Click the "Process Image" button in the image modal for a specific image to process it individually.

5. **Search images:**

    Enter your search query in the search bar and click "Search". The application will display images matching your query.

6. **Refresh images:**

    Click the "Refresh" button to rescan the folder and update the image list.

## Project Structure

-   `main.py`: Contains the FastAPI backend logic, including API endpoints for image processing, searching, and serving static files.
-   `image_processor.py`: Handles image processing using Ollama and updates the metadata.
-   `index.html`: The main HTML file for the frontend user interface with Tailwind CSS and Vue3.

## API Endpoints

-   `GET /`: Serves the main `index.html` page.
-   `POST /images`: Accepts a folder path and returns a list of images found in that folder.
-   `GET /image/{path:path}`: Serves an image file from the selected folder.
-   `POST /search`: Accepts a search query and returns a list of matching images.
-   `POST /refresh`: Refreshes the image list for the current folder.
-   `POST /process-image`: Processes a single image to generate tags, description, and extract text.

## Future Enhancements

-   **Vector Search**: Integrate vector search capabilities using ChromaDB to improve search accuracy and relevance.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.