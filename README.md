<h2 align="center">FSTR hackathon </h2>

Бэкенд для мобильного приложения на Django REST framework

**Ссылки**:
- [Heroku](https://serene-plains-41198.herokuapp.com/api/)

### Инструменты разработки

**Стек:**
- Python 3.10.2
- Django Rest Framework
- Postgres 14.1

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up
    
##### 3) Перейти по адресу

    http://127.0.0.1:8000/swagger/
    
    http://127.0.0.1:8000/api/submitData/

                                                        
##### 4) Если нужно очистить БД

    docker-compose down -v
 
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)



