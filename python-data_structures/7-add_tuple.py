#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples.
    
    Args:
        tuple_a: First tuple
        tuple_b: Second tuple
    
    Returns:
        A tuple with 2 integers:
        - The first element is the addition of the first elements of each argument
        - The second element is the addition of the second elements of each argument
    """
    # Handle cases where tuple_a is smaller than 2
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    
    # Handle cases where tuple_b is smaller than 2
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    
    return (a1 + b1, a2 + b2)
