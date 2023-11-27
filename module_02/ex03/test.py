from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('tes.csv', header=True) as file:
        if file == None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print('data: ', data)
            print('header: ', header)



