"""
Experiment 15 - Garbage Collection in Python (CO-5)
Research on automatic garbage collection and experiments with the gc module.

Notes:
1. Reference counting: every object keeps a count of references to it.
   When the count becomes 0, memory is freed immediately.
2. Reference counting cannot free reference cycles (A -> B -> A),
   so Python also has a cyclic garbage collector (the gc module).
3. The cyclic GC is generational: objects live in generations 0, 1 and 2.
   New objects start in gen 0; objects that survive a collection move up.
   Younger generations are collected more often.
"""
import gc
import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

    def __del__(self):
        print(f"  Node {self.name} destroyed")


# ---------- 1. Reference counting ----------
print("1. Reference counting")
a = [1, 2, 3]
print("  Ref count of a:", sys.getrefcount(a) - 1)   # -1 for the temporary argument
b = a
print("  After b = a   :", sys.getrefcount(a) - 1)
del b
print("  After del b   :", sys.getrefcount(a) - 1)

# ---------- 2. GC status and thresholds ----------
print("\n2. GC information")
print("  GC enabled :", gc.isenabled())
print("  Thresholds :", gc.get_threshold())
print("  Counts     :", gc.get_count())

# ---------- 3. Reference cycle and manual collection ----------
print("\n3. Creating a reference cycle")
gc.disable()                  # turn off automatic collection
n1, n2 = Node("A"), Node("B")
n1.ref, n2.ref = n2, n1       # cycle: A -> B -> A
del n1, n2
print("  Deleted references, but objects still exist due to the cycle")
print("  Running gc.collect() manually...")
collected = gc.collect()
print("  Unreachable objects collected:", collected)
gc.enable()

# ---------- 4. Changing thresholds ----------
print("\n4. Changing thresholds")
original = gc.get_threshold()
gc.set_threshold(500, 5, 5)
print("  New thresholds:", gc.get_threshold())
gc.set_threshold(*original)    # restore original values

# ---------- 5. Collect a specific generation ----------
print("\n5. Collecting generation 0 only:", gc.collect(0), "objects")
print("   Tracked objects count:", len(gc.get_objects()))
