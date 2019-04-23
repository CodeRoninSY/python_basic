#!/usr/bin/env python
'''
journey_class.py

Synopsis: Journey class
Author: CodeRoninSY
Date: <2019-04-23>

'''

import json
from pprint import pprint


class Journey(object):
    ''' Journey '''
    JID         = 0
    origin      = "Istanbul"
    destination = "Izmir"
    travelers   = ["CodeRoninSY"]
    notes       = ["Prep list"]
    style       = "Flight"
    start       = "2019-04-23"
    end         = "2019-04-23"
    total_p_y   = 0
    cost        = 100
    duration    = 0

    def __init__(self, JID=JID, origin=origin, destination=destination,
                 travelers=travelers, notes=notes, style=style,
                 start=start, end=end, total_p_y=total_p_y,
                 cost=cost, duration=duration):
        self.JID            = JID
        self.origin         = origin
        self.destination    = destination
        self.travelers      = travelers
        self.notes          = notes
        self.style          = style
        self.start          = start
        self.end            = end
        self.total_p_y      = total_p_y
        self.cost           = cost
        self.duration       = duration

    def __str__(self):
        return f"--> JID:       {self.JID}\n\
            --> origin:         {self.origin}\n\
            --> destination:    {self.destination}\n\
            --> travelers:      {self.travelers}\n\
            --> notes:          {self.notes}\n\
            --> style:          {self.style}\n\
            --> start:          {self.start}\n\
            --> end:            {self.end}\n\
            --> Total/year:     {self.total_p_y}\n\
            --> Cost:           {self.cost}\n\
            --> Duration:       {self.duration}\n"

    def __repr__(self):
        return str({'JID': self.JID, 'origin': self.origin,
                    'destination': self.destination,
                    'travelers': self.travelers,
                    'notes': self.notes, 'style': self.style,
                    'start': self.start, 'end': self.end,
                    'total_p_y': self.total_p_y,
                    'cost': self.cost,
                    'duration': self.duration})

    def __write__(self, file):
        with open(file, 'a') as out:
            out.write(f"Journey: {self!r}")

    def add_traveler(self, name):
        ''' add_traveler '''
        if name != any(self.travelers):
            self.travelers.append(name)
        else:
            print(f"{name} is already going on the journey!")

    @property
    def describe(self):
        ''' describe '''
        return f"From {self.origin} to {self.destination}"

    @property
    def note(self):
        ''' note '''
        return self.notes

    @note.setter
    def note(self, item):
        return self.notes.append(item)

    def add_note(self, item):
        ''' add_note '''
        return self.notes.append(item)

    @note.getter
    def note(self):
        ''' note.getter '''
        return f"Note: {self.notes}"

    @property
    def _cost(self):
        ''' cost property '''
        return self.cost

    @_cost.setter
    def _cost(self, cost_val):
        ''' cost setter '''
        self.cost = cost_val

    @_cost.getter
    def _cost(self):
        return f"Cost of {self.JID} is {self.cost}"


def main():
    ''' Main '''
    vacation = Journey()
    pprint(vacation)
    print(f"Vacation: {vacation!s}")
    vacation.__write__("Journey_db.txt")

    vacation = Journey(origin="Sweden",
                       destination="Switzerland",
                       notes=["Pack hiking gear"],
                       travelers=["Elif", "Alya"])

    print(f"Origin: {vacation.origin}")
    print(f"Destination: {vacation.destination}")
    print(f"Notes: {vacation.notes}")
    print(f"Travelers: {vacation.travelers}")

    vacation.add_traveler("Ali")
    print(f"Travelers: {vacation.travelers}")

    vacation.add_note("Add medkit to bag")
    print(f"Notes: {vacation.notes}")

    vacation.note = "Put dry food to prep list"
    print(f"Notes: {vacation.notes}")

    print(f"Describe: {vacation.describe}")

    print(f"Vacation: {vacation!s}")

    pprint(vacation)


if __name__ == "__main__":
    main()
