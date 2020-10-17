from django.shortcuts import render
from . import utils

def home(request):
  result  = None
  if request.method == 'POST':
    # 初期値を取得
    x = eval(request.POST['x'])
    n = eval(request.POST['n'])
    dt = eval(request.POST['dt'])
    t = 0
    # dx/dtの方程式を文字列として取得
    equation1 = request.POST['equation']
    
    # グラフ用のリスト
    x_list = [x]
    t_list = [0]
    for n in range(0,n):
      x = utils.next_x(equation1, x, dt)
      t += dt

      x_list.append(x)
      t_list.append(t)
      print(x)
    
    result = x_list
    # 以下グラフ用の処理
    utils.create_graph(x_list, t_list)
  return render(request, 'differential/home.html', {'result': result})

