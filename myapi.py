"""
An API for a simple shopping list application.
The application is built using FastAPI and includes
a simple in-memory data store for demonstration purposes.

It includes the following endpoints:
- GET /: Returns a welcome message.
- GET /shopping_list/: Returns the list of items in the
  shopping list.
- GET /shopping_list/{item_id}: Returns the details of a
  specific item by its ID.
- POST /shopping_list/: Creates a new item in the shopping
  list.
- PUT /shopping_list/{item_id}: **coming soon** Updates an
  existing item in the shopping list.
- DELETE /shopping_list/{item_id}: **coming soon** Deletes
  an item from the shopping list.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Item(BaseModel):
    """
    A model representing an item in the shopping list.
    """
    id: int
    name: str
    quantity: int
items = [
        {"id": 1, "name": "Apple", "quantity": 5},
        {"id": 2, "name": "Banana", "quantity": 10},
        {"id": 3, "name": "Orange", "quantity": 7}
    ]

app = FastAPI()

@app.get('/', status_code=status.HTTP_200_OK)
def index() -> JSONResponse:
    """
    Index route that returns a simple message.
    :return: A JSON response with a welcome message.
    """
    message = {"message": "Hello, World!"}
    return JSONResponse(content=message)

@app.get('/shopping_list/', status_code=status.HTTP_200_OK)
def shopping_list() -> JSONResponse:
    """
    Get the shopping list items.
    :return: A JSON response with the list of items, or
            a message if the list is empty.
    """
    if not items:
        message = {"message": "No items found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=message)
    return JSONResponse(content=items)

@app.get('/shopping_list/{item_id}',status_code=status.HTTP_200_OK)
def get_item(item_id: int) -> JSONResponse:
    """
    Get an item from the shopping list by its ID.
    :param item_id: The ID of the item to retrieve
    :return: A JSON response with the item details,
            or a message if the item is not found.
    """
    item = [item for item in items if item['id'] == item_id]
    if item:
        return JSONResponse(content=item)
    message = {"message": f"Item with id {item_id} not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=message)

@app.post('/shopping_list/', status_code=status.HTTP_201_CREATED)
async def create_item(new_item: Item) -> JSONResponse:
    """
    Create a new item in the shopping list.
    :param new_item: An item object to be added
    :return: a JSON response with the created item,
            or a message if the item already exists.
    """
    for item in items:
        if new_item.name == item['name']:
            message = {"message": f"Item {item['name']} already exists"}
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=message)

    item = new_item.model_dump()
    items.append(item)
    content = {"message": "Item added successfully",
               "new_item": item}
    return JSONResponse(content=content)

@app.put('/shopping_list/{item_id}', status_code=status.HTTP_200_OK)
async def update_item(item_id: int,
                      updated_item: Item) -> JSONResponse:
    """
    Update an existing item in the shopping list.
    :param item_id:
    :param updated_item:
    :return:
    """
    for item in items:
        if item['id'] == item_id:
            item.update(updated_item.model_dump())
            message = {"message": "Item updated successfully",
                       "updated_item": item}
            return JSONResponse(content=message)

    message = {"message": f"Item with id {item_id} not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=message)
