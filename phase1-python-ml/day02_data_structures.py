# =============================================================
# Day 2 — Data Structures in Depth
# Author  : Satya Sundar
# Email   : satyasundar439@gmail.com
# Date    : May 2, 2026
# Goal    : Master lists, tuples, sets, and dictionaries
#           from first principles with practical ML examples
# Run     : python day02_data_structures.py
# =============================================================


# ─────────────────────────────────────────────────────────────
# SECTION 1 : LISTS
# ─────────────────────────────────────────────────────────────

def section_lists():
    """Demonstrate every important list operation with explanation."""

    print("=" * 60)
    print("  SECTION 1 : LISTS")
    print("=" * 60)

    # ── CREATING LISTS ───────────────────────────────────────
    print("\n── creating lists ──────────────────────────────────────")

    empty      = []
    marks      = [85, 92, 78, 95, 88, 72, 90]
    names      = ["Satya", "Priya", "Raju", "Meena", "Arjun"]
    mixed      = [1, "hello", 3.14, True, None]
    from_range = list(range(1, 11))

    print(f"empty      = {empty}")
    print(f"marks      = {marks}")
    print(f"names      = {names}")
    print(f"mixed      = {mixed}")
    print(f"from_range = {from_range}")
    print(f"len(marks) = {len(marks)}")
    print(f"type(marks)= {type(marks)}")

    # ── INDEXING ─────────────────────────────────────────────
    print("\n── indexing ────────────────────────────────────────────")
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    #  fwd :    0         1         2        3         4
    #  bwd :   -5        -4        -3       -2        -1

    print(f"fruits        = {fruits}")
    print(f"fruits[0]     = {fruits[0]}")    # first
    print(f"fruits[2]     = {fruits[2]}")
    print(f"fruits[-1]    = {fruits[-1]}")   # last
    print(f"fruits[-2]    = {fruits[-2]}")   # second from last

    # ── SLICING ──────────────────────────────────────────────
    print("\n── slicing [start:stop:step] ───────────────────────────")
    numbers = list(range(10))                # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"numbers        = {numbers}")
    print(f"numbers[2:5]   = {numbers[2:5]}")    # indices 2, 3, 4
    print(f"numbers[:4]    = {numbers[:4]}")     # from start to 4
    print(f"numbers[7:]    = {numbers[7:]}")     # from 7 to end
    print(f"numbers[::2]   = {numbers[::2]}")    # every 2nd
    print(f"numbers[1::2]  = {numbers[1::2]}")   # odd indices
    print(f"numbers[::-1]  = {numbers[::-1]}")   # reversed
    print(f"numbers[-3:]   = {numbers[-3:]}")    # last 3
    print(f"numbers[:-1]   = {numbers[:-1]}")    # all except last

    # ── MODIFYING LISTS ──────────────────────────────────────
    print("\n── modifying lists ─────────────────────────────────────")
    scores = [85, 92, 78]
    print(f"start          = {scores}")

    scores.append(95)
    print(f"after append   = {scores}")

    scores.insert(1, 88)
    print(f"insert(1, 88)  = {scores}")

    scores.extend([70, 75])
    print(f"extend [70,75] = {scores}")

    scores.remove(78)
    print(f"remove(78)     = {scores}")

    popped = scores.pop()
    print(f"pop()          = {scores}  (removed: {popped})")

    popped_idx = scores.pop(1)
    print(f"pop(1)         = {scores}  (removed: {popped_idx})")

    scores.sort()
    print(f"sort()         = {scores}")

    scores.sort(reverse=True)
    print(f"sort(desc)     = {scores}")

    scores.reverse()
    print(f"reverse()      = {scores}")

    print(f"index(92)      = {scores.index(92)}")
    print(f"count(85)      = {scores.count(85)}")

    # ── USEFUL BUILT-INS ─────────────────────────────────────
    print("\n── useful built-ins ────────────────────────────────────")
    data = [85, 92, 78, 95, 88, 72, 90]
    print(f"data           = {data}")
    print(f"len(data)      = {len(data)}")
    print(f"sum(data)      = {sum(data)}")
    print(f"min(data)      = {min(data)}")
    print(f"max(data)      = {max(data)}")
    print(f"average        = {sum(data) / len(data):.2f}")
    print(f"sorted(data)   = {sorted(data)}")          # returns new list
    print(f"sorted(desc)   = {sorted(data, reverse=True)}")
    print(f"95 in data     = {95 in data}")
    print(f"100 in data    = {100 in data}")

    # ── THE COPY TRAP ─────────────────────────────────────────
    print("\n── the copy trap ───────────────────────────────────────")

    original = [1, 2, 3]
    wrong    = original           # both names point to SAME list
    wrong.append(99)
    print(f"original after wrong.append(99) = {original}  ← CHANGED! Bug!")

    original = [1, 2, 3]
    correct  = original.copy()   # independent copy
    correct.append(99)
    print(f"original after correct.append() = {original}  ← Unchanged. Safe.")
    print(f"correct                         = {correct}")

    # ── NESTED LISTS ─────────────────────────────────────────
    print("\n── nested lists (2D matrix) ────────────────────────────")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print("Matrix:")
    for row in matrix:
        print(f"  {row}")
    print(f"matrix[1][2]   = {matrix[1][2]}")   # row 1, col 2 → 6

    # ── LIST COMPREHENSION ───────────────────────────────────
    print("\n── list comprehension ──────────────────────────────────")

    squares      = [i ** 2 for i in range(1, 6)]
    even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
    raw          = [45, 78, 92, 23, 67, 88]
    lo, hi       = min(raw), max(raw)
    normalised   = [round((x - lo) / (hi - lo), 4) for x in raw]

    print(f"squares        = {squares}")
    print(f"even_squares   = {even_squares}")
    print(f"raw scores     = {raw}")
    print(f"normalised     = {normalised}")

    # ── ENUMERATE AND ZIP ────────────────────────────────────
    print("\n── enumerate and zip ───────────────────────────────────")
    students = ["Satya", "Priya", "Raju"]
    results  = [85, 92, 78]

    print("enumerate:")
    for rank, name in enumerate(students, start=1):
        print(f"  Rank {rank}: {name}")

    print("zip:")
    for name, mark in zip(students, results):
        print(f"  {name}: {mark}")


# ─────────────────────────────────────────────────────────────
# SECTION 2 : TUPLES
# ─────────────────────────────────────────────────────────────

def section_tuples():
    """Demonstrate tuples — ordered, immutable sequences."""

    print("\n" + "=" * 60)
    print("  SECTION 2 : TUPLES")
    print("=" * 60)

    # ── CREATING TUPLES ──────────────────────────────────────
    print("\n── creating tuples ─────────────────────────────────────")

    coordinates = (20.2961, 85.8245)         # Bhubaneswar lat/lon
    rgb_red     = (255, 0, 0)
    info        = ("Satya", 22, "CSE", 8.5)
    single      = (42,)                      # trailing comma required
    not_a_tuple = (42)                       # this is just int 42

    print(f"coordinates = {coordinates}  → type: {type(coordinates)}")
    print(f"rgb_red     = {rgb_red}")
    print(f"info        = {info}")
    print(f"single      = {single}         → type: {type(single)}")
    print(f"not_a_tuple = {not_a_tuple}            → type: {type(not_a_tuple)}")

    # ── IMMUTABILITY ─────────────────────────────────────────
    print("\n── immutability ────────────────────────────────────────")
    point = (3, 4)
    print(f"point = {point}")
    print("Trying point[0] = 99 → ", end="")
    try:
        point[0] = 99
    except TypeError as e:
        print(f"TypeError: {e}")

    # ── TUPLE OPERATIONS ─────────────────────────────────────
    print("\n── tuple operations ────────────────────────────────────")
    marks = (85, 92, 78, 95, 88)
    print(f"marks          = {marks}")
    print(f"len(marks)     = {len(marks)}")
    print(f"min(marks)     = {min(marks)}")
    print(f"max(marks)     = {max(marks)}")
    print(f"sum(marks)     = {sum(marks)}")
    print(f"marks.count(85)= {marks.count(85)}")
    print(f"marks.index(92)= {marks.index(92)}")
    print(f"85 in marks    = {85 in marks}")

    # ── TUPLE UNPACKING ──────────────────────────────────────
    print("\n── tuple unpacking ─────────────────────────────────────")
    name, age, programme = ("Satya", 22, "M.Tech CSE")
    print(f"name       = {name}")
    print(f"age        = {age}")
    print(f"programme  = {programme}")

    # Function returning multiple values as tuple
    def min_max_avg(numbers):
        """Return (min, max, average) of a list."""
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    lo, hi, avg = min_max_avg([85, 92, 78, 95, 88])
    print(f"\nmin={lo}, max={hi}, avg={avg:.2f}")

    # ── WHEN TO USE TUPLE VS LIST ─────────────────────────────
    print("\n── tuple vs list: when to use each ─────────────────────")
    print("Use LIST  when data changes: student marks, training losses")
    print("Use TUPLE when data is fixed: coordinates, RGB, config values")

    # Tuples can be used as dictionary keys — lists cannot
    grid = {}
    grid[(0, 0)] = "origin"
    grid[(3, 4)] = "destination"
    print(f"\ngrid[(0,0)]    = {grid[(0, 0)]}")
    print(f"grid[(3,4)]    = {grid[(3, 4)]}")


# ─────────────────────────────────────────────────────────────
# SECTION 3 : SETS
# ─────────────────────────────────────────────────────────────

def section_sets():
    """Demonstrate sets — unordered collections of unique items."""

    print("\n" + "=" * 60)
    print("  SECTION 3 : SETS")
    print("=" * 60)

    # ── CREATING SETS ────────────────────────────────────────
    print("\n── creating sets ───────────────────────────────────────")

    fruits     = {"apple", "banana", "cherry"}
    duplicates = {85, 92, 78, 85, 92, 95, 78}   # duplicates removed
    empty_set  = set()                            # {} creates dict, not set
    from_list  = set(["python", "ml", "python", "ai", "ml"])

    print(f"fruits         = {fruits}")
    print(f"duplicates     = {duplicates}  ← duplicates removed automatically")
    print(f"empty_set type = {type(empty_set)}")
    print(f"from_list      = {from_list}  ← unique tags only")

    # ── SET OPERATIONS ───────────────────────────────────────
    print("\n── set operations ──────────────────────────────────────")

    python_skills = {"Python", "NumPy", "Pandas", "Matplotlib"}
    ml_skills     = {"Python", "Scikit-learn", "NumPy", "TensorFlow"}

    print(f"python_skills  = {python_skills}")
    print(f"ml_skills      = {ml_skills}")
    print(f"\nunion  (|)     = {python_skills | ml_skills}")
    print(f"intersect (&)  = {python_skills & ml_skills}")
    print(f"difference (-) = {python_skills - ml_skills}")
    print(f"sym_diff (^)   = {python_skills ^ ml_skills}")

    # ── MEMBERSHIP AND METHODS ───────────────────────────────
    print("\n── membership and methods ──────────────────────────────")

    skills = {"Python", "NumPy", "Pandas"}
    print(f"skills         = {skills}")
    print(f"'Python' in    = {'Python' in skills}")
    print(f"'Java' in      = {'Java' in skills}")

    skills.add("PyTorch")
    print(f"after add      = {skills}")

    skills.discard("NumPy")          # no error if missing
    print(f"after discard  = {skills}")

    a = {1, 2, 3}
    b = {1, 2, 3, 4, 5}
    print(f"\na.issubset(b)    = {a.issubset(b)}")
    print(f"b.issuperset(a)  = {b.issuperset(a)}")
    print(f"a.isdisjoint({6,7}) = {a.isdisjoint({6, 7})}")

    # ── PRACTICAL USE ────────────────────────────────────────
    print("\n── practical: removing duplicates from dataset labels ───")
    raw_labels   = ["cat", "dog", "cat", "bird", "dog", "cat", "fish"]
    unique_labels = sorted(set(raw_labels))
    print(f"raw_labels     = {raw_labels}")
    print(f"unique_labels  = {unique_labels}")
    print(f"num_classes    = {len(unique_labels)}")


# ─────────────────────────────────────────────────────────────
# SECTION 4 : DICTIONARIES
# ─────────────────────────────────────────────────────────────

def section_dictionaries():
    """Demonstrate dictionaries — key-value pairs, the ML workhorse."""

    print("\n" + "=" * 60)
    print("  SECTION 4 : DICTIONARIES")
    print("=" * 60)

    # ── CREATING DICTIONARIES ────────────────────────────────
    print("\n── creating dictionaries ───────────────────────────────")

    student = {
        "name"       : "Satya Sundar",
        "age"        : 22,
        "city"       : "Cuttack",
        "marks"      : 85,
        "is_enrolled": True,
    }

    print(f"student        = {student}")
    print(f"type           = {type(student)}")
    print(f"len            = {len(student)}")

    # ── ACCESSING VALUES ─────────────────────────────────────
    print("\n── accessing values ────────────────────────────────────")

    print(f"['name']       = {student['name']}")
    print(f"['marks']      = {student['marks']}")
    print(f".get('city')   = {student.get('city')}")
    print(f".get('grade')  = {student.get('grade')}")           # None
    print(f".get('grade','N/A') = {student.get('grade', 'N/A')}")  # default

    # ── MODIFYING ────────────────────────────────────────────
    print("\n── modifying dictionaries ──────────────────────────────")

    config = {"model": "bert", "epochs": 10, "lr": 0.001}
    print(f"start          = {config}")

    config["batch_size"] = 32          # add new key
    print(f"after add      = {config}")

    config["epochs"] = 20             # update existing key
    print(f"after update   = {config}")

    del config["batch_size"]          # delete a key
    print(f"after del      = {config}")

    removed = config.pop("lr")        # remove and return
    print(f"after pop      = {config}  (removed: {removed})")

    config.update({"lr": 2e-5, "dropout": 0.1, "warmup": 500})
    print(f"after update() = {config}")

    # ── DICTIONARY METHODS ───────────────────────────────────
    print("\n── dictionary methods ──────────────────────────────────")

    hyperparams = {
        "learning_rate": 0.001,
        "epochs"       : 10,
        "batch_size"   : 32,
        "dropout"      : 0.1,
    }

    print(f"keys()         = {list(hyperparams.keys())}")
    print(f"values()       = {list(hyperparams.values())}")
    print(f"items()        = {list(hyperparams.items())}")

    # ── LOOPING ──────────────────────────────────────────────
    print("\n── looping through dictionaries ────────────────────────")

    print("keys only:")
    for key in hyperparams:
        print(f"  {key}")

    print("key-value pairs:")
    for key, value in hyperparams.items():
        print(f"  {key:15s}: {value}")

    # ── DICTIONARY COMPREHENSION ─────────────────────────────
    print("\n── dictionary comprehension ────────────────────────────")

    names  = ["Satya", "Priya", "Raju", "Meena"]
    scores = [85, 92, 78, 95]

    grade_book = {name: score for name, score in zip(names, scores)}
    print(f"grade_book     = {grade_book}")

    passed     = {name: score for name, score in grade_book.items() if score >= 80}
    print(f"passed (>=80)  = {passed}")

    doubled    = {k: v * 2 for k, v in {"a": 1, "b": 2, "c": 3}.items()}
    print(f"doubled vals   = {doubled}")

    # ── NESTED DICTIONARIES ──────────────────────────────────
    print("\n── nested dictionaries ─────────────────────────────────")

    student_record = {
        "name"    : "Satya Sundar",
        "personal": {
            "age"  : 22,
            "city" : "Cuttack",
            "state": "Odisha",
        },
        "academic": {
            "programme": "M.Tech CSE",
            "college"  : "ABIT",
            "subjects" : ["ML", "DL", "NLP", "RAG"],
            "cgpa"     : 8.5,
        },
    }

    print(f"name           = {student_record['name']}")
    print(f"city           = {student_record['personal']['city']}")
    print(f"subjects       = {student_record['academic']['subjects']}")
    print(f"3rd subject    = {student_record['academic']['subjects'][2]}")
    print(f"cgpa           = {student_record['academic']['cgpa']}")

    # ── PRACTICAL ML: HYPERPARAMETER CONFIG ──────────────────
    print("\n── practical: ML experiment config ────────────────────")

    experiment = {
        "name"         : "bert-indic-rag-v1",
        "model"        : "bert-base-multilingual-cased",
        "dataset"      : "odia-news-classification",
        "training"     : {
            "epochs"       : 5,
            "batch_size"   : 16,
            "learning_rate": 2e-5,
            "warmup_steps" : 500,
            "weight_decay" : 0.01,
        },
        "evaluation"   : {
            "metrics"      : ["accuracy", "f1", "precision", "recall"],
            "split"        : 0.2,
        },
    }

    print("Experiment config:")
    for section, value in experiment.items():
        if isinstance(value, dict):
            print(f"  {section}:")
            for k, v in value.items():
                print(f"    {k}: {v}")
        else:
            print(f"  {section}: {value}")


# ─────────────────────────────────────────────────────────────
# SECTION 5 : PRACTICAL COMPARISON
# ─────────────────────────────────────────────────────────────

def section_comparison():
    """Side-by-side comparison of all four data structures."""

    print("\n" + "=" * 60)
    print("  SECTION 5 : WHEN TO USE WHICH STRUCTURE")
    print("=" * 60)

    print("""
  ┌─────────────┬──────────┬───────────┬────────────┬───────────┐
  │ Structure   │ Ordered? │ Mutable?  │ Duplicates │ Key-Value │
  ├─────────────┼──────────┼───────────┼────────────┼───────────┤
  │ list  [ ]   │   Yes    │   Yes     │    Yes     │    No     │
  │ tuple ( )   │   Yes    │   No      │    Yes     │    No     │
  │ set   { }   │   No     │   Yes     │    No      │    No     │
  │ dict  {k:v} │   Yes    │   Yes     │ Keys: No   │    Yes    │
  └─────────────┴──────────┴───────────┴────────────┴───────────┘

  When to use each:
  ─────────────────────────────────────────────────────────────
  LIST   → ordered sequence that changes: training losses, dataset
  TUPLE  → fixed data that must not change: coordinates, RGB, config
  SET    → unique items, membership test, deduplication
  DICT   → labelled data, config, JSON responses, hyperparameters
""")


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    section_lists()
    section_tuples()
    section_sets()
    section_dictionaries()
    section_comparison()

    print("\n" + "=" * 60)
    print("  day02_data_structures.py — ALL SECTIONS COMPLETE")
    print("=" * 60)