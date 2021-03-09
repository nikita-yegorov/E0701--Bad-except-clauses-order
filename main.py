from pyStaticAnalyzer.checker import add_method, Checker
from pyStaticAnalyzer.kernel import FileKernel
import ast
import re




def dfs_check_bad_order(k, cur, used):
    if cur not in used:
        if cur.endswith('.py'):
            messages = []
            cur_ast = k.get_file_ast(cur)
            for i, node in enumerate(ast.walk(cur_ast)):
                if isinstance(node, ast.Try):
                    children = []
                    exceptions = []
                    ex_num = 0

                    for  child in ast.iter_child_nodes(node):
                        if isinstance(child, ast.ExceptHandler):
                            children.append(child)
                            exceptions.append(child.type.id)
                            if child.type.id == 'Exception':
                                ex_num = child.type.lineno


                    if 'Exception' in exceptions and exceptions[len(exceptions) - 1] != 'Exception':
                        messages.append(f'line '
                                        f'{ex_num}:'
                                        f' E0701 - Bad except clauses order')

            if messages:
                print(cur)
                for message in messages:
                    print(message)
                print()

    used.add(cur)
    for child in k.get_structure[cur]:
        dfs_check_bad_names(k, child, used)


@add_method(Checker)
def check_bad_order(k):
    used = set()
    dfs_check_bad_order(k, k.get_path, used)




if __name__ == "__main__":
    kernel = FileKernel('tests.py')
    checker = Checker()
    checks = checker.get_all_checks()
    print('Checks:   ', checks)
    # kernel.print_file_ast('tests.py')
    checker.run_check('check_bad_order', kernel)
