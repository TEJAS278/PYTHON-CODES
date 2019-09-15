from pyexcel_xls import save_data
data={"sheet1":[[10,40,50],[75,85,74]]}
save_data("demo_excel.xls",data)


from pyexcel_xls import read_data
data=read_data("demo_excel.xls")
print(data)

