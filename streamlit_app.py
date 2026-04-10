import streamlit as st  # <--- هذا السطر كان ناقصاً
import streamlit.components.v1 as components

def main():
    st.title("تطبيق الفيزياء الحديثة التفاعلي")
    
    # قراءة ملف HTML
    with open("app.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # عرض ملف HTML داخل التطبيق
    components.html(html_code, height=1000, scrolling=True)

if __name__ == "__main__":
    main()