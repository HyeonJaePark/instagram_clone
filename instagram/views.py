from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print('GET 호출')
        return render(request, 'instagram/main.html')

    def post(self, request):
        print('POST 호출')
        return render(request, 'instagram/main.html')