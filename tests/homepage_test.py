"""This tests the homepage and about page"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"This is  Website" in response.data

    def test_request_about(client):
        """This makes the index page"""
        response = client.get("/about")
        assert response.status_code == 200
        assert b"Lorem ipsum" in response.data
