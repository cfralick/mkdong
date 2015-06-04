from dong import Defaults
from mkdong import parser

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed = parser(Defaults).parse_args()
    sys.exit(parsed.func(parsed))

if __name__ == '__main__':
    main()
