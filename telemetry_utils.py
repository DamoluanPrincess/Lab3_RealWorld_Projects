import random

LAST_NAME = "DAMOLUAN"
SEED_NUM = 8
FAVORITE_ARTIST = "ILUNA"


def generate_student_telemetry(last_name, seed_num, favorite_artist):
    """Generate deterministic telemetry readings from the student profile."""
    seed_value = sum(ord(char) for char in last_name + favorite_artist) + seed_num
    rng = random.Random(seed_value)
    readings = [round(rng.uniform(40.0, 150.0), 2) for _ in range(6)]
    return readings


def normalize_reading(value):
    """Validate and convert a telemetry reading to float."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Non-numeric telemetry received: {value}")
    numeric_value = float(value)
    if numeric_value < 0 or numeric_value > 200:
        raise ValueError(f"Telemetry out of bounds (0-200): {numeric_value}")
    return numeric_value


def detect_abnormal_values(values, index=0, abnormal=None):
    """Recursively find telemetry values that exceed the normal band."""
    if abnormal is None:
        abnormal = []

    if index >= len(values):
        return abnormal

    reading = values[index]
    if reading > 120 or reading < 40:
        abnormal.append(reading)

    return detect_abnormal_values(values, index + 1, abnormal)
