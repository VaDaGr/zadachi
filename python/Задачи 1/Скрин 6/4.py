names = {'num1':'1',
        'num2':'2',
        'num3':'3',
        'num4':'4',
        'num5':'5',
        }
def dictionarium(dicts):
    keys = list(dicts.keys())
    dicts[keys[0]], dicts[keys[-1]] = dicts[keys[-1]], dicts[keys[0]]
    del dicts[keys[1]]
    dicts['new key'] = 'new value'
    return dicts
print (dictionarium(names))