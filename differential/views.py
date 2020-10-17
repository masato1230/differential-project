from django.shortcuts import render
from . import utils

def home(request):
  if request.method == 'POST':
    # 初期値を取得
    x = eval(request.POST['x'])
    n = eval(request.POST['n'])
    dt = eval(request.POST['dt'])
    # dx/dtの方程式を文字列として取得
    equation1 = request.POST['equation']
    
    for n in range(0,n):
      x = utils.next_x(equation1, x, dt)
      print(x)
    
    result = x

  return render(request, 'differential/home.html', {'result': result})