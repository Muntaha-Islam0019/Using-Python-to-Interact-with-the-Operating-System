# assert and raise examples

def validate_user(username, minlen):

    # Assert keyword verify that the conditional expression is true and if it's false it raises an assertion error with the indicated message
    # Assertions will be removed from the code if we ask te interpreter to optimize it to run faster
    assert type(username) == str, "username must be a string"

    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
    

# We should use 'raise' to check for conditions that we expect to happen during normal execution of our code
# We should use 'assert' to verify the situations that aren't expected but that might cause our code to misbehave