import xlsxwriter
from practice import array

def writer(parametr):
    """
    Writes the data from the `parametr` function to an Excel file.

    Parameters:
        parametr (function): A function that returns a list of lists, where each
        inner list represents a row of data. This function creates an Excel workbook
        and worksheet, sets the column widths, and iterates over the data returned by the
        `parametr` function. It writes each item in the inner list to a cell in the worksheet,
        starting from the top-left corner and moving down and to the right. The function closes
        the workbook when it is finished writing data.
    """
    book = xlsxwriter.Workbook('/Users/alexanderbeloglazov/Desktop/data.xlsx')
    page = book.add_worksheet('Книги')


    row = 0
    column = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        row += 1
   
    book.close()


writer(array)