
class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom


    def __enter__(self):
        try :
            self.file = open(self.filename, 'r')
            return self 
        except FileNotFoundError as err:
            print(f"{self.filename} not found")
    
    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self, 'file') and self.file is not None:
            self.file.close()

    def getdata(self):
        if self.header is True:
            nb_columns = (len(str(self.getheader()).split(self.sep)))
            if self.getheader().split(self.sep)[nb_columns-1] == '\n':
                nb_columns-=1

        else:
            nb_columns = -1
        data = []
        lines = self.file.readlines()
        if self.skip_bottom == 0:
            self.skip_bottom = len(lines)
    
        for line in lines[self.skip_top:self.skip_bottom+1]:
            if nb_columns == -1:
                nb_columns = len(line.split(self.sep))
                if nb_columns <= 1:
                    print('File  cdscorrupted')
                    return None
            if nb_columns != len(line.split(self.sep)):
                print('File  corrupted')
                return None
            if line.split(self.sep)[nb_columns-1] == '\n':
                print('File  corrupted')
                return None
            data.append(line.split(self.sep))
        return data

    def getheader(self):
        if self.header is not True:
            return None
        self.file.seek(0)
        return ''.join(self.file.readline())