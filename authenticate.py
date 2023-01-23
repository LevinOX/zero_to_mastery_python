# an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:

user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrap_func(*args, **kwarg):
        if args[0]['valid'] == True:
            fn(*args, **kwarg)
        else:
            print('not authenticated')
    return wrap_func


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
