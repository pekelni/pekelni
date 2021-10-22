import json
import os
import re
import shutil
import subprocess
import traceback


def get_repo_path(repo_name='pekelni'):
    abs_path = os.path.dirname(os.path.abspath(__file__))
    join_abs_path = abs_path.split(os.sep)
    path_to_data_list = join_abs_path[:join_abs_path.index(repo_name) + 1]
    return os.sep.join(path_to_data_list)


def bash(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    process.communicate()


def create_htmls():
    lesson_src_path = get_repo_path() + '/уроки/'
    html_path = get_repo_path() + '/html/'

    try:
        shutil.rmtree(html_path)
    except FileNotFoundError:
        pass
    os.makedirs(html_path)

    for lesson_name in os.listdir(lesson_src_path):
        current_lesson_path = lesson_src_path + lesson_name
        for notebook in os.listdir(current_lesson_path):
            if notebook.endswith('.ipynb'):
                converted_name = notebook.replace(' ', '_').replace('.ipynb', '.html')
                src_notebook = f'{current_lesson_path}/{notebook}'
                os.makedirs(f'{html_path}/{lesson_name}', exist_ok=True)
                html_notebook = f'{html_path}/{lesson_name}/{converted_name}'
                command = f'jupyter nbconvert --to html {src_notebook} --output {html_notebook}'
                bash(command)


def create_solution_notebook(lines):
    while True:
        if lines[-1].strip():
            lines[-1] = lines[-1].rstrip()
            break
        else:
            del lines[-1]

    return {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": 666,
                "metadata": {},
                "outputs": [],
                "source": lines,
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.11"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }


def create_notebooks_for_solutions():
    lesson_src_path = get_repo_path() + '/lessons/'

    count = 0
    for lesson_name in os.listdir(lesson_src_path):
        try:
            solution_filenames = os.listdir(f'{lesson_src_path}{lesson_name}/solutions')
        except (FileNotFoundError, NotADirectoryError):
            continue
        try:
            shutil.rmtree(f'{lesson_src_path}{lesson_name}/solution_notebooks')
        except FileNotFoundError:
            pass
        os.makedirs(f'{lesson_src_path}{lesson_name}/solution_notebooks')
        for solution_file in solution_filenames:
            if solution_file == '.ipynb_checkpoints':
                continue
            try:
                with open(f'{lesson_src_path}{lesson_name}/solutions/{solution_file}', errors='ignore') as f:
                    solution_lines = f.readlines()
                notebook = create_solution_notebook(solution_lines)
                solution_file = solution_file.replace('.py', '.ipynb')
                destination_path = f'{lesson_src_path}{lesson_name}/solution_notebooks/{solution_file}'
                with open(destination_path, 'w') as out:
                    json.dump(notebook, out, indent=4, ensure_ascii=False)
                count += 1
                # print(f'Saved for {destination_path}')
            except Exception:
                traceback.print_exc()
                print(f'Failed on {solution_file}')
    print(f'Saved {count} solutions and hints')


class LocLineEnhancer:
    markdown_link_pattern = re.compile(r'\[.+\]\(.+\/(?P<name>.+)\.ipynb\)')
    loc_metrics_pattern = re.compile(r'\(≈\d+ ряд\w+ коду\)')

    def __init__(self):
        self.stats = self._get_solution_stats()

    @staticmethod
    def _get_complexity(lines):
        count = 0
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            count += 1
        return count

    def _get_solution_stats(self):
        lesson_src_path = get_repo_path() + '/lessons/'
        stats = dict()

        for lesson_name in os.listdir(lesson_src_path):
            try:
                solution_filenames = os.listdir(f'{lesson_src_path}{lesson_name}/solutions')
            except (FileNotFoundError, NotADirectoryError):
                continue
            for solution_file in solution_filenames:
                if solution_file == '.ipynb_checkpoints':
                    continue
                with open(f'{lesson_src_path}{lesson_name}/solutions/{solution_file}', errors='ignore') as f:
                    solution_lines = f.readlines()
                key = solution_file.replace('.py', '')
                assert key not in stats, key
                stats[key] = self._get_complexity(solution_lines)
        return stats

    @staticmethod
    def _get_match(line, pattern):
        links = list()
        for match in re.finditer(pattern, line):
            links.append(match.group())
        assert len(links) <= 1, line
        if links:
            return links[0]

    def _extract_link(self, line):
        return self._get_match(line, self.markdown_link_pattern)

    def _extract_metrics(self, line):
        return self._get_match(line, self.loc_metrics_pattern)

    def _get_metrics(self, name):
        try:
            loc = self.stats[name]
            return f'(≈{loc} рядків коду)'
        except KeyError:
            pass

    def get_new_line(self, line):
        link = self._extract_link(line)
        if not link:
            return
        metrics = self._extract_metrics(line)
        if metrics:
            line = line.replace(metrics, '')
        name = self.markdown_link_pattern.match(link).group('name')
        metrics = self._get_metrics(name)
        if not metrics:
            if 'підказка' not in link.lower():
                print(f'no metrics for {name}')
            return
        line = line.replace(link, f'{link} {metrics}')
        return line

    def clear(self):
        pass


class ExerciseCounterEnhancer:
    EXERCISE_HEADER_PREFIX_PATTERN = re.compile(r'(?P<exercise_header_prefix>##\s(\d+\.\s)?).+')

    def __init__(self):
        self.last_seen_exercise_num = 0
        self.total = 0

    def clear(self):
        self.last_seen_exercise_num = 0

    def get_new_line(self, line):
        prefixes = list()
        for match in re.finditer(self.EXERCISE_HEADER_PREFIX_PATTERN, line.strip()):
            prefixes.append(match.group('exercise_header_prefix'))
        assert len(prefixes) <= 1, prefixes
        if not prefixes:
            return
        self.last_seen_exercise_num += 1
        self.total += 1
        new_prefix = f'## {self.last_seen_exercise_num}. '
        return line.replace(prefixes[0], new_prefix)


class LocMetricsAdder:
    def __init__(self):
        self.counter_enhancer = ExerciseCounterEnhancer()
        self.enhancers = [
            LocLineEnhancer(),
            self.counter_enhancer,
        ]

    def __call__(self):
        lesson_src_path = get_repo_path() + '/lessons/'

        for lesson_name in os.listdir(lesson_src_path):
            try:
                filenames = os.listdir(f'{lesson_src_path}{lesson_name}/')
            except NotADirectoryError:
                continue
            for f in filenames:
                if not f.startswith('exercises'):
                    continue
                assert f.endswith('.ipynb'), f
                full_path = f'{lesson_src_path}{lesson_name}/{f}'
                with open(full_path, 'r') as notebook_file:
                    notebook_dict = json.load(notebook_file)
                print(full_path, len(notebook_dict['cells']))
                for cell in notebook_dict['cells']:
                    self._handle_cell(cell)
                for enhancer in self.enhancers:
                    enhancer.clear()
                with open(full_path, 'w', encoding='utf-8') as notebook_file:
                    json.dump(notebook_dict, notebook_file, indent=4, ensure_ascii=False)
        print(f'processed {self.counter_enhancer.total} exercises')

    def _handle_cell(self, cell):
        if cell['cell_type'] != 'markdown':
            return
        cell_source = cell['source']
        for i in range(len(cell_source)):
            line = cell_source[i]
            for enhancer in self.enhancers:
                new_line = enhancer.get_new_line(line)
                if new_line and new_line.strip() != line.strip():
                    cell_source[i] = new_line
                    line = new_line


if __name__ == '__main__':
    LocMetricsAdder()()
    create_notebooks_for_solutions()
