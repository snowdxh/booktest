# booktest

api：
http://127.0.0.1:8000/api/books/book/
请求方式get,post,put,delete,对应查询、添加、修改、删除

还书和借书api：
http://127.0.0.1:8000/api/books/book/<int:pk>/give_book/  借书
http://127.0.0.1:8000/api/books/book/<int:pk>/return_book/  还书

中间件RequestDateMiddleware，记录请求时间和参数

celery发布定时任务：
celery -A booktest worker --loglevel=info -P eventlet (window下运行)
celery -A booktest beat --loglevel=info

日志配置在settings.py中

