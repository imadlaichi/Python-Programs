# USED LIBRARIES
import math

# CALCULATE THE NUMBER OF STATIONS IN THE INDUSTRY
n_stations = int(input("How many stations do you want your industry to have?: "))
print("")

productions = []
cycle_times = []
for i in range(1, n_stations + 1):
    # CALCULATE THE PRODUCTION EACH STATION MAKES (U/H)
    production = float(input(f"Enter the production in units/hour (u/h) of station {i}: "))
    productions.append(production)
    # Calculate the cycle time for each station
    calculate_cycle_time = 60 / production
    cycle_times.append(calculate_cycle_time)
    # Calculate the lead time of the industry
    lead_time = sum(cycle_times)

# CYCLE TIMES
print("CYCLE TIMES:")
for i in range(len(cycle_times)):
    print(f"The cycle time of Station {i+1}: {cycle_times[i]:.0f} min/unit")
  
# LEAD TIME
print("LEAD TIME:")
print(f"The lead time is: {lead_time:.1f} minutes")

# TAKT TIME
takt_time = max(cycle_times)
print("TAKT TIME")
print("The takt time of the industry is:", takt_time, "minutes")

# BOTTLENECK
bottleneck = cycle_times.index(max(cycle_times)) + 1
print("BOTTLENECK")
print("The station that is bottlenecking is station:", bottleneck)

# WORK IN PROGRESS
wip = lead_time * 1 / takt_time
print(f"The work in progress of your industry is: {wip:.2f} units")
