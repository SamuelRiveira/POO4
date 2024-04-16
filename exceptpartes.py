values = [4, 2, 7]
try:
    r = values[25]
except IndexError:
    print('Error: Index not in list')
except Exception:
    print()
else:
    print(f'Your wishes are my command: {r}')
finally:
    print('Have a good day!')