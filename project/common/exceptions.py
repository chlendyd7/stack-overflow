class RaiseError(BaseException):
    
    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code
