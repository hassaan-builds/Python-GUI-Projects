def mera_kudh_ka_loop(iterable):
    iterator=iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


a=[1,2,3]
b=range(1,30)
c=(34,56,78,33,55,67,77,77)
d={3,2,1}
e={0:1,9:2}

print(mera_kudh_ka_loop(e))