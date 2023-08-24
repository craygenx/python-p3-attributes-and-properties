#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name):
        self._name = name.title()
        self._job = None
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) >= 25:
            print("Name must be string under 25 characters.")
        else:
            self._name = value.title()
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if value not in Person.approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value
