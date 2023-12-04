def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.
    If the sentence is empty, the first character should be equal to None
    """
    if len(sentence) > 0:
        firstChar = sentence[0]
    else:
        firstChar = None
    return (len(sentence), firstChar)