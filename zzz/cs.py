def XX():
    a = False
    b = 'xxxx'
    return a,b

def Q():
    a, b=XX()
    if a is False:
        x ='qwer'
    else:
        x= 'asdf'
    print(x)
    print(b)

if __name__ == '__main__':
    Q()

# /var/log/uwsgi/app/parkhero.log