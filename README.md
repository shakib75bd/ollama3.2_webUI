# Ollama Offline Chatbot Interface

A simple ChatGPT like chatbot interface that integrates with the Ollama model, allowing you to run commands and receive responses through a web-based UI.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Features
- Interactive chatbot UI similar to ChatGPT.
- Run commands and receive responses in real-time.
- Responsive design for various screen sizes.
- Easy to set up and use.

## Technologies Used
- **Python** - Backend framework (Django).
- **HTML/CSS** - Frontend interface.
- **JavaScript** - For handling user input and fetching responses.
- **Ollama** - Model integration for generating responses.

## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites
Make sure you have the following installed:
- Python (3.8 or above)
- Django
- Ollama (Ensure it's installed and configured correctly)
 <br>
**Install Ollama**
```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
```bash
   ollama  serve
   ```
 ```bash
   ollama run llama3.2
   ```
- Anaconda or virtual environment (optional but recommended)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shakib75bd/ollama3.2_webUI
   cd ollama3.2_webUI
   ```

2. **Create a Virtual Environment (Optional)**
   ```bash
   conda create -n ollamaChatbot python=3.9
   conda activate ollamaChatbot
   ```

3. **Install Required Packages**
   Ensure you are in the project directory and run:
   ```bash
   pip install django
   ```

4. **Start the Development Server**
    ```bash
    python manage.py runserver
    ```

5. **Access the Chatbot Interface**
    Open your web browser and go to:
    ```
    http://127.0.0.1:8000
    ```

## Usage
- Enter your command in the input field and click "Run Command" or press Enter.
- The chatbot will display the response in the chat box.

## Credits
- Shakib Hossen Shanto, 2024
