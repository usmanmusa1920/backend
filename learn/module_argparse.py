import argparse


# print(help(argparse.ArgumentParser().add_argument(dest=False)))

def main_parse():
    # prog is the name of the program, default=sys.argv[0]
    parser = argparse.ArgumentParser(prog='main', description='A simple function for new beeiess!')
    
    # this is positional argument
    parser.add_argument('user', default='root', type=str, help='Who is the user? ')
    
    # metavar make the -help to look cleaan
    
    # the port is required
    parser.add_argument('--port', '-p', required=True, default=1.0, type=int, metavar='', help='What is the port? ')
    parser.add_argument('--x', '-x', default=1.0, type=float, metavar='', help='What is the first number? ')
    parser.add_argument('--y', '-y', default=1.0, type=float, metavar='', help='What is the second number? ')
    parser.add_argument('--operator', '-o', default='add', type=str, metavar='', help='What is the operation? ')
    
    # mutally exclusive, you don't need to specify either, you can specify one but you cant specify morethan one
    group = parser.add_mutually_exclusive_group()
    # quiet mean to print out one little thing as the answer
    group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
    # verbose mean to print out alot such as the argument you specify beign add, sub, mul and div
    group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
    

    args = parser.parse_args()
    if args.quiet:
        print(calc(main_parse()))
    elif args.verbose:
        print('%d %d' % (args.x, args.y))
    else:
        print('No group specify')
    return args


def calc(args):
    if args.operator == 'add':
        return 'The sum of %d and %d is: %d' % (args.x, args.y, args.x + args.y)
    elif args.operator == 'sub':
        return args.x - args.y
    elif args.operator == 'mul':
        return args.x * args.y
    elif args.operator == 'div':
        return args.x / args.y
    

if __name__ == '__main__':
    print(calc(main_parse()))
