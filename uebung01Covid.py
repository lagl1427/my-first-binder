def loadData ( country , fname ):
    with open ( fname ) as csvfile :
        lines = csvfile . readlines ()
    for line in lines :
        if line . startswith ('Province '):
            date_str = line
        if line . startswith (','+ country ):
            data_str = line
            break
    date_lst = date_str . rstrip ('\n'). split (',')
    data_lst = data_str . rstrip ('\n'). split (',')
    
    province , country , latitude , longitude = data_lst [:4]
    
    dates = date_lst [4:]
    counts = np. array ([ int(i) for i in data_lst [4:]])
    
    return country , latitude , longitude , dates , counts