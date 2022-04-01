import poly.parser as parser
import poly.solver as solver

figure = parser.load("shapes/figure.pol")

for idx, s in enumerate(solver.auto_congruent_polyomino_split(figure, 5)):
    parser.save_solution_to_svg(s, "output/" + str(idx) + "th_sol.svg")
    parser.pretty_print_solution(s)
    print()
