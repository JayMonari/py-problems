from typing import List, Union
from math import ceil


def round_scores(student_scores: List[Union[float, int]]) -> List[int]:
    '''
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    '''
    student_scores.reverse()
    return list(map(lambda num: round(num), student_scores))


def count_failed_students(student_scores: List[int]) -> int:
    '''
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    '''
    return len([low for low in student_scores if low <= 40])


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    '''
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    '''
    return [above for above in student_scores if above >= threshold]


def letter_grades(highest: int) -> List[int]:
    '''
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    '''
    lowest = 41
    step = (highest - lowest) / 4
    return [ceil(lowest + step * i) for i in range(4)]


def student_ranking(student_scores: List[int],
                    student_names: List[str]) -> List[str]:
    '''
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    '''
    rankings: List[str] = []
    for rank, [name, score] in enumerate(zip(student_names, student_scores),
                                         start=1):
        rankings.append(f"{rank}. {name}: {score}")

    return rankings


MaybePerfectScore = Union[str, List[Union[str, int]]]


def perfect_score(student_info: List[str]) -> MaybePerfectScore:
    '''
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    '''
    for [name, score] in student_info:
        if score == 100:
            return [name, score]

    return "No perfect score."
