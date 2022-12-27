import math

def divide(N,D):
    """
    Use python divition to get the quotient and rest.
    Return (Q,R) such that Q is the quotient and R is the rest.
    """
    Q = N/D
    Q = math.ceil(Q) if Q < 0 else math.floor(Q)
    R = N - Q*D
    return (Q,R)

def divide_with_decimals(N,D, steps):
    """
    Divide 'N' by 'D' and returns it's decimals as an array of
    'steps'-dimension. Notice that position 0 of the array is the Quotient of the
    divition.
    """

    if N < 0 and D < 0:
        return divide_with_decimals(-N,-D,steps)

    if (N < 0):
        res = divide_with_decimals(-N, D, steps)
        res[0] = -res[0]
        return res
    
    if (D < 0 ):
        res = divide_with_decimals(N, -D, steps)
        res[0] = -res[0]
        return res

    _N, _D = N,D
    res = [] 
    for _ in range(0,steps+1):
        Q, R = divide(_N, _D)
        res.append(Q)

        # We can't divide the rest further, so we multiply it by 10 and continue
        # the next step in the divition algorithhm
        _N = R * 10
    return res