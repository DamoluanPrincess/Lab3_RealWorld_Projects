from telemetry_utils import (
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST,
    generate_student_telemetry,
    normalize_reading,
    detect_abnormal_values,
)


def process_telemetry(readings):
    """Validate telemetry readings and analyze abnormal values."""
    valid_values = []
    abnormal_values = []
    invalid_values = 0

    for value in readings:
        try:
            normalized = normalize_reading(value)
            valid_values.append(normalized)
        except (TypeError, ValueError) as exc:
            invalid_values += 1
            print(f"[INVALID] {value} -> {exc}")

    abnormal_values = detect_abnormal_values(valid_values)
    average = sum(valid_values) / len(valid_values) if valid_values else 0

    print("--- 3. Intelligent Equipment Monitoring Pipeline ---")
    print(f"Telemetry Data: {readings}")
    print(f"Valid Readings: {valid_values}")
    print(f"Invalid Readings Count: {invalid_values}")
    print(f"Abnormal Values Detected: {abnormal_values}")
    print(f"Average Telemetry: {average:.2f}")

    if average < 70:
        status = "CRITICAL_LOW"
    elif average <= 120:
        status = "NORMAL"
    else:
        status = "ABNORMAL"

    print(f"Final Status: {status}")


if __name__ == "__main__":
    telemetry = generate_student_telemetry(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    process_telemetry(telemetry)
