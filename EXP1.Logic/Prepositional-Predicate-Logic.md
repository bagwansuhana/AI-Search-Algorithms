# Assignment 9 – Implementation of Propositional and Predicate Logic

## Aim

To study and implement Propositional Logic and Predicate Logic using Python and understand their use in knowledge representation and reasoning in Artificial Intelligence.

---

# 1. Introduction

Logic is an important part of Artificial Intelligence. It provides a formal method for representing knowledge and deriving conclusions from given facts and rules.

The two important types of logic used in AI are:

1. Propositional Logic
2. Predicate Logic

---

# 2. Propositional Logic

## Definition

Propositional Logic is a type of logic in which statements called propositions are represented using symbols. Each proposition has a truth value of either TRUE or FALSE.

### Example

    P = "It is raining."
    Q = "The ground is wet."

P and Q are propositions.

---

## 3. Logical Operators

| Operator | Symbol | Meaning |
|---|---|---|
| NOT | ¬P | Negation |
| AND | P ∧ Q | Both P and Q |
| OR | P ∨ Q | At least one is true |
| IMPLIES | P → Q | If P, then Q |
| BICONDITIONAL | P ↔ Q | P if and only if Q |

---

# 4. Program 1 – Propositional Logic Using Logical Operators

### Program

    # Propositional Logic using logical operators

    P = True
    Q = False

    print("P =", P)
    print("Q =", Q)

    print("\nLogical Operations:")
    print("NOT P =", not P)
    print("P AND Q =", P and Q)
    print("P OR Q =", P or Q)

    # P -> Q is equivalent to (NOT P) OR Q
    print("P IMPLIES Q =", (not P) or Q)

    # P <-> Q
    print("P BICONDITIONAL Q =", P == Q)

### Output

    P = True
    Q = False

    Logical Operations:
    NOT P = False
    P AND Q = False
    P OR Q = True
    P IMPLIES Q = False
    P BICONDITIONAL Q = False

---

# 5. Program 2 – Propositional Logic Using Truth Table

### Program

    # Truth table for AND operation

    values = [True, False]

    print("P\tQ\tP AND Q")

    for P in values:
        for Q in values:
            result = P and Q
            print(P, "\t", Q, "\t", result)

### Output

    P       Q       P AND Q
    True    True    True
    True    False   False
    False   True    False
    False   False   False

---

# 6. Propositional Reasoning

Propositional logic can be used to derive conclusions from given statements.

### Example

Given:

    P → Q
    P

Therefore:

    Q

This is called Modus Ponens.

### Modus Ponens

    P → Q
    P
    -----
    ∴ Q

Example:

    P = It is raining.
    Q = The ground is wet.

If:

    It is raining → The ground is wet.
    It is raining.

Then:

    The ground is wet.

---

# 7. Predicate Logic

## Definition

Predicate Logic, also called First-Order Predicate Logic (FOPL), is an extension of propositional logic used to represent objects, properties, and relationships.

It uses:

- Constants
- Variables
- Predicates
- Functions
- Quantifiers

---

# 8. Components of Predicate Logic

## 1. Constants

Constants represent specific objects.

Examples:

    Ram
    Mumbai
    Book1

---

## 2. Variables

Variables represent general or unknown objects.

Examples:

    x
    y
    z

---

## 3. Predicates

Predicates represent properties or relationships.

Examples:

    Student(x)
    Intelligent(x)
    Likes(x, y)

---

## 4. Functions

Functions represent relationships that return an object.

Example:

    FatherOf(x)

---

## 5. Quantifiers

### Universal Quantifier

Symbol:

    ∀

Meaning:

    "For all"

Example:

    ∀x (Student(x) → Intelligent(x))

Meaning:

    "All students are intelligent."

### Existential Quantifier

Symbol:

    ∃

Meaning:

    "There exists"

Example:

    ∃x (Student(x) ∧ Intelligent(x))

Meaning:

    "There exists a student who is intelligent."

---

# 9. Predicate Logic Examples

### Example 1

Statement:

    All humans are mortal.

Predicate Logic:

    ∀x (Human(x) → Mortal(x))

### Example 2

Statement:

    Socrates is a human.

Predicate Logic:

    Human(Socrates)

### Example 3

Statement:

    Some students are intelligent.

Predicate Logic:

    ∃x (Student(x) ∧ Intelligent(x))

### Example 4

Statement:

    Every student studies AI.

Predicate Logic:

    ∀x (Student(x) → Studies(x, AI))

---

# 10. Program 3 – Predicate Logic Using Facts and Rules

### Program

    # Predicate Logic using facts and rules

    humans = ["Socrates", "Plato", "Aristotle"]

    print("Facts:")
    for person in humans:
        print("Human(" + person + ")")

    print("\nRule:")
    print("Human(x) -> Mortal(x)")

    print("\nConclusions:")

    for person in humans:
        print("Mortal(" + person + ")")

### Output

    Facts:
    Human(Socrates)
    Human(Plato)
    Human(Aristotle)

    Rule:
    Human(x) -> Mortal(x)

    Conclusions:
    Mortal(Socrates)
    Mortal(Plato)
    Mortal(Aristotle)

---

# 11. Program 4 – Predicate Logic Using Student Facts

### Program

    # Predicate Logic for student knowledge

    students = ["Amit", "Priya", "Rahul"]

    intelligent = ["Amit", "Priya"]

    print("Students who are intelligent:")

    for student in students:
        if student in intelligent:
            print(student, "is intelligent.")

### Output

    Students who are intelligent:
    Amit is intelligent.
    Priya is intelligent.

---

# 12. Program 5 – Predicate Logic With Relationships

### Program

    # Predicate Logic representing relationships

    likes = {
        "Amit": ["Python", "AI"],
        "Priya": ["AI"],
        "Rahul": ["Python"]
    }

    print("Students and their interests:")

    for student, subjects in likes.items():
        for subject in subjects:
            print("Likes(" + student + ", " + subject + ")")

### Output

    Students and their interests:
    Likes(Amit, Python)
    Likes(Amit, AI)
    Likes(Priya, AI)
    Likes(Rahul, Python)

---

# 13. Difference Between Propositional and Predicate Logic

| Propositional Logic | Predicate Logic |
|---|---|
| Uses propositions | Uses predicates |
| Represents complete statements | Represents objects and relationships |
| Does not use variables | Uses variables |
| Does not use quantifiers | Uses quantifiers |
| Less expressive | More expressive |
| Example: P | Example: Student(x) |
| Suitable for simple statements | Suitable for complex knowledge representation |

---

# 14. Applications

Propositional and Predicate Logic are used in:

1. Knowledge Representation
2. Expert Systems
3. Automated Reasoning
4. Natural Language Processing
5. Intelligent Agents
6. Theorem Proving
7. Planning
8. Rule-Based Systems
9. Robotics
10. Artificial Intelligence

---

# 15. Advantages

## Propositional Logic

- Simple and easy to understand.
- Easy to implement.
- Useful for Boolean reasoning.
- Can be represented using truth tables.
- Useful for simple decision-making.

## Predicate Logic

- More expressive than propositional logic.
- Represents objects and relationships.
- Supports variables and quantifiers.
- Useful for knowledge representation.
- Supports complex reasoning.

---

# 16. Limitations

## Propositional Logic

- Cannot represent relationships between objects.
- Cannot use variables.
- Cannot use quantifiers.
- Becomes difficult for large knowledge bases.

## Predicate Logic

- More complex than propositional logic.
- Reasoning can be computationally expensive.
- Requires proper representation of facts and relationships.
- Large knowledge bases can become difficult to manage.

---

# 17. Conclusion

Propositional Logic and Predicate Logic are important techniques used in Artificial Intelligence for knowledge representation and reasoning.

Propositional Logic represents simple statements using TRUE and FALSE values, while Predicate Logic provides a more powerful representation using objects, predicates, variables, functions, and quantifiers.

The Python programs demonstrate the implementation of logical operators, truth tables, facts, rules, and relationships.

---

# Result

Thus, the implementation and study of Propositional Logic and Predicate Logic was successfully completed using Python.