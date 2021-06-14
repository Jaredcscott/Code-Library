Dim date
date = now
'The date will be in this format: yyyymmddHHnn
wscript.echo ((year(date)*100 + month(date))*100 + day(date))*10000 + hour(date)*100 + minute(date)