megavar = -1
def fun():
    global megavarvar 
    var = 42
    try:
        return var
    except Exception:
        print('oops')
    finally:
        var = 3.14
        megavar = 1

print(fun(), megavar)