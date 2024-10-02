def kg_to_lbs(weight):
    return weight * 0.45


def lbs_to_kg(weight):
    return weight/ 0.45


def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
    