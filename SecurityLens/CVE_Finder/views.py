# from django.shortcuts import render
# #from django.http import HttpResponse
# import openai
# from django.http import JsonResponse
# from django.conf import settings
# from UI.models import SearchQuery
# from .forms import UI_form



# # openai.api_key = settings.OPENAI_API_KEY
# # Create your views here.

# def index(request):
#     return HttpResponse('Home Page')

# def userInterface(request):

#     if request.method == 'POST':
#         fm = UI_form(request.POST)
#         if fm.is_valid():
            
#             query =  fm.cleaned_data['search_box']
#             db_data = SearchQuery(id = None, search_box=query)
#             db_data.save()

#     else:
#         fm = UI_form()
#     return render(request, 'UI_files/mainUI.html', {'forms':fm})  

#     #return render(request, 'UI_files/mainUI.html')




# # def showformdata(request):
# #     fm = UI_form()
# #     return render(request, 'UI_files/mainUI.html', {'forms':fm})


# def query_view(request): 
#     if request.method == 'POST': 
#         prompt = request.POST.get('prompt') 
#         response = get_completion(prompt) 
#         return JsonResponse({'response': response}) 
#     return render(request, 'UI_files/chat.html')



from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .openai_utils import get_chatgpt_response

@csrf_exempt  # Temporarily disable CSRF protection for testing (remove in production)


def cve_chatbot(request):
    # Handle GET request to render the HTML page
    if request.method == 'GET':
        return render(request, 'CVE_Finder/cve_chatbot.html')

    # Handle POST request for AJAX interactions
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message')
            if user_message:
                bot_response = get_chatgpt_response(user_message)
                return JsonResponse({'response': bot_response})
            return JsonResponse({'response': 'Error: No message provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'response': 'Error: Invalid JSON'}, status=400)

    return JsonResponse({'response': 'Error: Invalid request'}, status=400)