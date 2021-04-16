import time
def countdown(n):
    li = (n)
    def next():
        r = li(0)
        li[0] -= 1
        return r
    return next
def main():
    next = countdown(3)
    while true :
        val = next()
        if val == 0:
            print('Yok bisa yok!')
            break
        print(val, end='')
        time.sleep(1)
        main()
