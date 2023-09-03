import streamlit as st

st.header('st.button use')
if "count" not in st.session_state :
    st.session_state["count"] = 0
if st.button('Say hello'):
    st.session_state["count"] += 1
    print(f"button clicked {st.session_state.count} times")
    if st.session_state.count%2 == 1 :
        st.write('Why hello there')
    else:
        st.write('Bye')
        st.button('Say bye')
else:
     st.write('Goodbye')