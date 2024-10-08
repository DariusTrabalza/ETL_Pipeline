'''
The aim of this script is to create mock data on cancer patients and save it to a CSV file 

'''
from faker import Faker
import random
from helper_functions import pretty_print, insert_errors, save_csv

def main():
    create_patients(30)
    


def create_patients(num):
    #create faker object
    fake = Faker()
    #create list of records
    data = []
    #set patient ID counter
    patient_id = 0
    #create num patients
    for _ in range(num):
        data.append({
            #generate fake data
            'patient_id': patient_id,
            'age': random.choice([None,random.randint(0,100),random.randint(0,100),random.randint(0,100)]),
            'name':fake.name(),
            'diagnosis':random.choice(['breast cancer','lung cancer', 'stomach cancer','liver cancer', 'brain cancer', 'Leukemia',None]),
            'tumor_size': f"{random.randint(1,45)}mm",
            'treatment':random.choice(['chemo therapy', 'radiation therapy', 'surgery','alternative therapy']),
            'status':random.choice(['remission','stage 1', 'stage 2', 'stage 3', 'stage 4', 'deceased', None]),
        })
        #update id
        patient_id += 1

    #print out the data
    pretty_print(data)
    #make the data unclean
    insert_errors(data)
    #save the data as csv
    save_csv(data)


if __name__ == "__main__":
    main()