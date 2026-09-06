#Cash Flow
def format_money(value):
    if abs(value) >= 1000:
        return f"${value / 1000:.2f}B"
    else:
        return f"${value:.2f}M"

        