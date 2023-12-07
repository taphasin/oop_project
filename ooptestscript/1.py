class test:
    
    def __init__(self) -> None:
        pass
    
    def make_pretty(func):
        def inner():
            print("a")
            func()
        return inner

    @make_pretty
    def ordinary():
        print("b")

    ordinary()