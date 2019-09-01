class Engine:

    def __init__(self):
        self.mach = None
        self.parts = []

    def add_part(self, name, part):
        self.parts.append((name, part))
