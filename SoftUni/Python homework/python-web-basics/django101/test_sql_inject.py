from django101.web.models import Todo

x = Todo()
todos = Todo.objects.all()
param = 'the'
todos = Todo.objects.raw('SELECT * FROM web_todo' 
                         f"WHERE title LIKE '%{param}%'",
                         (param))