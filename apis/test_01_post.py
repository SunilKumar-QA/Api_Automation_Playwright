from playwright.sync_api import sync_playwright

def test_TC_POST_01(): # Create user with valid data

    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Ali",
            "email": "ali@test.com",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 201
        assert res["name"] == user_data["name"]
        assert res["email"] == user_data["email"]
        assert res["gender"] == user_data["gender"]
        print(f"User created with ID: {res['id']}")
        context.dispose()

def test_TC_POST_02(): # Create user without gender

    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Sara",
            "email": "sara@test.com",
            
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 201
        assert res["name"] == user_data["name"]
        assert res["email"] == user_data["email"]
        print(f"User created with ID: {res['id']}")
        context.dispose() 

def test_TC_POST_03(): # Create user with capital email
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Sam",
            "email": "SAM@TEST.COM",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 201
        assert res["name"] == user_data["name"]
        assert res["email"] == user_data["email"]
        assert res["gender"] == user_data["gender"]
        print(f"User created with ID: {res['id']}")
        context.dispose() 

def test_TC_POST_04(): # Missing name field (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            
            "email": "test1@test.com",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Name is required"
        print(res["error"])
        context.dispose()

def test_TC_POST_05(): # Missing email field (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            
            "name": "John",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Email is required"
        print(res["error"])
        context.dispose() 

def test_TC_POST_06(): # Missing both email & name field (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "gender": "female"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Name is required"
        print(res["error"])
        context.dispose()

def test_TC_POST_07(): # Email already exists (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Zara",
            "email": "ali@test.com",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Email must be unique"
        print(res["error"])
        context.dispose()

def test_TC_POST_08(): # invalid email format (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "test",
            "email": "test@",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Invalid email format"
        print(res["error"])
        context.dispose()                               

def test_TC_POST_09(): # Empty name field (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "",
            "email": "empty@test.com",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Name is required"
        print(res["error"])
        context.dispose()

def test_TC_POST_10(): # Empty name field (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Tester",
            "email": "",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Email is required"
        print(res["error"])
        context.dispose()

def test_TC_POST_11(): # Extra unexpected field (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Alex",
            "email": "alex@test.com",
            "gender": "male",
            "age":25
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Only name, email, and gender fields are allowed"
        print(res["error"])
        context.dispose() 

def test_TC_POST_12(): # Whitespace in name/email (Negative TC)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": " ",
            "email": " ",
            "gender": "male",
            
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Name should not contain only whitespaces"
        print(res["error"])
        context.dispose()

def test_TC_POST_13():  # name and email field empty (Negative Tc)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "",
            "email": "",
            "gender": "male"
        }

        response = context.post("/users", data=user_data)
        res = response.json()

        assert response.status == 400
        assert "error" in res
        assert res["error"] == "Name is required"
        print(res["error"])
        context.dispose()        




                        





