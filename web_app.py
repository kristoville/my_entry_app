import streamlit as st
import functions

entries = functions.get_reading()


def add_entry():
    enter = st.session_state['new_entry'] + "\n"
    entries.append(enter)
    functions.get_writing(entries)


st.title('Avbenake first web app')
st.subheader('Its a new one actually')
st.write('This seems amazing to write and design,'
         ' pretty easy to design I did say.'
         ' Check out the entries below')

for index, entry in enumerate(entries):
    checked = st.checkbox(entry, key=entry)
    if checked:
        entries.pop(index)
        functions.get_writing(entries)
        del st.session_state[entry]
        st.experimental_rerun()

st.text_input(label="Enter a todo for yourself",
              placeholder="Add new entry...", on_change=add_entry,
              key='new_entry')

print('yes oh')
st.session_state
