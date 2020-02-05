import uuid


def createUUID(num):
    l = []
    for k in range(0,num):
        l.append(uuid.uuid4())
    return l

def fnc(opt,count):
    if(opt == 'uuid'):
        return createUUID(count)
    elif(opt== 'ascending'):
        return [x for x in range(count)]
    elif(opt == 'descending'):
        return list(reversed([x for x in range(count)]))
    else:
        return []
