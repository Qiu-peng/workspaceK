import easygui

# 返回值
# title = easygui.msgbox(msg='提示信息', title='标题部分', ok_button="OK")
# msg = easygui.msgbox('Hello Easy GUI')
# print("返回值:%s"% msg)
# ccbox = easygui.ccbox("here is Continue | Cancel Box!")
# print("返回值:%s"% str(ccbox))
# ynbox = easygui.ynbox("Yes Or No Button Box!")
# print("返回值:%s"% str(ynbox))

# 选择
# msg = '选择此列表项中你喜欢的一个吧'
# title = '必须选择一个哦'
# choices = ['1', '2', '3', '4', '5', '6', '7']
# answer = easygui.choicebox(msg, title, choices)
# print('你选择了:%s' % str(answer))

# 展示图片
# easygui.buttonbox("美否?", image="gufen.jpg", choices=("美", "非常美"))

# 下拉框
# msg = "选择你喜欢的一种业余生活"
# title = ""
# choicess_list = ["看书","游泳","骑自行车","玩游戏"]
# reply = easygui.choicebox(msg,choices=choicess_list)

# 多选
# easygui.multchoicebox(msg="请选择你爱吃哪些水果?",title="",choices=("西瓜","香蕉","苹果","梨"))

# 登录
# msg = "请输入用户名和密码"
# title = "用户登录接口"
# user_info = []
# user_info = easygui.multpasswordbox(msg,title,("用户名","密码"))
# print(user_info)