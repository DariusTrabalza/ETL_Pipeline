# ETL pipeline

## Installing dependancies
Make sure you have Python3 installed

Use the command 'pip install -r requirements.txt ' on windows to install the relevant packages

## Generating patient data
Use the generate_data file to create a csv file filled with mock patient data.
You can control how many records are created by editing the argument in the main function where the 'create_patients' function is called. The data generated will have a random number of 'None' values. The 'insert_errors' function adds blemishes to the data so the data can be cleaned later on.
