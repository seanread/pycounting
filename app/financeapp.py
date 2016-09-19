class finance(object):

    def __init__(self, dataset):

        import cPickle as pickle

        self.dataname = dataset

        with open(dataset) as myballs:
            self.dataset = pickle.load(myballs)
            if type(self.dataset) is not dict:
                self.dataset = {}

    def init(self):
        import cPickle as pickle
        self.dataset = {}
        pickle.dump(self.dataset, open(self.dataname, 'wb'))


class sheet(finance):

    def __init__(self, dataset, st):

        super(sheet, self).__init__(dataset)
        if st not in self.dataset:
            self.dataset[st] = {}
        self.sheet = self.dataset[st]

    def add(self, item, cost):
        import cPickle as pickle
        import datetime
        x = str(datetime.date.today())
        if x not in self.sheet:
            self.sheet[x] = {}
        self.sheet[x][item] = cost

        pickle.dump(self.dataset, open(self.dataname, 'wb'))

    def __str__(self):
        return str(self.sheet)

    def sumday(self, day):

        return sum([self.sheet[day][x] for x in self.sheet[day].keys()])

    def tot(self):

        return sum([sum([self.sheet[x][y] for y in self.sheet[x].keys()])
                    for x in self.sheet.keys()])

    def bup(self):

        import cPickle as pickle
        import datetime

        pickle.dump(self.dataset,
                    open('bup/'+str(datetime.date.today())+'.p', 'wb'))
    def Prrint(self):
        for key in self.sheet:
            print(key)
            for key1 in self.sheet[key]:
                print key1 + " " + str(self.sheet[key][key1])
