from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value, args):
    if args == 'change':
        value = 'Shahin Khan'
        return value
    if args == 'title':
        return value.title()


def show_courses():
    courses = [
        {
            'id' : 1,
            'course' : 'C',
            'teacher' : 'Rahim'
        },
        {
            'id' : 2,
            'course' : 'C++',
            'teacher' : 'KhaRahim'
        },
        {
            'id' : 3,
            'course' : 'Python',
            'teacher' : 'Fahim'
        }]

    return {'courses' : courses }

courses_template = get_template('f_app/courses.html')
register.filter('change_name', my_template)
register.inclusion_tag(courses_template)(show_courses)