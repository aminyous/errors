class MyCustomError(Exception):
    """ This is a doc string for this particular class """
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code


raise MyCustomError("OUCH! An error happened", 500)



