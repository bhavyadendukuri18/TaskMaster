import streamlit as st
import functions

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="TaskMaster",
    page_icon="✅",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.main{
    background-color:#f5f7fa;
}

h1{
    color:#2E86C1;
}

.stButton>button{
    background-color:#2E86C1;
    color:white;
    border-radius:8px;
}

div[data-testid="stSidebar"]{
    background-color:#EAF2F8;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Read Todos ----------------
todos = functions.get_todos()

# ---------------- Add Function ----------------
def add_todo():
    todo = st.session_state["new_todo"].strip()

    if todo != "":
        todos.append(todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

# ---------------- Sidebar ----------------
with st.sidebar:

    st.title("📌 TaskMaster")

    st.write("### Productivity Dashboard")

    st.metric("Pending Tasks", len(todos))

    st.write("---")

    st.write("""
### Tips

✔ Finish difficult tasks first

✔ Keep tasks short

✔ Complete one task at a time

✔ Stay consistent
""")

# ---------------- Header ----------------
st.title("✅ TaskMaster")
st.subheader("Organize your day efficiently")

st.write("""
Welcome to **TaskMaster**.

Manage your daily work, stay organized,
and increase your productivity.
""")

st.write("---")

# ---------------- Input ----------------
st.text_input(
    "Add New Task",
    placeholder="Enter a new task...",
    key="new_todo",
    on_change=add_todo
)

st.write("## 📋 Your Tasks")

# ---------------- Display Todos ----------------
if len(todos) == 0:
    st.info("🎉 No pending tasks. Add one above!")
else:

    for index, todo in enumerate(todos):

        if st.checkbox(todo.strip(), key=todo):

            todos.pop(index)
            functions.write_todos(todos)

            del st.session_state[todo]

            st.rerun()

# ---------------- Footer ----------------
st.write("---")

st.caption("Made with ❤️ using Python & Streamlit")