import gspread

class EditGoogleSheet:
    def __init__(self):
        # self.__gc = gspread.authorize(creds)
        self.__data = None
        self.__worksheet = None
        self.__spreadsheet = None
        self.__gc = gspread.service_account('../../auth_files/secrets.json')

    def open_spreadsheet(self, name_spreadsheet):
        """
        :param name_spreadsheet: Mở file excel
        :return:
        """
        self.__spreadsheet = self.__gc.open(name_spreadsheet)
        return self.__spreadsheet

    def open_worksheet(self, page):
        """
        :param page: mở page trong file excel khi đã có file excel, truyền vào index sheet hoặc tên sheet
        :return: 
        """
        self.__worksheet = self.__spreadsheet.get_worksheet(page)

    def get_data(self):
        """
        :return: all records in sheet
        """
        self.__data = self.__worksheet.get_all_records()
        return self.__data
        
    def edit_cell(self, *args):
        """
        :param args: update a cell
        :return: 
        """
        if len(args) == 2:
            self.__worksheet.update(*args)
        if len(args) == 3:
            self.__worksheet.update_cell(*args)

    def print_data(self):
        print(self.__data)
        
        
if __name__ == '__main__':
    gc = EditGoogleSheet()
    gc.open_spreadsheet('Orders')
    gc.open_worksheet(0)
    data = gc.get_data()
    print(data)
    gc.edit_cell('B2', 'Tinh')
    gc.edit_cell(5, 2, 12345)
