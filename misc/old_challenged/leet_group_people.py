# groupSizes = [2, 1, 3, 3, 3, 2]
groupSizes = [3, 3, 3, 3, 3, 1, 3]

final_answer = []
dict_tracker = {}

for index, value in enumerate(groupSizes):
    if value not in dict_tracker.keys():
        dict_tracker[value] = [index]  # initialize group size with a person
    else:
        # Check if group is full
        if len(dict_tracker[value]) == value:
            final_answer.append(dict_tracker[value])  # if full, append to final_answer
            dict_tracker[value] = [index]  # remake a new group
        else:
            dict_tracker[value].append(index)  # if not full, add a person to it

# add to the list all of the "left over" groups
for key in dict_tracker.keys():
    final_answer.append(dict_tracker[key])

print(final_answer)
