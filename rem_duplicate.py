#monsijb
# Define the remove_duplicates function
def remove_duplicates(input_list):
    new_list = []
    for i in input_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


my_list=["a","b","c","d","a","m","c"]
print(remove_duplicates(my_list))
