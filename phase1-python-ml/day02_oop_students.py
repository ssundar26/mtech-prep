# =============================================================
# Day 2 — Object-Oriented Programming : Student Management
# Author  : Satya Sundar
# Email   : satyasundar439@gmail.com
# Date    : May 2, 2026
# Goal    : Build a complete Student class from first principles,
#           process 20 students, save and reload from JSON
# Run     : python day02_oop_students.py
# Output  : students.json (created automatically)
# =============================================================

import json


# =============================================================
# THE STUDENT CLASS
# =============================================================

class Student:
    """
    Represents a student with academic information and behaviour.

    A class is a blueprint. Every Student object (instance) created
    from this blueprint gets its own copy of the attributes defined
    in __init__, and shares access to all the methods defined here.

    Attributes
    ----------
    name        : str   — full name of the student
    roll_number : str   — unique identifier
    marks       : dict  — {subject: marks_scored}  (0 – 100)
    age         : int   — age in years

    Class variable
    --------------
    PASS_MARK   : int   — minimum mark to pass a subject (50)

    Examples
    --------
    >>> s = Student("Satya", "ABIT2024001", {"Math": 88, "ML": 92}, 22)
    >>> s.average()
    90.0
    >>> s.grade()
    'A+'
    >>> s.passed()
    True
    """

    # ── CLASS VARIABLE ───────────────────────────────────────
    # Shared by every instance — not per-student data
    PASS_MARK = 50

    # ── __init__ : INITIALISE THE INSTANCE ───────────────────
    def __init__(self, name, roll_number, marks, age):
        """
        Initialise a Student instance.

        Called automatically by Python when you write:
            student = Student(name, roll_number, marks, age)

        'self' refers to the specific instance being created.
        self.name = name stores the argument as an instance attribute
        so that this particular student remembers its own name.

        Parameters
        ----------
        name        : str  — full name
        roll_number : str  — unique roll number
        marks       : dict — {subject (str): marks (int or float)}
        age         : int  — age in years

        Raises
        ------
        TypeError  — if marks is not a dict
        ValueError — if any mark is outside the range 0 – 100
        ValueError — if age is not a positive integer
        """
        # ── input validation ─────────────────────────────────
        if not isinstance(marks, dict):
            raise TypeError(
                f"marks must be a dict, got {type(marks).__name__}"
            )
        for subject, mark in marks.items():
            if not isinstance(mark, (int, float)):
                raise TypeError(
                    f"Mark for '{subject}' must be a number, "
                    f"got {type(mark).__name__}"
                )
            if not (0 <= mark <= 100):
                raise ValueError(
                    f"Marks must be 0 – 100. "
                    f"Got {mark} for '{subject}'"
                )
        if not isinstance(age, int) or age <= 0:
            raise ValueError(
                f"age must be a positive integer, got {age}"
            )

        # ── store as instance attributes ──────────────────────
        self.name        = name
        self.roll_number = roll_number
        self.marks       = marks          # dict: {subject: mark}
        self.age         = age

    # ── COMPUTED PROPERTIES ───────────────────────────────────

    def average(self):
        """
        Calculate the average marks across all subjects.

        Returns
        -------
        float — average marks, 0.0 if no subjects recorded

        Example
        -------
        >>> Student("S","001",{"Math":80,"CS":90},20).average()
        85.0
        """
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        """
        Return the letter grade based on average marks.

        Scale
        -----
        A+ : 90 and above
        A  : 80 – 89
        B  : 70 – 79
        C  : 60 – 69
        D  : 50 – 59
        F  : below 50

        Returns
        -------
        str — one of 'A+', 'A', 'B', 'C', 'D', 'F'
        """
        avg = self.average()
        if   avg >= 90: return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        elif avg >= 50: return "D"
        else:           return "F"

    def passed(self, pass_mark=None):
        """
        Check whether the student has passed ALL subjects.

        Parameters
        ----------
        pass_mark : int, optional
            Minimum marks to pass. Defaults to Student.PASS_MARK (50).

        Returns
        -------
        bool — True if every subject mark >= pass_mark
        """
        threshold = pass_mark if pass_mark is not None else Student.PASS_MARK
        return all(mark >= threshold for mark in self.marks.values())

    def highest_subject(self):
        """
        Return the subject with the highest marks.

        Returns
        -------
        tuple — (subject_name: str, marks: int|float)
                (None, None) if no subjects recorded
        """
        if not self.marks:
            return None, None
        best = max(self.marks, key=self.marks.get)
        return best, self.marks[best]

    def lowest_subject(self):
        """
        Return the subject with the lowest marks.

        Returns
        -------
        tuple — (subject_name: str, marks: int|float)
                (None, None) if no subjects recorded
        """
        if not self.marks:
            return None, None
        worst = min(self.marks, key=self.marks.get)
        return worst, self.marks[worst]

    def subjects_below(self, threshold):
        """
        Return a list of subjects where marks are below the threshold.

        Parameters
        ----------
        threshold : int — the mark boundary

        Returns
        -------
        list — subject names (str) where marks < threshold
        """
        return [
            subject
            for subject, mark in self.marks.items()
            if mark < threshold
        ]

    def subjects_above(self, threshold):
        """
        Return a list of subjects where marks are above the threshold.

        Parameters
        ----------
        threshold : int — the mark boundary

        Returns
        -------
        list — subject names (str) where marks >= threshold
        """
        return [
            subject
            for subject, mark in self.marks.items()
            if mark >= threshold
        ]

    def rank_subjects(self):
        """
        Return all subjects ranked from highest to lowest marks.

        Returns
        -------
        list of tuples — [(subject, marks), ...] sorted descending
        """
        return sorted(
            self.marks.items(),
            key=lambda item: item[1],
            reverse=True,
        )

    def performance_summary(self):
        """
        Return a concise performance dict for this student.

        Returns
        -------
        dict — summary with name, roll, average, grade, passed, best, worst
        """
        best_sub,  best_mark  = self.highest_subject()
        worst_sub, worst_mark = self.lowest_subject()
        return {
            "name"          : self.name,
            "roll_number"   : self.roll_number,
            "age"           : self.age,
            "average"       : round(self.average(), 2),
            "grade"         : self.grade(),
            "passed"        : self.passed(),
            "best_subject"  : best_sub,
            "best_marks"    : best_mark,
            "worst_subject" : worst_sub,
            "worst_marks"   : worst_mark,
        }

    def to_dict(self):
        """
        Convert the Student object to a fully serialisable dict.

        Used when saving to JSON. Custom objects cannot be written
        to JSON directly — they must first be converted to plain
        Python types (dict, list, str, int, float, bool, None).

        Returns
        -------
        dict — all student data as JSON-safe types
        """
        best_sub,  best_mark  = self.highest_subject()
        worst_sub, worst_mark = self.lowest_subject()
        return {
            "name"          : self.name,
            "roll_number"   : self.roll_number,
            "age"           : self.age,
            "marks"         : self.marks,
            "average"       : round(self.average(), 2),
            "grade"         : self.grade(),
            "passed"        : self.passed(),
            "best_subject"  : best_sub,
            "best_marks"    : best_mark,
            "worst_subject" : worst_sub,
            "worst_marks"   : worst_mark,
            "subjects_below_60": self.subjects_below(60),
            "ranked_subjects"  : self.rank_subjects(),
        }

    # ── SPECIAL (DUNDER) METHODS ──────────────────────────────

    def __str__(self):
        """
        Human-readable representation. Called by print(student).

        Without this method, print(student) shows something like:
            <__main__.Student object at 0x7f3a2c1d4e50>
        which is useless. __str__ lets you control the output.
        """
        best_sub, best_mark   = self.highest_subject()
        worst_sub, worst_mark = self.lowest_subject()
        status = "PASSED" if self.passed() else "FAILED"

        lines = [
            f"┌─────────────────────────────────────────┐",
            f"  Student : {self.name} ({self.roll_number})",
            f"  Age     : {self.age}",
            f"  Average : {self.average():.2f}",
            f"  Grade   : {self.grade()}",
            f"  Status  : {status}",
            f"  Best    : {best_sub} ({best_mark})",
            f"  Worst   : {worst_sub} ({worst_mark})",
            f"  Marks   :",
        ]
        for subject, mark in self.marks.items():
            lines.append(f"    {subject:<12}: {mark}")
        lines.append(f"└─────────────────────────────────────────┘")
        return "\n".join(lines)

    def __repr__(self):
        """
        Developer / debugging representation.
        Called in the Python shell or inside lists/dicts.
        Should return enough info to recreate the object.
        """
        return (
            f"Student("
            f"name='{self.name}', "
            f"roll='{self.roll_number}', "
            f"avg={self.average():.1f}, "
            f"grade='{self.grade()}')"
        )

    def __eq__(self, other):
        """Two students are equal if their roll numbers match."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.roll_number == other.roll_number

    def __lt__(self, other):
        """Less-than based on average marks (enables sorting)."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average() < other.average()


# =============================================================
# 20 STUDENT INSTANCES
# =============================================================

# Raw data: (name, roll_number, marks_dict, age)
_RAW_DATA = [
    (
        "Satya Sundar", "ABIT2024001",
        {"Math": 88, "Python": 92, "ML": 90, "DSA": 85, "OS": 82},
        22,
    ),
    (
        "Priya Patel", "ABIT2024002",
        {"Math": 95, "Python": 88, "ML": 93, "DSA": 91, "OS": 89},
        21,
    ),
    (
        "Raju Kumar", "ABIT2024003",
        {"Math": 72, "Python": 68, "ML": 75, "DSA": 70, "OS": 65},
        23,
    ),
    (
        "Meena Dash", "ABIT2024004",
        {"Math": 45, "Python": 55, "ML": 48, "DSA": 42, "OS": 50},
        22,
    ),
    (
        "Arjun Singh", "ABIT2024005",
        {"Math": 98, "Python": 95, "ML": 97, "DSA": 96, "OS": 94},
        21,
    ),
    (
        "Sita Mohanty", "ABIT2024006",
        {"Math": 60, "Python": 72, "ML": 65, "DSA": 58, "OS": 63},
        23,
    ),
    (
        "Vikram Nair", "ABIT2024007",
        {"Math": 83, "Python": 79, "ML": 81, "DSA": 85, "OS": 78},
        22,
    ),
    (
        "Anjali Reddy", "ABIT2024008",
        {"Math": 37, "Python": 45, "ML": 40, "DSA": 38, "OS": 42},
        24,
    ),
    (
        "Rohit Sharma", "ABIT2024009",
        {"Math": 77, "Python": 82, "ML": 79, "DSA": 74, "OS": 80},
        22,
    ),
    (
        "Kavya Rao", "ABIT2024010",
        {"Math": 91, "Python": 89, "ML": 94, "DSA": 92, "OS": 88},
        21,
    ),
    (
        "Deepak Joshi", "ABIT2024011",
        {"Math": 55, "Python": 60, "ML": 52, "DSA": 58, "OS": 56},
        23,
    ),
    (
        "Nisha Gupta", "ABIT2024012",
        {"Math": 84, "Python": 87, "ML": 86, "DSA": 83, "OS": 89},
        22,
    ),
    (
        "Arun Pillai", "ABIT2024013",
        {"Math": 67, "Python": 71, "ML": 69, "DSA": 65, "OS": 68},
        23,
    ),
    (
        "Pooja Verma", "ABIT2024014",
        {"Math": 79, "Python": 76, "ML": 82, "DSA": 77, "OS": 74},
        22,
    ),
    (
        "Suresh Mishra", "ABIT2024015",
        {"Math": 43, "Python": 38, "ML": 46, "DSA": 41, "OS": 44},
        24,
    ),
    (
        "Lakshmi Iyer", "ABIT2024016",
        {"Math": 90, "Python": 93, "ML": 91, "DSA": 88, "OS": 92},
        21,
    ),
    (
        "Manoj Tiwari", "ABIT2024017",
        {"Math": 62, "Python": 58, "ML": 64, "DSA": 60, "OS": 55},
        23,
    ),
    (
        "Divya Krishnan", "ABIT2024018",
        {"Math": 86, "Python": 90, "ML": 88, "DSA": 84, "OS": 87},
        22,
    ),
    (
        "Rahul Bose", "ABIT2024019",
        {"Math": 74, "Python": 78, "ML": 72, "DSA": 76, "OS": 70},
        23,
    ),
    (
        "Anita Chatterjee", "ABIT2024020",
        {"Math": 96, "Python": 94, "ML": 98, "DSA": 95, "OS": 97},
        21,
    ),
]

# Build the list of Student objects using a list comprehension
# For each tuple in _RAW_DATA, unpack name/roll/marks/age
# and create a Student instance
students = [
    Student(name, roll, marks, age)
    for name, roll, marks, age in _RAW_DATA
]


# =============================================================
# ANALYSIS FUNCTIONS
# =============================================================

def separator(title="", width=60):
    """Print a visual separator with an optional centred title."""
    if title:
        print(f"\n{'=' * width}")
        print(f"  {title}")
        print(f"{'=' * width}")
    else:
        print("-" * width)


def class_summary(student_list):
    """
    Print headline statistics for the entire class.

    Parameters
    ----------
    student_list : list[Student]
    """
    separator("CLASS SUMMARY")

    total        = len(student_list)
    averages     = [s.average() for s in student_list]
    passed_count = sum(1 for s in student_list if s.passed())
    failed_count = total - passed_count
    class_avg    = sum(averages) / total

    print(f"  Total students      : {total}")
    print(f"  Passed              : {passed_count}")
    print(f"  Failed              : {failed_count}")
    print(f"  Pass rate           : {passed_count / total:.1%}")
    print(f"  Class average       : {class_avg:.2f}")
    print(f"  Highest average     : {max(averages):.2f}")
    print(f"  Lowest average      : {min(averages):.2f}")

    # grade distribution
    separator("GRADE DISTRIBUTION")
    grade_counts = {}
    for s in student_list:
        g = s.grade()
        grade_counts[g] = grade_counts.get(g, 0) + 1

    for grade in ["A+", "A", "B", "C", "D", "F"]:
        count = grade_counts.get(grade, 0)
        bar   = "█" * count + "░" * (total - count)
        print(f"  {grade:2s} | {bar} | {count:2d} students")


def rank_students(student_list):
    """
    Print a formatted rank table sorted by average (descending).

    Parameters
    ----------
    student_list : list[Student]
    """
    separator("STUDENT RANKINGS  (sorted by average)")

    ranked = sorted(student_list, reverse=True)   # uses __lt__

    header = (
        f"  {'Rank':<5} "
        f"{'Name':<20} "
        f"{'Roll':<15} "
        f"{'Average':>8} "
        f"{'Grade':>6} "
        f"{'Status':>7}"
    )
    print(header)
    print("  " + "-" * 58)

    for rank, student in enumerate(ranked, start=1):
        status = "PASS" if student.passed() else "FAIL"
        print(
            f"  {rank:<5} "
            f"{student.name:<20} "
            f"{student.roll_number:<15} "
            f"{student.average():>8.2f} "
            f"{student.grade():>6} "
            f"{status:>7}"
        )


def top_performers(student_list, n=3):
    """
    Return and display the top n students by average.

    Parameters
    ----------
    student_list : list[Student]
    n            : int — how many to return (default 3)

    Returns
    -------
    list[Student] — top n students, highest first
    """
    separator(f"TOP {n} PERFORMERS")
    top = sorted(student_list, reverse=True)[:n]
    for rank, s in enumerate(top, start=1):
        best_sub, best_mark = s.highest_subject()
        print(
            f"  {rank}. {s.name:<22} "
            f"Average: {s.average():.2f}  "
            f"Grade: {s.grade()}  "
            f"Best: {best_sub} ({best_mark})"
        )
    return top


def students_needing_help(student_list, threshold=60):
    """
    Find students with at least one subject below the threshold.

    Parameters
    ----------
    student_list : list[Student]
    threshold    : int — mark below which help is needed (default 60)

    Returns
    -------
    list[Student]
    """
    separator(f"STUDENTS NEEDING ATTENTION  (any subject < {threshold})")
    at_risk = [s for s in student_list if s.subjects_below(threshold)]

    if not at_risk:
        print("  No students below threshold. Well done!")
        return []

    for s in at_risk:
        weak = s.subjects_below(threshold)
        print(
            f"  {s.name:<22} "
            f"Average: {s.average():.2f}  "
            f"Weak subjects: {weak}"
        )
    return at_risk


def failed_students(student_list):
    """
    Display students who have failed (any subject < PASS_MARK).

    Parameters
    ----------
    student_list : list[Student]

    Returns
    -------
    list[Student]
    """
    separator(f"FAILED STUDENTS  (any subject < {Student.PASS_MARK})")
    failed = [s for s in student_list if not s.passed()]

    if not failed:
        print("  All students passed!")
        return []

    for s in failed:
        print(
            f"  {s.name:<22} "
            f"Average: {s.average():.2f}  "
            f"Grade: {s.grade()}  "
            f"Failed subjects: {s.subjects_below(Student.PASS_MARK)}"
        )
    return failed


def subject_statistics(student_list):
    """
    Print per-subject statistics (average, highest, lowest).

    Parameters
    ----------
    student_list : list[Student]
    """
    separator("PER-SUBJECT STATISTICS")

    # collect all subject names from the first student
    # (all students share the same subjects in this dataset)
    subjects = list(student_list[0].marks.keys())

    header = (
        f"  {'Subject':<14} "
        f"{'Average':>9} "
        f"{'Highest':>9} "
        f"{'Lowest':>9} "
        f"{'Pass rate':>10}"
    )
    print(header)
    print("  " + "-" * 55)

    for subject in subjects:
        subject_marks = [s.marks[subject] for s in student_list]
        avg      = sum(subject_marks) / len(subject_marks)
        highest  = max(subject_marks)
        lowest   = min(subject_marks)
        pass_rate = sum(1 for m in subject_marks if m >= Student.PASS_MARK)
        pass_pct = pass_rate / len(subject_marks)

        print(
            f"  {subject:<14} "
            f"{avg:>9.2f} "
            f"{highest:>9} "
            f"{lowest:>9} "
            f"{pass_pct:>10.1%}"
        )


# =============================================================
# JSON : SAVE AND LOAD
# =============================================================

def save_students_to_json(student_list, filename="students.json"):
    """
    Serialise a list of Student objects and write to a JSON file.

    Serialisation = converting Python objects into a storable format.
    JSON cannot store custom objects directly, so we call to_dict()
    on each student to get a plain Python dict first.

    Parameters
    ----------
    student_list : list[Student]
    filename     : str — output file path (default 'students.json')
    """
    averages     = [s.average() for s in student_list]
    passed_count = sum(1 for s in student_list if s.passed())

    data = {
        "metadata": {
            "total_students" : len(student_list),
            "class_average"  : round(sum(averages) / len(averages), 2),
            "highest_average": round(max(averages), 2),
            "lowest_average" : round(min(averages), 2),
            "pass_rate"      : f"{passed_count / len(student_list):.1%}",
            "pass_mark"      : Student.PASS_MARK,
            "subjects"       : list(student_list[0].marks.keys()),
            "generated_by"   : "Satya Sundar — Day 2 OOP Project",
            "date"           : "2026-05-02",
        },
        "students": [s.to_dict() for s in student_list],
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"\n  Saved {len(student_list)} students → '{filename}'")


def load_students_from_json(filename="students.json"):
    """
    Read and deserialise student data from a JSON file.

    Deserialisation = converting stored data back into Python objects.

    Parameters
    ----------
    filename : str — path to the JSON file

    Returns
    -------
    dict — full data dict with 'metadata' and 'students' keys
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"  Loaded {data['metadata']['total_students']} students ← '{filename}'")
    return data


def verify_json(filename="students.json"):
    """
    Reload the JSON file and print a spot-check to confirm integrity.

    Parameters
    ----------
    filename : str
    """
    separator(f"JSON VERIFICATION  ({filename})")

    data = load_students_from_json(filename)

    print("\n  Metadata:")
    for key, value in data["metadata"].items():
        print(f"    {key:<20}: {value}")

    print(f"\n  First student record:")
    first = data["students"][0]
    for key, value in first.items():
        print(f"    {key:<20}: {value}")

    print(f"\n  Last student record:")
    last = data["students"][-1]
    for key, value in last.items():
        print(f"    {key:<20}: {value}")

    print(f"\n  Total records in file: {len(data['students'])}")


# =============================================================
# MAIN — ENTRY POINT
# =============================================================

if __name__ == "__main__":

    # ── 1. SHOW FIRST THREE STUDENTS IN FULL DETAIL ──────────
    separator("SAMPLE STUDENT DETAILS  (first 3)")
    for s in students[:3]:
        print(s)
        print()

    # ── 2. DEMONSTRATE INDIVIDUAL METHODS ────────────────────
    separator("METHOD DEMONSTRATIONS  (Satya Sundar)")
    satya = students[0]
    print(f"  name              : {satya.name}")
    print(f"  roll_number       : {satya.roll_number}")
    print(f"  age               : {satya.age}")
    print(f"  marks             : {satya.marks}")
    print(f"  average()         : {satya.average():.2f}")
    print(f"  grade()           : {satya.grade()}")
    print(f"  passed()          : {satya.passed()}")
    print(f"  highest_subject() : {satya.highest_subject()}")
    print(f"  lowest_subject()  : {satya.lowest_subject()}")
    print(f"  rank_subjects()   : {satya.rank_subjects()}")
    print(f"  subjects_below(90): {satya.subjects_below(90)}")
    print(f"  subjects_above(88): {satya.subjects_above(88)}")
    print(f"  repr              : {repr(satya)}")

    # ── 3. CLASS-LEVEL ANALYSIS ───────────────────────────────
    class_summary(students)
    rank_students(students)
    top_performers(students, n=3)
    students_needing_help(students, threshold=60)
    failed_students(students)
    subject_statistics(students)

    # ── 4. SORTING DEMONSTRATION ──────────────────────────────
    separator("SORTING USING __lt__  (sorted() uses Student.__lt__)")
    ascending  = sorted(students)
    descending = sorted(students, reverse=True)
    print("  Sorted ascending (lowest average first):")
    for s in ascending[:3]:
        print(f"    {s.name:<22} avg={s.average():.2f}")
    print("  Sorted descending (highest average first):")
    for s in descending[:3]:
        print(f"    {s.name:<22} avg={s.average():.2f}")

    # ── 5. EQUALITY DEMONSTRATION ─────────────────────────────
    separator("EQUALITY USING __eq__  (based on roll_number)")
    s1 = students[0]
    s2 = Student(
        "Satya Sundar", "ABIT2024001",
        {"Math": 88, "Python": 92, "ML": 90, "DSA": 85, "OS": 82},
        22,
    )
    s3 = students[1]
    print(f"  s1.roll = {s1.roll_number}, s2.roll = {s2.roll_number}")
    print(f"  s1 == s2 (same roll)  : {s1 == s2}")
    print(f"  s1 == s3 (diff roll)  : {s1 == s3}")

    # ── 6. INPUT VALIDATION DEMONSTRATION ────────────────────
    separator("INPUT VALIDATION DEMONSTRATION")
    print("  Attempting bad marks (marks outside 0-100)...")
    try:
        bad = Student("Test", "BADROLL", {"Math": 110}, 20)
    except ValueError as e:
        print(f"  ValueError caught  : {e}")

    print("  Attempting wrong type for marks...")
    try:
        bad = Student("Test", "BADROLL", "not a dict", 20)
    except TypeError as e:
        print(f"  TypeError caught   : {e}")

    print("  Attempting negative age...")
    try:
        bad = Student("Test", "BADROLL", {"Math": 80}, -5)
    except ValueError as e:
        print(f"  ValueError caught  : {e}")

    # ── 7. PERFORMANCE SUMMARY DICT ──────────────────────────
    separator("PERFORMANCE SUMMARY DICT  (Anita Chatterjee — top student)")
    top_student = sorted(students, reverse=True)[0]
    summary     = top_student.performance_summary()
    print(f"  performance_summary() for {top_student.name}:")
    for key, value in summary.items():
        print(f"    {key:<16}: {value}")

    # ── 8. SAVE TO JSON ───────────────────────────────────────
    separator("SAVING ALL 20 STUDENTS TO JSON")
    save_students_to_json(students, "students.json")

    # ── 9. RELOAD AND VERIFY ──────────────────────────────────
    verify_json("students.json")

    # ── 10. REBUILD STUDENT OBJECTS FROM JSON ────────────────
    separator("REBUILDING STUDENT OBJECTS FROM JSON")
    loaded_data      = load_students_from_json("students.json")
    rebuilt_students = [
        Student(
            record["name"],
            record["roll_number"],
            record["marks"],
            record["age"],
        )
        for record in loaded_data["students"]
    ]
    print(f"\n  Rebuilt {len(rebuilt_students)} Student objects from file.")
    print(f"  First rebuilt student  : {repr(rebuilt_students[0])}")
    print(f"  Last  rebuilt student  : {repr(rebuilt_students[-1])}")
    print(f"  Average of first       : {rebuilt_students[0].average():.2f}")
    print(f"  Grade of first         : {rebuilt_students[0].grade()}")

    # ── DONE ─────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  day02_oop_students.py — COMPLETE")
    print("  Outputs  : students.json")
    print("  Classes  : Student")
    print("  Students : 20")
    print("  Methods  : 12 instance methods + 3 dunder methods")
    print("=" * 60)