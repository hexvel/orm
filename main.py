from models import IntegerField, CharField
from models import Model


class test(Model):
    id = IntegerField()
    name = CharField()
    population = IntegerField()

    def __repr__(self):
        return f'<Test {self.id}: {self.name}; {self.population}>'


if __name__ == '__main__':
    print(test.objects.filter(id=1).fetch())