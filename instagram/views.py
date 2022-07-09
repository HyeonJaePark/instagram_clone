from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print(1)
        return render(request, 'instagram/main.html')

    def post(self,request):
        print(2)
        return render(request, 'instagram/main.html')