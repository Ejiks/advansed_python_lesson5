import datetime

def log_path_way(filepath):
    def old_functiondec(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(filepath, mode='a', encoding='utf8') as f:
                f.write(f'Время и дата вызова функции: {datetime.datetime.today()}\
                        \rИмя вызываемой функции: {old_function.__name__}\
                        \rРезультат: {result}\
                        \rАргументы: {args} {kwargs}\n')
            return result
        return new_function
    return old_functiondec