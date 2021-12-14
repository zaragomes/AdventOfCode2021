from day14 import polymer_growth_after_days, get_totals
from collections import Counter

days = 40
new_polymer, overlapping_elements = polymer_growth_after_days(days)
totals = get_totals(new_polymer, overlapping_elements)
most_common = max(Counter(totals).values())
least_common = min(Counter(totals).values())
print(most_common - least_common)

