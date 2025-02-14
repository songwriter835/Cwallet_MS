import pytest
from ulid import ULID
from Cwallet_MS.common.api  import OpenApi
from Cwallet_MS.common.utils import *
# # 测试数据读取
API = OpenApi()
RESET = "\033[0m"  # 重置样式
BLUE = "\033[34m"  # 字体颜色


class Test_api:

    # 登陆-邮件验证
    @staticmethod
    def test_login_email():
        adata = API.Login_email("songwriter835@gmail.com", aotug=False)
        print(adata)
        assert adata.get("code") == 10000 and adata.get("msg") == "Success", \
            f"登陆-邮件验证失败，错误码[{adata.get("code")}]msg[{adata.get("msg")}]"

    # 登陆-账户验证
    @staticmethod
    def test_login():
        adata = API.Login("songwriter835@gmail.com","Jj@12345", aotug=False)
        print(adata)
        assert adata.get("code") == 10000 and adata.get("msg") == "Success", \
            f"登陆-账户验证失败，错误码[{adata.get("code")}]msg[{adata.get("msg")}]"

if __name__ == '__main__':
    pytest.main(["-vs", __file__])
