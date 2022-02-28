"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Some quick example text to build on the card title and make up the bulk of the card's content." in response.data
