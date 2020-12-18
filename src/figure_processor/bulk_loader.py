from src.figure_processor.figures import *

all_figure_classes = [Triangle, Parallelagramm]


def _read_figure(str):
    for figure_type in all_figure_classes:
        figure_obj = figure_type()
        if figure_obj.is_readable(str):
            figure_obj.read(str)
            return figure_obj
    return None


def bulk_load(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        all_figures = [_read_figure(line) for line in lines]
        all_figures_without_none = [figure for figure in all_figures if figure is not None]
        return all_figures_without_none
