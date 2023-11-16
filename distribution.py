class Distribution:
    # a, b, c, d, f are the grades
    # w is the number of withdrawals
    def __init__(self, a: int, b: int, c: int, d: int, f: int, w: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.f = f
        self.w = w

    def to_dict(self):
        return {
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "d": self.d,
            "f": self.f,
            "w": self.w
        }