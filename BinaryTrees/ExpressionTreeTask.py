import re

class ExpressionTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def tokenize_expression(self, expression):
        # Quita los espacios de la expresion
        expression = expression.replace(" ", "")
        
        # Usa expresiones regulares para tokenizar la expresion
        tokens = re.findall(r"\d+|[()+\-*/]", expression)
        return tokens

    def is_operator(self, token):
        return token in "+-*/"

    def precedence(self, operator):
        if operator in "+-":
            return 1
        if operator in "*/":
            return 2
        return 0

    def infix_to_postfix(self, expression):
        output = []           # Lista para almacenar la expresión en notación postfija
        operator_stack = []   # Pila para almacenar operadores y paréntesis temporales
        
        for token in tokens:
            if token.isdigit():
                output.append(token)  # Agregar operandos directamente a la salida
            elif token == "(":
                operator_stack.append(token)  # Empujar paréntesis izquierdo a la pila
            elif token == ")":
                # Sacar operadores de la pila hasta encontrar el paréntesis izquierdo correspondiente
                while operator_stack and operator_stack[-1] != "(":
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Sacar el paréntesis izquierdo de la pila
            elif self.is_operator(token):
                # Sacar operadores de la pila mientras tengan mayor o igual precedencia
                while operator_stack and self.is_operator(operator_stack[-1]) and self.precedence(operator_stack[-1]) >= self.precedence(token):
                    output.append(operator_stack.pop())
                operator_stack.append(token)  # Empujar el operador actual a la pila
        
        # Sacar cualquier operador restante de la pila y agregarlo a la salida
        while operator_stack:
            output.append(operator_stack.pop())
        
        return output

    def build_expression_tree(self, postfix):
        # Implementar metodo aqui
        return None


    def evaluate_expression_tree(self, root):
        # Implementar metodo aqui
        return None

tree = ExpressionTree()  
expression = "3 +    ( 4  * 5 )"
tokens = tree.tokenize_expression(expression) 
postfix = tree.infix_to_postfix(tokens)
root = tree.build_expression_tree(postfix)
result = tree.evaluate_expression_tree(root)
print(f"Expression Tree Evaluation: {expression.replace(' ', '')} = {result}")