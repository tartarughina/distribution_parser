class Term:
    def __init__(self, semester, year) -> None:
        self.semester = semester
        self.year = year
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
    
    def to_dict(self):
        return {
            "semester": self.semester,
            "year": self.year,
            "courses": [course.to_dict() for course in self.courses]
        }