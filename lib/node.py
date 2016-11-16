class Node:

    def __init__(self, score, movie):
        self.data = {movie: score}
        self.left = None
        self.right = None

    def score(self):
        return self.data.values()[0]
