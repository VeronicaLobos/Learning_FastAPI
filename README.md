## Learning FastAPI

A simple project to learn the fundamentals of FastAPI.  
While I already completed my first projects with Flask, I wanted to try FastAPI and async programming in Python.  
Async programming is a new concept for me, and I am excited to learn it.  
```Work in Progress``` I'll be adding features while learning.

## Fun FastAPI Facts I Learned (compared to Flask)
- FastAPI is built on top of Python 3.6+ type hints, which allows for automatic data validation and serialization. Particularly, FastAPI uses ```Pydantic``` for data validation and serialization, which allows you to define data models using Python classes. This makes it easy to validate incoming data and serialize outgoing data.
- FastAPI creates an OpenAPI schema for your API automatically, which can be used to generate documentation.
- While your server is running, you can modify your code and the server will automatically reload, making development faster and easier.
- Path parameters are handled differently in FastAPI compared to Flask:
  - In Flask, you define the path parameters in the route using angle brackets `<>`, and then you can access them using the `request` object.
  - In FastAPI, define them in the route between curly braces `{}`. FastAPI automatically extracts these values and makes them available as function parameters, you can use type hints to specify the type of the parameter, and FastAPI will automatically validate it for you.
- The type of the request method is defined in the function name, e.g. `@app.get("/items/{item_id}")` for a GET request, `@app.post("/items/")` for a POST request, etc.
- Status codes are handled differently in FastAPI compared to Flask:
  - In Flask, you can return a tuple with the response data and the status code, e.g. `return jsonify({"message": "Hello World!"}), 200`.
  - In FastAPI, you can use the `JSONResponse` class to create a response with a specific status code, e.g. `return JSONResponse(content={"message": "Hello World!"}, status_code=200)`.
  - In FastAPI, you can also use the `status` module to define common status codes, e.g. `from fastapi import status` and then use `status.HTTP_200_OK` instead of hardcoding the status code.

## Technologies
- Python
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- Uvicorn: ASGI server for Python
- Pydantic: Data validation and settings management using Python type annotations.
- MyPy (optional): Static type checker for Python. It checks the types of your code and helps you catch type errors before runtime.
- pytest (optional): A testing framework for Python. Checks syntax and type errors in your code.

## API routes

- `/`: A simple GET request that returns a welcome message.
- `/shopping_list/`: A GET request that returns a list of items in the shopping list.
- `/shopping_list/{item_id}`: A GET request that returns a specific item in the shopping list based on the item ID.
- `/shopping_list/`: A POST request that adds a new item to the shopping list.
- `more soon...`

## Run
I assume you have Python 3.6+ installed on your machine and a package manager like `pip` or `pip3` installed.  
Setting a virtual environment is recommended, but not required.  
To create a virtual environment, you can use the following commands:
```bash
python3 -m venv venv
activate venv/bin/activate
```

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/VeronicaLobos/Learning_FastAPI.git
```

After cloning this repository, you can run the following commands to install the dependencies and run the FastAPI application:

```bash
python3 -m pip install fastapi
pip instal uvicorn
uvicorn myapi:app --reload
```

## Test
Once you have the server running, you can test the API by opening your web browser and navigating to the following URLs:
* http://127.0.0.1:8000 in your navigator. You should see the FastAPI welcome page.  
* http://127.0.0.1:8000/docs in your navigator. You should see the Swagger UI documentation for the API.
You can test the API from there by clicking on the endpoints and trying them out.  

To close the server, you can use `CTRL + C` in the terminal where the server is running.