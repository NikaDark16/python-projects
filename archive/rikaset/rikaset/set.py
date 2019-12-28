__author__ = "IceArrow256"
__version__ = '4'


def union(first, second):
    result = set()
    for i in first:
        result.add(i)
    for i in second:
        if i not in result:
            result.add(i)
    return result


def intersection(first, second):
    result = set()
    for i in first:
        if i in second:
            result.add(i)
    return result


def difference(first, second):
    result = set()
    for i in first:
        if i not in second:
            result.add(i)
    return result


def symmetric_difference(first, second):
    result = set()
    for i in first:
        if i not in second:
            result.add(i)
    for i in second:
        if i not in first:
            result.add(i)
    return result


class Set:
    def __init__(self, name: str = "", data: set = None, venn_num=0):
        if data is None:
            data = set()
        self.data = set()
        if venn_num == 0:
            self.venn_set = set()
        if venn_num == 1:
            self.venn_set = {'100', '110', '101', '111'}
        elif venn_num == 2:
            self.venn_set = {'010', '110', '011', '111'}
        elif venn_num == 3:
            self.venn_set = {'001', '101', '011', '111'}
        for i in data:
            if i:
                self.data.add(i)
        self.name = name

    def __str__(self):
        if self.data:
            return str(self.data)
        else:
            return "{0}"
    def union(self, other):
        # u
        result = Set(self.name + ' u ' + other.name, union(self.data, other.data))
        result.venn_set = union(self.venn_set, other.venn_set)
        return result

    def intersection(self, other):
        # n
        result = Set(self.name + ' n ' + other.name, intersection(self.data, other.data))
        result.venn_set = intersection(self.venn_set, other.venn_set)
        return result

    def difference(self, other):
        # \
        result = Set(self.name + ' \\ ' + other.name, difference(self.data, other.data))
        result.venn_set = difference(self.venn_set, other.venn_set)
        return result

    def symmetric_difference(self, other):
        # +
        result = Set(self.name + ' + ' + other.name, symmetric_difference(self.data, other.data))
        result.venn_set = symmetric_difference(self.venn_set, other.venn_set)
        return result

    def addition(self, U):
        result = Set('_' + self.name, difference(U.data, self.data))
        result.venn_set = difference(U.venn_set, self.venn_set)
        return result
