requests1 = [10, 25, 60, -3, 0, 45, 80]
requests2 = [5, 15, 30, 55, 100, -10, 0]
requests3 = [0, 20, 40, 70, 90, -5, 10]


#Full Name = Naseer Hussain
#Length excluding spaces = 13

length = 13
pli = length % 3

low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []
valid_count = 0

for req in requests1:
    if req < 0:
        invalid_requests.append(req)
    elif req == 0:
        continue
    elif req >= 1 and req <= 20:
        low_demand.append(req)
        valid_count += 1
    elif req >= 21 and req <= 50:
        moderate_demand.append(req)
        valid_count += 1
    elif req > 50:
        high_demand.append(req)
        valid_count += 1

removed_count = 0

if pli == 0:
    removed_count = len(low_demand)
    low_demand = []
elif pli == 1:
    removed_count = len(high_demand)
    high_demand = []
elif pli == 2:
    removed_count = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []

print("L =", length)
print("PLI =", pli)
print("Total valid requests =", valid_count)
print("Removed due to PLI =", removed_count)
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
