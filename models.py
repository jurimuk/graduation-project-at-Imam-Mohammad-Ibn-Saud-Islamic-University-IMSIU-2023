from dataclasses import dataclass

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///university.db'
# app.app_context()

# with app.app_context():
#     # within this block, current_app points to app.
#     print (current_app.name)
db = SQLAlchemy()

@dataclass()
class Instructor(db.Model):
    id: str
    first_name: str
    middle_name: str
    last_name: str
    position: str
    course_number: str
    section_number: str
    email: str
    office_telephone_number: str
    office_floor: str
    office_number: str

    id = db.Column('instructor_id',db.Integer(), primary_key=True)
    first_name=db.Column(db.String(length=123),nullable=False)
    middle_name = db.Column(db.String(length=123), nullable=False)
    last_name=db.Column(db.String(length=123),nullable=False)
    position =db.Column(db.String(length=123),nullable=False)
    course_number = db.Column(db.String(length=123),nullable=False)
    section_number = db.Column(db.String(length=123), nullable=False)
    email = db.Column(db.String(length=123), nullable=False)
    office_telephone_number = db.Column(db.String(length=123),nullable=False)
    office_floor = db.Column(db.String(length=123), nullable=False)
    office_number = db.Column(db.String(length=123), nullable=False)

@dataclass()
class TechnicalSupport(db.Model):
    id: str
    name: str
    telephone_number: str
    email: str
    description: str

    id = db.Column('support_id',db.Integer(), primary_key=True)
    name=db.Column(db.String(length=123),nullable=False)
    telephone_number=db.Column(db.String(length=123),nullable=False)
    email = db.Column(db.String(length=123), nullable=False)
    description = db.Column(db.String(length=123),nullable=False)

@dataclass()
class MajorPlan(db.Model):
    id: str
    name: str
    courses_names: str
    courses_numbers: str
    total_courses: str
    total_hours: str
    name_acronym: str
    total_levels: str

    id = db.Column('mojorplan_id', db.Integer(), primary_key=True)
    name = db.Column(db.String(length=123), nullable=False)
    courses_names = db.Column(db.String(length=123), nullable=False)
    courses_numbers = db.Column(db.String(length=123), nullable=False)
    total_courses = db.Column(db.String(length=123), nullable=False)
    total_hours = db.Column(db.String(length=123), nullable=False)
    name_acronym = db.Column(db.String(length=123), nullable=False)
    total_levels = db.Column(db.String(length=123), nullable=False)

@dataclass()
class Level(db.Model):
    id: str
    level_code: str
    level_number: str
    level_major: str
    no_of_optional_courses: str
    no_of_mandatory_courses: str
    leve_courses_names: str
    leve_courses_numbers: str
    min_term_hours: str
    max_term_hours: str

    id = db.Column('level_id', db.Integer(), primary_key=True)
    level_code = db.Column(db.String(length=123), nullable=False)
    level_number = db.Column(db.String(length=123), nullable=False)
    level_major = db.Column(db.String(length=123), nullable=False)
    no_of_optional_courses = db.Column(db.String(length=123), nullable=False)
    no_of_mandatory_courses = db.Column(db.String(length=123), nullable=False)
    leve_courses_names = db.Column(db.String(length=123), nullable=False)
    leve_courses_numbers = db.Column(db.String(length=123), nullable=False)
    min_term_hours = db.Column(db.String(length=123), nullable=False)
    max_term_hours = db.Column(db.String(length=123), nullable=False)


@dataclass
class Course(db.Model):
    id: str
    course_name: str
    course_number: str
    course_description: str
    course_requirements: str
    course_dependent: str
    major: str
    expected_term: str
    no_of_hours: str
    course_type: str
    no_of_available_sections: str

    id = db.Column('course_id',db.Integer(),primary_key=True)
    course_name = db.Column(db.String(length=123), nullable=False)
    course_number = db.Column(db.String(length=123), nullable=False)
    course_description = db.Column(db.String(length=123), nullable=False)
    course_requirements = db.Column(db.String(length=123), nullable=False)
    course_dependent = db.Column(db.String(length=123), nullable=False)
    major = db.Column(db.String(length=123), nullable=False)
    expected_term = db.Column(db.String(length=123), nullable=False)
    no_of_hours = db.Column(db.String(length=123), nullable=False)
    course_type = db.Column(db.String(length=123), nullable=False)
    no_of_available_sections = db.Column(db.String(length=123), nullable=False)


@dataclass
class Section(db.Model):
    id: str
    course_name: str
    course_number: str
    section_number: str
    major: str
    no_of_hours: str
    reference_number: str
    seats: str
    classroom: str
    daytime_days: str
    daytime_time: str

    id = db.Column('section_id',db.Integer(),primary_key=True)
    course_name = db.Column(db.String(length=123), nullable=False)
    course_number = db.Column(db.String(length=123), nullable=False)
    section_number = db.Column(db.String(length=123), nullable=False)
    major = db.Column(db.String(length=123), nullable=False)
    no_of_hours = db.Column(db.String(length=123), nullable=False)
    reference_number = db.Column(db.String(length=123), nullable=False)
    seats = db.Column(db.String(length=123), nullable=False)
    classroom = db.Column(db.String(length=123), nullable=False)
    daytime_days = db.Column(db.String(length=123), nullable=False)
    daytime_time = db.Column(db.String(length=123), nullable=False)

@dataclass
class Stats(db.Model):
    id: str
    req: str
    res: str
    time_start: str
    time_end: str
    tag: str

    id = db.Column('stats_id',db.Integer(),primary_key=True)
    req = db.Column(db.String(length=123), nullable=False)
    res = db.Column(db.String(length=123), nullable=False)
    time_start = db.Column(db.String(length=123), nullable=False)
    time_end = db.Column(db.String(length=123), nullable=False)
    tag = db.Column(db.String(length=123), nullable=False)