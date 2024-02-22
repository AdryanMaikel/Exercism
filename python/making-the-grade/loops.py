"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list[float]) -> list[int]:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    return [round(score) for score in student_scores]


def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine how many of the provided student scores were 'the best'
    based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best"
    threshold.
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade thresholds based on the provided highest
    grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade
    interval.
            For example, where the highest score is 100, and failing is
            <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    return [41 + round((highest - 40) / 4) * count for count in range(4)]


def student_ranking(student_scores: list[int], student_names: list[str]):
    """Organize the student's rank, name, and grade information in
    descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in
    descending order.
    :return: list - of strings in format ["<rank>. <student name>:
    <score>"].
    """
    rank = list(range(1, len(student_names)+1))
    return [f"{rank}. {name}: {score}"
            for rank, name, score in zip(rank, student_names, student_scores)]


def perfect_score(student_info: list[list[str, int]]) -> list[str, int]:
    """Create a list that contains the name and grade of the first
    student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student
    score of 100 is found.
    """
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []
