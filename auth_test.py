def authenticate(username, password, database):
    """Checks if credentials match a record in the database."""
    if username in database:
        if database[username] == password:
            return "Success"
    return "Access Denied"


def test_authenticate_valid_user():
    # Setup: Define what our "mock" database looks like
    mock_db = {"alice": "p@ssword123", "bob": "12345"}
    
    # Assert: Alice provides the right password
    assert authenticate("alice", "p@ssword123", mock_db) == "Success"

def test_authenticate_invalid_password():
    mock_db = {"alice": "p@ssword123"}
    
    # Assert: Alice provides the wrong password
    assert authenticate("alice", "abc123", mock_db) == "Access Denied"

def test_authenticate_unknown_user():
    mock_db = {"alice": "p@ssword123"}
    
    # Assert: Trying to log in as someone not in the system
    assert authenticate("charlie", "any_pass", mock_db) == "Access Denied"