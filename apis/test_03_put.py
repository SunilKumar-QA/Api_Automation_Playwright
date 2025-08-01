from playwright.sync_api import sync_playwright

def test_TC_PUT_01(): # Update all fields with valid data
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Ali Khan",
            "email": "ali.khan@example.com",
            "gender":"female",   
        }

        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 200
        assert response.status_text == "OK"
        assert res["name"] == user_data["name"]
        assert res["email"] == user_data["email"]
        assert res["gender"] == user_data["gender"]
        context.dispose()

def test_TC_PUT_02(): # Update with same email (own record)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Ali Khan",
            "email": "ali.khan@example.com",
            "gender":"female",   
        }

        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 200
        assert response.status_text == "OK"
        assert res["name"] == user_data["name"]
        assert res["email"] == user_data["email"]
        assert res["gender"] == user_data["gender"]
        context.dispose()        

def test_TC_PUT_03(): # Update only required fields
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Fatima",
            "email": "fatima@example.com",  
        }

        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 200
        assert response.status_text == "OK"
        assert res["name"] == user_data["name"]
        assert res["email"] == user_data["email"]
        context.dispose()


def test_TC_PUT_04(): # Missing Name Field
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "email": "test@example.com",
            "gender":"male",   
        }

        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 400
        
        assert res["error"] == "Name is required for update"
        print(res["error"])
        context.dispose() 


def test_TC_PUT_05(): # Missing Email
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "akshay",
            "email": "",
            "gender":"male",   
        }

        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 400
        
        assert res["error"] == "Email is required for update"
        print(res["error"])
        context.dispose()

def test_TC_PUT_06(): # Both name and email missing
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "gender":"male"   
        }

        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 400
        
        assert res["error"] == "Name is required for update"
        print(res["error"])
        context.dispose()

def test_TC_PUT_07(): # Empty Name
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
                "name": "", 
                "email": "test@example.com",
                "gender": "male"
            }


        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 400
        
        assert res["error"] == "Name is required for update"
        print(res["error"])
        context.dispose()

def test_TC_PUT_08(): # Empty Email
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "", 
            "email": "",
            "gender": "male"   
        }

        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 400
        
        assert res["error"] == "Name is required for update"
        print(res["error"])
        context.dispose() 

def test_TC_PUT_09(): # Invalid email format
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={"name": "Test", "email": "invalidemail", "gender": "male"}


        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 400
        
        assert res["error"] == "Invalid email format"
        print(res["error"])
        context.dispose()               

def test_TC_PUT_10(): # Duplicate Email
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={"name": "Test", "email": "sara@test.com", "gender": "male"}


        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 400
        
        assert res["error"] == "Email must be unique"
        print(res["error"])
        context.dispose()

def test_TC_PUT_11(): # Extra undefined field in request
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={"name": "Ali", "email": "ali@example.com", "gender": "male", "age": 25}

        response = context.put("/users/1", data=user_data)
        res = response.json()
        
        assert response.status == 400
        
        assert res["error"] == "Only name, email, and gender fields are allowed"
        print(res["error"])
        context.dispose()        

def test_TC_PUT_12(): # PUT to non-existing user ID
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={"name": "Ali", "email": "ali@example.com", "gender": "male"}

        response = context.put("/users/50", data=user_data)
        res = response.json()
        
        assert response.status == 404
        
        assert res["error"] == "User not found"
        print(res["error"])
        context.dispose()


