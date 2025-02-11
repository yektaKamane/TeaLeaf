import re
import matplotlib.pyplot as plt

# File path for the log file
log_file = "tea.out"
output_image = "incremental_wallclock_vs_timestep.png"

# Lists to store timestep numbers and wallclock times
timesteps = []
wallclock_times = []

# Regular expression patterns to match timesteps and wallclock times
timestep_pattern = re.compile(r"Timestep (\d+)")
wallclock_pattern = re.compile(r"Wallclock:\s+([\d.]+)s")

# Read the log file and extract data
with open(log_file, "r") as file:
    for line in file:
        # Check for a timestep match
        timestep_match = timestep_pattern.search(line)
        if timestep_match:
            timesteps.append(int(timestep_match.group(1)))
        
        # Check for a wallclock time match
        wallclock_match = wallclock_pattern.search(line)
        if wallclock_match:
            wallclock_times.append(float(wallclock_match.group(1)))

# Calculate incremental wallclock time for each timestep
incremental_times = [
    wallclock_times[i] - wallclock_times[i - 1]
    for i in range(1, len(wallclock_times))
]

# Plot incremental wallclock time vs timestep
plt.figure(figsize=(10, 6))
plt.plot(timesteps[1:], incremental_times, marker='o', color='b', linestyle='-')
plt.title("Incremental Wallclock Time per Timestep")
plt.xlabel("Timestep")
plt.ylabel("Time Taken (s)")
plt.grid(True)

# Save the plot as a PNG file
plt.savefig(output_image, format='png')
print(f"Plot saved as {output_image}")
