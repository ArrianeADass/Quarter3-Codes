import numpy as np

#names and days
names = ["Me", 'Lia', 'Jake']
days = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday']

#Row-- me, lia and jake
#column-- days mon-fri

step = np.array([

  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])

print("Daily Step Counts - Monday to Friday")
for i in range(len(names)):
    print(names[i], ':', step[i])

import numpy as np

# names and days
names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# rows = people, columns = days
step = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

print("Daily Step Counts - Monday to Friday\n")
for i in range(len(names)):
    print(names[i], ":", step[i])

print("Statistics\n")

for i in range(len(names)):
    total_steps = np.sum(step[i])
    average_steps = np.mean(step[i])
    min_steps = np.min(step[i])
    max_steps = np.max(step[i])

    print(
        f"{names[i]} - Total Steps: {total_steps} | "
        f"Average: {average_steps:.1f} | "
        f"Min: {min_steps} | Max: {max_steps}"
    )

