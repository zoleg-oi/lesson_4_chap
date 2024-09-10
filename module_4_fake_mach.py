# module_4_fake_mach

def divide(first, second):
    # Можно отработать исключение, но так будет проще
    if second == 0:
        text_r = "Ошибка"
        return text_r
    else:
        return first / second
