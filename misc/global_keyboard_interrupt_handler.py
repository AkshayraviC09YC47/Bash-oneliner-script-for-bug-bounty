import functools

def global_keyboard_interrupt_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\nQuitting...")
            exit(1)
    return wrapper

@global_keyboard_interrupt_handler
def testing():
    name = input("[+]Name: ")
    print(name)
testing()
