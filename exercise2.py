LAST_NAME = "DAMOLUAN"
SEED_NUM = 8
FAVORITE_ARTIST = "ILUNA"


def generate_fault_code(last_name, seed_num, favorite_artist):
    """Generate a deterministic fault code based on student data."""
    value = sum(ord(char) for char in last_name + favorite_artist) + seed_num
    return (value % 97) + 33


def trace_fault(code, trace=None, count=None):
    """Recursively trace the fault until it reaches the base condition."""
    if trace is None:
        trace = []
    if count is None:
        count = {"calls": 0}

    count["calls"] += 1
    trace.append(code)

    print(f"[TRACE] Recursive call {count['calls']}: fault code = {code}")

    if code <= 1:
        print("[BASE CASE] Reached termination condition.")
        return trace, count["calls"]

    if code % 2 == 0:
        next_code = code // 2
    else:
        next_code = code - 3

    if next_code <= 0:
        next_code = 1

    return trace_fault(next_code, trace, count)


def run_diagnostics():
    fault_code = generate_fault_code(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    print("--- 2. Recursive Fault Trace ---")
    print(f"Generated Fault Data: {fault_code}")

    trace, total_calls = trace_fault(fault_code)

    print("\nRecursive Trace:")
    print(" -> ".join(str(step) for step in trace))
    print(f"\nNumber of Recursive Calls: {total_calls}")
    print("\nExecution Log:")
    print("A recursive diagnostic sequence was performed until the fault reached the base condition.")
    print("\nFinal Output:")
    print("Fault resolved successfully. System status: NORMAL")


if __name__ == "__main__":
    run_diagnostics()
