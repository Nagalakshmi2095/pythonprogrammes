from django.shortcuts import render
from rest_framework import generics
from .models import Notemodel
from .serializers import  NoteSerializer


# Create your views here.
class Noteview(generics.ListAPIView):
    queryset =Notemodel.objects.all()
    serializer_class =NoteSerializer
class Notedetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset =Notemodel.objects.all()
    serializer_class =NoteSerializer
