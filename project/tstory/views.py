from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create your views here.

def auto_create_blog(self, request):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 브라우저를 열지 않고 실행
    chrome_service = Service('C:\Users\admin\Desktop\Chrome for Developers.exe')  # ChromeDriver 경로 설정