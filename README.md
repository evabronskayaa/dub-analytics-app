# DUB Analytics App

## Описание

Сервис аналитики, реализующий парсинг различных SKU категории "Одежда" по конкурентам fashion-индустрии с различных маркетплейсов: wildberries, lamoda и т.д
Результаты парсинга обрабатываются и отображаются на дашборде в виде графических визуализаций и вычисленных топ-10 SKU по продажам с учетом выбранных фильтров.   

## Дизайн сервиса

Взаимодействие пользователя с сервисом происходит через дашборд

![](https://drive.google.com/file/d/1HAPnAC7PMXksq5gNU8zIG-nKlECOly0T/view?usp=drive_link)

Главная задача сервиса: собирать самую актуальную информацию по потребительскому спросу в разных категориях одежды

![](https://drive.google.com/file/d/1G7BXZw15s2_pvmhoz-hGn9oS7tDEBdWH/view?usp=drive_link)

Для удобства работы продумана гибкая система фильтрации:  
    - бренд (конкурент)  
    - пол  
    - категория одежды
    - размер

![](https://drive.google.com/file/d/14TotJ38J1BYKWgzqVx9CIkmAJkURCDkJ/view?usp=drive_link)

## Дерево файлов

├───ai
├───app
│   └───assets
├───data
├───parsing
│   ├───lamoda
│   ├───ozon
│   └───wildberries
└───venv

## Запуск

```bash
cd app
python3 index.py
```