import csv
import random

def pretty_print(data):
    #print list of dicts cleanly
    for record in data:
        for k,v in record.items():
            print(f"{k}:{v}")
        print()

def save_csv(data):
    #check for data
    if not data:
        raise ValueError('No data found')

    #get field names
    field_names = data[0].keys()

    #write to file
    try:
        with open('patients.csv','w',newline='') as file:  
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f'An error occured:\n{e}')

def open_csv():
    records = []
    try:
        with open('patients.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        print("File was not found")
    except Exception as e:
        print(f"An error ocurred:\n{e}")

    return records
    

def insert_errors(data):
    #for a random number of names at either [*,!, ?]
    num_of_records = len(data)
    dirty_items = ['!','?','*']

    #alter 10% of records to have symbols
    for _ in range(num_of_records//10):
        rand_int = random.randint(0,num_of_records - 1)
        data[rand_int]['name']+=random.choice(dirty_items)

    #alter 5% of records to wrong type
    for _ in range(num_of_records//20):
        rand_int = random.randint(0,num_of_records - 1)
        #check if None
        if data[rand_int]['age'] is not None:
            data[rand_int]['age'] = str(data[rand_int]['age'])

    #for random number of tumor size replace mm with cm
    for _ in range(num_of_records//3):
        rand_int = random.randint(0,num_of_records - 1)
        #check if None
        if data[rand_int]['tumor_size'] and 'mm' in data[rand_int]['tumor_size']:
            data[rand_int]['tumor_size'] = data[rand_int]['tumor_size'].replace('mm','cm')
    
    return data