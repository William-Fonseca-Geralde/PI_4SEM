from django.shortcuts import render
from django.views import View
import requests

# Create your views here.
class IndexView(View):
  def get(self, request):
    return render(request, 'index.html')
  
class ApiTesteView(View):
  def get(self, request):
    return render(request, 'apiTeste.html')
  
  def apiCall(request):
    url = 'https://whois.whoisxmlapi.com/signup'
    
    response = request.get(url)
    
    if response.status_code == 200:
      dados = response.json()
      
      return JsonResponse(dados)
    else:
      return JsonResponse({'error': 'Erro ao fazer a chamada da API'}, status=500)