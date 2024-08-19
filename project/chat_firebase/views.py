from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials, db
import time

# Create your views here.
cred = credentials.Certificate(
    '/Users/doyoungchoi/Documents/GitHub/stack-overflow/dev-chat-cea35-firebase-adminsdk-hj8kj-e9f825e65b.json')
# Firebase 앱 초기화
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://dev-chat.firebaseio.com/'
})

# 예시: 데이터베이스에 데이터 쓰기
ref = db.reference('messages')
ref.push({
    'username': 'user1',
    'message': 'Hello, world!',
    'timestamp': int(time.time())
})
