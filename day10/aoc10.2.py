from day10 import get_total_points_of_missing_chars, find_corruptions_and_incompletes

corruptions, incomplete_stack = find_corruptions_and_incompletes()
totals = get_total_points_of_missing_chars(incomplete_stack)

print(totals[int((len(totals)-1)/2)])
