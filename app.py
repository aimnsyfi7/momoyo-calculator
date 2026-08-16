
import calendar
import streamlit as st

st.set_page_config(
    page_title="MOMOYO Daily Sale Calculator", page_icon="🍦", layout="centered"
)

# --- KAWALAN AKSES ---
password = st.text_input("Masukkan Kata Laluan:", type="password")

if password == "AimanHensem":
    st.title("🍦 MOMOYO Daily Sale Calculator")
    st.markdown("---")

    # --- INPUT ASAS & JUALAN HARIAN ---
    st.subheader("📌 Maklumat Asas & Jualan Harian")
    col_date, col_weather = st.columns(2)
    with col_date:
        tarikh = st.date_input("Tarikh")
    with col_weather:
        cuaca = st.selectbox("Cuaca", ["Sunny", "Rainy", "Cloudy"])

    daily_sales = st.number_input(
        "Daily Sales (RM):", value=0.0, step=0.01, format="%.2f"
    )
    cash_sales = st.number_input(
        "Cash Sales (RM):", value=0.0, step=0.01, format="%.2f"
    )
    qr_sales = st.number_input(
        "QR Sales (RM):", value=0.0, step=0.01, format="%.2f"
    )

    st.markdown("---")

    # --- POS SYSTEM VS SYSTEM DEKAT PHONE ---
    col_pos, col_phone = st.columns(2)

    with col_pos:
        st.subheader("🖥️ POS System")
        pos_qr = st.number_input(
            "POS QR (RM):", value=0.0, step=0.01, format="%.2f"
        )
        pos_grab = st.number_input(
            "POS Grab (RM):", value=0.0, step=0.01, format="%.2f"
        )
        pos_fp = st.number_input(
            "POS Food Panda (RM):", value=0.0, step=0.01, format="%.2f"
        )
        pos_shopee = st.number_input(
            "POS Shopee (RM):", value=0.0, step=0.01, format="%.2f"
        )

    with col_phone:
        st.subheader("📱 System Dekat Phone")
        phone_qr = st.number_input(
            "Phone QR (RM):", value=0.0, step=0.01, format="%.2f"
        )
        phone_grab = st.number_input(
            "Phone Grab (RM):", value=0.0, step=0.01, format="%.2f"
        )
        phone_fp = st.number_input(
            "Phone Foodpanda (RM):", value=0.0, step=0.01, format="%.2f"
        )
        phone_shopee = st.number_input(
            "Phone Shopee (RM):", value=0.0, step=0.01, format="%.2f"
        )

    st.markdown("---")

    # --- INVENTORY & PRESTASI JUALAN ---
    st.subheader("📦 Stok & Target Jualan")
    thai_matcha = st.number_input(
        "Thai Coconut Matcha (Cup):", value=0, step=1
    )
    target_sales = st.number_input(
        "Target Sales (RM):", value=85000.0, step=1000.0, format="%.2f"
    )
    accum_before = st.number_input(
        "Accumulated Sale Before (RM):", value=0.0, step=0.01, format="%.2f"
    )

    # --- BUTANG KIRA ---
    if st.button("🚀 Kira & Jana Laporan", type="primary"):
        # 1. Beza POS vs Phone
        diff_qr = phone_qr - pos_qr
        diff_grab = phone_grab - pos_grab
        diff_fp = phone_fp - pos_fp
        diff_shopee = phone_shopee - pos_shopee

        # 2. Accumulated Sales = Accumulated before + Daily sales
        accumulated_sales = accum_before + daily_sales

        # 3. % of Delivery = ((Grab + Foodpanda + Shopee) / Daily sales) * 100
        total_delivery = pos_grab + pos_fp + pos_shopee + phone_qr
        pct_delivery = (
            (total_delivery / daily_sales * 100) if daily_sales > 0 else 0.0
        )

        # 4. Tetapan Tarikh & Jumlah Hari Dalam Bulan
        day_of_month = tarikh.day
        num_days_in_month = calendar.monthrange(tarikh.year, tarikh.month)[1]

        # 5. Complete Rate = (Accumulated / Target sales) * 100
        complete_rate = (
            (accumulated_sales / target_sales * 100)
            if target_sales > 0
            else 0.0
        )

        # 6. Time Progress = (Tarikh harini / Jum hari bulan ni) * 100
        time_progress = (day_of_month / num_days_in_month) * 100

        # 7. Expected Sale Volume = (Accumulated / Tarikh harini) * Jum hari bulan ni
        expected_sales_vol = (
            (accumulated_sales / day_of_month) * num_days_in_month
            if day_of_month > 0
            else 0.0
        )

        # 8. Expected Completion Rate = (Expected sale volume / Target sales) * 100
        expected_comp_rate = (

(expected_sales_vol / target_sales * 100)
            if target_sales > 0
            else 0.0
        )

        st.success("✅ Pengiraan Selesai!")

        # --- PAPARAN HASIL BENTUK TEKS BOLEH-COPY ---
        st.subheader("📄 Laporan Format Mesej")

        report_text = f"""Date: {tarikh.strftime('%d/%m/%Y')}
Weather: {cuaca.lower()}

Daily Sales: Rm {daily_sales:.2f}
Cash Sales: Rm {cash_sales:.2f}
QR Sales: Rm {qr_sales:.2f}

Pos System -
QR: RM {pos_qr:.2f}
Grab: Rm {pos_grab:.2f}
Food Panda: RM {pos_fp:.2f}
Shopee: RM {pos_shopee:.2f}

SYSTEM DEKAT PHONE -
QR: RM {phone_qr:.2f}
Grab: RM {phone_grab:.2f}
Foodpanda: RM {phone_fp:.2f}
Shopee: RM {phone_shopee:.2f}

Thai coconut matcha:
{thai_matcha} (cup)

Lebih / kurang :
QR: RM {diff_qr:.2f}
Grab: RM {diff_grab:.2f}
Foodpanda: RM {diff_fp:.2f}
Shopee: RM {diff_shopee:.2f}

% of Delivery: {pct_delivery:.2f}%

Sales Performance:
Target Sales: {target_sales/1000:.0f}k
Accumulated Sales: Rm {accumulated_sales:.2f}
Complete Rate: {complete_rate:.2f}%
Time Progress: {time_progress:.2f}%
Expected Sales Volume: Rm {expected_sales_vol:.2f}
Expected Completion Rate: {expected_comp_rate:.2f}%"""

        st.code(report_text, language="text")

elif password != "":
    st.error("Kata laluan salah!")

