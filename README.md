# Ollama Chatbot Interface

A simple chatbot interface that integrates with the Ollama model, allowing you to run commands and receive responses through a web-based UI.

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
- Anaconda or virtual environment (optional but recommended)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ollama-chatbot.git
   cd ollama-chatbot
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

4. **Setup Django Project**
   - Navigate to the project directory and create a new Django project:
     ```bash
     django-admin startproject ollama_project
     cd ollama_project
     ```

5. **Create a Django App**
   ```bash
   python manage.py startapp chatbot
   ```

6. **Configure Settings**
   - Open `ollama_project/settings.py` and add your app to `INSTALLED_APPS`:
     ```python
     INSTALLED_APPS = [
         ...
         'chatbot',
     ]
     ```

7. **Setup URLs**
   - In `ollama_project/urls.py`, add the following:
     ```python
     from django.urls import path
     from chatbot import views

     urlpatterns = [
         path('run_command/', views.run_command, name='run_command'),
         # Add other URLs as needed
     ]
     ```

8. **Create a View for Command Execution**
   - In `chatbot/views.py`, create a view to handle command execution:
     ```python
     from django.http import JsonResponse
     import subprocess

     def run_command(request):
         if request.method == 'POST':
             command = request.POST.get('command')
             # Run the command and get the output
             result = subprocess.run(command.split(), capture_output=True, text=True)
             return JsonResponse({'result': result.stdout.strip(), 'error': result.stderr.strip()})
     ```

9. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

10. **Start the Development Server**
    ```bash
    python manage.py runserver
    ```

11. **Access the Chatbot Interface**
    Open your web browser and go to:
    ```
    http://127.0.0.1:8000
    ```

## Usage
- Enter your command in the input field and click "Run Command" or press Enter.
- The chatbot will display the response in the chat box.

## Credits
- Shakib Hossen Shanto, 2024
