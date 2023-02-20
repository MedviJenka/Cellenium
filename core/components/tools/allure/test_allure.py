#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_allure.py
@time:2020/10/10
"""
import allure


@allure.feature('登录模块')
class TestLogin:
    @allure.story('登录成功')
    @allure.title('登录成功标题')
    def test_login_sucess(self):
        with allure.step('步骤1：打开应用'):
            print('应用已打开')
        with allure.step('步骤2：进入登录页面'):
            print('登录页面已打开')
        with allure.step('步骤3：输入用户名和密码'):
            print('用户名和密码输入成功')
        print('登录测试用例：登录成功')

    @allure.story('登录成功')
    def test_login_success2(self):
        assert '1' == 1
        print('登录测试用例：登录成功')

    @allure.story('登录失败')
    def test_login_failure_a(self):
        print('登录测试用例：登录失败，用户名缺失')

    @allure.story('登录失败')
    def test_login_failure_b(self):
        print('登录测试用例：登录失败，密码缺失')

    @allure.story('登录失败')
    def test_login_failure_c(self):
        with allure.step('输入用户名'):
            print('已输入用户名')
        with allure.step('输入密码'):
            print('已输入密码')
        with allure.step('点击登录'):
            print('已点击登录')
        print('登录测试用例：登录失败，密码错误')


@allure.feature('搜索模块')
class TestSearch:

    def test_search1(self):
        print('搜索用例1')

    TEST_CASE_LINK = 'https://mirrors.huaweicloud.com/'

    @allure.testcase(TEST_CASE_LINK,'测试用例连接')
    def test_search2(self):
        print('搜索用例2')

    @allure.step('搜索步骤')
    def test_search3(self):
        print('搜索用例3')
