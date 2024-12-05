import unittest
import RunTest
import TurnTest

runST=unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunTest.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(TurnTest.TournamentTest))

TextTestRunner=unittest.TextTestRunner(verbosity=2)
TextTestRunner.run(runST)