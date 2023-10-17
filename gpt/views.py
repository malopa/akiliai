from django.shortcuts import render
from rest_framework.response import Response
import openai
from rest_framework.views import APIView

# Create your views here.

class OpenAIGPTView(APIView):

   def get(self, request):
       input = request.GET.get('q')
       openai.api_key = "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"
       completion = openai.ChatCompletion.create(
       model="gpt-3.5-turbo", 
       messages=[{"role": "user", "content": input}]
       )
       answer = completion['choices'][0]['message']['content']
       return Response(answer)
