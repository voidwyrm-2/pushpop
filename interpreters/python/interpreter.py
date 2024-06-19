


def interpreter(text: str | list[str]):
    generate_lines = lambda i: [l.split('.', 1)[0].strip().casefold() for l in i.strip().split('\n')]

    lines: list[str] = generate_lines(text) if isinstance(text, str) else list(text)

    acc: int = 0
    stack: list[int] = []
    funcs: list[list[str]] = []

    variables: dict[str, int] = {}

    ignore_end = False

    ln = 0

    convert_value = lambda v: int(v) if v.isdigit() else variables.get(v, f"unknown value '{v}'")
    def get_instruction(instruct: str, acc: int):
        err = True
        match instruct:
            case 'inc':
                acc = acc + 1 if acc + 1 < 128 else 0

            case 'dec':
                acc = acc - 1 if acc - 1 > 0 else 127

            case 'put':
                print(f"accumulator: {acc}")

            case 'push':
                stack.append(acc)

            case 'pop':
                if not len(stack):
                    return 'cannot pop from stack, stack is empty'
                acc = stack.pop()

            case 'popn':
                if not len(stack):
                    return 'cannot pop from stack, stack is empty'
                stack.pop()

            case 'puts':
                print('stack:')
                stack_str = [str(s) + '\n-' for s in stack]
                stack_str.reverse()
                print('\n'.join(stack_str).removesuffix('-').strip())

            case 'show':
                stack_ascii = [('0' if s == 0 else chr(s)) for s in stack]
                stack_ascii.reverse()
                print(''.join(stack_ascii))

            case 'do':
                return None, acc, True

            case '':
                pass
            case '':
                pass
            case '':
                pass
            case '':
                pass
            case '':
                pass
            case '':
                pass
            case '':
                pass
            case '':
                pass
            case '':
                pass
            case '':
                pass

            case other:
                return object(), acc, False
        return None, acc, False

    print_error = lambda msg: print(f"error on line {ln + 1}: {msg}")
    assert_res = lambda r: print_error(r) if isinstance(r, str) and r != '' else print_error(f"unknown instruction '{lines[ln]}'") if r != None else object()
    while ln < len(lines):
        if not lines[ln]:
            ln += 1; continue

        if lines[ln] == 'end':
            if ignore_end:
                ln += 1; continue
            else:
                print_error("unexpected 'end'"); return
            
        if lines[ln].startswith('(') and ')' in lines[ln]:
            loops, loop_instruction = lines[ln].removeprefix('(').split(')', 1)
            val = convert_value(loops.strip())
            if not isinstance(val, int):
                print_error(val); return
            for _ in range(val):
                if loop_instruction.strip() in ('do', 'end', 'func'):
                    print_error(f"'{loop_instruction.strip()}' instructions cannot be used in loops")
                    return
                res, acc, _ = get_instruction(loop_instruction.strip(), acc)
                if assert_res(res) == None: return
            ln += 1; continue
        elif lines[ln].startswith('define '):
            pass
        elif lines[ln].startswith('call '):
            pass

        # I have to pass in `acc` like this because for some reason using `global acc` doesn't work
        res, acc, ignore_end = get_instruction(lines[ln], acc)
        if assert_res(res) == None: return
        ln += 1


interpreter(
    "(80) inc\n"
    "push\n"
    "(20) inc\n"
    "push\n"
    "push\n"
    "(10) dec\n"
    "push\n"
    "put\n"
    "puts\n"
    "show"
)