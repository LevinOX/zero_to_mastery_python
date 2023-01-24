def do_stuff(num=0):
    try:
        if num or isinstance(num, int):
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err
    except TypeError as err:
        return err
