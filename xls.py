from pyexcel_xls import save_data
data={"EmpId":[[101,102,103],[65,47,789]]}
save_data("d:\\emp.xls",data)
from pyexcel_xls import read_data
data1=read_data('d:\\emp.xls')
print(data1)
