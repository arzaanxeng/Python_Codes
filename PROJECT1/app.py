import json
import re
from pathlib import Path
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="School Management",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Data layer ────────────────────────────────────────────────────────────────

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "school_data.json"


def load_data():
    if Path(DATABASE).exists():
        content = Path(DATABASE).read_text()
        if content.strip():
            return json.loads(content)
    return {"students": [], "teachers": []}

def save_data(data):
    Path(DATABASE).write_text(json.dumps(data, indent=4))

def validate_email(email):
    return bool(re.match(r"[a-zA-Z0-9]+@[a-zA-Z]+\.com", email))

if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data

# ── Styles ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Background */
.stApp {
    background: #0f1117;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #161b27 !important;
    border-right: 1px solid #1e2a3a;
}
section[data-testid="stSidebar"] * { color: #c9d1e0 !important; }
section[data-testid="stSidebar"] .stRadio label { font-size: 0.92rem; }

/* Title banner */
.banner {
    background: linear-gradient(135deg, #1a2744 0%, #0d1b35 60%, #162038 100%);
    border: 1px solid #1e3a5f;
    border-radius: 16px;
    padding: 32px 36px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 20px;
}
.banner-icon { font-size: 3rem; line-height: 1; }
.banner-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #e8edf5;
    margin: 0;
    letter-spacing: -0.5px;
}
.banner-sub { font-size: 0.88rem; color: #6b8aac; margin-top: 4px; }

/* Cards */
.card {
    background: #161b27;
    border: 1px solid #1e2a3a;
    border-radius: 12px;
    padding: 22px 24px;
    margin-bottom: 14px;
    transition: border-color .2s;
}
.card:hover { border-color: #3a7bd5; }
.card-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.05rem;
    font-weight: 600;
    color: #e8edf5;
}
.card-meta { font-size: 0.82rem; color: #6b8aac; margin-top: 4px; }
.badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-right: 6px;
}
.badge-student { background: #1a3a5c; color: #60a5fa; }
.badge-teacher { background: #1e3320; color: #4ade80; }
.grade-chip {
    display: inline-block;
    background: #1e2a3a;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.8rem;
    color: #93c5fd;
    margin: 2px 3px;
}

/* Stat boxes */
.stat-row { display: flex; gap: 14px; margin-bottom: 28px; }
.stat-box {
    flex: 1;
    background: #161b27;
    border: 1px solid #1e2a3a;
    border-radius: 12px;
    padding: 20px 22px;
    text-align: center;
}
.stat-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #3a7bd5;
}
.stat-label { font-size: 0.78rem; color: #6b8aac; margin-top: 2px; }

/* Section heading */
.sec-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: #adbdd0;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 24px 0 14px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.sec-heading::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1e2a3a;
}

/* Input overrides */
.stTextInput input, .stSelectbox select {
    background: #1e2a3a !important;
    border: 1px solid #2a3a50 !important;
    border-radius: 8px !important;
    color: #e8edf5 !important;
}
.stTextInput label, .stSelectbox label, .stNumberInput label {
    color: #6b8aac !important;
    font-size: 0.85rem !important;
}

/* Button */
.stButton > button {
    background: #3a7bd5 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.4rem !important;
    transition: background .2s !important;
}
.stButton > button:hover { background: #2563b0 !important; }

/* Success / error */
.stSuccess, .stError { border-radius: 8px !important; }

div[data-testid="stNotification"] { border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar nav ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:18px 0 10px;'>
        <span style='font-family:Space Grotesk;font-size:1.25rem;font-weight:700;color:#e8edf5;'>
            🎓 School Admin
        </span>
        <div style='font-size:0.75rem;color:#4a6080;margin-top:4px;'>Management Portal</div>
    </div>
    <hr style='border-color:#1e2a3a;margin:10px 0 20px;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["Dashboard", "Students", "Teachers"],
        label_visibility="collapsed",
    )

# ── Banner ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="banner">
    <div class="banner-icon">🎓</div>
    <div>
        <div class="banner-title">School Management System</div>
        <div class="banner-sub">Register students & teachers · Assign grades · View records</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════
# PAGE: DASHBOARD
# ═════════════════════════════════════════════════════════════
if page == "Dashboard":
    n_students = len(data["students"])
    n_teachers = len(data["teachers"])

    # compute avg grade across all students
    all_avgs = []
    for s in data["students"]:
        g = s.get("grades", {})
        if g:
            try:
                vals = [float(v) for v in g.values()]
                all_avgs.append(sum(vals) / len(vals))
            except:
                pass
    overall_avg = f"{sum(all_avgs)/len(all_avgs):.1f}" if all_avgs else "—"

    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-box">
            <div class="stat-num">{n_students}</div>
            <div class="stat-label">Students Enrolled</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">{n_teachers}</div>
            <div class="stat-label">Teachers Registered</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">{overall_avg}</div>
            <div class="stat-label">Overall Average Score</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="sec-heading">Recent Students</div>', unsafe_allow_html=True)
        if not data["students"]:
            st.info("No students yet. Register one from the Students tab.")
        for s in data["students"][-5:][::-1]:
            grades = s.get("grades", {})
            try:
                avg = f"{sum(float(v) for v in grades.values())/len(grades):.1f}" if grades else "—"
            except:
                avg = "—"
            chips = "".join(f'<span class="grade-chip">{sub}: {m}</span>' for sub, m in grades.items())
            st.markdown(f"""
            <div class="card">
                <span class="badge badge-student">Student</span>
                <span class="card-name">{s['name']}</span>
                <div class="card-meta">Roll #{s['roll_no']} · Age {s['age']} · Avg: <b>{avg}</b></div>
                <div style="margin-top:8px">{chips if chips else '<span style="color:#4a6080;font-size:0.8rem">No grades yet</span>'}</div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="sec-heading">Recent Teachers</div>', unsafe_allow_html=True)
        if not data["teachers"]:
            st.info("No teachers yet. Register one from the Teachers tab.")
        for t in data["teachers"][-5:][::-1]:
            st.markdown(f"""
            <div class="card">
                <span class="badge badge-teacher">Teacher</span>
                <span class="card-name">{t['name']}</span>
                <div class="card-meta">Emp #{t['emp_id']} · {t['subject']}</div>
                <div class="card-meta" style="margin-top:4px"> {t['email']}</div>
            </div>
            """, unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════
# PAGE: STUDENTS
# ═════════════════════════════════════════════════════════════
elif page == "Students":
    tab1, tab2, tab3 = st.tabs(["Register", "Add Grades", "View Records"])

    # ── Register ──
    with tab1:
        st.markdown('<div class="sec-heading">Register a Student</div>', unsafe_allow_html=True)
        with st.form("reg_student", clear_on_submit=True):
            c1, c2 = st.columns(2)
            name     = c1.text_input("Full Name")
            age      = c2.text_input("Age")
            email    = c1.text_input("Email")
            roll_no  = c2.text_input("Roll Number")
            submitted = st.form_submit_button("Register Student", use_container_width=True)

        if submitted:
            if not all([name, age, email, roll_no]):
                st.error("All fields are required.")
            elif not validate_email(email):
                st.error("Invalid email address.")
            elif any(s["roll_no"] == roll_no for s in data["students"]):
                st.warning(f"Roll no {roll_no} already registered.")
            else:
                data["students"].append({
                    "roll_no": roll_no, "name": name,
                    "age": age, "email": email, "grades": {}
                })
                save_data(data)
                st.session_state.data = data
                st.success(f" {name} registered successfully!")

    # ── Add Grades ──
    with tab2:
        st.markdown('<div class="sec-heading">Assign Grades</div>', unsafe_allow_html=True)
        if not data["students"]:
            st.info("No students registered yet.")
        else:
            options = {f"{s['name']} (#{s['roll_no']})": s["roll_no"] for s in data["students"]}
            chosen_label = st.selectbox("Select Student", list(options.keys()))
            roll_no = options[chosen_label]

            with st.form("add_grade", clear_on_submit=True):
                c1, c2 = st.columns(2)
                subject = c1.text_input("Subject")
                marks   = c2.text_input("Marks")
                submitted = st.form_submit_button("Save Grade", use_container_width=True)

            if submitted:
                if not subject or not marks:
                    st.error("Both subject and marks are required.")
                else:
                    for s in data["students"]:
                        if s["roll_no"] == roll_no:
                            s["grades"][subject] = marks
                            save_data(data)
                            st.session_state.data = data
                            st.success(f" {subject}: {marks} saved for {s['name']}.")
                            break

    # ── View Records ──
    with tab3:
        st.markdown('<div class="sec-heading">Student Records</div>', unsafe_allow_html=True)
        search = st.text_input("Search by name or roll number", placeholder="e.g. Arzaan or 101")
        filtered = [
            s for s in data["students"]
            if search.lower() in s["name"].lower() or search in s["roll_no"]
        ] if search else data["students"]

        if not filtered:
            st.info("No matching students found.")
        for s in filtered:
            grades = s.get("grades", {})
            try:
                avg = f"{sum(float(v) for v in grades.values())/len(grades):.1f}" if grades else "—"
            except:
                avg = "—"
            chips = "".join(f'<span class="grade-chip">{sub}: {m}</span>' for sub, m in grades.items())
            st.markdown(f"""
            <div class="card">
                <div style="display:flex;justify-content:space-between;align-items:flex-start">
                    <div>
                        <span class="badge badge-student">Student</span>
                        <span class="card-name"> {s['name']}</span>
                        <div class="card-meta" style="margin-top:5px">
                            Roll #{s['roll_no']} · Age {s['age']} ·  {s['email']}
                        </div>
                    </div>
                    <div style="text-align:right">
                        <div style="font-family:Space Grotesk;font-size:1.6rem;font-weight:700;color:#3a7bd5">{avg}</div>
                        <div style="font-size:0.72rem;color:#6b8aac">avg score</div>
                    </div>
                </div>
                <div style="margin-top:10px">{chips if chips else '<span style="color:#4a6080;font-size:0.8rem">No grades assigned yet</span>'}</div>
            </div>
            """, unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════
# PAGE: TEACHERS
# ═════════════════════════════════════════════════════════════
elif page == "Teachers":
    tab1, tab2 = st.tabs(["Register", "View Records"])

    with tab1:
        st.markdown('<div class="sec-heading">Register a Teacher</div>', unsafe_allow_html=True)
        with st.form("reg_teacher", clear_on_submit=True):
            c1, c2 = st.columns(2)
            name    = c1.text_input("Full Name")
            age     = c2.text_input("Age")
            email   = c1.text_input("Email")
            subject = c2.text_input("Subject")
            emp_id  = c1.text_input("Employee ID")
            submitted = st.form_submit_button("Register Teacher", use_container_width=True)

        if submitted:
            if not all([name, age, email, subject, emp_id]):
                st.error("All fields are required.")
            elif not validate_email(email):
                st.error("Invalid email address.")
            elif any(t["emp_id"] == emp_id for t in data["teachers"]):
                st.warning(f"Employee ID {emp_id} already registered.")
            else:
                data["teachers"].append({
                    "name": name, "age": age, "email": email,
                    "subject": subject, "emp_id": emp_id
                })
                save_data(data)
                st.session_state.data = data
                st.success(f" {name} registered successfully!")

    with tab2:
        st.markdown('<div class="sec-heading">Teacher Records</div>', unsafe_allow_html=True)
        search = st.text_input("Search by name or employee ID", placeholder="e.g. Sharma or EMP001")
        filtered = [
            t for t in data["teachers"]
            if search.lower() in t["name"].lower() or search in t["emp_id"]
        ] if search else data["teachers"]

        if not filtered:
            st.info("No matching teachers found.")
        for t in filtered:
            st.markdown(f"""
            <div class="card">
                <span class="badge badge-teacher">Teacher</span>
                <span class="card-name"> {t['name']}</span>
                <div class="card-meta" style="margin-top:5px">
                    Emp #{t['emp_id']} · Age {t['age']} ·  {t['subject']}
                </div>
                <div class="card-meta" style="margin-top:3px"> {t['email']}</div>
            </div>
            """, unsafe_allow_html=True)
