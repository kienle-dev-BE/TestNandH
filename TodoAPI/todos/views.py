from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer

class TodoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # List all todos or Retrieve a single todo
    def get(self, request, id=None):
        try:
            if id:
                # Retrieve a single todo
                todo = get_object_or_404(Todo, id=id)
                serializer = TodoSerializer(todo)
            else:
                # List all todos
                todos = Todo.objects.all()
                serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": "Server Error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Create a new todo
    def post(self, request):
        try:
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": "Server Error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Update a todo
    def put(self, request, id):
        try:
            todo = get_object_or_404(Todo, id=id)
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": "Server Error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Delete a todo
    def delete(self, request, id):
        try:
            todo = get_object_or_404(Todo, id=id)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": "Server Error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
