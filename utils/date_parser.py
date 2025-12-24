import json
from datetime import datetime
import os

# Load date formats from config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "date_formats.json")
with open(CONFIG_PATH, "r") as f:
    DATE_CONFIG = json.load(f)

DATE_FORMATS = DATE_CONFIG.get("formats", ["%d-%b-%Y"])


def parse_date(date_str):
    """
    Try to parse a string using all configured date formats.
    Returns a standardized string in "%d-%b-%Y" format.
    Raises ValueError if no format matches.
    """
    for fmt in DATE_FORMATS:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            # Standardize output format
            return dt.strftime("%d-%b-%Y")
        except ValueError:
            continue
    raise ValueError(f"Date '{date_str}' does not match any known format.")
