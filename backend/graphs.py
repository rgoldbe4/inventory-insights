from backend.models import *

def monthlySales(session, id):
    sales = session.query(Order).all()
    carts = session.query(Cart).all()
    print(len(carts))
    jan = 0
    feb = 0
    mar = 0
    apr = 0
    may = 0
    jun = 0
    jul = 0
    aug = 0
    sep = 0
    oct = 0
    nov = 0
    dec = 0
    for sale in sales:
        for item in sale.items:
            if item.id == id:
                if sale.date.month == 1:
                    jan +=1
                elif sale.date.month == 2:
                    feb +=1
                elif sale.date.month == 3:
                    mar +=1 
                elif sale.date.month == 4:
                    apr +=1
                elif sale.date.month == 5:
                    may +=1
                elif sale.date.month == 6:
                    jun +=1
                elif sale.date.month == 7:
                    jul +=1
                elif sale.date.month == 8:
                    aug +=1
                elif sale.date.month == 9:
                    sep +=1
                elif sale.date.month == 10:
                    oct +=1 
                elif sale.date.month == 11:
                    nov +=1
                elif sale.date.month == 12:
                    dec +=1
    print(len(sales))
    return jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec
