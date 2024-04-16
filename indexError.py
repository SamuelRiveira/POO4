try:
    [1,2][5]
except IndexError:
    print("IndexError")
except Exception:
    print("Otro error")