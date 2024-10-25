
# Flask CRUD API

This is a basic CRUD (Create, Read, Update, Delete) RESTful API built with Flask. It uses an in-memory data store (Python dictionary) to manage items and provides basic functionality to add, retrieve, update, and delete items.

## Features
- **Health Check**: Ensures the API is running.
- **Create Item**: Allows you to create a new item.
- **Get All Items**: Retrieves all stored items.
- **Get Single Item**: Retrieves a specific item by ID.
- **Update Item**: Updates an item’s details.
- **Delete Item**: Removes an item by its ID.

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Create a virtual environment and install the required packages:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install Flask
   ```

## Running the API

To start the Flask server:

```bash
python app.py
```

The API will be running at `http://0.0.0.0:5000`.

## API Endpoints

### Health Check
- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Checks if the API is running.
- **Response**:
  ```json
  { "status": "API is running" }
  ```

### Create Item
- **Endpoint**: `/items`
- **Method**: `POST`
- **Description**: Creates a new item.
- **Request Body**:
  ```json
  {
    "name": "Item Name",
    "description": "Item Description"
  }
  ```
- **Response**:
  ```json
  {
    "id": "1",
    "name": "Item Name",
    "description": "Item Description"
  }
  ```

### Get All Items
- **Endpoint**: `/items`
- **Method**: `GET`
- **Description**: Retrieves all items.
- **Response**:
  ```json
[
  {
    "id": "1",
    "name": "Item Name",
    "description": "Item Description"
  },
  "..."
]
```

### Get Single Item
- **Endpoint**: `/items/<item_id>`
- **Method**: `GET`
- **Description**: Retrieves a specific item by its ID.
- **Response**:
  ```json
  {
    "id": "1",
    "name": "Item Name",
    "description": "Item Description"
  }
  ```

### Update Item
- **Endpoint**: `/items/<item_id>`
- **Method**: `PUT`
- **Description**: Updates an item’s `name` and/or `description`.
- **Request Body**:
  ```json
  {
    "name": "Updated Item Name",
    "description": "Updated Description"
  }
  ```
- **Response**:
  ```json
  {
    "id": "1",
    "name": "Updated Item Name",
    "description": "Updated Description"
  }
  ```

### Delete Item
- **Endpoint**: `/items/<item_id>`
- **Method**: `DELETE`
- **Description**: Deletes an item by ID.
- **Response**:
  ```json
  {
    "message": "Item deleted"
  }
  ```

## Error Handling

- **400 Bad Request**: Returned if the request data is invalid.
- **404 Not Found**: Returned if the requested item is not found.

## License

This project is licensed under the MIT License.
