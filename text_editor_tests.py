import unittest
import text_editor_2

class testText(unittest.TestCase):

    def testPush(self):
        editor = text_editor_2.Stack()

        editor.push("typing")
        editor.push("typing")
        editor.push("deleting")

        self.assertNotEqual(editor.lista, [])


    def testPop(self):
        editor = text_editor_2.Stack()

        editor.push("typing")
        editor.pop()

        self.assertEqual(editor.lista, [])

    def testPeek(self):
        editor = text_editor_2.Stack()
        editor.push("typing")

        self.assertEqual("typing", editor.peek())

if __name__ == "__main__":
    unittest.main()