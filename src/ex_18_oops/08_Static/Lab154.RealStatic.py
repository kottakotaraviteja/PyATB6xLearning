class ExcelReader:

    @staticmethod
    def read_excel():
        print("Reading Excel File")

class MySqlReader:
    @staticmethod
    def read_sql():
        print("Reading Sql File")

class TcReader:

    def runtc(self):
        ExcelReader.read_excel()
        MySqlReader.read_sql()

tcReader = TcReader()
tcReader.runtc()