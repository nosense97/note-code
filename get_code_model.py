# -*- coding: utf-8 -*-
"""Copy of cứu thằng cu em.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kLhGLS_u43l34UHtPooUT3zTDc297p3m
"""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')
url_excel = r'/content/drive/My Drive/don_le_1.11.2.xlsx'

def get_code_model():

    def get_product_code(df, sheet_name):
        compact_df = df.head(5).iloc[4][2]  
        customer_code = compact_df[0:8]
        product_code = df.iloc[:, [1]][13:]

        def get_product_code(product_code):
            result = []
            for i in range(len(product_code)):
                product = df.iloc[:, [1]][(13+i):(13+i+1)]
                condition = (product.convert_dtypes().dtypes == 'string')
                if condition[0] == False:
                    return result
                else:
                    result.append(product)

        product_list_temp = get_product_code(product_code)
        customer_list = []
        for idx, i in enumerate(product_list_temp):
            customer_list.append(i.iloc[0][0])

        def concat_id(customer_code, customer_list, sheet_name):
            result = []
            result.append(sheet_name)
            for i in customer_list:
                result.append(customer_code + '_' + i)
            return result

        return concat_id(customer_code, customer_list, sheet_name)
    
    def get_result(url_excel):
        data_model = []
        file_excel = pd.ExcelFile(url_excel)
        numberOfSheets = len(file_excel.sheet_names)

        for i in range(numberOfSheets):
            sheet_name_temp = 'Sheet' + str( i+1 )
            print(sheet_name_temp)
            df = pd.read_excel(url_excel, sheet_name = sheet_name_temp)
            data = get_product_code(df, sheet_name_temp)
            data_model.append(data)    
        return data_model
    return get_result(url_excel)

print(get_code_model())

