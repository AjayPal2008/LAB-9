# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 9 individual
# Date: 10/23/2026
import math

def parta(a):
    # Sort a copy to find the median without changing the original list.
    numbers = sorted(a)
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        median = (numbers[middle - 1] + numbers[middle]) / 2
    else:
        median = numbers[middle]
    return numbers[0], median, numbers[-1]

def partb(list_time,list_dist):
    # Divide each change in distance by the corresponding change in time.
    list_vel = [(list_dist[i + 1] - list_dist[i]) /(list_time[i + 1] - list_time[i])for i in range(len(list_time) - 1)]
    return list_vel

def partc(numbers):
    # Check pairs of distinct list positions for a sum of 2030.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 2030:
                return numbers[i] * numbers[j]
    return False

def partd(n):
    # For each possible length, solve for the first positive even number.
    count = 2
    while count * (count + 1) <= n:
        remainder = n - count * (count - 1)
        if remainder % count == 0:
            first = remainder // count
            if first > 0 and first % 2 == 0:
                return list(range(first, first + 2 * count, 2))
        count += 1
    return False

def parte(sphere_radius, hole_radius):
    # Exact integral of the bead's circular cross-sectional area.
    if not 0 <= hole_radius <= sphere_radius:
        raise ValueError("Radii must satisfy 0 <= hole_radius <= sphere_radius.")
    return (4 * math.pi / 3) * (sphere_radius**2 - hole_radius**2)**1.5


def partf(character, name, company, email):
    # Center entries with two spaces on each side of the longest entry.
    entries = [name, company, email]
    width = max(len(entry) for entry in entries) + 4
    border = character * (width + 2)
    lines = [border]
    for entry in entries:
        lines.append(character + entry.center(width) + character)
    lines.append(border)
    return "\n".join(lines)


def partg(x, tolerance):
    # Add series terms until the next term is smaller than the tolerance.
    if not -1 < x < 1:
        raise ValueError("x must be between -1 and 1, exclusive.")
    if tolerance <= 0:
        raise ValueError("Tolerance must be positive.")

    total = 0.0
    n = 1
    term = 2 * x
    while abs(term) >= tolerance:
        total += term
        n += 1
        term = 2 * x**(2 * n - 1) / (2 * n - 1)
    return total
