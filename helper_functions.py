def pretty_print(data):
    #print list of dicts cleanly
    for record in data:
        for k,v in record.items():
            print(f"{k}:{v}")
        print()