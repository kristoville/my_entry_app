import streamlit as st
import functions
import os

if not os.path.exists("xmas.txt"):
    with open("xmas.txt", "w") as oge:
        pass

entries = functions.get_reading()
# st.set_page_config(layout='wide')


def add_entry():
    enter = st.session_state['new_entry'] + "\n"
    entries.append(enter)
    functions.get_writing(entries)


st.title('Young Avbenake web app')
st.subheader('Some Christmas wishes from us')
st.write('Lets act like kids again and make christmas wishes below,'
         ' who knows; a Father christmas might be watching '
         'and passing by.'
         ' <b>Make your entries below. You can enter more than one, '
         'and can click to delete</b>',
         unsafe_allow_html=True)                    # to allow for html format

st.text_input(label="Enter Christmas wishes for yourself",
              placeholder="Add a wish...", on_change=add_entry,
              key='new_entry')

for index, entry in enumerate(entries):
    checked = st.checkbox(entry, key=entry)
    if checked:
        entries.pop(index)
        functions.get_writing(entries)
        del st.session_state[entry]
        st.experimental_rerun()

print('yes oh')
# st.session_state
