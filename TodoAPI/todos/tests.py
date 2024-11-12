import pytest
from rest_framework import status
from rest_framework.test import APIClient
from todos.models import Todo
from django.contrib.auth.models import User

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password123')

@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def todo():
    return Todo.objects.create(title="Test Todo", description="Test description", completed=False)

# Test GET /todos/ (List all todos)
@pytest.mark.django_db
def test_list_todos(api_client):
    response = api_client.get('/api/todos/')
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list) 

# Test GET /todos/<id>/ (Retrieve a single todo)
@pytest.mark.django_db
def test_retrieve_todo(api_client, todo):
    response = api_client.get(f'/api/todos/{todo.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == todo.id
    assert response.data['title'] == todo.title

# Test POST /todos/ (Create a new todo)
@pytest.mark.django_db
def test_create_todo(api_client):
    new_todo = {
        'title': 'todo 01',
        'description': 'todo new 01',
        'completed': False
    }
    response = api_client.post('/api/todos/', new_todo, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == new_todo['title']

# Test PUT /todos/<id>/ (Update a todo)
@pytest.mark.django_db
def test_update_todo(api_client, todo):
    update_todo = {
        'title': 'todo 01 update',
        'description': 'Updated todo o1',
        'completed': True
    }
    response = api_client.put(f'/api/todos/{todo.id}/', update_todo, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == update_todo['title']
    assert response.data['completed'] == update_todo['completed']

# Test DELETE /todos/<id>/ (Delete a todo)
@pytest.mark.django_db
def test_delete_todo(api_client, todo):
    response = api_client.delete(f'/api/todos/{todo.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Todo.objects.filter(id=todo.id).count() == 0


