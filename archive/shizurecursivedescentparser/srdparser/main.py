import srdparser.parser as parser

__author__ = "IceArrow256"
__version__ = '2'


def main():
    try:
        math = parser.Parser("2*(3+80575706607)+20/2")
        print(math.execute())
    except RuntimeError as e:
        print(e)


if __name__ == '__main__':
    main()
