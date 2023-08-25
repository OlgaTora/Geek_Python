Документация к модулю работы с модификатором строки
===
Описание функции string_modify()
---

>>> from Immersion_in_Python.Seminar_14.str_modify.main import string_modify


строка без изменений
>>> string_modify('it was long thought')
'it was long thought'

строка с изменением регистра и все
>>> string_modify('It was Long thought')
'it was long thought'

строка с удалением пунктуации
>>> string_modify('it was, long thought!')
'it was long thought'

строка с удалением букв другого алфавита
>>> string_modify('it was long thought да дорогая')
'it was long thought  '

строки со всеми пт, кроме 1
>>> string_modify('It was Long thought, да дорогая?')
'it was long thought  '


<!--python3 -m doctest doc_test.md-->