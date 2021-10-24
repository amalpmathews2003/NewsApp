









def html():
      with open('news.txt','r',encoding='utf-8') as f:
            data=f.read()
            data=eval(data)
      html=""
      table="<table border='1px'>{table}</table>"
      tr="<tr>{row}</tr>"
      th="<th>{title}</th>"
      td='<td style="overflow:hidden width=100px height=100px">{val}</td>'
      temp=""
      heading=""
      for key,articles in data.items():
            for article in articles:
                  for title,val in article.items():
                        heading+=th.format(title=title)
                  break
            break
      temp+=tr.format(row=heading)
      for key,articles in data.items():
            for article in articles:
                  tds=''
                  for title,val in article.items():
                        tds+=td.format(val=val)
                  temp+=tr.format(row=tds)
      temp=table.format(table=temp)
      with open('temp.html','w',encoding='utf-8') as f:
            f.write(temp)



html()