# Пространство имен
def test_function():
    txt = "Я в области видимости функции test_function!!!"
    txt1= "Я в области видимости функции test_function!!!"
    def inner_function():
        nonlocal txt
        nonlocal txt1
        # Так мы присваиваем переменной новое значение, но мы все равно ее видим, потому что стоит nonlocal
        txt = "Я в области видимости функции inner_function"
        print(txt)
        print(txt1)
    inner_function()
    return
test_function()

try:
    inner_function()
except NameError:
    print('Так данную функцию вызвать нельзя, она определена и находится в пространстве test_function')
    print('В глобальном пространстве ее не видно')
