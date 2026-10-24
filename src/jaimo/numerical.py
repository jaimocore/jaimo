import math

def f(input_fun: str, **kwargs) -> float:
    """
    Enter the function and the function value, 
    then perform the calculation.
    """
    safe_env = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        **kwargs
    }
    try:
        return float(eval(input_fun, {"__builtins__": {}}, safe_env))
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        # Throw a clear prompt when the input falls outside the defined domain.
        raise ValueError(
            f"Calculation error: The input values {kwargs} "
            f"may fall outside the domain of the function '{input_fun}'. "
            f"Details: {e}"
        )

def zero(
        input_fun: str, 
        min_val: float, 
        max_val: float, 
        epsilon: float, 
        dec_len: int
    ) -> float:
    """
    Find the zero of a monotonic function 
    within the interval [min_val, max_val], 
    with a precision requirement of "epsilon",
    provide the result rounded to "dec_len" decimal places.
    """
    is_increasing = f(input_fun, x=min_val) < f(input_fun, x=max_val)
    guess = (min_val + max_val) / 2
    guess_val = f(input_fun, x=guess)

    while abs(guess_val) >= epsilon:
        if is_increasing:
            if guess_val > 0:
                max_val = guess
            else:
                min_val = guess
        else:
            if guess_val > 0:
                min_val = guess
            else:
                max_val = guess
        guess = (min_val + max_val) / 2
        guess_val = f(input_fun, x=guess)
    return round(guess, dec_len)
