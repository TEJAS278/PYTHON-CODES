from pyexcel_xls import save_data
data={"Data1":[[123,45,56],[23,34,35]]}
save_data('D:\Shubham\Python\programs\excelDemo1.xls',data)
from pyexcel_xls import read_data
data1=read_data('D:\Shubham\Python\programs\excelDemo1.xls')
print(data1)
