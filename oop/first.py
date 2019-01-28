# from second import create_foam,push_foam



class CoffeeMachine:

    def __init__(self,mls,grams):
        self.mls = mls
        self.grams = grams

    def make_coffee(self):
        self.get_water(self.mls)
        self.get_beens(self.grams)



    def get_water(self,mls):
        self.mls = mls
        print('get {} of water'.format(self.mls))


    def get_beens(self,grams):
        self.grams = grams
        print('get {} of coofee beens'.format(self.grams))



class Cappuchinator:

    def create_foam(self):
        self.prepare_milk()
        self.push_foam()


    def prepare_milk(self):
        print('boil a milk')

    def push_foam(self):
        print('sqwirt a milk foam')


class CappuccinoMachine(CoffeeMachine, Cappuchinator):
    pass


class CapsuleMachine(CoffeeMachine):

    def __init__(self,mls):
        self.mls = mls


    def make_coffee(self):
        self.get_water(self.mls)
        self.get_capsule()


    def get_capsule(self):
        print('work with capsule')

r = CappuccinoMachine(200,30)
r.make_coffee()
r.create_foam()
