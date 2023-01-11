# A funtion that reads the headers   
def header_reader(data):
    item = data.strip().split(',')
    return item

# A function that reads the values and convert them to floats
def values_reader(data):
    values = []
    for item in data.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values

# Creating a dictionary item for each row.
def dict_item(headers, values):
    my_dict = {}
    for header, value in zip(headers, values):
        my_dict[header] = value
    return my_dict

# Creating a general function that reads the file and stores each row in a dictionary
def read_csv(path):
    # Opening the file and reading its contents.
    result = []
    with open(path, mode='r') as f1:
        file = f1.readlines()
       
        # reading the headers
        headers = header_reader(file[0])

        for line in file[1:]:
            # Reading the values
            values = values_reader(line)

            # Storing the features for each item
            item = dict_item(headers, values)

            # Storing the dictionary elements in a list
            result.append(item)

    return result
    # Creating a dictionary item for each row

print(read_csv('ENSO.csv'))
