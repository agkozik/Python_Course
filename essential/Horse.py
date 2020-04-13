class Horse:
    def run(self):
        print("I can run. Тык-дык-Тык-дык")


class Bird:
    def fly(self):
        print("I can fly.")


class Pegas(Horse, Bird):
    pass


def main():
    pegas = Pegas()
    pegas.fly()
    pegas.run()

if __name__ == '__main__':
    main()