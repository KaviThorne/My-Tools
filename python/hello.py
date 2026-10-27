# @deps: pendulum
# @target: utils/time_helpers.py
import pendulum

def get_current_utc_time(as_iso: bool = True) -> str:
    """
    Returns the current UTC time formatted as an ISO 8601 string or standard datetime string.
    """
    now = pendulum.now("UTC")
    return now.to_iso8601_string() if as_iso else now.to_datetime_string()