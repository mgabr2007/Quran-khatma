import streamlit as st
from datetime import datetime, timedelta

# Start date from which Thursdays are counted
start_date = datetime(2024, 4, 11)

# Names and initial numbers
initial_numbers = {
    "عمو أحمد": 30,
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

def app():
    st.title('Name and Number Manager')

    today = datetime.today().date()
    delta_days = (today - start_date.date()).days
    thursday_count = delta_days // 7

    # Display today's date and the number of weeks added
    st.write(f"Today's Date: {today.strftime('%B %d, %Y')}")
    st.write(f"Weeks since April 11, 2024: {thursday_count}")

    # Increment the initial numbers by the number of past Thursdays
    updated_numbers = {name: (number + thursday_count - 1) % 30 + 1 for name, number in initial_numbers.items()}

    # Display names and numbers
    for name, number in updated_numbers.items():
        hindi_number = convert_to_hindi(number)
        st.write(f'{name} {hindi_number}')

    # Button to copy all entries
    if st.button('Copy all entries'):
        formatted_text = '\n'.join([f"{name} {convert_to_hindi(updated_numbers[name])}" for name in updated_numbers])
        st.text_area('Copy from here:', formatted_text, height=250)

if __name__ == '__main__':
    app()
