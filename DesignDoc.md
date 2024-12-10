# Image tagger

## What the app does
- On first open, it will prompt users to choose a folder.
- It will scan the folder and subfolder for images (png/jpg/jpeg) and initialize an index record (if not initialized in this folder, we can probably use a JSON as initialization record? This can also be used for tracking new/deleted images.)
- It will then create taggings of the images with Llama3.2 Vision with Ollama when "Start Tagging". It will create tags of elements/styles, a short description of the image, text within the images. The image path, tags, description, text within the images will be saved to a vector database for easier retrieval later.
- Users can then query the images with natural language. During querying, it will use full-text search, consine similarity to find the most relevant images.
- Users can browse the images on the UI, on click thumbnail, modal opens with image and its tags, description, and text within the image.

## UI
- Local server web page with Tailwind CSS, Vue3, and HTML.
    - Tailwind CSS CDN:   <script src="https://cdn.tailwindcss.com"></script>
    - Vue3 CDN: <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
- A search box at the top. Folders in the left side bar. Image grid in the main area.

## Backend
- Local server with Python FastAPI.
- Ollama for running Llama model:
```
import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['image.jpg']
    }]
)

print(response)
```
- ChromaDB for vector database.
