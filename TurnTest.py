import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen=True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            my_str=''
            for key, value in test_value.items():
                my_str+=f'{key}: {value} '
            #print(my_str)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn = Tournament(90, self.runner_1, self.runner_3)
        result = turn.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn = Tournament(90, self.runner_2, self.runner_3)
        result = turn.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn= Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['3'] = result

    if __name__ == "__main__":
        unittest.main()