import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen=False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        tst=Runner("Тест")
        sum=0
        for i in range(10):
            tst.walk()
        self.assertEqual(tst.distance,50)
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        tst=Runner("Тест")
        sum=0
        for i in range(10):
            tst.run()
        self.assertEqual(tst.distance,100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge (self):
        tst_1=Runner("Тест 1")
        tst_2=Runner("Тест 2")
        sum=0
        for i in range(10):
            tst_1.walk()
            tst_2.run()
        self.assertNotEqual(tst_1.distance,tst_2.distance)

if __name__=="__main__":
    unittest.main