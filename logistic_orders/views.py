from django.shortcuts import render
# Create your views here.

import gspread

class EditGoogleSheet:
    def __init__(self):
        # self.__gc = gspread.authorize(creds)
        self.__gc = gspread.service_account('../auth_files/secrets.json')

    def open_spreadsheet(self, name_spreadsheet):
        self.spreadsheet = self.__gc.open(name_spreadsheet)

    def open_worksheet(self, page):
        self.worksheet = self.spreadsheet.get_worksheet(page)

    def get_data(self):
        self.data = self.worksheet.get_all_records()

    def print_data(self):
        print(self.data)


if __name__ == '__main__':
    gc = gspread.service_account('../auth_files/secrets.json')
    print(gc)

    spreadsheet = gc.open('Orders')

    worksheet1 = spreadsheet.get_worksheet(0)

    data = worksheet1.get_all_records()
    print(data)
    worksheet1.update('B2', 'Tinh')
    worksheet1.update_cell(5, 2, 12345)
