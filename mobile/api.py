from rest_framework import generics
from rest_framework.response import Response
from .serializer import MobileSerializer
from .models import Mobile

class MobileCreateApi(generics.CreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
class MobileApi(generics.ListAPIView):
    queryset= Mobile.objects.all()
    serializer_class=MobileSerializer
class MobileUpdateApi(generics.RetrieveUpdateAPIView):
    queryset= Mobile.objects.all()
    serializer_class=MobileSerializer
class MobileDeleteApi(generics.DestroyAPIView):
    queryset= Mobile.objects.all()
    serializer_class=MobileSerializer