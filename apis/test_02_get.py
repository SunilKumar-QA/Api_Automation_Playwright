from playwright.sync_api import sync_playwright

def test_get_valid_user():
    with sync_playwright() as p:
        context = p.request.new_context()
        response = context.get("http://localhost:3000/users/1")

        assert response.status == 200
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "Ali"
        assert data["email"] == "ali@test.com"
        assert data["gender"] == "male"
        context.dispose()

def test_get_invalid_user():
    with sync_playwright() as p:
        context = p.request.new_context()
        response = context.get("http://localhost:3000/users/10")

        assert response.status == 404
        error = response.json()
        assert "error" in error
        assert error["error"] == "User not found"
        context.dispose()