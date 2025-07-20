class Comp:
    comps = []
    def __init__(self, mode, name, comps):
        self.mode = mode
        self.name = name
        self.comps = comps

class CompList:
    def __init__(self, battles, priority_order):
        self.battles = battles
        self.priority_order = priority_order

    def get_battles_by_priority(self):
        # Returns battles reordered according to priority_order
        return [self.battles[i - 1] for i in self.priority_order]
