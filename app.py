import streamlit as st
import pyperclip

# Names and initial numbers
names_numbers = {
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

def app():
    st.title('Name and Number Manager')

    # Display names and numbers
    for name, number in names_numbers.items():
        st.write(f'{name} {number}')

    # Button to increment numbers
    if st.button('Add 1 to all numbers'):
        for name in names_numbers:
            names_numbers[name] += 1
        st.experimental_rerun()

    # Button to copy all entries
    if st.button('Copy all entries'):
        formatted_text = '\n'.join([f'{name} {number}' for name, number in names_numbers.items()])
        pyperclip.copy(formatted_text)
        st.success('Copied to clipboard!')

if __name__ == '__main__':
    app()
