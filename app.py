from flask import Flask, render_template

app = Flask(__name__)

@app.get("/hw1")
def home():
    return render_template("hw1.html", title="웹캠 자세 교정 서비스 | 프로젝트 계획서")

if __name__ == "__main__":
    app.run() # 기본 : http://127.0.0.1:5000