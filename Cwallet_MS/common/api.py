import base64
import json
import requests
import inspect
from Cwallet_MS.data.EnvConfig import *
from Cwallet_MS.common.utils import *
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


class OpenApi(object):


    def __init__(self):
        # 环境 prod/test/local
        match env:
            case "prod":
                self.host = PROD_HOST
            case "test":
                self.host = TEST_HOST
                self.Device_id = envs_test.get("Device_id")
            case "local":
                self.host = LOCAL_HOST

    def getHeaders(self):
        """
        获取请求头
        """
        headers = ""
        match env:
            case "prod":
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json, text/plain, */*",
                    "x-device-id": self.Device_id,
                    "x-device-scene": "beta",
                    "x-device-type": "web",
                    "x-sign-key": "",
                    "x-sign-source": "",
                }
            case "beta":
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json, text/plain, */*",
                    "x-device-id": self.Device_id,
                    "x-device-scene": "beta",
                    "x-device-type": "web",
                    "x-sign-key": "",
                    "x-sign-source": "",
                }
            case "test":
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json, text/plain, */*",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                    "x-device-id": self.Device_id,
                    "x-device-scene": "test",
                    "x-device-type": "web",
                    "x-sign-key": "",
                    "x-sign-source": "",

            }
        return headers

    def getSign(self, params=None):
        """
        生成签名

        Args:
            params (dict): 参数字典，默认值为空字典。

        Returns:
            str: 签名字符串。
        """
        if params is None:
            params = {}
        pass

    def Unifiedrequest(self, data, aotug, defname):
        """
        统一请求
        签名控制
        """
        url = self.host+addr_info.get(f'{defname}_addr')
        header = self.getHeaders()
        if aotug:
            header['sign'] = self.getSign(data)
        else:
            header['sign'] = json.dumps(data)
        response = requests.post(url=url, headers=header, json=data)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("not JSON response:", response.text)

    def Login_email(self, email, aotug=True):
        """
        登陆邮件账户验证
        """
        data = {
            "device": "web",
            "device_id": "e3cfd97d6874cbc4819eea9100b85f22",
            "email": email
        }

        return self.Unifiedrequest(data, aotug, inspect.currentframe().f_code.co_name)

    def Login(self, email, password, aotug=True):
        """
        登陆账户验证
        """
        password = get_md5(password)
        data = {
            'platform': 'email',
            'param': {
                'email': email,
                'login_type': '1',
                'password': f'{password}'
            },
            'device': 'web',
            'device_name': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'device_id': self.Device_id,
            'timestamp': f'{get_timestamp()}'
        }

        return self.Unifiedrequest(data, aotug, inspect.currentframe().f_code.co_name)
