def readable_value(value):
    """
    Makes sure the value is easier to read than the default output
    """
    if isinstance(value, float):
        output = f"{value:.2f}"
    else:
        output = str(value)
    return output


def check_result(result, expected):
    icon = "✓" if result == expected else "✗"

    print(f"The result should be "
          f"{readable_value(expected):10s} and it is "
          f"{readable_value(result):10s}: {icon}")
