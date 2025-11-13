import streamlit as st

# --- Διαμόρφωση Σελίδας ---
st.set_page_config(page_title="Gym-Bot: LEVEL UP!", page_icon="🏆")

# --- SIDEBAR: Λογότυπο & Πληροφορίες ---
with st.sidebar:
    logo_url = "https://raw.githubusercontent.com/GiorgosBouh/test_sub8/main/logo1.png"
    st.image(logo_url, width=150)
    
    st.divider() # Διακριτική διαχωριστική γραμμή

    # 2. Κείμενο Αναφοράς και Άδειας
    st.caption(
        "Αυτή η εφαρμογή (application) αναπτύχθηκε τον Νοέμβριο του 2025 στα πλαίσια της επιμόρφωσης "
        "από τον **Γεώργιο Μπουχουρά**."
    )
    st.caption(
        "Μπορεί να χρησιμοποιηθεί ελεύθερα για τους σκοπούς που αναφέρονται "
        "από όλους τους εκπαιδευτικούς."
    )
    st.caption("Άδεια Χρήσης: [Creative Commons CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)")

# --- ΑΡΧΙΚΟΠΟΙΗΣΗ "ΜΝΗΜΗΣ" (Session State) ---
# Αυτό είναι το κλειδί. Για να "θυμάται" η εφαρμογή τις ενέργειες.
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False
if 'plan_text' not in st.session_state:
    st.session_state.plan_text = ""
if 'goal' not in st.session_state:
    st.session_state.goal = ""

# --- ΚΥΡΙΑ ΕΦΑΡΜΟΓΗ ---
st.title("🏆 Gym-Bot: LEVEL UP!")
st.write(f"Γεια, future athlete! Είμαι ο Gym-Bot 🤖")
st.write("Έτοιμος να δούμε τα stats σου; Φέρε το **'Φύλλο Αποστολής' (Mission Log)** από την αυλή και πάμε!")

# --- 1. ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ (C) ---
st.header("📋 Mission 1: Upload Stats")

col1, col2 = st.columns(2)
with col1:
    pushups = st.number_input("Πόσες Κάμψεις (Push-ups) έκανες;", min_value=0, step=1)
    plank = st.number_input("Πόσα δευτερόλεπτα έκανες Σανίδα (Plank);", min_value=0, step=1)
with col2:
    # Πιο "game" επιλογές
    feeling_pushups = st.selectbox(
        "Difficulty Level (Κάμψεις);",
        ["", "Easy Peasy", "Challenging", "Hard Mode", "Boss Level!"]
    )
    feeling_plank = st.selectbox(
        "Difficulty Level (Σανίδα);",
        ["", "Easy Peasy", "Challenging", "Hard Mode", "Boss Level!"]
    )

# --- 2. ΚΟΥΜΠΙ ΑΝΑΛΥΣΗΣ ---
if st.button("🚀 Analyze My Stats!"):
    if not feeling_pushups or not feeling_plank or feeling_pushups == "" or feeling_plank == "":
        st.warning("Whoops! Πρέπει να συμπληρώσεις *όλα* τα stats σου για να συνεχίσεις!")
        st.session_state.analysis_done = False
    else:
        st.session_state.analysis_done = True
        
        # Υπολογισμός "Score" για τις μπάρες προόδου
        # (Αυθαίρετες τιμές για να φαίνονται ωραία - π.χ. 20 κάμψεις = 100%)
        pushup_score = min(int((pushups / 20.0) * 100), 100) 
        # (π.χ. 60 δευτ. σανίδα = 100%)
        plank_score = min(int((plank / 60.0) * 100), 100)
        
        analysis_texts = []
        if feeling_pushups == "Boss Level!" or pushups < 10:
            analysis_texts.append(("info", "💪 **STR (Strength):** Καλή προσπάθεια! Οι κάμψεις ήταν 'Hard Mode'. Αυτό είναι το skill που θα 'farm-άρεις' (βελτιώσεις)! +10 XP για την προσπάθεια!"))
        else:
            analysis_texts.append(("success", "💪 **STR (Strength):** Nice! Έχεις ήδη καλό skill στη Δύναμη. Έτοιμος για το επόμενο level!"))

        if feeling_plank == "Boss Level!" or plank < 20:
            analysis_texts.append(("info", "🧘 **CORE (Πυρήνας):** Η σανίδα ήταν 'Boss Level'! Ο πυρήνας (κοιλιά/ράχη) είναι η βάση σου. Χρειάζεται training!"))
        else:
            analysis_texts.append(("success", "🧘 **CORE (Πυρήνας):** Solid! Ο πυρήνας σου είναι 'tank'! Πολύ καλό stat!"))
        
        st.session_state.analysis_output = analysis_texts
        st.session_state.pushup_score = pushup_score
        st.session_state.plank_score = plank_score
        st.session_state.goal = ""
        st.session_state.plan_text = ""

# --- 3. ΕΜΦΑΝΙΣΗ ΑΝΑΛΥΣΗΣ ΚΑΙ ΣΤΟΧΩΝ ---
if st.session_state.analysis_done:
    st.header("📊 Your Stats Debrief")
    
    # Οι "Game-like" Μπάρες Προόδου
    st.write("Skill Δύναμης (STR):")
    st.progress(st.session_state.pushup_score)
    
    st.write("Skill Πυρήνα (CORE):")
    st.progress(st.session_state.plank_score)
    
    # Εμφάνιση μηνυμάτων (info/success)
    for msg_type, text in st.session_state.analysis_output:
        if msg_type == "info":
            st.info(text)
        else:
            st.success(text)

    st.header("🎯 Mission 2: Set Your Quest")
    st.write("Τώρα που είδες τα stats, γράψε τη νέα σου αποστολή (Quest)!")
    
    goal_input = st.text_area("Γράψε το Quest σου (π.χ. 'Level up στις κάμψεις, να κάνω 3 παραπάνω')", key="goal_text_area")

    if st.button("📜 Lock-in Quest!"):
        if not goal_input:
            st.warning("Πρέπει να γράψεις το Quest σου πρώτα!")
            st.session_state.plan_text = ""
        else:
            st.session_state.goal = goal_input
            st.balloons()
            st.success(f"Quest Acquired: '{st.session_state.goal}'! Λαμβάνεις το Training Scroll σου!")
            
            plan_text = f"## 📜 Training Scroll 📜\n\n"
            plan_text += f"**Quest:** {st.session_state.goal}\n\n"
            
            # Δημιουργία πλάνου
            if "κάμψεις" in st.session_state.goal.lower() or "pushups" in st.session_state.goal.lower():
                plan_text += "Για να πετύχεις αυτό το Quest, προτείνω αυτό το **Training Plan**:\n"
                plan_text += "1. 🗓️ **Συχνότητα:** 3 φορές την εβδομάδα (π.χ. Δευτέρα-Τετάρτη-Παρασκευή).\n"
                plan_text += "2. 🏋️ **Sets:** 3 σετ κάμψεις (μπορείς να βάζεις τα γόνατα κάτω αν κουράζεσαι).\n"
                plan_text += "3. 📈 **Reps (Επαναλήψεις):** Σε κάθε σετ, κάνε όσες μπορείς! Προσπάθησε την επόμενη φορά να κάνεις +1!"
                
            elif "σανίδα" in st.session_state.goal.lower() or "plank" in st.session_state.goal.lower():
                plan_text += "Για να πετύχεις αυτό το Quest, προτείνω αυτό το **Training Plan**:\n"
                plan_text += "1. 🗓️ **Συχνότητα:** 4 φορές την εβδομάδα (ακόμα και για 1 λεπτό την ημέρα).\n"
                plan_text += "2. 🏋️ **Sets:** 3 σετ σανίδα.\n"
                plan_text += "3. 📈 **Reps (Χρόνος):** Προσπάθησε να κρατήσεις 5 δευτερόλεπτα παραπάνω σε κάθε σετ!"
                
            else:
                plan_text += "Αυτό είναι ένα Epic Quest! Για να το πετύχεις, θυμήσου τον χρυσό κανόνα:\n"
                plan_text += "1. 🗓️ **Συνέπεια:** Κάνε κάτι κάθε μέρα (π.χ. 10 λεπτά άσκηση).\n"
                plan_text += "2. 🔥 **Ένταση:** Πρέπει να λαχανιάζεις λιγάκι (να νιώθεις το 'burn'!).\n"
                plan_text += "3. 🍎 **Καλή διατροφή:** Μην ξεχνάς τα 'health potions' (φρούτα/νερό)!"
            
            st.session_state.plan_text = plan_text
            
    # Εμφάνιση του πλάνου (αν υπάρχει στη μνήμη)
    if st.session_state.plan_text:
        st.markdown(st.session_state.plan_text, unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Your Quest!",
            data=st.session_state.plan_text,
            file_name=f"My_Quest.txt" # Αλλάξαμε το όνομα αρχείου
        )