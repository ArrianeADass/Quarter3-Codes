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

import numpy as np

names = ["Me", "Lia", "Jake"]

step = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])


total_steps = np.sum(step, axis=1)
for i in range(len(names)):
    print(f"{names[i]} - Total Steps: {total_steps[i]}")

highest_index = np.argmax(total_steps)
lowest_index = np.argmin(total_steps)
print(f"\nPerson with the highest total steps: {names[highest_index]} ({total_steps[highest_index]})")
difference = total_steps[highest_index] - total_steps[lowest_index]
print(f"Difference between highest and lowest total steps: {difference}")
