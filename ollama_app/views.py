from django.shortcuts import render
from django.http import JsonResponse
import subprocess

def index(request):
    return render(request, 'ollama_app/index.html')

def run_command(request):
    if request.method == 'POST':
        user_input = request.POST.get('command')  # Get the user input (e.g., "Hey")

        if user_input:
            try:
                # Run the llama3.2 model and pass the user input directly
                result = subprocess.run(
                    ['ollama', 'run', 'llama3.2', user_input],  # Pass input directly
                    capture_output=True, text=True, check=True
                )
                return JsonResponse({'result': result.stdout})
            except subprocess.CalledProcessError as e:
                return JsonResponse({
                    'error': f"Command failed with error: {e.stderr}",
                    'details': e.stderr
                })
        else:
            return JsonResponse({'error': 'No command provided'})
