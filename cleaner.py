import pandas as pd

def main():
    #open file
    data = pd.read_csv('patients.csv',index_col = 'patient_id')
    #convert to df
    df = pd.DataFrame(data)
    print(df.head())
    print(df.info())
    #remove null rows
    #split names in first and last and title
    #remove word cancer
    #remove mm
    #change column title to include mm
    #remove therapy

if __name__ == '__main__':
    main()