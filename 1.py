def div(*args):
    try:
        arg1 = int(input("enter dividend: "))
        arg2 = int(input("enter divider: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"
    return res
print(f'result  {div()}')