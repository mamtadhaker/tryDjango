from rest_framework import generics
from rest_framework.views import APIView
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status

class MessageList(APIView):
    # queryset = Message.objects.all()
    # serializer_class = MessageSerializer
    def get(self, request, format=None):
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
