from simple_mc import simple_mc
from condition import ConditionType, Condition

# Hard code inputs for now, could be a user input
time = 1/3  # yrs
boundary = 50  # boundary level
level = 55  # current level
vol = 0.1  # standard deviation
drift = 0.08  # mean drift of the process
n_paths = 10**4  # number paths to simulate

# Create the lower and upper boundary condition objects
lower_condition = Condition(boundary, ConditionType.lower)
upper_condition = Condition(boundary, ConditionType.upper)

result_lower = simple_mc(lower_condition.condition,
                         time, level, vol, drift, n_paths)
result_upper = simple_mc(upper_condition.condition,
                         time, level, vol, drift, n_paths)

print(f"The average lower-bounded level value is {result_lower} \n")
print(f"The average upper-bounded level value is {result_upper} \n")

# compare this to the exact value of 6.33436
