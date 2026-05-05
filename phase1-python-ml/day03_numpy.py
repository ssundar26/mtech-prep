# =============================================================
# Day 3 — NumPy: The Mathematical Foundation of ML
# Author  : Satya Sundar
# Email   : sundar.satya.ai@gmail.com
# Date    : May 3, 2026
# Goal    : Master NumPy arrays, indexing, broadcasting,
#           linear algebra, random, and save/load.
#           Finish with a complete logistic regression
#           built in pure NumPy — no sklearn, no shortcuts.
# Run     : python day03_numpy.py
# Outputs : embeddings.npy, dataset_splits.npz, marks.csv
# =============================================================

import numpy as np
import time


# ─────────────────────────────────────────────────────────────
# SECTION 1 : CREATING ARRAYS
# ─────────────────────────────────────────────────────────────

def section_creating_arrays():
    """
    Eight essential ways to create NumPy arrays.

    Why NumPy is faster than Python lists:
    1. Contiguous memory  — values stored in one block, no scatter
    2. Fixed dtype        — no type checking overhead per element
    3. C / Fortran backend — operations run at CPU speed, not Python speed

    Result: NumPy is typically 50x – 300x faster for numerical work.
    Every ML library (PyTorch, TensorFlow, JAX) is built on the same ideas.
    """

    print("=" * 60)
    print("  SECTION 1 : CREATING ARRAYS")
    print("=" * 60)

    # ── method 1 : np.array() from a Python list ─────────────
    print("\n── method 1 : np.array() ───────────────────────────────")

    a1d_int   = np.array([1, 2, 3, 4, 5])
    a1d_float = np.array([1.0, 2.0, 3.0])
    a2d       = np.array([[1, 2, 3],
                           [4, 5, 6]])

    print(f"1D int    : {a1d_int}          dtype={a1d_int.dtype}")
    print(f"1D float  : {a1d_float}      dtype={a1d_float.dtype}")
    print(f"2D array  :\n{a2d}  shape={a2d.shape}")

    # ── method 2 : zeros, ones, full, eye ────────────────────
    print("\n── method 2 : zeros / ones / full / eye ────────────────")

    zeros_1d = np.zeros(5)
    zeros_2d = np.zeros((3, 4))
    ones_2d  = np.ones((2, 3))
    fives    = np.full((3, 3), 5.0)
    identity = np.eye(4)

    print(f"zeros(5)        : {zeros_1d}")
    print(f"zeros((3,4))    :\n{zeros_2d}")
    print(f"ones((2,3))     :\n{ones_2d}")
    print(f"full((3,3), 5)  :\n{fives}")
    print(f"eye(4)          :\n{identity}")

    # ── method 3 : np.arange() ───────────────────────────────
    print("\n── method 3 : np.arange(start, stop, step) ────────────")

    r1 = np.arange(10)           # 0 – 9
    r2 = np.arange(1, 11)        # 1 – 10
    r3 = np.arange(0, 1, 0.1)   # floats 0.0 – 0.9
    r4 = np.arange(10, 0, -1)   # countdown

    print(f"arange(10)       : {r1}")
    print(f"arange(1,11)     : {r2}")
    print(f"arange(0,1,0.1)  : {np.round(r3, 1)}")
    print(f"arange(10,0,-1)  : {r4}")

    # ── method 4 : np.linspace() ─────────────────────────────
    print("\n── method 4 : np.linspace(start, stop, num) ───────────")
    # Unlike arange, linspace INCLUDES the stop value

    lr_schedule = np.linspace(0.1, 0.001, 10)   # learning rate decay
    angles      = np.linspace(0, 360, 7)         # 0° – 360° in 7 steps

    print(f"lr schedule  : {np.round(lr_schedule, 4)}")
    print(f"angles 0-360 : {angles}")

    # ── method 5 : np.random ─────────────────────────────────
    print("\n── method 5 : np.random ────────────────────────────────")

    np.random.seed(42)                                   # reproducibility
    r_uniform  = np.random.rand(3, 4)                   # uniform [0, 1)
    r_normal   = np.random.randn(3, 4)                  # standard normal
    r_integers = np.random.randint(0, 100, size=(3, 4)) # integers [0,100)

    print(f"rand(3,4)         :\n{np.round(r_uniform, 3)}")
    print(f"randn(3,4)        :\n{np.round(r_normal, 3)}")
    print(f"randint(0,100,3,4):\n{r_integers}")

    # ── method 6 : _like variants ────────────────────────────
    print("\n── method 6 : zeros_like / ones_like ──────────────────")

    original  = np.array([[1.5, 2.5], [3.5, 4.5]])
    zero_copy = np.zeros_like(original)   # same shape AND dtype
    ones_copy = np.ones_like(original)

    print(f"original   :\n{original}")
    print(f"zeros_like :\n{zero_copy}")
    print(f"ones_like  :\n{ones_copy}")

    # ── method 7 : np.empty() ────────────────────────────────
    print("\n── method 7 : np.empty() ───────────────────────────────")

    buffer = np.empty((2, 3))   # allocates memory WITHOUT initialising
    print(f"empty(2,3) — uninitialized memory:\n{buffer}")
    print("  Always fill empty() before reading — values are garbage")

    # ── method 8 : np.fromfunction() ─────────────────────────
    print("\n── method 8 : np.fromfunction() ────────────────────────")

    mult_table = np.fromfunction(
        lambda i, j: (i + 1) * (j + 1),
        shape=(5, 5),
        dtype=int,
    )
    print(f"5×5 multiplication table:\n{mult_table}")


# ─────────────────────────────────────────────────────────────
# SECTION 2 : ARRAY ATTRIBUTES
# ─────────────────────────────────────────────────────────────

def section_attributes():
    """
    Inspect any array before using it.
    The first thing you do when debugging ML code is check
    .shape, .dtype, .ndim, .size, .nbytes.
    """

    print("\n" + "=" * 60)
    print("  SECTION 2 : ARRAY ATTRIBUTES")
    print("=" * 60)

    # Simulate BERT embeddings: 32 samples × 768 features
    np.random.seed(42)
    embeddings = np.random.randn(32, 768).astype(np.float32)

    print(f"\nSimulated BERT embeddings (32 images, 768-dim each):")
    print(f"  .shape     : {embeddings.shape}")
    print(f"  .ndim      : {embeddings.ndim}")
    print(f"  .dtype     : {embeddings.dtype}")
    print(f"  .size      : {embeddings.size}  (total elements)")
    print(f"  .itemsize  : {embeddings.itemsize} bytes per element")
    print(f"  .nbytes    : {embeddings.nbytes} bytes "
          f"({embeddings.nbytes / 1024:.1f} KB)")

    # Memory comparison across dtypes
    print("\n── dtype memory cost for 1 million elements ────────────")
    n      = 1_000_000
    dtypes = [np.int8, np.int32, np.int64,
              np.float16, np.float32, np.float64]

    for dt in dtypes:
        arr = np.zeros(n, dtype=dt)
        print(
            f"  {dt.__name__:<10} : "
            f"{arr.itemsize} bytes/elem  "
            f"total = {arr.nbytes / 1024 / 1024:.1f} MB"
        )

    # Shape of common ML tensors
    print("\n── shapes of common ML tensors ─────────────────────────")
    tensors = {
        "Scalar"                       : np.array(42),
        "Feature vector (784,)"        : np.zeros(784),
        "Batch of sentences (16, 128)" : np.zeros((16, 128)),
        "Grayscale image (1, 28, 28)"  : np.zeros((1, 28, 28)),
        "Batch of RGB images (32,3,224,224)": np.zeros((32, 3, 224, 224)),
    }
    for desc, arr in tensors.items():
        print(f"  {desc:<42}: shape={arr.shape}  ndim={arr.ndim}")


# ─────────────────────────────────────────────────────────────
# SECTION 3 : INDEXING
# ─────────────────────────────────────────────────────────────

def section_indexing():
    """
    1D, 2D, boolean, and integer array indexing.
    Used every day: selecting batches, filtering samples,
    masking invalid data, gathering predictions.
    """

    print("\n" + "=" * 60)
    print("  SECTION 3 : INDEXING")
    print("=" * 60)

    # ── 1D indexing ──────────────────────────────────────────
    print("\n── 1D indexing ─────────────────────────────────────────")

    losses = np.array([0.95, 0.82, 0.74, 0.63,
                       0.55, 0.48, 0.41, 0.36, 0.31, 0.28])
    #  fwd:  0     1     2     3     4     5     6     7     8     9
    #  bwd: -10   -9    -8    -7    -6    -5    -4    -3    -2    -1

    print(f"losses        : {losses}")
    print(f"losses[0]     : {losses[0]}")     # first epoch
    print(f"losses[-1]    : {losses[-1]}")    # last epoch
    print(f"losses[4]     : {losses[4]}")
    print(f"losses[-3]    : {losses[-3]}")

    # ── 1D slicing ───────────────────────────────────────────
    print("\n── 1D slicing [start:stop:step] ────────────────────────")

    numbers = np.arange(10)
    print(f"numbers       : {numbers}")
    print(f"[2:5]         : {numbers[2:5]}")   # indices 2, 3, 4
    print(f"[:4]          : {numbers[:4]}")    # start → 4
    print(f"[7:]          : {numbers[7:]}")    # 7 → end
    print(f"[::2]         : {numbers[::2]}")   # every 2nd
    print(f"[::-1]        : {numbers[::-1]}")  # reversed
    print(f"[-3:]         : {numbers[-3:]}")   # last 3

    # ── 2D indexing ──────────────────────────────────────────
    print("\n── 2D indexing — [row, col] ────────────────────────────")

    # 5 students × 4 subjects
    marks = np.array([
        [88, 92, 85, 90],    # row 0 : Satya
        [95, 88, 91, 89],    # row 1 : Priya
        [72, 68, 70, 75],    # row 2 : Raju
        [45, 55, 42, 50],    # row 3 : Meena
        [98, 95, 96, 94],    # row 4 : Arjun
    ], dtype=np.float32)
    # cols: Math(0) Python(1) ML(2) DSA(3)

    print(f"marks (5 students × 4 subjects):\n{marks}")
    print(f"\nmarks[0, 0]   : {marks[0, 0]}   ← Satya's Math")
    print(f"marks[1, 2]   : {marks[1, 2]}   ← Priya's ML")
    print(f"marks[-1, -1] : {marks[-1, -1]}   ← Arjun's DSA")
    print(f"marks[2]      : {marks[2]}  ← Raju's all marks")
    print(f"marks[:, 0]   : {marks[:, 0]}  ← Math for all")
    print(f"marks[:, 2]   : {marks[:, 2]}  ← ML for all")

    # ── 2D slicing ───────────────────────────────────────────
    print("\n── 2D slicing ──────────────────────────────────────────")

    print(f"marks[0:2, :]   — first 2 students:\n{marks[0:2, :]}")
    print(f"marks[:, 0:2]   — first 2 subjects:\n{marks[:, 0:2]}")
    print(f"marks[1:4, 1:3] — sub-matrix:\n{marks[1:4, 1:3]}")

    # ── boolean indexing ─────────────────────────────────────
    print("\n── boolean indexing (masking / filtering) ───────────────")

    scores = np.array([85, 42, 92, 38, 78, 95, 55, 47, 88, 62])
    print(f"scores        : {scores}")

    mask = scores >= 60
    print(f"mask (>=60)   : {mask}")
    print(f"passed        : {scores[mask]}")
    print(f"failed        : {scores[scores < 60]}")
    print(f"excellent     : {scores[scores >= 90]}")
    print(f"count passed  : {np.sum(scores >= 60)}")
    print(f"pass rate     : {np.mean(scores >= 60):.1%}")

    # Boolean indexing on 2D — select rows by condition
    row_avgs    = marks.mean(axis=1)
    top_mask    = row_avgs >= 85
    top_students = marks[top_mask]
    print(f"\nRow averages  : {np.round(row_avgs, 2)}")
    print(f"Top students (avg>=85):\n{top_students}")

    # ── integer array indexing ───────────────────────────────
    print("\n── integer array indexing ──────────────────────────────")

    data    = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    indices = np.array([0, 2, 4, 7, 9])
    print(f"data          : {data}")
    print(f"indices       : {indices}")
    print(f"data[indices] : {data[indices]}")

    # Select specific students
    chosen = np.array([0, 2, 4])     # Satya, Raju, Arjun
    print(f"\nChosen rows:\n{marks[chosen]}")

    # ── np.where ─────────────────────────────────────────────
    print("\n── np.where(condition, if_true, if_false) ──────────────")

    raw = np.array([85, 42, 92, 38, 78, 95])
    grades  = np.where(raw >= 60, "PASS", "FAIL")
    capped  = np.where(raw > 90, 90, raw)

    print(f"raw           : {raw}")
    print(f"grades        : {grades}")
    print(f"capped at 90  : {capped}")


# ─────────────────────────────────────────────────────────────
# SECTION 4 : ELEMENT-WISE OPERATIONS AND UFUNCS
# ─────────────────────────────────────────────────────────────

def section_operations():
    """
    NumPy applies operations to every element without loops.
    This is called vectorisation — the core reason NumPy is fast.
    """

    print("\n" + "=" * 60)
    print("  SECTION 4 : ELEMENT-WISE OPERATIONS")
    print("=" * 60)

    a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    b = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

    # ── arithmetic ───────────────────────────────────────────
    print("\n── arithmetic (applied to every element) ───────────────")
    print(f"a             : {a}")
    print(f"b             : {b}")
    print(f"a + b         : {a + b}")
    print(f"a - b         : {a - b}")
    print(f"a * b         : {a * b}")
    print(f"b / a         : {b / a}")
    print(f"a ** 2        : {a ** 2}")
    print(f"np.sqrt(a)    : {np.round(np.sqrt(a), 4)}")
    print(f"np.log(a)     : {np.round(np.log(a), 4)}")
    print(f"np.exp(a)     : {np.round(np.exp(a), 2)}")

    # ── scalar operations ────────────────────────────────────
    print("\n── scalar operations ───────────────────────────────────")
    marks = np.array([85.0, 92.0, 78.0, 95.0, 88.0])
    print(f"marks         : {marks}")
    print(f"marks + 5     : {marks + 5}")
    print(f"marks * 0.1   : {marks * 0.1}")
    print(f"marks - mean  : {np.round(marks - marks.mean(), 2)}")

    # ── neural network activations ───────────────────────────
    print("\n── neural network activation functions ─────────────────")

    z = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])

    sigmoid = 1 / (1 + np.exp(-z))
    relu    = np.maximum(0, z)
    tanh    = np.tanh(z)
    exp_z   = np.exp(z - np.max(z))         # subtract max for stability
    softmax = exp_z / exp_z.sum()

    print(f"z             : {z}")
    print(f"sigmoid(z)    : {np.round(sigmoid, 4)}")
    print(f"relu(z)       : {relu}")
    print(f"tanh(z)       : {np.round(tanh, 4)}")
    print(f"softmax(z)    : {np.round(softmax, 4)}")
    print(f"softmax sum   : {softmax.sum():.6f}  ← always 1.0")

    # ── speed benchmark ──────────────────────────────────────
    print("\n── speed: Python loop vs NumPy ─────────────────────────")

    n   = 1_000_000
    arr = np.random.rand(n)

    t0          = time.perf_counter()
    _           = [x ** 2 for x in arr]
    t_loop      = time.perf_counter() - t0

    t0          = time.perf_counter()
    _           = arr ** 2
    t_numpy     = time.perf_counter() - t0

    print(f"Python loop   : {t_loop:.4f}  seconds")
    print(f"NumPy         : {t_numpy:.6f} seconds")
    print(f"NumPy is {t_loop / t_numpy:.0f}x faster")


# ─────────────────────────────────────────────────────────────
# SECTION 5 : BROADCASTING
# ─────────────────────────────────────────────────────────────

def section_broadcasting():
    """
    Broadcasting lets NumPy operate on arrays of different shapes.
    Understanding it prevents 80% of shape errors in PyTorch.

    The three rules:
    1. Arrays with fewer dims are padded with 1s on the LEFT.
    2. Dimensions of size 1 are stretched to match the other.
    3. If sizes differ and neither is 1 → ValueError.
    """

    print("\n" + "=" * 60)
    print("  SECTION 5 : BROADCASTING")
    print("=" * 60)

    # ── case 1: scalar + 1D ──────────────────────────────────
    print("\n── case 1: scalar and 1D array ─────────────────────────")
    arr    = np.array([1.0, 2.0, 3.0, 4.0, 5.0])   # shape (5,)
    scalar = 10.0
    print(f"arr           : {arr}  shape={arr.shape}")
    print(f"arr + 10.0    : {arr + scalar}")
    print("  scalar treated as [10, 10, 10, 10, 10]")

    # ── case 2: 1D + 2D ──────────────────────────────────────
    print("\n── case 2: 1D array and 2D array ───────────────────────")

    matrix   = np.array([[1,  2,  3,  4],
                          [5,  6,  7,  8],
                          [9, 10, 11, 12]])       # shape (3, 4)
    row_bias = np.array([10, 20, 30, 40])          # shape (4,) → (1,4)
    result   = matrix + row_bias

    print(f"matrix shape  : {matrix.shape}")
    print(f"row_bias shape: {row_bias.shape}")
    print(f"matrix:\n{matrix}")
    print(f"row_bias      : {row_bias}")
    print(f"matrix + row_bias:\n{result}")
    print("  row_bias broadcast across all 3 rows")

    # ── case 3: column vector + row vector ───────────────────
    print("\n── case 3: outer addition (column + row) ───────────────")

    col    = np.array([[1], [2], [3]])    # shape (3, 1)
    row    = np.array([[10, 20, 30]])     # shape (1, 3)
    result = col + row                    # shape (3, 3)

    print(f"col (3,1):\n{col}")
    print(f"row (1,3): {row}")
    print(f"col + row → (3,3):\n{result}")

    # ── practical: normalise a batch ─────────────────────────
    print("\n── practical: normalise BERT embeddings ────────────────")

    np.random.seed(42)
    batch = np.random.randn(32, 768).astype(np.float32)  # (32, 768)
    mean  = batch.mean(axis=0)     # shape (768,) — per-feature mean
    std   = batch.std(axis=0)      # shape (768,)
    norm  = (batch - mean) / (std + 1e-8)  # broadcast over 32 rows

    print(f"batch shape   : {batch.shape}")
    print(f"mean shape    : {mean.shape}")
    print(f"normalised mean : {norm.mean():.6f}  ← near 0")
    print(f"normalised std  : {norm.std():.6f}   ← near 1")

    # ── practical: linear layer forward pass ─────────────────
    print("\n── practical: linear layer — X @ W + b ─────────────────")

    np.random.seed(0)
    X = np.random.randn(8, 4)     # shape (8, 4)
    W = np.random.randn(4, 3)     # shape (4, 3)
    b = np.random.randn(3)        # shape (3,)  → broadcast over 8 rows
    out = X @ W + b               # (8,4)@(4,3)=(8,3), +(3,)→(8,3)

    print(f"X shape       : {X.shape}")
    print(f"W shape       : {W.shape}")
    print(f"b shape       : {b.shape}")
    print(f"output shape  : {out.shape}")
    print(f"output[:2]    :\n{np.round(out[:2], 4)}")
    print("  This is exactly what nn.Linear does in PyTorch")

    # ── broadcasting error ───────────────────────────────────
    print("\n── what causes a broadcasting error ────────────────────")
    a = np.array([1, 2, 3])    # shape (3,)
    b = np.array([1, 2])        # shape (2,)
    print("Trying shapes (3,) + (2,) ...")
    try:
        _ = a + b
    except ValueError as e:
        print(f"ValueError: {e}")
    print("Neither dim is 1, sizes differ → cannot broadcast")


# ─────────────────────────────────────────────────────────────
# SECTION 6 : AGGREGATION AND AXIS
# ─────────────────────────────────────────────────────────────

def section_aggregation():
    """
    Aggregation reduces an array along an axis.
    Getting the axis wrong is the most common NumPy mistake.

    axis=0 → collapse ROWS   → result keeps column dimension
    axis=1 → collapse COLS   → result keeps row dimension
    axis=None → collapse ALL → single scalar
    """

    print("\n" + "=" * 60)
    print("  SECTION 6 : AGGREGATION AND AXIS")
    print("=" * 60)

    print("""
  For shape (rows, cols):
    axis=0 → operate DOWN  rows → result shape: (cols,)
    axis=1 → operate ALONG cols → result shape: (rows,)
""")

    # 5 students × 4 subjects
    marks    = np.array([
        [88, 92, 85, 90],    # Satya
        [95, 88, 91, 89],    # Priya
        [72, 68, 70, 75],    # Raju
        [45, 55, 42, 50],    # Meena
        [98, 95, 96, 94],    # Arjun
    ], dtype=np.float64)
    subjects = ["Math", "Python", "ML", "DSA"]
    names    = ["Satya", "Priya", "Raju", "Meena", "Arjun"]

    print(f"marks:\n{marks}")

    # ── sum ──────────────────────────────────────────────────
    print("\n── np.sum() ────────────────────────────────────────────")
    print(f"sum all       : {marks.sum()}")
    print(f"sum axis=0    : {marks.sum(axis=0)}  ← total per subject")
    print(f"sum axis=1    : {marks.sum(axis=1)}  ← total per student")

    # ── mean ─────────────────────────────────────────────────
    print("\n── np.mean() ───────────────────────────────────────────")
    student_avgs  = marks.mean(axis=1)
    subject_avgs  = marks.mean(axis=0)
    class_average = marks.mean()

    print(f"class average : {class_average:.2f}")
    print("Subject averages:")
    for subj, avg in zip(subjects, subject_avgs):
        print(f"  {subj:<8}: {avg:.2f}")
    print("Student averages:")
    for name, avg in zip(names, student_avgs):
        print(f"  {name:<8}: {avg:.2f}")

    # ── std and var ──────────────────────────────────────────
    print("\n── std and var ─────────────────────────────────────────")
    print(f"class std     : {marks.std():.4f}")
    print(f"subject stds  : {np.round(marks.std(axis=0), 2)}")
    print(f"student stds  : {np.round(marks.std(axis=1), 2)}")

    # ── min, max, argmin, argmax ─────────────────────────────
    print("\n── min, max, argmin, argmax ────────────────────────────")
    print(f"class min     : {marks.min()}")
    print(f"class max     : {marks.max()}")
    print(f"min per student: {marks.min(axis=1)}")
    print(f"max per student: {marks.max(axis=1)}")

    best_subject_idx = marks.argmax(axis=1)   # index of best subject
    print("\nBest subject per student:")
    for i, idx in enumerate(best_subject_idx):
        print(f"  {names[i]:<8}: {subjects[idx]} ({marks[i, idx]:.0f})")

    best_student_idx = marks.mean(axis=1).argmax()
    print(f"\nTop student   : {names[best_student_idx]} "
          f"(avg={marks.mean(axis=1)[best_student_idx]:.2f})")

    # ── cumsum ───────────────────────────────────────────────
    print("\n── cumulative sum ──────────────────────────────────────")
    sales      = np.array([120, 85, 140, 95, 200, 110, 175])
    cumulative = np.cumsum(sales)
    print(f"daily sales   : {sales}")
    print(f"cumulative    : {cumulative}")
    print(f"total         : {cumulative[-1]}")

    # ── percentile and median ────────────────────────────────
    print("\n── percentile and median ───────────────────────────────")
    flat = marks.flatten()
    print(f"median        : {np.median(flat):.2f}")
    print(f"25th pct      : {np.percentile(flat, 25):.2f}")
    print(f"75th pct      : {np.percentile(flat, 75):.2f}")
    print(f"IQR           : "
          f"{np.percentile(flat,75) - np.percentile(flat,25):.2f}")


# ─────────────────────────────────────────────────────────────
# SECTION 7 : RESHAPING
# ─────────────────────────────────────────────────────────────

def section_reshaping():
    """
    Reshape changes structure without changing data.
    Required every day in ML — models need exact input shapes.
    """

    print("\n" + "=" * 60)
    print("  SECTION 7 : RESHAPING")
    print("=" * 60)

    # ── reshape ──────────────────────────────────────────────
    print("\n── reshape() ───────────────────────────────────────────")

    arr = np.arange(1, 25)                   # shape (24,)
    print(f"original      : {arr}  shape={arr.shape}")

    r1 = arr.reshape(4, 6)                   # (4, 6)
    r2 = arr.reshape(2, 3, 4)               # (2, 3, 4)
    r3 = arr.reshape(6, -1)                  # -1 computed → (6, 4)
    r4 = arr.reshape(-1, 8)                  # -1 computed → (3, 8)

    print(f"reshape(4,6)  :\n{r1}")
    print(f"reshape(2,3,4): shape={r2.shape}")
    print(f"reshape(6,-1) : shape={r3.shape}  ← -1 computed as 4")
    print(f"reshape(-1,8) : shape={r4.shape}  ← -1 computed as 3")

    # ── flatten vs ravel ─────────────────────────────────────
    print("\n── flatten() vs ravel() ────────────────────────────────")

    mat   = np.array([[1, 2, 3], [4, 5, 6]])
    flat  = mat.flatten()   # returns a COPY — safe to modify
    ravel = mat.ravel()     # returns a VIEW — modifying changes original

    print(f"mat           :\n{mat}")
    print(f"flatten()     : {flat}  ← copy  (always safe)")
    print(f"ravel()       : {ravel}  ← view (may change original)")

    # ── expand_dims and squeeze ───────────────────────────────
    print("\n── expand_dims() and squeeze() ─────────────────────────")

    vec     = np.array([1, 2, 3, 4])           # shape (4,)
    row_vec = np.expand_dims(vec, axis=0)       # (1, 4)
    col_vec = np.expand_dims(vec, axis=1)       # (4, 1)

    print(f"vec shape     : {vec.shape}")
    print(f"expand axis=0 : {row_vec.shape}  ← row vector")
    print(f"expand axis=1 : {col_vec.shape}  ← column vector")

    bloated  = np.zeros((1, 5, 1, 3))
    squeezed = bloated.squeeze()
    print(f"\nsqueeze input : {bloated.shape}")
    print(f"squeezed      : {squeezed.shape}  ← size-1 dims removed")

    # ── practical: feeding one image to a CNN ────────────────
    print("\n── practical: single image → batch for CNN ─────────────")
    single_image = np.random.rand(3, 224, 224)           # (3, H, W)
    as_batch     = np.expand_dims(single_image, axis=0)  # (1, 3, H, W)
    print(f"single image  : {single_image.shape}")
    print(f"as batch      : {as_batch.shape}")
    print("  CNN expects (batch, C, H, W) — expand_dims adds batch dim")

    # ── transpose ────────────────────────────────────────────
    print("\n── transpose ───────────────────────────────────────────")

    M = np.array([[1, 2, 3], [4, 5, 6]])    # (2, 3)
    print(f"M shape       : {M.shape}\n{M}")
    print(f"M.T shape     : {M.T.shape}\n{M.T}")

    # Self-attention score matrix: Q @ K.T / sqrt(d_k)
    d_k    = 64
    Q      = np.random.randn(8, d_k)
    K      = np.random.randn(8, d_k)
    scores = Q @ K.T / np.sqrt(d_k)
    print(f"\nAttention Q@K.T/√d_k : shape={scores.shape}")
    print("  This is the scaled dot-product attention you build on Day 56")


# ─────────────────────────────────────────────────────────────
# SECTION 8 : STACKING AND SPLITTING
# ─────────────────────────────────────────────────────────────

def section_stacking():
    """Combine and split arrays — used to build datasets and batches."""

    print("\n" + "=" * 60)
    print("  SECTION 8 : STACKING AND SPLITTING")
    print("=" * 60)

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.array([7, 8, 9])

    # ── concatenate ──────────────────────────────────────────
    print("\n── np.concatenate() ────────────────────────────────────")

    cat_1d = np.concatenate([a, b, c])
    print(f"concatenate   : {cat_1d}")

    mat_a  = np.ones((2, 3))
    mat_b  = np.ones((2, 3)) * 2
    cat_r  = np.concatenate([mat_a, mat_b], axis=0)   # more rows
    cat_c  = np.concatenate([mat_a, mat_b], axis=1)   # more cols
    print(f"cat axis=0    : shape={cat_r.shape}")
    print(f"cat axis=1    : shape={cat_c.shape}")

    # ── vstack and hstack ────────────────────────────────────
    print("\n── vstack and hstack ───────────────────────────────────")

    v = np.vstack([a, b, c])    # (3, 3) — stacks as rows
    h = np.hstack([a, b, c])    # (9,)   — joins end to end

    print(f"vstack:\n{v}  shape={v.shape}")
    print(f"hstack: {h}  shape={h.shape}")

    # ── practical: combine mini-batches ──────────────────────
    print("\n── practical: combining embedding batches ───────────────")

    np.random.seed(42)
    b1   = np.random.randn(16, 768).astype(np.float32)
    b2   = np.random.randn(16, 768).astype(np.float32)
    b3   = np.random.randn(16, 768).astype(np.float32)
    full = np.vstack([b1, b2, b3])
    print(f"each batch    : {b1.shape}")
    print(f"combined      : {full.shape}")

    # ── split ────────────────────────────────────────────────
    print("\n── train / val / test split ────────────────────────────")

    data      = np.random.randn(1000, 10)
    train     = data[:700]
    val       = data[700:850]
    test      = data[850:]

    print(f"full dataset  : {data.shape}")
    print(f"train         : {train.shape}")
    print(f"val           : {val.shape}")
    print(f"test          : {test.shape}")


# ─────────────────────────────────────────────────────────────
# SECTION 9 : LINEAR ALGEBRA
# ─────────────────────────────────────────────────────────────

def section_linear_algebra():
    """
    np.linalg — the operations that power every neural network.
    Matrix multiply IS the forward pass.
    Cosine similarity IS your FAISS index metric.
    Eigenvalues ARE what PCA computes.
    """

    print("\n" + "=" * 60)
    print("  SECTION 9 : LINEAR ALGEBRA")
    print("=" * 60)

    # ── dot product ──────────────────────────────────────────
    print("\n── dot product and matrix multiply ─────────────────────")

    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, 5.0, 6.0])
    print(f"a             : {a}")
    print(f"b             : {b}")
    print(f"np.dot(a, b)  : {np.dot(a, b)}  (1×4 + 2×5 + 3×6 = 32)")
    print(f"a @ b         : {a @ b}  (@ is the matmul operator)")

    # 2D matrix multiply
    A = np.array([[1, 2], [3, 4], [5, 6]])    # (3, 2)
    B = np.array([[7, 8, 9], [10, 11, 12]])   # (2, 3)
    C = A @ B                                  # (3, 3)

    print(f"\nA shape       : {A.shape}")
    print(f"B shape       : {B.shape}")
    print(f"A @ B         :\n{C}  shape={C.shape}")

    # ── neural network forward pass ──────────────────────────
    print("\n── 2-layer MLP forward pass ────────────────────────────")

    np.random.seed(42)
    X  = np.random.randn(10, 784)    # 10 flattened MNIST images
    W1 = np.random.randn(784, 256)
    b1 = np.zeros(256)
    W2 = np.random.randn(256, 10)
    b2 = np.zeros(10)

    h1     = np.maximum(0, X @ W1 + b1)   # ReLU hidden layer
    output = h1 @ W2 + b2                  # logits

    print(f"X  (10,784)  @ W1 (784,256) → {(X@W1).shape}")
    print(f"h1 after ReLU                 : {h1.shape}")
    print(f"h1 (10,256)  @ W2 (256,10)  → {output.shape}")
    print("output = 10 class scores for each of 10 images")

    # ── transpose ────────────────────────────────────────────
    print("\n── transpose ───────────────────────────────────────────")
    M = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"M:\n{M}  shape={M.shape}")
    print(f"M.T:\n{M.T}  shape={M.T.shape}")

    # ── determinant ──────────────────────────────────────────
    print("\n── determinant ─────────────────────────────────────────")
    sq  = np.array([[3.0, 1.0], [2.0, 4.0]])
    det = np.linalg.det(sq)
    print(f"matrix:\n{sq}")
    print(f"det           : {det:.4f}  (3×4 − 1×2 = 10)")

    # ── inverse ──────────────────────────────────────────────
    print("\n── matrix inverse ──────────────────────────────────────")
    inv = np.linalg.inv(sq)
    print(f"inverse:\n{np.round(inv, 4)}")
    print(f"M @ M_inv:\n{np.round(sq @ inv, 6)}  ← should be identity")

    # ── eigenvalues ──────────────────────────────────────────
    print("\n── eigenvalues and eigenvectors ────────────────────────")
    M = np.array([[4.0, 2.0], [1.0, 3.0]])
    eigenvalues, eigenvectors = np.linalg.eig(M)
    print(f"matrix:\n{M}")
    print(f"eigenvalues   : {eigenvalues}")
    print(f"eigenvectors  :\n{eigenvectors}")
    print("Eigenvalues used in PCA (dimensionality reduction, Day 35)")

    # ── norm and cosine similarity ────────────────────────────
    print("\n── norm and cosine similarity ──────────────────────────")
    v = np.array([3.0, 4.0])
    print(f"vector        : {v}")
    print(f"L2 norm       : {np.linalg.norm(v):.4f}  (√(9+16) = 5)")
    print(f"L1 norm       : {np.linalg.norm(v, ord=1):.4f}  (3+4 = 7)")

    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, 5.0, 6.0])
    cosine_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    print(f"\ncosine_sim(a,b): {cosine_sim:.4f}")
    print("This is the metric FAISS uses to rank your RAG documents")

    # ── solve linear system ───────────────────────────────────
    print("\n── np.linalg.solve(A, b) ───────────────────────────────")
    # 3x + y = 9
    # x + 2y = 8
    A = np.array([[3.0, 1.0], [1.0, 2.0]])
    b = np.array([9.0, 8.0])
    x = np.linalg.solve(A, b)
    print(f"A:\n{A}")
    print(f"b: {b}")
    print(f"solution: x={x[0]:.2f}, y={x[1]:.2f}")
    print(f"verify: 3×{x[0]:.0f}+{x[1]:.0f}={3*x[0]+x[1]:.0f}  "
          f"{x[0]:.0f}+2×{x[1]:.0f}={x[0]+2*x[1]:.0f}")


# ─────────────────────────────────────────────────────────────
# SECTION 10 : RANDOM MODULE AND REPRODUCIBILITY
# ─────────────────────────────────────────────────────────────

def section_random():
    """
    Random generation and why fixing the seed is mandatory in ML.
    Same seed → same random numbers → reproducible experiments.
    Every paper you read fixes their seed. You must too.
    """

    print("\n" + "=" * 60)
    print("  SECTION 10 : RANDOM MODULE AND REPRODUCIBILITY")
    print("=" * 60)

    # ── why seeds matter ─────────────────────────────────────
    print("\n── why fixing the seed matters ─────────────────────────")

    a = np.random.rand(3)
    b = np.random.rand(3)
    print(f"without seed run 1: {np.round(a, 4)}")
    print(f"without seed run 2: {np.round(b, 4)}  ← different!")

    np.random.seed(42)
    c = np.random.rand(3)
    np.random.seed(42)
    d = np.random.rand(3)
    print(f"\nwith seed=42  run 1: {np.round(c, 4)}")
    print(f"with seed=42  run 2: {np.round(d, 4)}  ← IDENTICAL")
    print("Same seed → reproducible experiments → publishable results")

    # ── generation functions ─────────────────────────────────
    print("\n── generation functions ────────────────────────────────")
    np.random.seed(42)

    print(f"rand(4)        : {np.round(np.random.rand(4), 4)}"
          "  ← uniform [0,1)")
    print(f"randn(4)       : {np.round(np.random.randn(4), 4)}"
          "  ← normal(0,1)")
    print(f"randint(0,10,6): {np.random.randint(0, 10, 6)}"
          "  ← integers [0,10)")
    print(f"uniform(5,10,4): {np.round(np.random.uniform(5,10,4),4)}"
          "  ← uniform [5,10)")
    print(f"choice(5 picks): {np.random.choice(['a','b','c','d'], 5)}")

    # ── weight initialisation ─────────────────────────────────
    print("\n── weight initialisation strategies ────────────────────")
    fan_in, fan_out = 256, 128

    # Xavier/Glorot — for sigmoid/tanh networks
    limit  = np.sqrt(6 / (fan_in + fan_out))
    xavier = np.random.uniform(-limit, limit, (fan_in, fan_out))
    print(f"Xavier shape  : {xavier.shape}  "
          f"range=[{xavier.min():.4f}, {xavier.max():.4f}]")

    # He — for ReLU networks
    std = np.sqrt(2 / fan_in)
    he  = np.random.randn(fan_in, fan_out) * std
    print(f"He shape      : {he.shape}  "
          f"std={he.std():.4f}  (target={std:.4f})")

    # ── shuffle and permutation ───────────────────────────────
    print("\n── shuffle and permutation ─────────────────────────────")
    np.random.seed(42)
    indices = np.arange(10)
    np.random.shuffle(indices)
    print(f"original      : {np.arange(10)}")
    print(f"shuffled      : {indices}")

    np.random.seed(42)
    perm = np.random.permutation(10)
    print(f"permutation   : {perm}  ← new array, original unchanged")

    # ── statistical distributions ─────────────────────────────
    print("\n── statistical distributions ───────────────────────────")
    np.random.seed(42)
    n = 10_000
    normal   = np.random.randn(n)
    uniform  = np.random.rand(n)
    binom    = np.random.binomial(n=1, p=0.3, size=n)

    print(f"normal(0,1)  n={n}: mean={normal.mean():.4f}  "
          f"std={normal.std():.4f}")
    print(f"uniform[0,1) n={n}: mean={uniform.mean():.4f}  "
          f"std={uniform.std():.4f}")
    print(f"binomial p=0.3 n={n}: mean={binom.mean():.4f}  "
          f"← should be 0.3")


# ─────────────────────────────────────────────────────────────
# SECTION 11 : SAVING AND LOADING
# ─────────────────────────────────────────────────────────────

def section_save_load():
    """
    Persist NumPy arrays to disk.
    Used to save FAISS embeddings, dataset splits,
    pre-computed features, and experiment results.
    """

    print("\n" + "=" * 60)
    print("  SECTION 11 : SAVING AND LOADING ARRAYS")
    print("=" * 60)

    np.random.seed(42)

    # ── .npy — single array, binary, fast ────────────────────
    print("\n── .npy (single array, binary) ─────────────────────────")

    embeddings = np.random.randn(500, 768).astype(np.float32)
    np.save("embeddings.npy", embeddings)
    loaded = np.load("embeddings.npy")

    print(f"saved shape   : {embeddings.shape}")
    print(f"loaded shape  : {loaded.shape}")
    print(f"values match  : {np.allclose(embeddings, loaded)}")

    # ── .npz — multiple arrays, compressed ───────────────────
    print("\n── .npz (multiple arrays, compressed) ──────────────────")

    X_train = np.random.randn(700, 10).astype(np.float32)
    y_train = np.random.randint(0, 2, 700)
    X_val   = np.random.randn(150, 10).astype(np.float32)
    y_val   = np.random.randint(0, 2, 150)
    X_test  = np.random.randn(150, 10).astype(np.float32)
    y_test  = np.random.randint(0, 2, 150)

    np.savez_compressed(
        "dataset_splits.npz",
        X_train=X_train, y_train=y_train,
        X_val=X_val,     y_val=y_val,
        X_test=X_test,   y_test=y_test,
    )

    splits = np.load("dataset_splits.npz")
    print(f"keys in file  : {list(splits.keys())}")
    print(f"X_train shape : {splits['X_train'].shape}")
    print(f"y_test shape  : {splits['y_test'].shape}")

    # ── CSV — human-readable ──────────────────────────────────
    print("\n── .csv (human-readable text) ──────────────────────────")

    marks = np.array([
        [88, 92, 85, 90],
        [95, 88, 91, 89],
        [72, 68, 70, 75],
    ])
    np.savetxt("marks.csv", marks, delimiter=",", fmt="%d",
               header="Math,Python,ML,DSA", comments="")
    loaded_marks = np.loadtxt("marks.csv", delimiter=",",
                              skiprows=1, dtype=int)

    print(f"saved marks:\n{marks}")
    print(f"loaded marks:\n{loaded_marks}")
    print(f"match: {np.array_equal(marks, loaded_marks)}")

    print("\nFiles created: embeddings.npy  dataset_splits.npz  marks.csv")


# ─────────────────────────────────────────────────────────────
# SECTION 12 : LOGISTIC REGRESSION IN PURE NUMPY
# ─────────────────────────────────────────────────────────────

def section_ml_pipeline():
    """
    A complete binary logistic regression trained with gradient descent.
    No sklearn. No PyTorch. Just the mathematics made visible.

    This is exactly what sklearn.LogisticRegression does internally.
    Understanding it here means you will understand PyTorch's training
    loop on Day 28 without any confusion.
    """

    print("\n" + "=" * 60)
    print("  SECTION 12 : LOGISTIC REGRESSION IN PURE NUMPY")
    print("=" * 60)

    np.random.seed(42)

    # ── generate linearly separable data ─────────────────────
    n_samples  = 200
    n_features = 2

    # Class 0 centred at ( 2,  2)
    # Class 1 centred at (-2, -2)
    X0 = np.random.randn(n_samples // 2, n_features) + np.array([ 2,  2])
    X1 = np.random.randn(n_samples // 2, n_features) + np.array([-2, -2])
    X  = np.vstack([X0, X1])
    y  = np.array([0] * (n_samples // 2) + [1] * (n_samples // 2))

    # shuffle
    perm = np.random.permutation(n_samples)
    X, y = X[perm], y[perm]

    # ── normalise ─────────────────────────────────────────────
    mean = X.mean(axis=0)
    std  = X.std(axis=0)
    X    = (X - mean) / std

    # ── train / test split ────────────────────────────────────
    split   = int(0.8 * n_samples)
    X_train = X[:split];   y_train = y[:split]
    X_test  = X[split:];   y_test  = y[split:]

    print(f"\nDataset       : {n_samples} samples, {n_features} features")
    print(f"Train         : {X_train.shape}")
    print(f"Test          : {X_test.shape}")

    # ── helper: sigmoid ──────────────────────────────────────
    def sigmoid(z):
        """σ(z) = 1 / (1 + e^{-z}) — clipped for numerical stability."""
        return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))

    # ── initialise weights ────────────────────────────────────
    W  = np.zeros(n_features)    # weight vector
    b  = 0.0                     # bias scalar
    lr = 0.1                     # learning rate

    # ── training loop ─────────────────────────────────────────
    print(f"\n{'Epoch':>6}  {'Loss':>10}  {'Train Acc':>10}")
    print("─" * 32)

    loss_history = []

    for epoch in range(1, 101):

        # Forward pass
        z      = X_train @ W + b       # shape (split,)
        y_hat  = sigmoid(z)            # predicted probabilities

        # Binary cross-entropy loss
        loss   = -np.mean(
            y_train * np.log(y_hat + 1e-15)
            + (1 - y_train) * np.log(1 - y_hat + 1e-15)
        )
        loss_history.append(loss)

        # Backward pass — gradients via chain rule
        error  = y_hat - y_train       # shape (split,)
        dW     = X_train.T @ error / len(y_train)   # shape (n_features,)
        db     = error.mean()

        # Gradient descent update
        W -= lr * dW
        b -= lr * db

        # Print every 10 epochs
        if epoch % 10 == 0:
            preds_train = (sigmoid(X_train @ W + b) >= 0.5).astype(int)
            acc_train   = np.mean(preds_train == y_train)
            print(f"{epoch:>6}  {loss:>10.4f}  {acc_train:>10.1%}")

    # ── evaluate on test set ──────────────────────────────────
    y_pred_prob  = sigmoid(X_test @ W + b)
    y_pred       = (y_pred_prob >= 0.5).astype(int)
    test_acc     = np.mean(y_pred == y_test)

    TP = np.sum((y_pred == 1) & (y_test == 1))
    TN = np.sum((y_pred == 0) & (y_test == 0))
    FP = np.sum((y_pred == 1) & (y_test == 0))
    FN = np.sum((y_pred == 0) & (y_test == 1))

    precision = TP / (TP + FP + 1e-15)
    recall    = TP / (TP + FN + 1e-15)
    f1        = 2 * precision * recall / (precision + recall + 1e-15)

    print(f"\n── test set results ────────────────────────────────────")
    print(f"  Accuracy    : {test_acc:.1%}")
    print(f"  Precision   : {precision:.4f}")
    print(f"  Recall      : {recall:.4f}")
    print(f"  F1 score    : {f1:.4f}")
    print(f"\n  Confusion matrix:")
    print(f"    TP={TP}  FP={FP}")
    print(f"    FN={FN}  TN={TN}")
    print(f"\n  Learned weights : W={np.round(W, 4)}, b={b:.4f}")
    print(f"  Loss at epoch 1  : {loss_history[0]:.4f}")
    print(f"  Loss at epoch 100: {loss_history[-1]:.4f}")
    print(f"  Improvement      : {loss_history[0] - loss_history[-1]:.4f}")
    print("\n  This is exactly what sklearn.LogisticRegression does.")
    print("  On Day 28 you implement the same thing in PyTorch.")


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    section_creating_arrays()
    section_attributes()
    section_indexing()
    section_operations()
    section_broadcasting()
    section_aggregation()
    section_reshaping()
    section_stacking()
    section_linear_algebra()
    section_random()
    section_save_load()
    section_ml_pipeline()

    print("\n" + "=" * 60)
    print("  day03_numpy.py — ALL 12 SECTIONS COMPLETE")
    print("  Files saved : embeddings.npy")
    print("               dataset_splits.npz")
    print("               marks.csv")
    print("=" * 60)