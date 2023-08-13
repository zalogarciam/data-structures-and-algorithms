import unittest
from ExpressionTree import ExpressionTree

class TestTokenization(unittest.TestCase):

    def setUp(self):
        self.tree = ExpressionTree()

    def test_tokenize_expression(self):
        expression = "8 - 2 * 3 + 6 / 2"
        tokens = self.tree.tokenize_expression(expression)
        self.assertEqual(tokens, ['8', '-', '2', '*', '3', '+', '6', '/', '2'])

class TestInfixToPostfix(unittest.TestCase):

    def setUp(self):
        self.tree = ExpressionTree()

    def test_infix_to_postfix(self):
        infix = ['8', '-', '2', '*', '3', '+', '6', '/', '2']
        postfix = self.tree.infix_to_postfix(infix)
        self.assertEqual(postfix, ['8', '2', '3', '*', '6', '2', '/', '+', '-'])

class TestExpressionTreeConstruction(unittest.TestCase):

    def setUp(self):
        self.tree = ExpressionTree()

    def test_build_expression_tree(self):
        postfix = ['8', '2', '3', '*', '6', '2', '/', '+', '-']
        root = self.tree.build_expression_tree(postfix)
        # Add your assertions for the expression tree construction here

class TestExpressionEvaluation(unittest.TestCase):

    def setUp(self):
        self.tree = ExpressionTree()

    def test_evaluate_expression_tree(self):
        root = self.tree.Node('-')
        root.left = self.tree.Node('+')
        root.left.left = self.tree.Node('8')
        root.left.right = self.tree.Node('*')
        root.left.right.left = self.tree.Node('2')
        root.left.right.right = self.tree.Node('3')
        root.right = self.tree.Node('/')
        root.right.left = self.tree.Node('6')
        root.right.right = self.tree.Node('2')
        result = self.tree.evaluate_expression_tree(root)
        # Add your assertions for expression tree evaluation here

if __name__ == '__main__':
    unittest.main()