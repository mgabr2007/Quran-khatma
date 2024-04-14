import streamlit as st
from datetime import datetime, timedelta
import locale

# Attempting to set the locale for Arabic - this might not work if the locale isn't installed on your system
try:
    locale.setlocale(locale.LC_ALL, 'ar_SA.utf8')
except:
    st.error("Failed to set locale: Arabic locale may not be installed on your system.")

# Start date from which Thursdays are counted
start_date = datetime(2020, 10, 22)

# Names and initial numbers
initial_numbers = {
    "عمو أحمد": 28,
    "طنط سوسو": 1,
    "سارة": 2,
    "ابراهيم": 3,
    "مصطفى": 4,
    "طنط عايدة": 5,
    "محمد حليم": 6,
    "أحمد حليم": 7,
    "محمود حليم": 8,
    "طنط عفاف": 9,
    "عمرو": 10,
    "مي": 11,
    "طنط ناني": 12,
    "عمو عبد الله": 13,
    "أحمد عبدالله": 14,
    "يارا": 15,
    "أحمد الهاجد": 16,
    "رباب": 17,
    "خالو عماد": 18,
    "طنط سامية": 19,
    "محمود عماد": 20,
    "شروق": 21,
    "طنط هناء": 22,
    "غادة": 23,
    "مصطفى على": 24,
    "طنط سحر": 25,
    "ميار": 26,
    "مروة": 27,
    "محمد عرفة": 28,
    "منى": 29
}

# Mapping Arabic to Hindi numerals
arabic_to_hindi = {
    '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
    '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'
}

def convert_to_hindi(number):
    return ''.join(arabic_to_hindi[digit] for digit in str(number))

def format_date_in_arabic(date):
    arabic_months = {
        1: 'يناير', 2: 'فبراير', 3: 'مارس', 4: 'أبريل', 5: 'مايو', 6: 'يونيو',
        7: 'يوليو', 8: 'أغسطس', 9: 'سبتمبر', 10: 'أكتوبر', 11: 'نوفمبر', 12: 'ديسمبر'
    }
    day = convert_to_hindi(date.day)
    month = arabic_months[date.month]
    year = convert_to_hindi(date.year)
    return f"{day} {month} {year}"

def app():
    st.title('ختمة القرآن لآل جبر')

    today = datetime.today().date()
    arabic_date = format_date_in_arabic(today)
    delta_days = (today - start_date.date()).days
    thursday_count = delta_days // 7

    # Display today's date and the number of weeks added in Arabic using Markdown for right alignment
    st.markdown(f"#### تاريخ اليوم: {arabic_date}", unsafe_allow_html=True)
    st.markdown(f"#### عدد الختمات منذ 22 أكتوبر 2020: {convert_to_hindi(thursday_count)}", unsafe_allow_html=True)

    # Increment the initial numbers by the number of past Thursdays
    updated_numbers = {name: (number + thursday_count) % 30 + 1 for name, number in initial_numbers.items()}

    # Display names and numbers right-aligned using Markdown
    for name, number in updated_numbers.items():
        hindi_number = convert_to_hindi(number)
        st.markdown(f"<p style='text-align: right;'>{name} {hindi_number}</p>", unsafe_allow_html=True)

    # Button to copy all entries
    if st.button('نسخ كل الإدخالات'):
        formatted_text = '\\n'.join([f"{name} {convert_to_hindi(updated_numbers[name])}" for name in updated_numbers])
        st.text_area('انسخ من هنا:', formatted_text, height=250)

if __name__ == '__main__':
    app()
