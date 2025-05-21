import unittest
import hospital_1

class testHospital(unittest.TestCase):

    
    def testEnqueue(self):
        hospital = hospital_1.Queue()
        before = []

        person1 = hospital_1.Patient("Adam", "tomorrow")
        hospital.enqueue(person1)

        self.assertNotEqual(hospital.lista, before)

    def testDequeue(self):
        hospital = hospital_1.Queue()

        person1 = hospital_1.Patient("Adam", "tomorrow")
        hospital.enqueue(person1)
        hospital.dequeue()

        self.assertEqual(hospital.lista, [])

    
    def testPeek(self):
        hospital = hospital_1.Queue()

        person1 = hospital_1.Patient("Adam", "tomorrow")
        hospital.enqueue(person1)

        self.assertEqual("Adam", hospital.peek().name)


if __name__ == "__main__":
    unittest.main()