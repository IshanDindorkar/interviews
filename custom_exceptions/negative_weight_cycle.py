class NegativeWeightCycle(Exception):
    def __init__(self):
        super().__init__("Negative weight cycle detected")

# EOF
