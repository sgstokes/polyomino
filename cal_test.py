import poly.parser as parser
import poly.solver as solver

import poly.polyomino as pm

figure = parser.load_file("shapes/figure_cal_0205.pol")
parts = ["L4", "L5", "O4", "P5", "T4", "U5", "X5", "Z4", "Z5"]
pols = set()

print(figure, "\n")

for p in parts:
    pol = parser.load_file(f"shapes/{p}.pol")
    pols.add(pol)

for idx, s in enumerate(solver.polomino_solve(figure, pols)):
    parser.save_solution_to_svg(s, "output/" + str(idx) + "th_sol.svg")
    parser.pretty_print_solution(s)
    print()
    if idx > 100:
        break
