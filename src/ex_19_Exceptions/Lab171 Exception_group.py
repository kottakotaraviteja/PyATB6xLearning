#Exception_group is available only in python
eg= ExceptionGroup("Multiple ex",[
    ValueError("Invalid error"),
    TypeError("Type error"),
    ZeroDivisionError("Zero division error"),
])

def check_div(a):
    if a == 0:
        raise eg