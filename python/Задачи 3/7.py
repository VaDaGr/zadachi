def good_password(password):
    params_pas = {
        'length>6': False,
        'up_letter': False,
        'low_letter': False,
        'numbers': False,
        'spec_sing': False
    }
    if len(password) > 6:
        params_pas['length>6'] = True
    for char in password:
        if char.isupper() and not params_pas['up_letter']:
            params_pas['up_letter'] = True
        if char.islower() and not params_pas['low_letter']:
            params_pas['low_letter'] = True
        if char.isdigit() and not params_pas['numbers']:
            params_pas['numbers'] = True
        if "!@#$%^&*()-+=_".find(char) != -1 and not params_pas['spec_sing']:
            params_pas['spec_sing'] = True
    return len([item for item in params_pas.values() if item])

print(good_password("rxyA34567="))