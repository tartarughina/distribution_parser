import argparse
import os
import csv
import json
import io
from course import Course
from distribution import Distribution
from encoder import Encoder
from term import Term


def get_args():
    parser = argparse.ArgumentParser(description="Distribution parser")
    parser.add_argument("dir", help="The directory to look for files")

    return parser.parse_args()


def main():
    args = get_args()

    grade_distribution = []

    for file in os.listdir(args.dir):
        if file.endswith(".csv"):
            name = file.replace(".csv", "").lower().split("_")

            semester = name[0]
            year = name[1]

            with open(os.path.join(args.dir, file), "r") as f:
                # skip the first line
                next(f)
                term = Term(semester, year)
                print(f"{semester} {year}")
                for line in f:
                    reader = csv.reader(io.StringIO(line))

                    parsed_line = next(reader)

                    distribution = Distribution(
                        int(parsed_line[5]),
                        int(parsed_line[6]),
                        int(parsed_line[7]),
                        int(parsed_line[8]),
                        int(parsed_line[9]),
                        int(parsed_line[20]),
                    )
                    course = Course(
                        parsed_line[0],
                        parsed_line[1],
                        parsed_line[2],
                        parsed_line[21],
                        distribution,
                    )

                    term.add_course(course)

            grade_distribution.append(term)
    
    with open("distribution.json", "w") as f:
        f.write(json.dumps(grade_distribution, cls=Encoder))


if __name__ == "__main__":
    main()
