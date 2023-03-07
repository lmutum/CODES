# Accept the names and dates of birth as input
names = input().split(',')
dates = list(map(int, input().split(',')))

# Create a dictionary to store people's names by date of birth
name_dict = {}
for i in range(len(names)):
    date = dates[i]
    name = names[i]
    if date not in name_dict:
        name_dict[date] = [name]
    else:
        name_dict[date].append(name)

# Find all pairs of names with the same date of birth
common = []
for date in name_dict:
    name_list = name_dict[date]
    if len(name_list) > 1:
        for i in range(len(name_list)):
            for j in range(i+1, len(name_list)):
                name1, name2 = name_list[i], name_list[j]
                if name1 < name2:
                    common.append([name1, name2])

# Print the list of common pairs
print(common)
