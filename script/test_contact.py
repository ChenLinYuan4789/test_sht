import allure
from appium import webdriver
import pytest

class TestContact():

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="登录的测试脚本")
    def test_login(self):
        allure.attach("输入用户名", "测试输入了:hello, 1, str")
        print("输入你的用户名")
        allure.attach("输入密码", "输入密码的描述")
        print("输入密码")
        allure.attach("登录", "登录的描述")
        print("点击登录")
        assert 0

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title="用户名的测试脚本")
    def test_username(self):
        assert 1

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step(title="密码的测试脚本")
    def test_password(self):
        assert 1
