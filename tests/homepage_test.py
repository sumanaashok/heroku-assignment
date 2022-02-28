"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"This is  Website" in response.data
