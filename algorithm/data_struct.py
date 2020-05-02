
class Example:

    def __init__(self, gene: str, positive: str):
        self.attributes = gene
        self.example_class = positive == '1'
