from datetime import datetime

dates=['20 Oct 2052','06 Jun 1933','26 May 1960']

def sortDates(dates):
    # Write your code here
    x=[]
    for items in dates:
        x.append(items.replace(" ","-"))
        
    z=sorted(x, key=lambda date: datetime.strptime(date, "%d-%b-%Y"))
    y=[]
    for i in z:
        w=i.replace("-"," ")
        y.append(w)
    return y 