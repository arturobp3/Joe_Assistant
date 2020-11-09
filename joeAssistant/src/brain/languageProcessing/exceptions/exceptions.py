class NoRequestHeardError(Exception):

    def __init__(self, message="The assistant couldn't hear any request"):
        self.message = message
        super().__init__(self.message)

    '''def __str__(self):
        return f'{self.salary} -> {self.message}'''


class LanguageProcessingGeneralError(Exception):

    def __init__(self, message="There has been a general error when analyzing the user's request"):
        self.message = message
        super().__init__(self.message)


class UnintelligibleRequestError(Exception):

    def __init__(self, message="The assistant couldn't understand the request"):
        self.message = message
        super().__init__(self.message)
