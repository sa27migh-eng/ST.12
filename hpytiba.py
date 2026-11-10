# -*- coding: utf-8 -*-
"""موقع طيوب - نسخة Streamlit للنشر على share.streamlit.io
التشغيل محلياً:  streamlit run app.py
"""
import base64
import html

import streamlit as st

# ───────────── عدّل هنا ─────────────
SITE_TITLE = "طيوب"
GREETING_TITLE = "كل عام وإنتِ بخير 🎂"
GREETING_TEXT = """كل عام وانتي بخير يا أمي وابوية وكل عام وضحكتچ الحلوة وعيونچ بخير

يمكن صارلنا بس ثلاث أسابيع نعرف بعض بس الغريب شكد نكدر نعبر هواي بهالوقت القليل وشكد أكو تفاصيل صغيرة منچ ضلت ببالي نظراتچ من تضحكين خدودچ الحلوة وحتى من فصلاتچ وكعدتچ وياي وطريقتچ بالحچي وكلشي بيچ بيه شي يخليني أريد أعرفچ أكثر.

يمكن اني ما جنت منتظر هالصدفة  ويمكن إنتي جيتي بالوقت اللي ما مفكر بيه بعلاقه ولا ادخل شخص لحياتي بس نوبات تجيك شغله حلوه وانت ممحسبلها حساب وناس تدخل بحياتك بدون ما أتوقع منها شي بس تخليني أبتسم من أتذكر تفاصيلها.

ما أريد أستعجل الأيام ولا أسبق الوقت بكلام أكبر من عمر معرفتنا بس أتمنى من كل گلبي تطلعين مثل ما أتمنى وأحلى وأتمنى الأيام تخلينا نعرف بعض أكثر ونبقى سبب ودافع وشي حلو بحياتنا.

ويمكن لهذا السبب اختاريت أغنية كبرت سنة لأن أتمنى كل سنة جديدة بعمرچ تجيب وياها أشياء حلوة وتكون إلي فرصة أكون واحد من هالأشياء.

حضر حالك يا قمر لتكون إنت الهدية بعيد ميلاد أغلى البشر

عيد ميلاد سعيد طيوبه ❤️"""
# ─────────────────────────────────────

QR_ROWS = [
    "11111110000011110001011111100010001111111",
    "10000010001010101101000111101101101000001",
    "10111010111110000011101101110111101011101",
    "10111010100000011010010110110000101011101",
    "10111010010011111110110110000010001011101",
    "10000010011110101001010000000110001000001",
    "11111110101010101010101010101010101111111",
    "00000000000111101101001011001000000000000",
    "00011011011000000010111011011101100001100",
    "01100001001010111011101100011111011110010",
    "00011011110100010110110100011000001000110",
    "11001100110101000000010010100111100011001",
    "10110110100111101001001100111100000100011",
    "11000101001111000110100000101011100110101",
    "10100111111001000100000111001011111110001",
    "00011001011000011110100101010000110110110",
    "11010010010011100011101101000000110000010",
    "01000100100011001101101001000110110010100",
    "10100011010000101001011001110111010110101",
    "11101001111000100100110100010000110011101",
    "10111010101100100001011011100011101010111",
    "01010000011111100110111000100100001010000",
    "10011110100010100000001110110000110000100",
    "00101000111101010001100001101101011111001",
    "01010110110101011111100001010001101101110",
    "00011100010111100110000001011100111110100",
    "00011010010011011101011011011111111111000",
    "00001001110100110110111011000001011001000",
    "00000110001110100110011010111011110110000",
    "00000000101111011111010001101100111000000",
    "00000010011000000010100110010100110000000",
    "00000000100010010111011001000010000000000",
    "11001111100011010010111011011100100000000",
    "00000000100001001000000011110100000000000",
    "11111110100100000011111001011000000000000",
    "10000010000001101101010111101000000000000",
    "10111010100000110110010111000000000000000",
    "10111010100000011101010000000000000000000",
    "10111010000000000010001100000000000000000",
    "10000010000000000000011000000000000000000",
    "11111110000000000001010000000000000000000",
]  # باركود القلب (1 = نقطة)
QR_COLOR = "#be0023"

st.set_page_config(page_title=SITE_TITLE, page_icon="🎁", layout="centered")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@700&family=Cairo:wght@400;700&display=swap');
:root{--bg:#2a0a18;--bg2:#3d1226;--card:#4a1830;--rose:#e8456b;--blush:#f7c6d2;--cream:#fff1ec}
#MainMenu,header,footer,[data-testid="stToolbar"],[data-testid="stDecoration"]{display:none !important;visibility:hidden}
.stApp{background:radial-gradient(120% 80% at 50% 0%,var(--bg2),var(--bg) 70%) fixed !important;
 font-family:'Cairo','Tajawal','Segoe UI',Tahoma,sans-serif;color:var(--cream);direction:rtl}
.block-container{padding:3rem 1.25rem 4rem !important;max-width:760px !important}
.site-title{font-family:'Aref Ruqaa','Amiri',serif;font-weight:700;font-size:clamp(4rem,16vw,7.5rem);
 line-height:1.1;color:var(--blush);text-shadow:0 0 40px rgba(232,69,107,.45);text-align:center}
.sub{margin-top:.5rem;color:#d9a9b8;font-size:1.1rem;text-align:center}
.gifts{margin-top:3rem;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1.5rem;width:100%}
@media(max-width:560px){.gifts{grid-template-columns:1fr}}
a.gift{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.9rem;
 min-height:260px;padding:2rem 1rem;border-radius:28px;text-decoration:none !important;color:var(--cream) !important;
 background:linear-gradient(160deg,var(--card),#35112a);border:1px solid rgba(247,198,210,.18);
 overflow:hidden;transition:transform .2s,border-color .2s}
a.gift:hover{transform:translateY(-6px);border-color:var(--rose)}
a.gift::before{content:"";position:absolute;inset:0 auto 0 50%;width:26px;margin-left:-13px;background:rgba(232,69,107,.28)}
a.gift::after{content:"";position:absolute;left:0;right:0;top:46%;height:26px;background:rgba(232,69,107,.28)}
.gift .icon,.gift .name{position:relative;z-index:1}
.icon{font-size:3.4rem;filter:drop-shadow(0 6px 14px rgba(0,0,0,.4))}
.name{font-size:1.5rem;font-weight:700;background:var(--bg);padding:.25rem 1.1rem;border-radius:999px}
.panel{margin:2.5rem auto 0;width:min(640px,100%);text-align:center;background:linear-gradient(160deg,var(--card),#35112a);
 border:1px solid rgba(247,198,210,.18);border-radius:28px;padding:2rem 1.5rem}
.panel h2{font-family:'Aref Ruqaa','Amiri',serif;font-size:2.2rem;color:var(--blush);margin-bottom:1.25rem;padding:0}
.panel img{width:100%;max-width:420px;height:auto;border-radius:18px;display:block;margin:0 auto}
.panel .msg{font-size:1.15rem;line-height:2.1;text-align:right}
.back-wrap{text-align:center}
a.back{margin-top:1.75rem;display:inline-block;padding:.7rem 1.6rem;border-radius:999px;background:var(--rose);
 color:#fff !important;text-decoration:none !important;font-weight:700;font-size:1.05rem}
a.back:hover{background:#f2607f}
"""


def qr_data_uri() -> str:
    """يرسم الباركود SVG ويرجعه كصورة مضمّنة (data URI)."""
    n, b = len(QR_ROWS), 4
    out = []
    for r, row in enumerate(QR_ROWS):
        for c, v in enumerate(row):
            if v != "1":
                continue
            x, y = c + b, r + b
            if (r < 7 and (c < 7 or c >= n - 7)) or (r >= n - 7 and c < 7):
                out.append(f'<rect x="{x}" y="{y}" width="1" height="1"/>')
            else:
                out.append(f'<circle cx="{x + .5}" cy="{y + .5}" r=".46"/>')
    size = n + 2 * b
    svg = (
        f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{size}" height="{size}" fill="#fff"/>'
        f'<g fill="{QR_COLOR}">' + "".join(out) + "</g></svg>"
    )
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def render(body: str):
    # ملاحظة: الـ HTML بدون مسافات بادئة وبدون أسطر فارغة حتى لا يفسّره Markdown ككود
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
    st.markdown(
        f'<div class="site-title">{html.escape(SITE_TITLE)}</div>{body}',
        unsafe_allow_html=True,
    )


BACK = '<div class="back-wrap"><a class="back" href="?" target="_self">الرجوع للهدايا</a></div>'

gift = st.query_params.get("gift")

if gift == "1":
    render(
        '<div class="panel"><h2>الهدية الأولى</h2>'
        f'<img src="{qr_data_uri()}" alt="باركود على شكل قلب"></div>' + BACK
    )
elif gift == "2":
    msg = html.escape(GREETING_TEXT).replace("\n", "<br>")
    render(
        f'<div class="panel"><h2>{html.escape(GREETING_TITLE)}</h2>'
        f'<p class="msg">{msg}</p></div>' + BACK
    )
else:
    render(
        '<p class="sub">اختار هديتك</p><div class="gifts">'
        '<a class="gift" href="?gift=1" target="_self"><span class="icon">🎁</span><span class="name">الهدية الأولى</span></a>'
        '<a class="gift" href="?gift=2" target="_self"><span class="icon">🎁</span><span class="name">الهدية الثانية</span></a>'
        "</div>"
    )
