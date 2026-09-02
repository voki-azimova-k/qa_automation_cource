from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent / "calculator_log.txt"


def log_operation(operation, arguments, result):
    log_entry = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "arguments": arguments,
        "result": result,
    }

    with open(LOG_FILE, "a") as file:
        file.write(str(log_entry) + "\n")


def log_error(operation, arguments, error):
    log_entry = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "arguments": arguments,
        "error": str(error),
    }

    with open(LOG_FILE, "a") as file:
        file.write(str(log_entry) + "\n")