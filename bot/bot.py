"""
OrangeX Telegram Bot — /start 수신 → 이벤트 안내 + orange-x.co.kr URL 버튼 응답

실행:
  1) pip install -r requirements.txt
  2) 환경변수 설정 (Windows PowerShell):
       $env:BOT_TOKEN = "123456:ABC..."   # BotFather에서 받은 토큰
  3) python bot.py
"""
import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s  %(levelname)s  %(name)s  %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "PUT-YOUR-BOT-TOKEN-HERE")
LANDING_URL = "https://orange-x.co.kr/"
SIGNUP_URL = "https://www.orangex.com/login"
KYC_URL = "https://www.orangex.com/login"

KYC_TEXT = (
    "✅ <b>KYC 본인인증 — 3분이면 끝!</b>\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "KYC를 완료해야 입출금·거래·이벤트 참여가 가능합니다.\n\n"
    "📌 <b>STEP 1 — Verify Now 클릭</b>\n"
    "로그인 후 상단 배너\n"
    "<i>\"Complete Identity Verification\"</i> 클릭\n"
    "또는 설정 → KYC 인증에서 시작\n\n"
    "📌 <b>STEP 2 — 기본 정보 + 신분증</b>\n"
    "• First Name / Last Name (영문)\n"
    "• 생년월일 입력\n"
    "• 신분증 택 1: 주민등록증 / 운전면허증 / 여권\n"
    "• 신분증 앞·뒤 사진 업로드\n"
    "  (jpg, jpeg, png / 5MB 이내)\n\n"
    "📌 <b>STEP 3 — 얼굴 인식 (셀피)</b>\n"
    "• 카메라 앞에서 3~10초간 얼굴 촬영\n"
    "• 촬영 후 <b>\"NEXT\"</b> 클릭하면 끝!\n\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "⏱ 평균 소요 시간: <b>약 3분</b>\n"
    "📧 승인 완료 시 이메일로 안내 발송\n"
    "❌ 미승인 시 재검토 요청 가능\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "👇 <b>지금 바로 KYC 인증하세요</b> 👇"
)

WELCOME_TEXT = (
    "✅ <b>KYC 본인인증 — 3분이면 끝!</b>\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "가입만 하면 끝이 아닙니다!\n"
    "<b>KYC 인증을 완료해야</b> 아래 혜택을 받을 수 있어요.\n\n"
    "🎁 손실공제 100% · PAYBACK 50%\n"
    "💰 입출금 · 거래 · 이벤트 참여\n"
    "━━━━━━━━━━━━━━━━━━━\n\n"
    "📌 <b>STEP 1 — 로그인 후 인증 시작</b>\n"
    '앱/웹 로그인 → 상단 배너\n'
    '<i>"Complete Identity Verification"</i> 클릭\n\n'
    "📌 <b>STEP 2 — 기본 정보 + 신분증</b>\n"
    "• 이름(영문) · 생년월일 입력\n"
    "• 신분증 택1: 주민등록증 / 운전면허증 / 여권\n"
    "• 앞·뒤 사진 업로드 (jpg/png, 5MB 이내)\n\n"
    "📌 <b>STEP 3 — 얼굴 인식 (셀피)</b>\n"
    "• 카메라 앞에서 3~10초 촬영\n"
    '• <b>"NEXT"</b> 클릭하면 끝!\n\n'
    "━━━━━━━━━━━━━━━━━━━\n"
    "⏱ 평균 소요 시간: <b>약 3분</b>\n"
    "📧 승인 완료 → 이메일 안내 발송\n"
    "❌ 미승인 → 재검토 요청 가능\n"
    "━━━━━━━━━━━━━━━━━━━\n"
    "👇 <b>지금 바로 KYC 인증하세요</b> 👇"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    args = context.args
    source = args[0] if args else "direct"
    logging.info("start from user=%s source=%s", user.id if user else "?", source)

    # KYC 안내 플로우
    if source == "kyc":
        kyc_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("✅  지금 KYC 인증하기", url=KYC_URL)],
                [InlineKeyboardButton("📖  KYC 상세 안내 보기", url=LANDING_URL + "#kyc")],
                [InlineKeyboardButton("🚀  가입 아직 안 했다면 →", url=SIGNUP_URL)],
                [InlineKeyboardButton("💬  그래도 어렵다면? 1:1 문의", url="https://t.me/OrangeX_KR_Support")],
            ]
        )
        await update.message.reply_text(
            KYC_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=kyc_keyboard,
            disable_web_page_preview=True,
        )
        return

    # 기본 메시지 — KYC 중심
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅  지금 KYC 인증하기", url=KYC_URL)],
            [InlineKeyboardButton("📖  KYC 상세 안내 보기", url=LANDING_URL + "#kyc")],
            [InlineKeyboardButton("🚀  아직 가입 안 했다면 →", url=SIGNUP_URL)],
            [InlineKeyboardButton("💬  그래도 어렵다면? 1:1 문의", url="https://t.me/OrangeX_KR_Support")],
        ]
    )

    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )


async def kyc_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Standalone /kyc command"""
    kyc_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅  지금 KYC 인증하기", url=KYC_URL)],
            [InlineKeyboardButton("📖  KYC 상세 안내 보기", url=LANDING_URL + "#kyc")],
            [InlineKeyboardButton("🚀  가입 아직 안 했다면 →", url=SIGNUP_URL)],
            [InlineKeyboardButton("💬  그래도 어렵다면? 1:1 문의", url="https://t.me/OrangeX_KR_Support")],
        ]
    )
    await update.message.reply_text(
        KYC_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=kyc_keyboard,
        disable_web_page_preview=True,
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "사용 가능한 명령:\n"
        "/start  — 공식 안내 및 사이트 바로가기\n"
        "/kyc    — KYC 본인인증 가이드\n"
        "/site   — 공식 사이트 버튼 다시 보기",
    )


async def site(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔗  공식 사이트 바로가기", url=LANDING_URL)]]
    )
    await update.message.reply_text(
        "OrangeX 공식 사이트로 이동합니다.",
        reply_markup=keyboard,
    )


def main() -> None:
    if BOT_TOKEN == "PUT-YOUR-BOT-TOKEN-HERE":
        raise SystemExit("환경변수 BOT_TOKEN 을 먼저 설정하세요. (BotFather 토큰)")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("kyc", kyc_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("site", site))

    logging.info("Bot starting (long polling)…")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
