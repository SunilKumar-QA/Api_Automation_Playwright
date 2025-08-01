from playwright.sync_api import sync_playwright

def test_TC_Patch_01(): #Update Only Name
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "Updated",
            }

        response = context.patch("/users/1", data=user_data)
        res = response.json()

        assert response.status == 200
        assert res["name"] == user_data["name"]
        context.dispose()


def test_TC_Patch_02(): #Update Only Email
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "email": "hyder.ali@gmail.com",
        }

        response = context.patch("/users/1", data=user_data)
        res = response.json()

        assert response.status == 200
        assert res["email"] == user_data["email"]
        context.dispose() 

def test_TC_Patch_03(): # Update email to same as current (excluding own record)
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "email": "hyder.ali@gmail.com",
        }

        response = context.patch("/users/1", data=user_data)
        res = response.json()

        assert response.status == 200
        assert res["email"] == user_data["email"]
        context.dispose()

def test_TC_Patch_04(): # Update all fields with valid values
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name":"Ali Zaman",
            "email": "sunil.kumar@gmail.com",
            "gender":"female"
        }

        response = context.patch("/users/1", data=user_data)
        res = response.json()

        assert response.status == 200
        assert res["name"] == user_data["name"]
        assert res["email"] == user_data["email"]
        assert res["gender"] == user_data["gender"]
        context.dispose()


def test_TC_Patch_05(): # Update with duplicate email
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "email": "sara@test.com",
        }

        response = context.patch("/users/1", data=user_data)
        res = response.json()

        assert response.status == 400
        assert res["error"] == "Email must be unique"
        print(res["error"])
        context.dispose()

def test_TC_Patch_06(): # update with empty name
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name": "",
        }

        response = context.patch("/users/1", data=user_data)
        res = response.json()

        assert response.status == 400
        assert res["error"] == "Name is required"
        print(res["error"])
        context.dispose()

def test_TC_Patch_07(): # update with empty email
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "email": "",
        }

        response = context.patch("/users/1", data=user_data)
        res = response.json()

        assert response.status == 400
        assert res["error"] == "Email is required"
        print(res["error"])
        context.dispose()

def test_TC_Patch_08(): # Update with invalid email format
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "email": "invalid-email",
        }

        response = context.patch("/users/1", data=user_data)
        res = response.json()

        assert response.status == 400
        assert res["error"] == "Invalid email format"
        print(res["error"])
        context.dispose()

def test_TC_Patch_09(): # Update with non-existent user ID
    with sync_playwright() as p:
        context = p.request.new_context(base_url="http://localhost:3000")

        user_data ={
            "name":"Ali Zaman",
            "email": "sunil.kumar@gmail.com",
            "gender":"female"
        }

        response = context.patch("/users/60", data=user_data)
        res = response.json()

        assert response.status == 404
        assert res["error"] == "User not found"
        print(res["error"])
        context.dispose()

                                


        
                       
        

        

        
        
