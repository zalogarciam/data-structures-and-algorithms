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
        stack = []  # Pila para almacenar nodos temporales
        
        for token in postfix:
            if token.isdigit():
                stack.append(self.Node(token))  # Crear nodo para operando y empujarlo a la pila
            elif self.is_operator(token):
                right_node = stack.pop()  # Sacar nodo derecho de la pila
                left_node = stack.pop()   # Sacar nodo izquierdo de la pila
                operator_node = self.Node(token)  # Crear nodo para operador
                operator_node.left = left_node   # Establecer el nodo izquierdo como hijo izquierdo
                operator_node.right = right_node  # Establecer el nodo derecho como hijo derecho
                stack.append(operator_node)  # Empujar el nodo operador a la pila
        
        return stack.pop()  # El nodo restante en la pila es la raíz del árbol

    def evaluate_expression_tree(self, root):
        if root.value.isdigit():
            return int(root.value)  # Si el nodo es un operando, devuelve su valor como entero
        left_value = self.evaluate_expression_tree(root.left)    # Evaluar el subárbol izquierdo
        right_value = self.evaluate_expression_tree(root.right)  # Evaluar el subárbol derecho
        if root.value == "+":
            return left_value + right_value   # Realizar suma
        elif root.value == "-":
            return left_value - right_value   # Realizar resta
        elif root.value == "*":
            return left_value * right_value   # Realizar multiplicación
        elif root.value == "/":
            return left_value / right_value   # Realizar división

tree = ExpressionTree()  
expression = "3 +    ( 4  * 5 )"
tokens = tree.tokenize_expression(expression) 
postfix = tree.infix_to_postfix(tokens)
root = tree.build_expression_tree(postfix)
result = tree.evaluate_expression_tree(root)
print(f"Expression Tree Evaluation: {expression.replace(' ', '')}={result}")