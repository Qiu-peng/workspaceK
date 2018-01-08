import easygui

# easygui.msgbox("hello world")


def create():
    # 创建一个新账号，并记录在字典user内
    name = easygui.enterbox(msg="请输入用户名", default="")
    while True:
        global user
        if name in user:
            name = easygui.enterbox(msg="该用户名已存在，请重新输入", default="")
        else:
            break

    key = easygui.passwordbox(msg="请输入密码：", default="")
    user[name] = key
    easygui.msgbox("注册成功")
    return


def log_in():
    # 登陆账户，需要输入账户名及密码
    name = easygui.enterbox(msg="请输入用户名", default="")
    print(user)
    while True:
        if user.get(name):
            break
        elif name == "":
            break
        else:
            name = easygui.enterbox(msg="您输入的用户名不对，请重新输入", default="")
    if name == "":
        return
    key = easygui.enterbox(msg="请输入用户密码：", default="")
    while True:
        if user[name] == key:
            easygui.msgbox(msg="欢迎进入湫")

            break
        elif key == "":
            break
        else:
            key = easygui.enterbox(msg="您输入的密码不对，请重输", default="")
    return


user = {}
while True:
    command = easygui.buttonbox(msg="请选择", title="", choices=('新建用户', '登录账号', '退出程序'))
    if command == "新建用户":
        create()
    elif command == "登录账号":
        log_in()
    elif command == "退出程序":
        break