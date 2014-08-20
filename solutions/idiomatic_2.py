def fail(classroom, scoring_function, maximum_score):
    for group in classroom:
        if scoring_function(group) > maximum_score:
            yield group
