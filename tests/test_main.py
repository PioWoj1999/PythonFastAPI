import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from main import app, items

client = TestClient(app)

def test_hello_get() -> None: 
    """Test to see Hello World! reply."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World!"}

def test_index_id_get() -> None: 
    """Test to check if item id 1 is properly returned."""
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {'name': 'Pliers', 'price': 5.99, 'count': 20, 'id': 1, 'category': 'tools'}

def test_index_id_not_found_get() -> None: 
    """Test to check 404 on item."""
    response = client.get("/items/44")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item ID: 44 is not found."}

def test_index_get() -> None: 
    """Test to return all item elements"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'0': {'name': 'Hammer', 'price': 9.99, 'count': 20, 'id': 0, 'category': 'tools'}, '1': {'name': 'Pliers', 'price': 5.99, 'count': 20, 'id': 1, 'category': 'tools'}, '2': {'name': 'Nails', 'price': 1.99, 'count': 100, 'id': 2, 'category': 'consumables'}}

def test_item_by_parameter_get() -> None: 
    """Test to get item by parameter."""
    response = client.get("/items?name=Hammer")
    assert response.status_code == 200
    assert response.json() == {'query': {'name': 'Hammer', 'price': None, 'count': None, 'category': None}, 'selection': [{'name': 'Hammer', 'price': 9.99, 'count': 20, 'id': 0, 'category': 'tools'}]}

def test_item_by_parameter_404_get() -> None: 
    """Test to get item by parameter."""
    response = client.get("/items?name=Tool")
    assert response.status_code == 200
    assert response.json() == {'query': {'name': "Tool", 'price': None, 'count': None, 'category': None}, 'selection': []}

def test_add_item_post() -> None: 
    post_data = {"name": "Screwdriver",
                "price": 3.99,
                "count": 1000,
                "id": 4,
                "category": "tools",}
    response = client.post(
        "/",
        json=post_data
    )
    assert response.status_code == 200
    assert response.json() == {"added":post_data}
