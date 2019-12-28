import rikaset.set as S
import rikaset.setscalculator as SC

__author__ = "IceArrow256"
__version__ = '4'


def smart_input(message: str, type_of_return: type, error_message=''):
    while True:
        try:
            data = type_of_return(input(message))
            break
        except ValueError:
            if error_message:
                print(error_message)
    return data


def main():
    set_expr = input("Input set's expresion, where 'u' - union, 'n' - intersection, '\\' - difference, "
                     "'+' - symmetric_difference, '_' - union of all set: ")
    expr = SC.SetsCalculator(set_expr)
    sets = {}
    for name in expr.sets:
        temp_set: str = input("Enter {}: ".format(name))
        sets[name] = S.Set(name, set(temp_set.split(" ")))
    expr.sets = sets
    try:
        result = expr.execute()
        print("Result: ", result.name)
        print("Result: ", result.data)
    except RuntimeError as e:
        print(e)


if __name__ == '__main__':
    main()
