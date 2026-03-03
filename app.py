from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Heroku! Jeongwoo Kim's first app is running."

if __name__ == '__main__':
    # Heroku는 포트 번호를 동적으로 할당하므로 아래 설정이 필수입니다.
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
