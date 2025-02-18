def calculate_lift_rounds(n, capacity):
    full_rounds = n // capacity

    if n % capacity != 0:
        return full_rounds + 1
    else:
        return full_rounds