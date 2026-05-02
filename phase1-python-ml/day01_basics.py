# =============================================================
# Day 1 — Python Foundation
# Author  : Satya Sundar
# Email   : satyasundar439@gmail.com
# Date    : May 1, 2026
# Goal    : Master variables, data types, operators,
#           strings, and control flow from first principles
# Run     : python day01_python_foundation.py
# =============================================================


# ─────────────────────────────────────────────────────────────
# SECTION 1 : VARIABLES
# ─────────────────────────────────────────────────────────────

def section_variables():
    """Demonstrate variable creation, naming, and reassignment."""

    print("=" * 55)
    print("  SECTION 1 : VARIABLES")
    print("=" * 55)

    # Basic variable assignment
    # The = sign means ASSIGN, not "equals"
    name       = "Satya Sundar"
    age        = 22
    height     = 5.8
    is_student = True

    print(f"name       = {name}")
    print(f"age        = {age}")
    print(f"height     = {height}")
    print(f"is_student = {is_student}")

    # Variables can be reassigned — old value is replaced
    age = 23
    print(f"\nAfter reassignment → age = {age}")

    # Augmented assignment shortcuts
    score = 10
    score += 5    # score = score + 5
    score -= 2    # score = score - 2
    score *= 3    # score = score * 3
    score //= 4   # score = score // 4  (floor division)
    print(f"\nAugmented ops on 10 (+5 -2 *3 //4) → score = {score}")

    # Multiple assignment on one line
    x, y, z = 1, 2, 3
    print(f"\nMultiple assignment → x={x}, y={y}, z={z}")

    # Swap two variables — no temp variable needed in Python
    a, b = 100, 200
    a, b = b, a
    print(f"After swap        → a={a}, b={b}")

    # Chain assignment — same value in multiple variables
    p = q = r = 0
    print(f"Chain assignment  → p={p}, q={q}, r={r}")


# ─────────────────────────────────────────────────────────────
# SECTION 2 : DATA TYPES
# ─────────────────────────────────────────────────────────────

def section_data_types():
    """Demonstrate Python's four fundamental data types."""

    print("\n" + "=" * 55)
    print("  SECTION 2 : DATA TYPES")
    print("=" * 55)

    # ── INT ──────────────────────────────────────────────────
    print("\n── int ─────────────────────────────────────────")
    student_count = 120
    year          = 2026
    negative      = -15
    big           = 1_000_000     # underscores improve readability

    print(f"student_count = {student_count}  → type: {type(student_count)}")
    print(f"year          = {year}  → type: {type(year)}")
    print(f"negative      = {negative}   → type: {type(negative)}")
    print(f"big           = {big}  → type: {type(big)}")

    # ── FLOAT ────────────────────────────────────────────────
    print("\n── float ───────────────────────────────────────")
    pi            = 3.14159
    learning_rate = 0.001         # you will use this in every ML model
    scientific    = 1.5e10        # 1.5 × 10^10

    print(f"pi            = {pi}    → type: {type(pi)}")
    print(f"learning_rate = {learning_rate}     → type: {type(learning_rate)}")
    print(f"scientific    = {scientific}  → type: {type(scientific)}")

    # Floating point imprecision — important for ML
    result = 0.1 + 0.2
    print(f"\n0.1 + 0.2 = {result}  ← floating point imprecision, NOT a bug")

    # ── BOOL ─────────────────────────────────────────────────
    print("\n── bool ────────────────────────────────────────")
    is_training  = True
    has_gpu      = False

    print(f"is_training = {is_training}   → type: {type(is_training)}")
    print(f"has_gpu     = {has_gpu}   → type: {type(has_gpu)}")

    # Booleans are integers (True=1, False=0)
    print(f"\nint(True)  = {int(True)}")
    print(f"int(False) = {int(False)}")

    # Practical ML use: compute accuracy from a list of booleans
    predictions = [True, False, True, True, False, True]
    accuracy    = sum(predictions) / len(predictions)
    print(f"\nPredictions: {predictions}")
    print(f"Accuracy   : {accuracy:.2%}")

    # ── STRING ───────────────────────────────────────────────
    print("\n── str ─────────────────────────────────────────")
    first_name = "Satya"
    last_name  = 'Sundar'         # single or double quotes — both valid
    multiline  = """This is
a multiline
string"""

    print(f"first_name = {first_name}   → type: {type(first_name)}")
    print(f"len(first_name) = {len(first_name)}")
    print(f"multiline:\n{multiline}")

    # ── NONE ─────────────────────────────────────────────────
    print("\n── NoneType ────────────────────────────────────")
    result = None
    print(f"result     = {result}  → type: {type(result)}")
    print(f"is None    = {result is None}")   # always use 'is' for None check

    # ── TYPE CONVERSION ──────────────────────────────────────
    print("\n── type conversion ─────────────────────────────")
    age_str     = "22"
    age_int     = int(age_str)        # str  → int
    price_str   = "4.99"
    price_float = float(price_str)    # str  → float
    number      = 42
    num_str     = str(number)         # int  → str

    print(f'int("22")     = {age_int}    → type: {type(age_int)}')
    print(f'float("4.99") = {price_float} → type: {type(price_float)}')
    print(f'str(42)       = "{num_str}"  → type: {type(num_str)}')

    # isinstance — the safe way to check type
    print(f"\nisinstance(42, int)      = {isinstance(42, int)}")
    print(f"isinstance(3.14, float)  = {isinstance(3.14, float)}")
    print(f"isinstance('hi', str)   = {isinstance('hi', str)}")
    print(f"isinstance(42, float)   = {isinstance(42, float)}")


# ─────────────────────────────────────────────────────────────
# SECTION 3 : OPERATORS
# ─────────────────────────────────────────────────────────────

def section_operators():
    """Demonstrate arithmetic, comparison, and logical operators."""

    print("\n" + "=" * 55)
    print("  SECTION 3 : OPERATORS")
    print("=" * 55)

    a, b = 17, 5

    # ── ARITHMETIC ───────────────────────────────────────────
    print("\n── arithmetic ──────────────────────────────────")
    print(f"{a} + {b}  = {a + b}")       # addition
    print(f"{a} - {b}  = {a - b}")       # subtraction
    print(f"{a} * {b}  = {a * b}")       # multiplication
    print(f"{a} / {b}  = {a / b}")       # division       → always float
    print(f"{a} // {b} = {a // b}")      # floor division → removes decimal
    print(f"{a} % {b}  = {a % b}")       # modulo         → remainder
    print(f"{a} ** {b} = {a ** b}")      # exponentiation

    # Modulo in practice
    print("\n── modulo in practice ──────────────────────────")
    for n in range(10):
        label = "even" if n % 2 == 0 else "odd"
        print(f"  {n} % 2 = {n % 2}  → {label}")

    # Modulo for ML training loop (print every 100 steps)
    print("\n  ML training: print every 3rd step (demo with range 12)")
    for step in range(12):
        if step % 3 == 0:
            print(f"  Step {step:2d}: loss = {1.0 / (step + 1):.4f}")

    # ── COMPARISON ───────────────────────────────────────────
    print("\n── comparison ──────────────────────────────────")
    x, y = 10, 20
    print(f"{x} == {y}  → {x == y}")    # equal to
    print(f"{x} != {y}  → {x != y}")    # not equal to
    print(f"{x} <  {y}  → {x <  y}")    # less than
    print(f"{x} >  {y}  → {x >  y}")    # greater than
    print(f"{x} <= {y}  → {x <= y}")    # less than or equal
    print(f"{x} >= {y}  → {x >= y}")    # greater than or equal

    # ── LOGICAL ──────────────────────────────────────────────
    print("\n── logical ─────────────────────────────────────")
    print(f"True  and True   = {True  and True}")
    print(f"True  and False  = {True  and False}")
    print(f"False and True   = {False and True}")
    print(f"False or  True   = {False or  True}")
    print(f"False or  False  = {False or  False}")
    print(f"not   True       = {not True}")
    print(f"not   False      = {not False}")

    # Practical: checking eligibility
    age       = 22
    has_btech = True
    cgpa      = 8.5
    eligible  = age >= 21 and has_btech and cgpa >= 7.0
    print(f"\nMTech eligibility check → {eligible}")


# ─────────────────────────────────────────────────────────────
# SECTION 4 : STRINGS IN DEPTH
# ─────────────────────────────────────────────────────────────

def section_strings():
    """Demonstrate string indexing, slicing, methods, and f-strings."""

    print("\n" + "=" * 55)
    print("  SECTION 4 : STRINGS IN DEPTH")
    print("=" * 55)

    # ── INDEXING ─────────────────────────────────────────────
    print("\n── indexing ────────────────────────────────────")
    word = "Python"
    #       P  y  t  h  o  n
    # fwd:  0  1  2  3  4  5
    # bwd: -6 -5 -4 -3 -2 -1
    print(f"word        = '{word}'")
    print(f"word[0]     = '{word[0]}'")     # first character
    print(f"word[-1]    = '{word[-1]}'")    # last character
    print(f"word[2]     = '{word[2]}'")
    print(f"word[-3]    = '{word[-3]}'")

    # ── SLICING ──────────────────────────────────────────────
    print("\n── slicing [start:stop:step] ───────────────────")
    text = "MachineLearning"
    print(f"text           = '{text}'")
    print(f"text[0:7]      = '{text[0:7]}'")    # start to 7 (not including 7)
    print(f"text[7:]       = '{text[7:]}'")     # from 7 to end
    print(f"text[:7]       = '{text[:7]}'")     # from start to 7
    print(f"text[:]        = '{text[:]}'")      # full copy
    print(f"text[::2]      = '{text[::2]}'")    # every 2nd character
    print(f"text[::-1]     = '{text[::-1]}'")   # reversed

    # ── STRING METHODS ───────────────────────────────────────
    print("\n── string methods ──────────────────────────────")
    raw = "  Hello, World!  "
    print(f"raw            = '{raw}'")
    print(f".strip()       = '{raw.strip()}'")
    print(f".lower()       = '{raw.strip().lower()}'")
    print(f".upper()       = '{raw.strip().upper()}'")
    print(f".title()       = '{raw.strip().title()}'")
    print(f".replace()     = '{raw.strip().replace('World', 'Python')}'")
    print(f".startswith()  = {raw.strip().startswith('Hello')}")
    print(f".endswith()    = {raw.strip().endswith('!')}")
    print(f".find('World') = {raw.find('World')}")
    print(f".count('l')    = {raw.count('l')}")
    print(f".isdigit()     = {'12345'.isdigit()}")
    print(f".isalpha()     = {'hello'.isalpha()}")

    # split and join
    print("\n── split and join ──────────────────────────────")
    csv = "Satya,22,Cuttack,CSE"
    parts = csv.split(",")
    print(f"split ','  → {parts}")
    rejoined = " | ".join(parts)
    print(f"join ' | ' → '{rejoined}'")

    # ── F-STRINGS ────────────────────────────────────────────
    print("\n── f-strings ───────────────────────────────────")
    name     = "Satya"
    age      = 22
    loss     = 0.34567
    accuracy = 0.9234

    print(f"Basic            : Hello, {name}! You are {age} years old.")
    print(f"Expression       : 7 × 6 = {7 * 6}")
    print(f"Float 4 decimals : loss = {loss:.4f}")
    print(f"Percentage       : accuracy = {accuracy:.2%}")
    print(f"Integer padding  : step {42:04d}")
    print(f"Left align 20    : |{'Satya':<20}|")
    print(f"Right align 20   : |{'Satya':>20}|")


# ─────────────────────────────────────────────────────────────
# SECTION 5 : CONTROL FLOW
# ─────────────────────────────────────────────────────────────

def section_control_flow():
    """Demonstrate if/elif/else, for, while, break, continue, comprehension."""

    print("\n" + "=" * 55)
    print("  SECTION 5 : CONTROL FLOW")
    print("=" * 55)

    # ── IF / ELIF / ELSE ─────────────────────────────────────
    print("\n── if / elif / else ────────────────────────────")
    marks = 85
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"marks={marks} → grade={grade}")

    # Nested condition
    age    = 22
    has_id = True
    if age >= 18:
        if has_id:
            print("Entry allowed")
        else:
            print("Show ID first")
    else:
        print("Entry denied — must be 18+")

    # ── FOR LOOP ─────────────────────────────────────────────
    print("\n── for loop ────────────────────────────────────")

    # range(start, stop, step)
    print("range(0, 10, 2):", end=" ")
    for i in range(0, 10, 2):
        print(i, end=" ")
    print()

    # Loop through a list
    subjects = ["Python", "ML", "DL", "NLP", "RAG"]
    for subject in subjects:
        print(f"  Learning: {subject}")

    # enumerate — index + value together
    print("\nenumerate (rank list):")
    for rank, subject in enumerate(subjects, start=1):
        print(f"  Rank {rank}: {subject}")

    # zip — loop two lists together
    print("\nzip (subjects + hours):")
    hours = [20, 40, 35, 30, 25]
    for subject, hour in zip(subjects, hours):
        print(f"  {subject:<10}: {hour} hours")

    # ── WHILE LOOP ───────────────────────────────────────────
    print("\n── while loop ──────────────────────────────────")
    loss  = 1.0
    epoch = 0
    print("Simulated training (stop when loss < 0.3):")
    while loss > 0.3:
        loss  = round(loss * 0.65, 4)
        epoch += 1
        print(f"  Epoch {epoch:2d}: loss = {loss:.4f}")
    print(f"Training done in {epoch} epochs")

    # ── BREAK AND CONTINUE ───────────────────────────────────
    print("\n── break ───────────────────────────────────────")
    print("Stop at 5:", end=" ")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")
    print()

    print("\n── continue ────────────────────────────────────")
    print("Skip even:", end=" ")
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

    # ── LIST COMPREHENSION ───────────────────────────────────
    print("\n── list comprehension ──────────────────────────")

    # Traditional loop
    squares_loop = []
    for i in range(1, 6):
        squares_loop.append(i ** 2)
    print(f"Loop       : {squares_loop}")

    # Comprehension — same result, one line
    squares_comp = [i ** 2 for i in range(1, 6)]
    print(f"Comprehension: {squares_comp}")

    # With condition
    even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
    print(f"Even squares : {even_squares}")

    # Normalise values to [0, 1] — common in ML preprocessing
    raw = [45, 78, 92, 23, 67, 88]
    lo, hi = min(raw), max(raw)
    normalised = [round((x - lo) / (hi - lo), 4) for x in raw]
    print(f"\nRaw scores : {raw}")
    print(f"Normalised : {normalised}")


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    section_variables()
    section_data_types()
    section_operators()
    section_strings()
    section_control_flow()

    print("\n" + "=" * 55)
    print("  day01_python_foundation.py — ALL SECTIONS DONE")
    print("=" * 55)