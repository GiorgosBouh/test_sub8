import streamlit as st
import os

# --- Διαμόρφωση Σελίδας ---
st.set_page_config(page_title="Gym-Bot: Ανέβα Επίπεδο!", page_icon="🏆")

# --- SIDEBAR: Λογότυπο & Πληροφορίες ---
with st.sidebar:
    if os.path.exists("logo1.png"):
        st.image("logo1.png", width=150)
    else:
        # Fallback αν το αρχείο δεν βρεθεί τοπικά (αν και θα έπρεπε)
        st.image("https://raw.githubusercontent.com/GiorgosBouh/test_sub8/main/logo1.png", width=150)
        
    st.divider()
    st.caption(
        "Αυτή η εφαρμογή αναπτύχθηκε τον Νοέμβριο του 2025 στα πλαίσια της επιμόρφωσης "
        "από τον **Γεώργιο Μπουχουρά**."
    )
    st.caption(
        "Μπορεί να χρησιμοποιηθεί ελεύθερα για τους σκοπούς που αναφέρονται "
        "από όλους τους εκπαιδευτικούς."
    )
    st.caption("Άδεια Χρήσης: [Creative Commons CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)")

# --- ΑΡΧΙΚΟΠΟΙΗΣΗ "ΜΝΗΜΗΣ" (Session State) ---
if 'plan_text' not in st.session_state:
    st.session_state.plan_text = ""
if 'goal' not in st.session_state:
    st.session_state.goal = ""
if 'analysis_output' not in st.session_state:
    st.session_state.analysis_output = []
if 'scores' not in st.session_state:
    st.session_state.scores = {}
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False

# --- ΚΥΡΙΑ ΕΦΑΡΜΟΓΗ ---
st.title("🏆 Gym-Bot: Ανέβα Επίπεδο!")
st.write(f"Γεια, μελλοντικέ ήρωα! Είμαι ο Gym-Bot 🤖")

# --- Download PDF ---
pdf_file_path = "instructions.pdf"
with st.expander("❓ Έχασες το 'Φύλλο Αποστολής' σου;"):
    st.write("Κατέβασε το ξανά από εδώ για να το εκτυπώσεις.")
    try:
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📥 Κατέβασε το Φύλλο Αποστολής (PDF)",
            data=PDFbyte,
            file_name="Fyllo_Apostolis.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.error(f"ΣΦΑΛΜΑ: Δεν βρέθηκε το αρχείο '{pdf_file_path}' στο GitHub repo!")
st.divider() 

# --- 1. ΕΙΣΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ (C) ---
st.header("📋 Αποστολή 1: Καταχώρησε τα Χαρακτηριστικά σου")
st.write("Κοίτα το 'Φύλλο Αποστολής' σου και συμπλήρωσε **όλα** τα σκορ σου.")

# --- ΖΩΝΗ 1: ΔΥΝΑΜΗ ---
with st.container(border=True):
    st.subheader("🔴 ΖΩΝΗ ΔΥΝΑΜΗΣ (ΔΥΝ)")
    col1, col2, col3 = st.columns(3)
    with col1:
        pushups = st.number_input("Σκορ Κάμψεις:", min_value=0, step=1, key="s_pushups")
        feel_pushups = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_pushups")
    with col2:
        squats = st.number_input("Σκορ Καθίσματα:", min_value=0, step=1, key="s_squats")
        feel_squats = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_squats")
    with col3:
        crunches = st.number_input("Σκορ Κοιλιακοί:", min_value=0, step=1, key="s_crunches")
        feel_crunches = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_crunches")

# --- ΖΩΝΗ 2: ΠΥΡΗΝΑΣ ---
with st.container(border=True):
    st.subheader("🔵 ΖΩΝΗ ΠΥΡΗΝΑ & ΙΣΟΡΡΟΠΙΑΣ (ΠΥΡ)")
    col1, col2, col3 = st.columns(3)
    with col1:
        plank_touch = st.number_input("Σκορ 'Σανίδα-Άγγιγμα':", min_value=0, step=1, key="s_plank")
        feel_plank = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_plank")
    with col2:
        birddog = st.number_input("Σκορ 'Ραχιαίοι (Εναλλάξ)':", min_value=0, step=1, key="s_birddog")
        feel_birddog = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_birddog")
    with col3:
        balance = st.number_input("Σκορ 'Πήδημα & Πάγωμα':", min_value=0, step=1, key="s_balance")
        feel_balance = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_balance")

# --- ΖΩΝΗ 3: ΑΝΤΟΧΗ ---
with st.container(border=True):
    st.subheader("🟢 ΖΩΝΗ ΑΝΤΟΧΗΣ (ΑΝΤ)")
    col1, col2, col3 = st.columns(3)
    with col1:
        jacks = st.number_input("Σκορ 'Jumping Jacks':", min_value=0, step=1, key="s_jacks")
        feel_jacks = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_jacks")
    with col2:
        high_knees = st.number_input("Σκορ 'Γόνατα Ψηλά':", min_value=0, step=1, key="s_knees")
        feel_knees = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_knees")
    with col3:
        slalom = st.number_input("Σκορ 'Γρήγορο Σλάλομ':", min_value=0, step=1, key="s_slalom")
        feel_slalom = st.selectbox("Δυσκολία:", ["", "Εύκολο", "Μέτριο", "Δύσκολο"], key="f_slalom")


# --- 2. ΚΟΥΜΠΙ ΑΝΑΛΥΣΗΣ ---
st.divider()
if st.button("🚀 Ανάλυση Όλων των Stats!", type="primary"):
    
    # Έλεγχος αν *όλα* τα πεδία αίσθησης έχουν συμπληρωθεί
    feelings = [feel_pushups, feel_squats, feel_crunches, feel_plank, feel_birddog, feel_balance, feel_jacks, feel_knees, feel_slalom]
    if "" in feelings:
        st.warning("Whoops! Πρέπει να συμπληρώσεις το πεδίο 'Δυσκολία' **για όλες τις 9 ασκήσεις**!")
        st.session_state.analysis_done = False
    else:
        st.session_state.analysis_done = True
        
        # Υπολογισμός "Score" για κάθε Ζώνη (Μέσος όρος)
        # (Αυθαίρετοι στόχοι για 100% - π.χ. 15 κάμψεις, 20 καθίσματα κλπ)
        score_dyn = int(((pushups/15.0) + (squats/20.0) + (crunches/20.0)) / 3 * 100)
        score_pyr = int(((plank_touch/20.0) + (birddog/15.0) + (balance/10.0)) / 3 * 100)
        score_ant = int(((jacks/50.0) + (high_knees/50.0) + (slalom/5.0)) / 3 * 100)
        
        st.session_state.scores = {
            'ΔΥΝ': min(score_dyn, 100), 
            'ΠΥΡ': min(score_pyr, 100), 
            'ΑΝΤ': min(score_ant, 100)
        }
        
        analysis_texts = []
        # Λογική: Δώσε σχόλιο για κάθε ζώνη
        if score_dyn < 40:
            analysis_texts.append(("info", "💪 **ΔΥΝ (Δύναμη):** Καλή προσπάθεια! Αυτή η ζώνη ήταν πρόκληση. Είναι τέλειο σημείο για να ξεκινήσεις τη βελτίωσή σου!"))
        else:
            analysis_texts.append(("success", "💪 **ΔΥΝ (Δύναμη):** Ωραίος! Έχεις ήδη καλή ικανότητα στη Δύναμη."))

        if score_pyr < 40:
            analysis_texts.append(("info", "🧘 **ΠΥΡ (Πυρήνας):** Ο Πυρήνας (κοιλιά/ράχη) είναι η βάση σου! Το ότι σε δυσκόλεψε σημαίνει ότι βρήκαμε ακριβώς πού θα δυναμώσεις!"))
        else:
            analysis_texts.append(("success", "🧘 **ΠΥΡ (Πυρήνας):** Ατσάλινος! Ο πυρήνας σου είναι πολύ δυνατός!"))

        if score_ant < 40:
            analysis_texts.append(("info", "⚡ **ΑΝΤ (Αντοχή):** Λαχάνιασες; Η αντοχή είναι κλειδί για το παιχνίδι. Καλός στόχος για εξάσκηση!"))
        else:
            analysis_texts.append(("success", "⚡ **ΑΝΤ (Αντοχή):** Τρέχεις σαν τον άνεμο! Εξαιρετική αντοχή."))
        
        st.session_state.analysis_output = analysis_texts
        st.session_state.goal = ""
        st.session_state.plan_text = ""


# --- 3. ΕΜΦΑΝΙΣΗ ΑΝΑΛΥΣΗΣ ΚΑΙ ΣΤΟΧΩΝ ---
if st.session_state.analysis_done:
    st.header("📊 Η Αναφορά σου")
    
    st.write("Ικανότητα Δύναμης (ΔΥΝ):")
    st.progress(st.session_state.scores.get('ΔΥΝ', 0))
    st.write("Ικανότητα Πυρήνα (ΠΥΡ):")
    st.progress(st.session_state.scores.get('ΠΥΡ', 0))
    st.write("Ικανότητα Αντοχής (ΑΝΤ):")
    st.progress(st.session_state.scores.get('ΑΝΤ', 0))
    
    for msg_type, text in st.session_state.analysis_output:
        if msg_type == "info":
            st.info(text)
        else:
            st.success(text)

    st.header("🎯 Αποστολή 2: Βάλε Στόχο")
    st.write("Τώρα που είδες την ανάλυση, γράψε τη νέα σου αποστολή!")
    
    goal_input = st.text_area("Γράψε την Αποστολή σου (π.χ. 'Να ανέβω επίπεδο στη Δύναμη, +3 κάμψεις')", key="goal_text_area")

    if st.button("📜 Κλείδωμα Αποστολής!"):
        if not goal_input:
            st.warning("Πρέπει να γράψεις την Αποστολή σου πρώτα!")
            st.session_state.plan_text = ""
        else:
            st.session_state.goal = goal_input
            st.balloons()
            st.success(f"Νέα Αποστολή: '{st.session_state.goal}'! Λαμβάνεις 'Πάπυρο Προπόνησης'!")
            
            plan_text = f"## 📜 Πάπυρος Προπόνησης 📜\n\n"
            plan_text += f"**Αποστολή:** {st.session_state.goal}\n\n"
            
            # --- Έξυπνη Δημιουργία Πλάνου ---
            # Βρίσκει τη ζώνη με το χαμηλότερο σκορ
            try:
                weakest_zone = min(st.session_state.scores, key=st.session_state.scores.get)
            except ValueError:
                weakest_zone = "ΔΥΝ" # Default

            if "δύναμη" in st.session_state.goal.lower() or "κάμψεις" in st.session_state.goal.lower() or (not "πυρήνα" in st.session_state.goal.lower() and not "αντοχή" in st.session_state.goal.lower() and weakest_zone == "ΔΥΝ"):
                plan_text += "Ο Bot προτείνει να εστιάσεις στη **ΔΥΝΑΜΗ**:\n"
                plan_text += "1. 🗓️ **Συχνότητα:** 3 φορές την εβδομάδα.\n"
                plan_text += "2. 🏋️ **Σετ:** 3 σετ Κάμψεις, 3 σετ Καθίσματα.\n"
                plan_text += "3. 📈 **Επαναλήψεις:** Κάνε όσες μπορείς! Προσπάθησε την επόμενη φορά να κάνεις +1!"
                
            elif "πυρήνα" in st.session_state.goal.lower() or "σανίδα" in st.session_state.goal.lower() or (not "δύναμη" in st.session_state.goal.lower() and not "αντοχή" in st.session_state.goal.lower() and weakest_zone == "ΠΥΡ"):
                plan_text += "Ο Bot προτείνει να εστιάσεις στον **ΠΥΡΗΝΑ**:\n"
                plan_text += "1. 🗓️ **Συχνότητα:** 4 φορές την εβδομάδα.\n"
                plan_text += "2. 🏋️ **Σετ:** 3 σετ 'Σανίδα με Άγγιγμα Ώμου', 3 σετ Ραχιαίους.\n"
                plan_text += "3. 📈 **Χρόνος/Reps:** Προσπάθησε να κάνεις +2 επαναλήψεις ή +5 δευτερόλεπτα σε κάθε σετ!"
            
            elif "αντοχή" in st.session_state.goal.lower() or "τρέξιμο" in st.session_state.goal.lower() or (not "δύναμη" in st.session_state.goal.lower() and not "πυρήνα" in st.session_state.goal.lower() and weakest_zone == "ΑΝΤ"):
                plan_text += "Ο Bot προτείνει να εστιάσεις στην **ΑΝΤΟΧΗ**:\n"
                plan_text += "1. 🗓️ **Συχνότητα:** 3-4 φορές την εβδομάδα.\n"
                plan_text += "2. 🏋️ **Δράση:** Παίξε κυνηγητό ή μπάσκετ στο διάλειμμα. Είναι η καλύτερη προπόνηση!\n"
                plan_text += "3. 📈 **Μπόνους:** Κάνε 4 σετ 'Γόνατα Ψηλά' για 1 λεπτό το καθένα."
            
            else: # Γενικός στόχος
                plan_text += "Αυτή είναι Επική Αποστολή! Για να την πετύχεις, θυμήσου τον χρυσό κανόνα:\n"
                plan_text += "1. 🗓️ **Συνέπεια:** Κάνε κάτι κάθε μέρα.\n"
                plan_text += "2. 🔥 **Ένταση:** Πρέπει να λαχανιάζεις λιγάκι!\n"
                plan_text += "3. 🍎 **Καλή διατροφή:** Μην ξεχνάς τα 'Φίλτρα Ζωής' (φρούτα/νερό)!"
            
            st.session_state.plan_text = plan_text
            
    # Εμφάνιση του πλάνου (αν υπάρχει στη μνήμη)
    if st.session_state.plan_text:
        st.markdown(st.session_state.plan_text, unsafe_allow_html=True)
        st.download_button(
            label="📥 Κατέβασε την Αποστολή σου!",
            data=st.session_state.plan_text,
            file_name=f"Η_Αποστολή_Μου.txt"
        )
        
        st.divider()
        st.header("✨ ΜΠΟΝΟΥΣ: Η 'Χρυσή Συμβουλή' σου")
        st.write("Θυμήσου τη συμβουλή που σου έδωσε ο φίλος σου στην αυλή (Μέρος 2 του Φύλλου).")
        # --- Η ΑΛΛΑΓΗ ΕΙΝΑΙ ΕΔΩ ---
        st.write("Πήγαινε στον ψηφιακό τοίχο της τάξης μας (Padlet) και γράψε την!")
        st.markdown("[➡️ Πάτα εδώ για τον Τοίχο (Padlet)](https://padlet.com/gb836188_/gym-bot-eowpms64kq0tyd6t)")