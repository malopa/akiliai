from django.shortcuts import render
from rest_framework.response import Response
import openai
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here


# Create your views here.

class OpenAIGPTView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
       input = request.GET.get('q')
       openai.api_key = "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"
       completion = openai.ChatCompletion.create(
       model="gpt-3.5-turbo", 
       messages=[{"role": "user", "content": input}]
       )
       answer = completion['choices'][0]['message']['content']
       return Response(answer)


# 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