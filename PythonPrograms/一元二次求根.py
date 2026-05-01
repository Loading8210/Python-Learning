while 1:
    print("ax^2+bx+c=0")
    ("一般形式:ax^2+bx+c=0")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    equation = f"{a}x^2+{b}x+{c}=0"
    print(f"方程为：{equation}")
    while 1:
        user_choice = input("确定？(y/n)")
        if user_choice == "y":
            if a == 0:
                print("不是二元一次方程!")
                break
            elif b**2-4*a*c < 0:
                print("无实数解!")
                break
            if b**2-4*a*c == 0:
                print(f"此方程的解为：x1 = x2 = {(-b+(b**2-4*a*c)**0.5)/2*a}")
            if b**2-4*a*c > 0:
                x1 = (-b+(b**2-4*a*c)**0.5)/2*a
                x2 = (-b-(b**2-4*a*c)**0.5)/2*a
                print(f"此方程的解为：x1 = {x1}或x2 = {x2}")
                break
        elif user_choice == "n":
            break