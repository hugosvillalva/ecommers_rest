from datetime import datetime

def validate_data(request, field,update = False):
    request = request.copy()
    if update:
        if type(request[field]) == str:
            request.__delitem__[field]
        else:
            #Coloca el field en None
            if type(request[field]) == str: request[field]:request.__setitem__(field, None)
    return request

def format_date(date) :
    date = datetime.strptime(date, '%d/%m/%y')
    date = f"{date.year}-{date.month}-{date.day}"
    return date