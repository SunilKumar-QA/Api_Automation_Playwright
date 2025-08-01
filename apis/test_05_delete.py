from playwright.sync_api import sync_playwright

def test_delete_method_api():
    with sync_playwright() as playwright:
        context = playwright.request.new_context(base_url="http://localhost:3000")

        response = context.delete("/users/1")

        res = response.json()

        # Assert that the response status code is 200 or 204 (commonly used for DELETE)
        assert response.status in [200, 204]

        # Optional: print the response text or status
        print("Delete Response Status:", response.status)
        print("Delete Response Text:", response.text())

        # Optionally, try to GET the same user to confirm it's deleted (should be 404)
        verify_response = context.get("/users/1")
        assert verify_response.status == 404

        # Clean up 
        context.dispose()

        
