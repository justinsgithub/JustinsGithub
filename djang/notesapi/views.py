from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

# DIFFERENCE BETWEEN REST API AND RESTFUL API

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/notes/',
            'method': 'GET',
            'body': None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint':'/notes/id',
            'method': 'GET',
            'body': None,
            'description':'Returns a single note object'
        },
        {
            'Endpoint':'/notes/create/',
            'method': 'POST',
            'body': {'body': ''},
            'description':'Creates a new note object'
        },
        {
            'Endpoint':'/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ''},
            'description':'Modifies an existing note object'
        },
        {
            'Endpoint':'/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description':'Deletes an existing note object'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)  # NOT GETTING ALL
    serializer = NoteSerializer(notes, many=False) # NOT GETTING MANY, GETTING ONE 
    return Response(serializer.data)
