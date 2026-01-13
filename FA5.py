import numpy as np

names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

step = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

# Calculate total steps per day (column-wise)
daily_totals = np.sum(step, axis=0)

# Print total steps for each day
print("Total Steps Per Day:\n")
for i in range(len(days)):
    print(f"{days[i]}: {daily_totals[i]}")

# Identify the most active day
most_active_index = np.argmax(daily_totals)
print(f"\nMost Active Day Overall: {days[most_active_index]} ({daily_totals[most_active_index]} steps)")
