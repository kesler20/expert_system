
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image as Img
from PIL import ImageTk as imgtk
import os

class DataProcessing(object):

    def __init__(self, data):
        self.data = data

    def get_datetime_from_twelve(self):
        data = pd.DataFrame(self.data)
        data.to_csv('batch.csv')
        data = pd.read_csv('batch.csv')
        print(data)
        try:
            t = data.datetime
        except KeyError:
            t = data.date
        return t

    def get_ticker_from_twelve(self):
        data = pd.DataFrame(self.data)
        print(data)
        data.to_csv('batch.csv')
        data0 = pd.read_csv('batch.csv')
        data = data.columns
        return data0[data[0]]

    def real_data_to_double(self,real_data):
        float_data = [float(x) for x in real_data]
        np_float_data = np.array(float_data)
        return np_float_data  
    
    def generate_n_lenght_list(self, n):
        t = []
        null = [t.append(i) for i in range(n)]
        return t

    def list_of_zeros(self, value):
        list_of_zeroes = []
        empty_container = [list_of_zeroes.append(0) for x in range(len(value) + 1)]
        return list_of_zeroes, empty_container
    
    def series_to_list(self, series):
        list1 = []
        for i in series:
            list1.append(i)
        return list1

    def remove_repeats(self, list1):
        list2 = []
        for i in list1:
            if i in list2:
                pass
            else:
                list2.append(i)
        return list2

    def find_location(self, value):
        i = self.data.isin([value])
        c = 0
        t = 0
        for p in i:
            c += 1
            if p == True:
                t = c
            else:
                pass
        return t

    def Convert(self, tup, di): 
        for a, b in tup: 
            di.setdefault(a, []).append(b) 
        return di 
    
    def seperate_even_location_odd_location(self):
        x = self.data
        even = []
        odd = []
        for i in range(len(x)):
            if i % 2 == 1:
                even.append(x[i])
            else:
                odd.append(x[i])

        df1 = pd.DataFrame(odd)
        df2 = pd.DataFrame(even)
        return df1, df2

    def dictionary_to_dataframe(self, dic, Keys):
        Keys : str
        lenght = []
        keys = []
        values = []
        none = [lenght.append(i) for i in range(len(dic))]
        none = [keys.append(i) for i in dic]
        
        for i in range(lenght[len(lenght) - 1]):
            value = dic[keys[i]]
            values.append(value)
        
        df = pd.DataFrame(lenght)
        df[Keys] = pd.DataFrame(keys)

        try:
            df['Values'] = pd.DataFrame(values)
        except ValueError as verr:
            print(verr)

            values_width = []
            tuple_values_index = []
            
            for j in range(len(values)):
                for i in range(len(values[0])): 
                    tuple_values_index.append((i, values[j][i]))

            for j in range(len(values[0])):
                values_width.append([])
            
            print(tuple_values_index)
            for i in range(len(tuple_values_index)):
                for k in range(len(values[0])):
                    # storing it as tuple because is always going to be one no matter the width the value will be stored as the second value of the tuple
                    if tuple_values_index[i][0] == k:
                        values_width[k].append(tuple_values_index[i][1])
                    else:
                        pass
            
            for x in range(len(values_width)):
                df[f'Column {x}'] = pd.DataFrame(values_width[x])
            df.drop([0], axis=1, inplace=True)
        '''
        or you could have just used :
        import pandas as pd
        data = {
            'Name': ['Microsoft Corporation', 'Google, LLC', 'Tesla, Inc.',\
                    'Apple Inc.', 'Netflix, Inc.'],
            'Symbol': ['MSFT', 'GOOG', 'TSLA', 'AAPL', 'NFLX'],
            'Shares': [100, 50, 150, 200, 80]
        }

        df = pd.DataFrame(data)
        making sure that each list in df is of the same lenght 
        and filling with 0's if it is not

        '''

        return df # in order to print this on the output summary file fx.to_html('output.html')
    
    def from_csv_to_html(dir_):
        files = os.listdir(dir_)
        for i in range(len(files)):
            file = files[i]
            if file.endswith('.csv'):
                data = pd.read_csv(r'app\{}'.format(file))
                data.to_html('file {i}')

    def save_to_text_doc(self, file_name, message):
        init_exercise_file = open(file_name, 'w')
        init_exercise_file.write(message)
        init_exercise_file.close()

    def textfile_i_o(self, filename, text, write):
        try:
            file = open(filename, 'r+')
        except FileNotFoundError:
            file = open(filename, 'w')
            file.close()
        file = open(filename, 'r+')
        content = file.read()
        if write:
            file.write(text)
        else:
            pass
        file.close()
        return content

    def apply_func_to_each_value_of_list(self, input_list, func):
        output_list = list(map(input_list, func))
        return output_list
    
  
    def __str__(self):
        
        for property, value in vars(self).items():
            print(property,':', value)


        return ''.join([property, " : ", str(value)])

    def from_string_comma_string_to_int(self,h):
        int1 = []
        int2 = []
        next_number_flag = False
        for i in h:
            if i == ',':
                next_number_flag = True
            else:
                pass
            if next_number_flag == False:
                int1.append(i)
            else:
                if i == ',':
                    pass
                else:
                    int2.append(i)
        x1 = ''
        x2 = ''
        for i in int1:
            x1 += str(i)
        for i in int2:
            x2 += str(i)
        try:
            x1 = int(x1)
            x2 = int(x2)
        except ValueError:
            x1 = float(x1)
            x2 = float(x2)
        return x1, x2
    
    def resize_image(self,width, height, filename):
        image = Img.open(filename)
        if filename == 'primary.PNG':
            width -=60
            height -=75
        elif filename == 'blue-box.png':
            height -= 55
        else:
            pass
        resize_image = image.resize((width, height))
        img = imgtk.PhotoImage(resize_image)
        return img
