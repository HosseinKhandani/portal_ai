import streamlit as st

# تنظیمات صفحه
st.set_page_config(
    page_title="گالری اپلیکیشن‌ها",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS برای طراحی مدرن و راست‌چین با فونت B homa
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Vazir:wght@300;400;500;600;700&display=swap');

/* فونت B homa برای تمام عناصر */
* {
    font-family: 'B homa', 'Vazir', sans-serif !important;
    direction: rtl;
    text-align: right;
}

.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 3rem 2rem;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 3rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.main-header h1 {
    color: white;
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    font-family: 'B homa', sans-serif !important;
}

.main-header p {
    color: rgba(255,255,255,0.9);
    font-size: 1.2rem;
    font-weight: 400;
    font-family: 'B homa', sans-serif !important;
}

.app-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    margin: 1rem;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    border: 1px solid #f0f0f0;
    height: 350px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.app-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
}

.app-icon {
    font-size: 4rem;
    text-align: center;
    margin-bottom: 1rem;
}

.app-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 1rem;
    font-family: 'B homa', sans-serif !important;
}

.app-description {
    color: #7f8c8d;
    text-align: center;
    line-height: 1.6;
    margin-bottom: 1.5rem;
    flex-grow: 1;
    font-family: 'B homa', sans-serif !important;
}

.stats-container {
    display: flex;
    justify-content: space-between;
    gap: 2rem;
    margin: 2rem 0;
}

.stat-card {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    border-radius: 20px;
    padding: 2rem;
    color: white;
    text-align: center;
    flex: 1;
    box-shadow: 0 8px 25px rgba(240, 147, 251, 0.3);
    transition: transform 0.3s ease;
}

.stat-card:nth-child(2) {
    background: linear-gradient(135deg, #4facfe 0%, #16cad3 100%);
    box-shadow: 0 8px 25px rgba(79, 172, 254, 0.3);
}

.stat-card:nth-child(3) {
    background: linear-gradient(135deg, #3ad56f 0%, #2cd1b4 100%);
    box-shadow: 0 8px 25px rgba(67, 233, 123, 0.3);
}

.stat-card:hover {
    transform: translateY(-5px);
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    display: block;
    margin-bottom: 0.5rem;
    font-family: 'B homa', sans-serif !important;
}

.stat-label {
    font-size: 1rem;
    opacity: 0.9;
    font-family: 'B homa', sans-serif !important;
}

.footer {
    background: #2c3e50;
    color: white;
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    margin-top: 3rem;
}

.footer h3, .footer p {
    font-family: 'B homa', sans-serif !important;
}

.feature-card {
    text-align: center;
    padding: 1.5rem;
    background: white;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    margin: 0.5rem;
    transition: transform 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
}

.feature-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.feature-title {
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
    font-family: 'B homa', sans-serif !important;
}

.feature-desc {
    color: #7f8c8d;
    font-size: 0.9rem;
    font-family: 'B homa', sans-serif !important;
}

.stButton > button {
    background: linear-gradient(135deg, #e5dec7, #4bc3b8) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.8rem 2rem !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    font-family: 'B homa', sans-serif !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2980b9, #3498db) !important;
    transform: scale(1.05) !important;
    box-shadow: 0 5px 15px rgba(52, 152, 219, 0.4) !important;
}

.stButton > button:focus {
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.3) !important;
}

/* تنظیمات فونت برای عناوین Streamlit */
h1, h2, h3, h4, h5, h6 {
    font-family: 'B homa', sans-serif !important;
}

.stMarkdown {
    font-family: 'B homa', sans-serif !important;
}

/* استایل برای لینک مستقیم */
.app-link-button {
    background: linear-gradient(135deg, #e5dec7, #4bc3b8);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 0.8rem 2rem;
    font-size: 1rem;
    font-weight: 500;
    width: 100%;
    font-family: 'B homa', sans-serif;
    text-decoration: none;
    display: inline-block;
    text-align: center;
    transition: all 0.3s ease;
    cursor: pointer;
}

.app-link-button:hover {
    background: linear-gradient(135deg, #2980b9, #3498db);
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(52, 152, 219, 0.4);
    text-decoration: none;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# هدر اصلی
st.markdown("""
<div class="main-header">
    <h1>🚀 گالری اپلیکیشن‌های هوشمند</h1>
    <p>مجموعه‌ای از ابزارهای پیشرفته و کاربردی برای تسهیل کار شما</p>
</div>
""", unsafe_allow_html=True)

# آمار سریع - 3 کارت
st.markdown("""
<div class="stats-container">
    <div class="stat-card">
        <span class="stat-number">9</span>
        <span class="stat-label">اپلیکیشن فعال</span>
    </div>
    <div class="stat-card">
        <span class="stat-number">6</span>
        <span class="stat-label">دسته‌بندی اپلیکیشن‌ها</span>
    </div>
    <div class="stat-card">
        <span class="stat-number">12,547</span>
        <span class="stat-label">کل درخواست‌ها</span>
    </div>
</div>
""", unsafe_allow_html=True)

# تعریف اپلیکیشن‌ها با عناوین و آیکون‌های جدید
apps = [
    {
        "icon": "🛰️",
        "title": "اپلیکیشن پردازش تصاویر ماهواره‌ای",
        "description": "پردازش و تحلیل تصاویر ماهواره‌ای با الگوریتم‌های پیشرفته هوش مصنوعی",
        "url": "https://019ef348-f229-effa-4012-40d943da9497.share.connect.posit.cloud/"
        #"url": "https://01975364-aa50-a99d-e2e6-741fe3760f53.share.connect.posit.cloud/"
    },
    {
        "icon": "📊",
        "title": "اپلیکیشن تحلیل صورت‌های مالی",
        "description": "تجزیه و تحلیل دقیق صورت‌های مالی و ارائه گزارش‌های تخصصی",
        "url": "https://01994c5f-cc2c-e454-6403-ee38942cf7a0.share.connect.posit.cloud/"
    },

     {
        "icon": "🧠",
        "title": "دستیار هوشمند قوانین و مقررات براساس فایل ورودی کاربر (RAG)",
        "description": "در این اپ کاربر روی فایل بارگذاری دلخواه خود میتواند پرسجو نمایید",
        "url": "https://01a015a6-d468-a9d3-fbb9-747ca9afb8ad.share.connect.posit.cloud/"
    },
    {
        "icon": "🛰️",
        "title": "حکمرانی و پایش منابع آب کشور",
        "description": "این ابزار پلتفرمی است برای پایش کیفیت و کودورت منابع آبی کشور",
        "url": "https://019ef348-f229-effa-4012-40d943da9497.share.connect.posit.cloud/"
    },
    
    {
        "icon": "🔍",
        "title": "اپلیکیشن Fact Checking اخبار",
        "description": "بررسی صحت اخبار و اطلاعات با استفاده از منابع معتبر و هوش مصنوعی",
        "url": "https://01992d7f-1978-2284-c6b6-83e751bd53c5.share.connect.posit.cloud/"
    },
      {
        "icon": "🛡️",
        "title": "اپ تحلیل اقتصادی بازارها",
        "description": "نظارت و تحلیل شاخص‌های امنیت اقتصادی و هشدارهای زودهنگام",
        "url": "https://01996c31-3ac8-5920-f955-b69e53a8c599.share.connect.posit.cloud/"
    },
    #{
    #    "icon": "🏠",
    #    "title": "اپ پیش‌بینی بازار خودرو/مسکن",
    #    "description": "پیش‌بینی قیمت و روند بازار املاک و خودرو با تحلیل داده‌های بازار",
    #    "url": "https://01948d8d-6555-1d15-da1b-0c4f51fa267d.share.connect.posit.cloud/"
    #},
 #   {
 #       "icon": "⚖️",
 #       "title": "تست - دستیار بررسی و تطابق سنجی رزومه های فها",
 #       "description": "مشاوره حقوقی هوشمند و جستجو در قوانین و مقررات",
 #       "url": "https://0199ba83-50df-1a06-c7cd-13893ecd791b.share.connect.posit.cloud/"
 #   }
]

# نمایش اپلیکیشن‌ها در شبکه
st.markdown("## 🎯 اپلیکیشن‌های موجود")

# ایجاد ردیف‌های کارت‌ها
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(apps):
            app = apps[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="app-card">
                    <div class="app-icon">{app['icon']}</div>
                    <div class="app-title">{app['title']}</div>
                    <div class="app-description">{app['description']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # روش 1: استفاده از لینک HTML مستقیم (بهترین روش)
                if app['url'] != "#":
                    st.markdown(f"""
                    <a href="{app['url']}" target="_blank" class="app-link-button">
                        🚀 ورود به سامانه
                    </a>
                    """, unsafe_allow_html=True)
                else:
                    # روش 2: استفاده از دکمه Streamlit با JavaScript برای اپ‌های غیرفعال
                    button_key = f"app_button_{i}_{j}"
                    if st.button("⏳ به زودی در دسترس", key=button_key, use_container_width=True, disabled=True):
                        st.info("⏳ این اپلیکیشن به زودی در دسترس خواهد بود!")

# بخش ویژگی‌ها
st.markdown("---")
st.markdown("## ✨ ویژگی‌های برجسته")

feature_cols = st.columns(4)
features = [
    {"icon": "⚡", "title": "دقت بالا", "desc": "دقت بالا و سرعت مناسب"},
    {"icon": "🔒", "title": "ایمن", "desc": "ایمن"},
    {"icon": "🌐", "title": "دسترسی آسان", "desc": "در همه جا قابل استفاده"},
    {"icon": "📱", "title": "واکنش‌گرا", "desc": "سازگار با تمام دستگاه‌ها"}
]

for i, feature in enumerate(features):
    with feature_cols[i]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{feature['icon']}</div>
            <div class="feature-title">{feature['title']}</div>
            <div class="feature-desc">{feature['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# فوتر
st.markdown("""
<div class="footer">
    <h3>📞 تماس با ما</h3>
    <p>برای پشتیبانی و راهنمایی با ما در تماس باشید</p>
    <p>📧 support@example.com | 📱 ۰۹۱۲۱۱۱۱۱۱۱</p>
    <p style="margin-top: 1rem; opacity: 0.8;">© ۱۴۰۴ - تمامی حقوق محفوظ است</p>
</div>
""", unsafe_allow_html=True)
















