def divide(N,D):
    """
    Described in euclide's elements, this is one of the first division algorithm.
    Returns a tuple (Q,R) such that 'Q' is the quotient and 'R' is the rest.
    """
    R = N
    Q = 0

    while R>= 0:
        R = R-D
        Q = Q+1

    return (Q,R)