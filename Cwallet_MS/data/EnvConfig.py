"""
==========  脚本控制  ==========
Environment configuration prod/beta/test/local
"""
from sympy.integrals.heurisch import BesselTable

# 运行环境 prod/beta/test/local
env = 'test'

"""=================================  接口地址  ======================================="""
# 生产环境
PROD_HOST = "https://cwallet.com"
# 灰度环境
BETA_HOST = "https://my-beta.cwallet.com"
# 测试环境
TEST_HOST = "https://f4658f7abeta-my.cwallet.com"
# 本地
LOCAL_HOST = "http://127.0.0.1:8032"
# addr
addr_info = {
    # 登陆
    'Login_email_addr':'/cctip/v1/account/register/check',
    'Login_addr':'/cctip/v1/account/auth/token/get'

}
"""=================================  正式环境参数  ======================================="""
prod_test = {
            "Device_id" : ""
}
"""=================================  测试环境参数  ======================================="""
envs_test = {
            "Device_id" : "e3cfd97d6874cbc4819eea9100b85f22"
}

