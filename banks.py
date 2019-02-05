import pandas as pd

#attach bank and books *.xls files to this project's code and name them "banks.xls" and "books.xls"


banks = pd.read_excel('banks.xls')
banks.fillna(0,inplace=True)

books = pd.read_excel('books.xls')
books.fillna(0,inplace=True)

#define paramaters names - coloumns representing CREDIT and DEBIT transactions in the files you have attached
bank_credit_col_name = 'סכום זכות'
bank_debit_col_name = 'סכום חובה'
books_credit_col_name = 'סכום זכות'
books_debit_col_name = 'סכום חובה'

for index, row in banks.iterrows():
    for index2, row2 in books.iterrows():
        if row[bank_credit_col_name] != 0 and row[bank_credit_col_name] == row2[books_debit_col_name]:
            banks = banks.drop(index)
            books = books.drop(index2)
            break

        if row[bank_debit_col_name] != 0 and row[bank_debit_col_name] == row2[books_credit_col_name]:
            banks = banks.drop(index)
            books = books.drop(index2)
            break

#save to file
banks.to_excel('banks_unresolved.xls')
books.to_excel('books_unresolved.xls')
