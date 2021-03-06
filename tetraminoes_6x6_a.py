import poly.parser as parser
import poly.solver as solver

figure = parser.load_file("shapes/figure_6x6_a.pol")
part = parser.load_file("shapes/X5.pol")

print(figure, "\n\n", part, "\n")

for idx, s in enumerate(solver.split_into_parts(figure, part)):
    parser.save_solution_to_svg(s, "output/" + str(idx) + "th_sol.svg")
    parser.pretty_print_solution(s)
    print()
    if idx > 100:
        break
