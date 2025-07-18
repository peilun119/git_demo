# 1. 加入例外處理
# 2. 重複輸入,直到a -> exit 離開,使用while True


while True:
    try:
        a = input('請輸入數字a:')
        if (a == 'exit'):
            break

        a = eval(a)
        b = eval(input('請輸入數字b:'))

        if (a > b):
            print(f'a比b大{a-b}')
        elif (b > a):
            print(f'b比a大{b-a}')
        else:
            print('a跟b一樣大')
    except Exception as e:
        print(e)