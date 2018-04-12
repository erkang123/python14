class ErkangException(Exception):
    def __init__(self,msg):
        self.message =msg
    def __str__(self):
        return self.message
try:
    raise ErkangException("我的异常")
except ErkangException as e:
    print(e)