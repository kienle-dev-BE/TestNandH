

## Local Development

### Prerequisites

- Python 3.x
- Pip

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd TodoAPI
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

1. Start the application:

    ```bash
    python manage.py runserver
    ```


### Testing

Run the tests using `pytest`:

```bash
pytest todos/tests.py
```
### Create User

``` bash
python manage.py createsuperuser
```

### Create Token 

``` bash
python manage.py drf_create_token '<username>'
```

## Endpoints

### List all todos

- **GET /api/todos/**
  - Method: GET
  - URL: /api/todos/ (http://127.0.0.1:8000/api/todos/)
  - Headers: 
    - - Authorization: Token <your_token>

### Create a new todo
- **POST /api/todos/**
  - Method: POST
  - URL: /api/todos/ (http://127.0.0.1:8000/api/todos/)
  - Headers: 
    - - Authorization: Token <your_token>
  - Body (JSON):
```bash
       {
            "title": "Todo 01",
            "description": "Todo 01 is real",
            "completed": false
        }
```

### Retrieve a single todo
- **GET  /api/todos/{id}/**
  - Method: GET 
  - URL: /api/todos/{id}/ (http://127.0.0.1:8000/api/todos/1/)
  - Headers: 
    - - Authorization: Token <your_token>

### Update a todo
- **PUT  /api/todos/{id}/**
  - Method: PUT 
  - URL: /api/todos/{id}/ (http://127.0.0.1:8000/api/todos/1/)
  - Headers: 
    - - Authorization: Token <your_token>
  - Body (JSON):
```bash
       {
            "title": "Todo 01 new",
            "description": "Todo 01 is update version 02",
            "completed": false
        }
```

### Delete a todo
- **DELETE  /api/todos/{id}/**
  - Method: DELETE 
  - URL: /api/todos/{id}/ (http://127.0.0.1:8000/api/todos/1/)
  - Headers: 
    - - Authorization: Token <your_token>


