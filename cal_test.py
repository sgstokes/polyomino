import polyomino.parser as parser
import polyomino.solver as solver

import polyomino.polyomino as pm

figure = parser.load("shapes/cal_figure.pol")
parts = ["L4", "L5", "O4", "P5", "T4", "U5", "X5", "Z4", "Z5"]
pols = {}

print(figure, "\n")

for p in parts:
    pol = parser.load(f"shapes/{p}.pol")
    pols.update(pol)
    print(pol, "\n")

print(pols)

pols = pm.generate(4)

print(pols)

for idx, s in enumerate(solver.polomino_solve(figure, pols)):
    parser.save_solution_to_svg(s, "output/" + str(idx) + "th_sol.svg")
    parser.pretty_print_solution(s)
    print()
