# ==========================================
# BODMAS INTERPRETER — Main Entry Point
# ==========================================
# Welcome to the heart of the interpreter.
# Here is where it all begins — the journey from a simple mathematical expression
# to a fully evaluated result, following the BODMAS rules step by step.
#
# Every interpreter follows a process — a pipeline that transforms plain text
# (what the user writes) into actions (what the computer understands and executes).
#
# While there can be many supporting stages, there are **three core ones**:
#   1. Lexical Analysis (Tokenization)
#   2. Parsing (Syntax Analysis)
#   3. Evaluation (Execution)
#
# These three steps form the backbone of every interpreter,
# from the simplest calculator to full programming languages like Python or Lua.

# We import our three core components — each one representing one of these stages.
from core import evaluator, parser, lexer


# ==========================================
# STEP 0: Collecting the Expression
# ==========================================
# Before any processing begins, we need input.
# In this interpreter, our input is a mathematical expression —
# something like:  2+2(3), (5+3)*2, or even nested ones like (2+(3*4))/2
#
# We use Python’s built-in input() function to collect the expression as a string.
bodmas_expression = input("Enter your expression: ")

# That string, stored in `bodmas_expression`, now becomes our "source code" —
# the text that our interpreter will read, understand, and execute.


# ==========================================
# STEP 1: Lexical Analysis — Tokenization
# ==========================================
# The first step in any interpreter’s pipeline is to *read the source code*
# and break it down into smaller, meaningful symbols called *tokens*.
#
# For example:
#     "2 + 3 * 4"
# becomes:
#     ["2", "+", "3", "*", "4"]
#
# Each token is a small unit — a number, operator, or parenthesis.
# The collection of tokens forms the language’s basic vocabulary.
#
# This process is handled by our `lexer` (Lexical Analyzer).
token = lexer.lex(bodmas_expression)

# You can uncomment the line below to see what tokens the interpreter generates.
# print(f"Tokens: {token}")


# ==========================================
# STEP 2: Parsing — Building the AST
# ==========================================
# Once we have the tokens, we need to understand how they fit together.
# The parser’s job is to analyze the tokens according to grammar rules
# and build an *Abstract Syntax Tree* (AST).
#
# The AST represents the structure and relationship between tokens.
# For example, the expression "2 + 3 * 4" becomes a tree that says:
#   multiply 3 and 4 first, then add 2.
#
# This structured form allows the interpreter to later evaluate the expression
# in the correct order — following BODMAS.
ast = parser.parse(None, token)

# Uncomment this line if you want to see the AST (Abstract Syntax Tree) that was built.
# print(f"AST: {ast}")


# ==========================================
# STEP 3: Evaluation — Executing the AST
# ==========================================
# The final stage is evaluation — where the actual computation happens.
# The evaluator walks through the AST, visiting each node and performing the
# appropriate operation in the right order.
#
# This is where your mathematical expression gets “executed”.
# The interpreter doesn’t compile to machine code — it directly reads and performs
# the computation step by step in memory.
result = evaluator.evaluate(ast)

# Print the final result to the screen.
print(f"Result: {result}")


# ==========================================
# END OF MAIN
# ==========================================
# That’s the complete journey of our mini-interpreter:
#
#     Input Expression (string)
#                ↓
#            Lexer → Tokens
#                ↓
#            Parser → AST
#                ↓
#          Evaluator → Result
#
# With these three steps, you’ve built the foundation of how interpreters work.
# From this point, you can extend it to handle variables, functions,
# custom syntax, or even build your own programming language.
#
# Explore the source files in `./core/`:
#   - lexer.py   → breaks expressions into tokens
#   - parser.py  → builds a syntax tree from tokens
#   - evaluator.py → interprets the tree to produce a result
#
# Once you understand this flow,
# you’ve crossed the threshold into the world of language design —
# where code becomes meaning, and meaning becomes execution.
