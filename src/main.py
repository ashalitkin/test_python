import sys
from src.figure_processor.bulk_loader import bulk_load

def group(figures):
    groups = {}
    for figure in figures:
        type = figure.sayName()
        if type in groups:
            groups[type].append(figure)
        else:
            groups[type] = [figure]
    return groups

def main(args):
    all_figures = bulk_load("test.txt")
    groups = group(all_figures)
    print(groups)
    for figure_type in groups:
        current_figure_list = groups[figure_type]
        size = len(current_figure_list)
        s = sum([figure.square() for figure in current_figure_list])
        print("for type {0} we have {1} figures the square sum is : {2}".format(figure_type, size, s))

if __name__ == '__main__':
    main(sys.argv)