import requests
import unittest
import time

class MyTest(unittest.TestCase):


    def login(self):
        url = "http://www.xiaojike.cn/sign_in/"
        result = requests.get(url)
        time.sleep(1)

        real_code = result.status_code
        self.assertEqual(200, real_code)

        real_text = result.text
        expect_text = '注册不到1秒钟'
        self.assertIn(expect_text, real_text)

    def test_err(self):
        self.assertEqual(3, 3)

if __name__ == '__main__':
    unittest.main()
    print("finish.")