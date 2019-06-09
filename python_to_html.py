# Python_to_Html

import webbrowser
import os
from txt_to_python import matrix
from get_report import title, html_output_path


# html_output_path = "C:\\Users\\zonghui\\Desktop\\python\\"
# title = "519-vent-v10-pp1-150mmfan-3800RPM"

print(matrix)


# write html tag for volume data table
def get_table(table_matrix, head):
    # table head line
    th_txt = ''
    for i in range(len(head)):
        th_txt = th_txt + '<th scope="col">%s</th>\n' % head[i]

    table = """
    <table class="hor-zebra">
		<thead>
			<tr>
				%s
			</tr>
		</thead>
		<tbody>""" % th_txt

    for i in range(len(table_matrix[0])):  # get how many lines
        if i%2 == 0:
            color_bar = 'class="odd"'
        else:
            color_bar = ''

        table += '\n<tr %s>' % color_bar
        for j in range(len(table_matrix)):
            table += '\n<td>' + table_matrix[j][i] + '</td>'

        table = table + '\n</tr>'

    table = table + '\n</tbody>'+'\n</table>'  # <tr> for line, </td> for cell, finish table

    return table


# get all table's html table
volume_table = get_table(matrix[0:3], ['Volume Flow Rate', '(L/S)', 'Percentage%%'])
sp_table = get_table(matrix[3:5], ['Static Pressure', '(Pa)'])
tp_table = get_table(matrix[5:7], ['Total Pressure', '(Pa)'])
uni_table = get_table(matrix[7:9], ['Uniformity', ' '])
moment_table = get_table(matrix[9:10], ['Torque(N/M)'])

# output to HTML

os.getcwd()
mydir = os.getcwd()  # get directory
ResultHtml = html_output_path + title + ".html"
report = open(ResultHtml, 'w')  # create html

# main frame for html

message = """
<html>
<head>
	<style type="text/css">
		.hor-zebra
		{
			font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
			font-size: 15px;
			
			text-align: left;
			border-collapse: collapse;
		}
		.hor-zebra th
		{
			font-size: 20px;
			font-weight: normal;
			width: 200px;
			padding: 10px 8px;
			color: #039;
		}
		.hor-zebra td
		{
		
			padding: 8px;
			color: #000;
		}
		.hor-zebra .odd
		{
			background: #e8edff; 
		}
		
		
		.lineblock{
			width:90%%;
			height:1.5px;
			margin:30px;
			background:linear-gradient(to left,#efefef,#ADADAD,#efefef);
		}
    </style>
</head>
<body>
     <div style="text-align:center;margin-top:20px;margin-bottom:10px">
	 <h1 style="font-size:65px;display:inline;">%s</h1>
	 
	 </div>
	 <div style="margin-top:5px;padding:0;text-align:center;">
	 <span>File Location: %s </span><span>&nbsp;&nbsp;&nbsp;</span>
	 <span> Author: Zonghui.Jin</span>
	 </div>
	 
	 <div class="lineblock"></div>

<body style="margin-left:120px;margin-right:120px" >
    <div summary = volume flow table">%s</div>
    <div class="lineblock"></div>
    <div>%s</div>
    
    <div class="lineblock"></div>
    <div>%s</div>
    
    <div class="lineblock"></div>
    <div>%s</div>
    
    <div class="lineblock"></div>
    <div>%s</div>
    
    <div class="lineblock"></div>
    <h3 style="font-size:42px">Pathline_sideview</h3>
    <img src="Pathline_sideview.jpg" />
    
    <div class="lineblock"></div>     
    <h3 style="font-size:42px">Pathline_upview</h3>
    <img src="Pathline_upview.jpg" />
    
    <div class="lineblock"></div>
    <h3 style="font-size:42px">Evap_out_Contour</h3>   
    <img src="evap_out.jpg" />
    
    <div class="lineblock"></div>
    <h3 style="font-size:42px">Evap_out_0-4_Contour</h3>   
    <img src="evap_out_0-4.jpg" /> 
    
    <div class="lineblock"></div>
    <h3 style="font-size:42px">Filter_out_Contour</h3>
    <img src="filter_out.jpg" />
        
    <div class="lineblock"></div> 
    <h3 style="font-size:42px">Filter_out_0-4_Contour</h3>
    <img src="filter_out_0-4.jpg" />
      
    <div class="lineblock"></div>      
    <h3 style="font-size:42px">Hc_out Contour</h3>
    <img src="hc_out.jpg" />      
    
</body>
</html>""" % (title, mydir, volume_table, sp_table, tp_table, uni_table, moment_table)

report.write(message)  # write to html
report.close()  # close edit
webbrowser.open(ResultHtml, 1)  # open web

