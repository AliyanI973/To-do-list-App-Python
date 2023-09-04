

def validate_entry_input(min_len):
    def decorator(func):
        def wrapper(P):
            if len(P) > min_len:
                return func(P)
            else:
                print("Input validation failed.")   
                return False
        return wrapper
    return decorator