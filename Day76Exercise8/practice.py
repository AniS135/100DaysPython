import os
from pypdf import PdfMerger

path = "C:\\Users\\AS\\Documents\\PythonHelp\\"

dir_list = os.listdir(path)

pdfs = []

for files_name in dir_list:
    if files_name.endswith(f".pdf") :
        pdfs.append(path + files_name)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(path + "result.pdf")
merger.close()

print("Successfully Merged the pdfs")