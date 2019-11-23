# Decimal To Binary Converter
My school homework

## Process
1. Split string to a list (Разделение строки на список)
2. Parse list, get numbers (Парсинг списка, получение чисел)
3. Convert numbers to needed num. system (Перевод в нужную СС)
4. Put converted numbers back in place (Занесение результатов в конечную строку)

## Todo
 - [x] First version (Первая версия)
 - [x] Support in-word numbers (Поддержка чисел, не обрамленных пробелами)
 - [ ] Support other numerical systems (Поддержка других СС)

## Examples
1. `He won 5 games in 2 days` => `He won 101 games in 10 days`
2. `Your order of 5pcs will be ready in 2 days` => `Your order of 101pcs will be ready in 10 days`
3. `1 2 3 4 5 6 7 8 9` => `1 10 11 100 101 110 111 1000 1001`
4. `adf896qk0h0084f38` => `adf1110000000qk0h1010100f100110`