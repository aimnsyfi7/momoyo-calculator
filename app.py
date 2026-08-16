import streamlit as st

st.set_page_config(page_title="Daily sale calculator", page_icon="MOMOYO", layout="centered")

# --- KAWALAN AKSES ---
password = st.text_input("Masukkan Kata Laluan:", type="password")

if password == "AimanHensem":
    st.title("MOMOYO Daily sale calculator")
    st.write("masukkan nilai di bawah untuk membuat pengiraan:")

    val_a = st.number_input("masukkan Nilai A:", value=0.0, step=0.1, format="%.2f")
    val_b = st.number_input("masukkan Nilai B:", value=0.0, step=0.1, format="%.2f")

    if st.button("kira sekarang", type="primary"):
        hasil = val_a * val_b / 2
        hasil2 = val_a + val_b

        st.divider()
        st.success("pengiraan Selesai!")
        
        col1, col2 = st.columns(2)
        col1.metric(label="Hasil 1", value=f"{hasil:.4f}")
        col2.metric(label="Hasil 2", value=f"{hasil2:.4f}")

elif password != "":
    st.error("Kata laluan salah!")
