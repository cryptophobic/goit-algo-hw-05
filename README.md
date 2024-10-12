# Домашнє завдання до теми “Алгоритми пошуку”


##Результати виконання.

```
Стаття 1, Підрядок існує:
KMP: 0.050929810999150504
Rabin-Karp: 0.10410765199958405
Boyer-Moore: 0.018677522999496432
Стаття 1, Підрядок не існує:
KMP: 1.99636371500128
Rabin-Karp: 4.580542943000182
Boyer-Moore: 0.45027198500065424
Стаття 2, Підрядок існує:
KMP: 0.013680685000508674
Rabin-Karp: 0.02964563199930126
Boyer-Moore: 0.006912108001415618
Стаття 2, Підрядок не існує:
KMP: 2.8686827320016164
Rabin-Karp: 6.534635197998796
Boyer-Moore: 0.8708971300002304
```

## Висновки:
Алгоритм Боєра-Мура мав найвищі показники для існуючого та неіснуючого входження.

Алгоритм Кнута-Морріса-Пратта середній.

Алгоритм Рабіна-Карпа найповільніший серед усіх алгоритмів для обох типів підрядків.

## Загальний висновок:
Серед трьох розглянутих алгоритмів алгоритм Боєра-Мура виявився найефективнішим для швидкого пошуку підрядків у тексті, як у випадку наявних, так і неіснуючих підрядків. 
