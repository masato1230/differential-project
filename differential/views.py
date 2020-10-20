from django.shortcuts import render
from . import utils

def home(request):
  result  = None
  graph1 = None
  graph2 = None
  error_message = None
  # x,yを初期化
  x = 0
  y = 0
  if request.method == 'POST':
    if request.POST['equation2']:
      try:
        if int(request.POST['n']) > 5000:
          return render(request, 'differential/home.html', {'error_message': "nは5000以下にしてください。"})
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
          x = utils.next_x(equation1, x, y, dt, t)
          y = utils.next_y(equation2, x, y, dt, t)
          t += dt

          print(t)

          x_list.append(x)
          y_list.append(y)
          t_list.append(t)

        # 以下グラフ用の処理
        utils.create_graph(x_list, t_list)
        graph1 = utils.get_image()

        utils.create_graph(y_list, t_list)
        graph2 = utils.get_image()
      except OverflowError:
        error_message = "計算結果が大きすぎます。nかdtの値を小さくしてください。"
      except ValueError:
        error_message = "n,dtは整数で入力してください"
      except NameError:
        error_message = "式の入力方法が間違っています。詳しくは、「使い方」を参照してください。"
      except TypeError:
        error_message = "式の入力方法が間違っています。詳しくは、「使い方」を参照してください。"
    
    else:
      try:
        if int(request.POST['n']) > 5000:
          return render(request, 'differential/home.html', {'error_message': "nは5000以下にしてください。"})

      # 初期値を取得
        x = eval(request.POST['x'])
        n = eval(request.POST['n'])
        dt = eval(request.POST['dt'])
        t = 0
        # dx/dtの方程式を文字列として取得
        equation1 = request.POST['equation1']

        # グラフ用のリスト
        x_list = [x]
        t_list = [0]
        for n in range(0,n):
          x = utils.next_x(equation1, x, y, dt, t)
          t += dt
          print(t)

          x_list.append(x)
          t_list.append(t)

        # 以下グラフ用の処理
        utils.create_graph(x_list, t_list)
        graph1 = utils.get_image()
      except ValueError:
        error_message = "n,dtは整数で入力してください"
      except OverflowError:
        error_message = "計算結果が大きすぎます。nかdtの値を小さくしてください。"
      except NameError:
        error_message = "式の入力方法が間違っています。詳しくは、「使い方」を参照してください。"
      except TypeError:
        error_message = "式の入力方法が間違っています。詳しくは、「使い方」を参照してください。"
  result = "(x,y) = (" + str(x)+ " ," + str(y) + ")"
  return render(request, 'differential/home.html', {'result': result, 'graph1': graph1, 'graph2': graph2, 'error_message': error_message})


