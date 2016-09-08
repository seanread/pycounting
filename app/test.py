def add(thing, amount):

    from financeapp import sheet

    x = sheet('dat.p', 'bs')

    x.add(thing, amount)

    print(x.tot())
