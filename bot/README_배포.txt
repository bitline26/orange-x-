OrangeX Telegram Bot — 실행 / 배포 가이드
==========================================

[STEP 1] 봇 만들기 (5분)
-------------------------
1. 텔레그램에서 @BotFather 검색
2. /newbot 입력
3. 봇 이름 입력 (예: OrangeX 공식 공지)
4. 봇 username 입력 — 반드시 _bot 으로 끝나야 함
   (예: OrangeX_news_bot, OrangeX_official_bot)
5. BotFather가 토큰 발급:
   예) 7123456789:AAFabcDEFghiJKLmnoPQRstUVwxyz-12345
   이 토큰을 절대 외부에 노출하지 말 것

(선택) 봇 프로필 꾸미기
   /setdescription  — 봇 설명
   /setabouttext    — 소개
   /setuserpic      — 프로필 사진 (OrangeX 로고)
   /setcommands     — 명령 목록
                       start - 공식 안내 및 사이트 바로가기
                       site  - 공식 사이트 버튼
                       help  - 도움말


[STEP 2] 로컬에서 테스트 실행
-----------------------------
cd "C:\Users\user\Desktop\orange-x exchange\bot"
pip install -r requirements.txt

# Windows PowerShell
$env:BOT_TOKEN = "7123456789:AAFabcDEFghiJKLmnoPQRstUVwxyz-12345"
python bot.py

# Windows cmd.exe
set BOT_TOKEN=7123456789:AAFabcDEFghiJKLmnoPQRstUVwxyz-12345
python bot.py

정상적으로 뜨면 "Bot starting (long polling)…" 로그 출력.
이 상태에서 텔레그램 앱을 열고 방금 만든 봇을 검색 → /start 눌러 테스트.


[STEP 3] home.html 의 텔레그램 버튼 링크 교체
-------------------------------------------
home.html 안의
    https://t.me/OrangeX_news_bot?start=home
를 방금 만든 봇 username 으로 교체:
    https://t.me/내봇username?start=home

news.html 도 동일하게 교체.


[STEP 4] 실제 배포 (24시간 돌리기)
-----------------------------------
로컬에서 python bot.py 로 돌리면 PC를 끄는 순간 죽습니다.
아래 중 하나를 권장:

■ Railway (월 $5, 가장 쉬움)
  1) railway.app 가입
  2) New Project → Deploy from GitHub or Upload
  3) bot 폴더 업로드
  4) Variables 에 BOT_TOKEN 추가
  5) Start Command: python bot.py
  → 자동 배포 완료

■ Render (무료 플랜 가능, sleep 있음)
  1) render.com 가입
  2) New → Background Worker
  3) 레포 연결 또는 Docker 이미지
  4) Environment 에 BOT_TOKEN 추가
  5) Start Command: python bot.py

■ VPS (Vultr/Oracle Free Tier)
  scp 로 bot.py 업로드 후
  nohup python3 bot.py > bot.log 2>&1 &
  systemd 서비스로 등록 권장


[STEP 5] 운영 체크
------------------
- 봇 토큰 절대 공개 레포에 커밋하지 말 것 (.env 또는 환경변수 사용)
- 광고 URL 은 반드시 home.html, 절대 t.me/... 가 아님
- 봇 메시지 본문은 자유롭게 편집 가능 (bot.py 의 WELCOME_TEXT)
- 이벤트 문구가 바뀌면 WELCOME_TEXT 만 수정 후 재배포


[플로우 요약]
  광고 → home.html → [텔레그램 채널 구독] 버튼 클릭
       → 텔레그램 앱 열림 → [시작] 탭
       → 봇이 이벤트 안내 메시지 + [공식 사이트 바로가기] URL 버튼
       → 유저가 탭 → 브라우저에서 orange-x.co.kr 오픈

구글은 home.html 한 장까지만 봅니다.
텔레그램 앱 내부는 구글이 접근 불가능합니다.
