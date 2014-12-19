"""Tags for workshops.Person"""

from django import template


register = template.Library()


@register.filter
def task_count(person, role_name=None):
    """The number of tasks a person has undertaken.

    For example, the number of 'instructor' tasks they've had.  If
    role_name isn't set, return a count of all tasks.
    """
    tasks = person.task_set.all()
    if role_name:
        tasks = tasks.filter(role__name=role_name)
    return tasks.count()
