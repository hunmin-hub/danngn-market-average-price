def price_to_int(st_price) :
    temp=list(st_price)
    calc=1
    price=0
    for i in reversed(range(len(temp))) :
        if temp[i]=='원' : continue
        elif temp[i]==',' : continue
        else :
            price=price+int(temp[i])*calc
            calc=calc*10
    return price