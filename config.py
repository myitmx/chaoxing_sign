# =================配置区start===================

# 学习通账号密码
USER_INFO = {
    'username': 'xxxx',
    'password': 'xxxx',
    'schoolid': ''  # 学号登录才需要填写
}

# server酱
SERVER_CHAN_SCKEY = 'xxxx'  # 申请地址http://sc.ftqq.com/3.version
SERVER_CHAN = {
    'status': True,  # 如果关闭server酱功能，请改为False
    'url': 'https://sc.ftqq.com/{}.send'.format(SERVER_CHAN_SCKEY)
}

# 学习通账号cookies缓存文件路径
COOKIES_PATH = "./"
COOKIES_FILE_PATH = COOKIES_PATH + "cookies.json"

# activeid保存文件路径
ACTIVEID_PATH = "./"
ACTIVEID_FILE_PATH = ACTIVEID_PATH + "activeid.json"

# 状态码
STATUS_CODE_DICT = {
    1000: '登录成功',
    1001: '登录信息有误',
    1002: '拒绝访问',
    2000: '当前暂无签到任务',
    2001: '有任务且签到成功',
    3000: '普通签到成功',
    3001: '手势签到成功',
    3002: '拍照签到成功',
    3003: '位置签到成功',
    3004: '二维码签到成功',
    3005: '任务已经签过了',
    4000: '未知错误',
}
# =================配置区end===================