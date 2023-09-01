"""
Naive backtracking search without any heuristics or inference.
"""

VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]


def backtrack(assigment):
    """Runs backtracing search to find an assigment."""

    # Check if assignment is complete
    if len(assigment) == len(VARIABLES):
        return assigment
    
    # Try a new variable
    var = select_unassigned_variable(assigment)
    for value in ["Monday", "Tuesday", "Wednesday"]:
        new_assigment = assigment.copy()
        new_assigment[var] = value
        if consistent(new_assigment):
            result = backtrack(new_assigment)
            if result is not None:
                return result
    return None


def select_unassigned_variable(assignment):
    """Chooses a variable not yet assigned, in order"""
    for variable in VARIABLES:
        if variable nor in assigment:
                return variable
    return None


def consistent(assignment):
     """Checks to see if an assignment is consistent."""
     for (x, y) in CONSTRAINTS:
          
          # Only consider arcs where both are assigned
          if x not in assignment or y not in assignment:
               continue
          
          # If both have same value, then not consistent
          if assignment[x] == assignment[y]:
               return False
          
          # If nothing inconsistent, then assignment is consistent
          return True
     

solution = backtrack(dict())
print(solution)