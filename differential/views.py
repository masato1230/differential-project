from django.shortcuts import render
from . import utils

def home(request):
  result  = None
  graph1 = None
  graph2 = None
  if request.method == 'POST':
    # 初期値を取得
    x = eval(request.POST['x'])
    y = eval(request.POST['y'])
    n = eval(request.POST['n'])
    dt = eval(request.POST['dt'])
    t = 0
    # dx/dtの方程式を文字列として取得
    equation1 = request.POST['equation1']
    equation2 = request.POST['equation2']
    
    # グラフ用のリスト
    x_list = [x]
    y_list = [y]
    t_list = [0]
    for n in range(0,n):
      x = utils.next_x(equation1, x, y, dt)
      y = utils.next_x(equation2, x, y, dt)
      t += dt

      x_list.append(x)
      y_list.append(y)
      t_list.append(t)
      print(x)
    
    result = y_list
    # 以下グラフ用の処理
    utils.create_graph(x_list, t_list)
    graph1 = utils.get_image()
    
    utils.create_graph(y_list, t_list)
    graph2 = utils.get_image()
  return render(request, 'differential/home.html', {'result': result, 'graph1': graph1, 'graph2': graph2})

