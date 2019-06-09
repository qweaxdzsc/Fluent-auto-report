import runpy

# Txt input path
txt_name = 'C:\\Users\\zonghui\\Desktop\\python\\519-vent.txt'


# Excel output
excel_name = "706-vent-v10-pp1-150mmfan"                  # Output excel name
sheet_name = "706-vent-v10-pp1-150mmfan"                  # The sheet in excel
Excel_output_path = "C:\\Users\\zonghui\\Desktop\\python\\%s.xlsx"%excel_name
data_name = '706-vent-v10-pp1-150mmfan'                  # get a title for your data

# Html output
html_output_path = "C:\\Users\\zonghui\\Desktop\\python\\"
title = "519-vent-v10-pp1-150mmfan-3800RPM"

# run module get excel
runpy.run_path('txt_to_python.py')


# run module get html
runpy.run_path('python_to_html.py')