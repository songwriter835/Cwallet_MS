import time
from pprint import pprint
import pytest
from ulid import ULID
from Cwallet_MS.common.api  import OpenApi
from Cwallet_MS.common.utils import send_request, random_12num

API = OpenApi()
bill_id = str(ULID())

""" 代收 """


""" openapi """
# if __name__ == '__main__':
#     pytest.main(['-vs','/Users/songwriter/Desktop/project/bankpayos-test-script/BankpayOS_MS/case/'
#                        'test_openapi.py::Test_api::test_GetServiceConfigsPayment'])

