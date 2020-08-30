import json
f=open('word.json',)
my_data=json.load(f)
fileout = open("word_table.html", "w")
table="<html>\n"
table+="<head>\n"
table+="	<title>Bootstrap Example</title>\n"
table+="	<meta charset='utf-8'>\n"
table+="	<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
table+="	<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>\n"
table+="  	<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>\n"
table+="  	<script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js'></script>\n"
table+="  	<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js'></script>\n"
table+="	<link rel='stylesheet' type='text/css' href='https://cdn.datatables.net/1.10.21/css/jquery.dataTables.css'>\n"
table+="	<script type='text/javascript' charset='utf8' src='https://cdn.datatables.net/1.10.21/js/jquery.dataTables.js'></script>\n"
table+="	<link href='css/addons/datatables2.min.css' rel='stylesheet'>\n"
table+="	<script src='js/addons/datatables2.min.js' type='text/javascript'></script>\n"
table+="	<link href='css/addons/datatables-select2.min.css' rel='stylesheet'>\n"
table+="	<script src='js/addons/datatables-select2.min.js' type='text/javascript'></script>\n"
table+="</head>\n"
table+="<body>\n"
table+= "<table class='table table-striped table-bordered table-hover' cellspacing='0' width='100%' id='doctableid'>\n"

# Create the table's column headers
header = "Word Number,Word".split(",")
table+="	<thead>\n"
table += "		<tr>\n"
for column in header:
    table += "			<th>{0}</th>\n".format(column.strip())
table += "		</tr>\n"
table+="	</thead>\n"

# Create the table's row data
table+='	<tbody id="doctab">\n'
for x,y in my_data.items():
    table += "		<tr>\n"
    table += "			<td>{0}</td>\n".format(x.strip())
    table += "			<td>{0}</td>\n".format(y.strip())
    table += "		</tr>\n"
table+="	</tbody>\n"
table += "</table>\n"
table +="<script> tableTemp = $('#doctableid').DataTable(); $(document).ready( function () {  $('#doctableid').DataTable(); } ); $('input').on( 'keyup', function () { $('#doctableid').DataTable().column( 1 ).search(('^'+document.getElementsByTagName(\"input\")[0].value+'.*$'),true,false).draw(); } );</script>\n"
table+="</body>\n"
table+="</html>"
fileout.writelines(table)
fileout.close()


#<input type="search" class="" placeholder="" aria-controls="doctableid">

#$('input.global_filter').on( 'keyup click', function () { $('#doctableid').DataTable().column( 1 ).search((document.getElementsByTagName(\"input\")[0].value+'.*$'),true,false).draw(); } );
#$('#doctableid').DataTable().column( 1 ).search((document.getElementsByTagName(\"input\")[0].value+'.*$'),true,false).draw();
