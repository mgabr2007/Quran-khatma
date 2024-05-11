import streamlit as st
from datetime import datetime, timedelta

# Arabic month names
arabic_months = {
    1: 'يناير', 2: 'فبراير', 3: 'مارس', 4: 'أبريل',
    5: 'مايو', 6: 'يونيو', 7: 'يوليو', 8: 'أغسطس',
    9: 'سبتمبر', 10: 'أكتوبر', 11: 'نوفمبر', 12: 'ديسمبر'
}

# Mapping Arabic to Hindi numerals
arabic_to_hindi = {
    '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
    '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'
}

def convert_to_hindi(number):
    return ''.join(arabic_to_hindi[digit] for digit in str(number))

def format_date_in_arabic(date):
    day = convert_to_hindi(date.day)
    month = arabic_months[date.month]
    year = convert_to_hindi(date.year)
    return f"{day} {month} {year}"

def find_last_thursday(date):
    weekday = date.weekday()
    # If today is Thursday (3) or later, go back to the most recent Thursday
    if weekday >= 3:
        last_thursday = date - timedelta(days=weekday - 3)
    else:
        last_thursday = date - timedelta(days=weekday + 4)
    return last_thursday

def app():
    st.title('ختمة القرآن لآل جبر')

    today = datetime.today().date()
    last_thursday = find_last_thursday(today)
    arabic_date = format_date_in_arabic(today)
    start_date = datetime(2020, 10, 22).date()
    delta_days = (last_thursday - start_date).days
    thursday_count = delta_days // 7

    # Weekly messages to be displayed every Thursday
    weekly_messages = [
        "اللهم زين بالقرآن أخلاقي، واغسل به درن قلبي، واجعله حجة لي لا علي.",
        "همة يا صاحب القمة، من يكن القرآن همّه كفاه الله باقي همه.",
        "همة يا صاحب القمة، من يكن القرآن همّه كفاه الله باقي همه.",
        # Add more messages as needed
    ]
    # Select message based on the number of Thursdays since the start date
    weekly_message = weekly_messages[thursday_count % len(weekly_messages)]

    st.markdown(f"#### تاريخ اليوم: {arabic_date}", unsafe_allow_html=True)
    st.markdown(f"#### عدد الختمات منذ ٢٢ أكتوبر ٢٠٢٠: {convert_to_hindi(thursday_count)}", unsafe_allow_html=True)
    st.markdown(f"#### رسالة الأسبوع: {weekly_message}", unsafe_allow_html=True)

    # Names and initial numbers
    initial_numbers = {
        "عمو أحمد": 28, "طنط سوسو": 29, "سارة": 30, "ابراهيم": 1, "مصطفى": 2,
        "طنط عايدة": 3, "محمد حليم": 4, "أحمد حليم": 5, "محمود حليم": 6, "طنط عفاف": 7,
        "عمرو": 8, "مي": 9, "طنط ناني": 10, "عمو عبد الله": 11, "أحمد عبدالله": 12,
        "يارا": 13, "أحمد الهاجد": 14, "رباب": 15, "خالو عماد": 16, "طنط سامية": 17,
        "محمود عماد": 18, "شروق": 19, "طنط هناء": 20, "غادة": 21, "مصطفى على": 22,
        "طنط سحر": 23, "ميار": 24, "مروة": 25, "محمد عرفة": 26, "منى": 27
    }

    # Increment the initial numbers by the number of past Thursdays
    updated_numbers = {name: (number + thursday_count) % 30 + 1 for name, number in initial_numbers.items()}

    # Display names and numbers right-aligned using Markdown
    for name, number in updated_numbers.items():
        hindi_number = convert_to_hindi(number)
        st.markdown(f"<p style='text-align: right;'>{name} {hindi_number}</p>", unsafe_allow_html=True)

    # Button to copy all entries
    if st.button('نسخ كل الإدخالات'):
        formatted_text = '\n'.join([f"{name} {convert_to_hindi(updated_numbers[name])}" for name in updated_numbers])
        st.text_area('انسخ من هنا:', formatted_text, height=250)

if __name__ == '__main__':
    app()
