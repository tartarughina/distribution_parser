class Course:
    def __init__(self, code, number, name, instructor, distribution) -> None:
        self.code = code
        self.number = number
        self.name = name
        self.instructor = instructor
        self.distribution = distribution

    def to_dict(self):
        return {
            "code": self.code,
            "number": self.number,
            "name": self.name,
            "instructor": self.instructor,
            "distribution": self.distribution.to_dict()
        }