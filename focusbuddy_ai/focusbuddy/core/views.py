import requests
import json
from django.shortcuts import render
from .forms import StudyForm
from .models import StudySession

GENAI_API_KEY = "PASTE_YOUR_API_KEY_HERE"

def get_gemini_response(prompt):
    """
    Connects directly to Google's API using the model available in your account.
    """
    
    target_model = "gemini-2.5-flash"
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{target_model}:generateContent?key={GENAI_API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            
            return f"Error {response.status_code}: {response.text}"
            
    except Exception as e:
        return f"Connection Failed: {str(e)}"

def home(request):
    response = None

    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            time = form.cleaned_data['time_available']
            energy = form.cleaned_data['energy_level']

            
            prompt = f"""
            You are a friendly study coach.
            Student wants to study '{subject}' for {time} minutes.
            Energy level: '{energy}'.
            
            Create a simple, realistic study plan with:
            - Clear time blocks
            - Small achievable tasks
            - A motivating tone
            """

            
            response = get_gemini_response(prompt)

            
            StudySession.objects.create(
                subject=subject,
                time_available=time,
                energy_level=energy,
                ai_response=response
            )
    else:
        form = StudyForm()

    return render(request, 'index.html', {'form': form, 'response': response})