import polyomino.parser as parser
import polyomino.solver as solver

figure = parser.load("shapes/figure.pol")
part = parser.load("shapes/_part.pol")

for idx, s in enumerate(solver.split_into_parts(figure, part)):
    parser.save_solution_to_svg(s, "output/" + str(idx) + "th_sol.svg")
    parser.pretty_print_solution(s)
