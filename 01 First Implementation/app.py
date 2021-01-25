from simple_mc import simple_mc


# Hard code inputs for now, could be a user input
time = 1/3  # yrs
boundary = 50  # boundary level
level = 55  # current level
vol = 0.1  # standard deviation
drift = 0.08  # mean drift of the process
n_paths = 10**4  # number paths to simulate

result = simple_mc(time, boundary, level, vol, drift, n_paths)

print(f"The average level value is {result} \n")

# compare this to the exact value of 6.33436
