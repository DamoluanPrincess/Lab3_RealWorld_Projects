import random
import functools
import time

LAST_NAME = "DAMOLUAN"
SEED_NUM = 8
FAVORITE_ARTIST = "ILUNA"


def diagnostic_decorator(func):
    """Decorator to log and record the execution process."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[EXECUTION LOG] Starting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[EXECUTION LOG] Completed {func.__name__} in {end_time - start_time:.6f} seconds.\n")
        return result
    return wrapper


def generate_readings(last_name, seed, artist):
    """Generates unique deterministic readings using student-specific info."""
    seed_value = sum(ord(char) for char in last_name + artist) + seed
    random.seed(seed_value)

    readings = [round(random.uniform(40.0, 160.0), 2) for _ in range(5)]
    return readings


def validate_reading(reading):
    """Validates the input type and acceptable boundary ranges."""
    if not isinstance(reading, (int, float)):
        raise TypeError(f"Non-numeric reading detected: {reading}")
    if reading < 0 or reading > 200:
        raise ValueError(f"Value out of operational bounds (0-200): {reading}")
    return True


def calculate_metrics(valid_readings):
    """Calculates average metric value."""
    if not valid_readings:
        return 0
    return sum(valid_readings) / len(valid_readings)


def classify_status(average):
    """Classifies condition based on calculated metrics."""
    if average < 70:
        return "CRITICAL_LOW"
    elif average <= 120:
        return "NORMAL"
    else:
        return "OVERHEATING"


@diagnostic_decorator
def run_diagnostics():
    print("--- 1. Equipment Diagnostic System ---")
    readings = generate_readings(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    print(f"Generated Equipment Data: {readings}\n")

    valid_readings = []
    validation_results = []

    for r in readings:
        try:
            validate_reading(r)
            valid_readings.append(r)
            validation_results.append(f"Reading {r}: VALID")
        except (TypeError, ValueError) as error:
            validation_results.append(f"Reading {r}: INVALID -> {error}")

    print("Validation Results:")
    for res in validation_results:
        print(f"  {res}")

    avg = calculate_metrics(valid_readings)
    status = classify_status(avg)

    print("\nDiagnostic Results:")
    print(f"  Processed Operational Average: {avg:.2f}")
    print(f"  Equipment Status Classification: {status}")


if __name__ == "__main__":
    run_diagnostics()