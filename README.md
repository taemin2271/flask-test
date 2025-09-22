# AI 웹캠 자세 교정 서비스 - 프로젝트 계획서

## 📋 프로젝트 개요

**빅데이터 수업**의 학기 프로젝트로 제안하는 'AI 웹캠을 활용한 실시간 자세 교정 및 건강 데이터 분석 서비스'의 계획서입니다. 이 페이지는 Flask를 이용하여 구축되었으며, 프로젝트의 목표와 주요 기능, 기술적 접근 방식을 설명합니다.

---

## ✨ 주요 기능

- **실시간 자세 분석:** 사용자의 웹캠을 통해 거북목, 라운드 숄더 등 나쁜 자세를 실시간으로 감지합니다.
- **데이터 기반 리포트:** 사용자의 자세 데이터를 기록하고 분석하여 개인화된 대시보드를 제공합니다.
- **맞춤형 솔루션:** 분석 결과를 바탕으로 사용자에게 가장 필요한 스트레칭 가이드 등을 추천합니다.
- **초기 자세 측정 (Calibration):** 사용자 개인의 체형과 환경에 맞는 최적의 자세를 기준으로 설정하여 분석의 정확도를 높입니다.

---

## 🛠️ 기술 스택

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Core AI Model (예정):** MediaPipe (Pose Estimation)

---

## 🚀 실행 방법

1.  **저장소 복제 (Clone)**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **가상 환경 생성 및 활성화**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **필요한 라이브러리 설치**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Flask 애플리케이션 실행**
    ```bash
    python app.py
    ```

5.  **웹 브라우저에서 확인**
    -   애플리케이션 실행 후, 웹 브라우저를 열어 아래 주소로 접속하세요.
    -   `http://127.0.0.1:5000/hw1`

---

## 👤 제출자 정보

-   **이름:** 홍태민
-   **학과:** 통계학과
-   **학번:** 202003785
