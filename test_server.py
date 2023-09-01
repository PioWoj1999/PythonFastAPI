import requests
from fastapi import HTTPException


def main():
    print(f"""All printed items:\n{requests.get("http://127.0.0.1:8000/").json()}""")
    print(f"""Item ID 1:\n{requests.get("http://127.0.0.1:8000/items/1").json()}""")
    print(
        f"""Item ID 44:\n{requests.get("http://127.0.0.1:8000/items/44").json()}"""
    )  # not found - raised error

    print(
        f"""\nItem Hammer:\n{requests.get("http://127.0.0.1:8000/items?name=Hammer").json()}"""
    )

    print("\n\nUpdating an item:")
    print(requests.put("http://127.0.0.1:8000/update/0?count=9001").json())
    print(requests.get("http://127.0.0.1:8000/").json())
    print()

    print("\n Adding new item:")
    print(
        requests.post(
            "http://127.0.0.1:8000/",
            json={"name": "Screwdriver",
            "price": 3.99,
            "count": 1000,
            "id": 4,
            "category": "tools",},
        ).json()
    )
    print(f"""All items: {requests.get("http://127.0.0.1:8000/").json()}""")


if __name__ == "__main__":
    main()
