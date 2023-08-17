# DUB Analytics App

## Описание

Сервис аналитики, реализующий парсинг различных SKU категории "Одежда" по конкурентам fashion-индустрии с различных маркетплейсов: wildberries, lamoda и т.д
Результаты парсинга обрабатываются и отображаются на дашборде в виде графических визуализаций и вычисленных топ-10 SKU по продажам с учетом выбранных фильтров.   

## Дизайн сервиса

Взаимодействие пользователя с сервисом происходит через дашборд  

![Screenshot 1. first view](https://github.com/evabronskayaa/dub-analytics-app/raw/master/app/assets/img/first_view.png)  

Главная задача сервиса: собирать самую актуальную информацию по потребительскому спросу в разных категориях одежды  

![Screenshot 2. grid SKU](https://github.com/evabronskayaa/dub-analytics-app/raw/master/app/assets/img/grid_SKU.png)  

Для удобства работы продумана гибкая система фильтрации:  
    - бренд (конкурент)  
    - пол  
    - категория одежды  
    - размер  

![Screenshot 3. filter menu](https://github.com/evabronskayaa/dub-analytics-app/raw/master/app/assets/img/filter_menu.png)  

## App components

- `app.py` - определение сервиса  
- `components.py` - отдельные компоненты сервиса: filters, header, cards, footer  
- `data_preprocessing.py` - функции генерации новых признаков  
- `data_processing.py` - функции обработки данных  
- `data.py` - обработка данных, генерация новых признаков  
- `index.py` - запуск приложения, callbacks  
- `layouts.py` - общая структура сервиса  
- `plots.py` - функции отрисовки графиков   

## Запуск

```bash
cd app
python3 index.py
```