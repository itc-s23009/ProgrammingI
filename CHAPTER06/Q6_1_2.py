class Person:
    def __init__(self, name = '', nationality = '', birth = '', address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前", self.name)
        print("国籍", self.nationality)
        print("生月日", self.birth)
        print("住んでる所", self.address)


heroine = Person('ルフィ','東の海','５月５日','サウザンドサニー号')
print(heroine.show_attributes())
