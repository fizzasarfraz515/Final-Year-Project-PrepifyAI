def compute_predictability(predicted: set[str], actual: set[str]) -> float:
    """Return overlap between predicted and actual topics."""

    if not actual:
        return 0.0
    return len(predicted & actual) / len(actual)
