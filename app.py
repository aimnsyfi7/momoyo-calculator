
import calendar
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="MOMOYO Daily Sale Calculator Pro",
    page_icon="🍦",
    layout="centered",
)


# --- FUNGSI HELPER: LEBIH / KURANG ---
def semak_lebih_kurang(val):
    if val > 0:
        return f"+RM {val:.2f} (Lebih)"
    elif val < 0:
        return f"-RM {abs(val):.2f} (Kurang)"
    else:
        return "RM 0.00"


# --- KAWALAN AKSES (PASSWORD) ---
password = st.text_input("Masukkan Kata Laluan:", type="password")

if password == "AimanHensem":
    st.title("🍦 MOMOYO Daily Sale Calculator Pro")
    st.caption("Sistem Pengiraan Jualan Harian & Analisis Prestasi")
    st.markdown("---")

    # --- INPUT MAKLUMAT HARIAN ---
    st.subheader("📌 1. Maklumat Asas & Jualan Harian")
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

    # --- POS VS PHONE ---
    st.subheader("📊 2. POS System vs Phone System")
    col_pos, col_phone = st.columns(2)

    with col_pos:
        st.markdown("**🖥️ POS System**")
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
        st.markdown("**📱 System Dekat Phone**")
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

    # --- STOK & TARGET ---
    st.subheader("📦 3. Stok & Target Jualan Bulanan")
    col_stok, col_target = st.columns(2)
    with col_stok:
        thai_matcha = st.number_input(
            "Thai Coconut Matcha (Cup):", value=0, step=1
        )
    with col_target:
        target_sales = st.number_input(
            "Target Sales (RM):", value=85000.0, step=1000.0, format="%.2f"
        )

    accum_before = st.number_input(
        "Accumulated Sale Before (RM):", value=0.0, step=0.01, format="%.2f"
    )

    st.markdown("---")

    # --- BUTANG PROSES ---
    if st.button("🚀 Kira & Jana Analisis", type="primary"):

        # 1. Beza Imbangan
        diff_qr = phone_qr - pos_qr
        diff_grab = phone_grab - pos_grab
        diff_fp = phone_fp - pos_fp
        diff_shopee = phone_shopee - pos_shopee
        ada_mismatch = any(
            d != 0 for d in [diff_qr, diff_grab, diff_fp, diff_shopee]
        )

        # 2. Formulasi Asas
        accumulated_sales = accum_before + daily_sales
        total_delivery = pos_grab + pos_fp + pos_shopee
        pct_delivery = (
            (total_delivery / daily_sales * 100) if daily_sales > 0 else 0.0
        )

        # 3. Formulasi Tarikh & Prestasi
        day_of_month = tarikh.day
        num_days_in_month = calendar.monthrange(tarikh.year, tarikh.month)[1]

        complete_rate = (
            (accumulated_sales / target_sales * 100)
            if target_sales > 0
            else 0.0
        )
        time_progress = (day_of_month / num_days_in_month) * 100
        expected_sales_vol = (


(accumulated_sales / day_of_month) * num_days_in_month
            if day_of_month > 0
            else 0.0
        )
        expected_comp_rate = (
            (expected_sales_vol / target_sales * 100)
            if target_sales > 0
            else 0.0
        )

        # --- BENTUK PABARAN TAB ---
        tab_report, tab_chart, tab_alerts = st.tabs(
            ["📄 Laporan Mesej", "📊 Carta & Metrics", "🔔 Status & Alerts"]
        )

        # TAB 1: LAPORAN TEXT (WHATSAPP READY)
        with tab_report:
            st.subheader("📄 Format Laporan WhatsApp")

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
QR: {semak_lebih_kurang(diff_qr)}
Grab: {semak_lebih_kurang(diff_grab)}
Foodpanda: {semak_lebih_kurang(diff_fp)}
Shopee: {semak_lebih_kurang(diff_shopee)}

% of Delivery: {pct_delivery:.2f}%

Sales Performance:
Target Sales: {target_sales/1000:.0f}k
Accumulated Sales: Rm {accumulated_sales:.2f}
Complete Rate: {complete_rate:.2f}%
Time Progress: {time_progress:.2f}%
Expected Sales Volume: Rm {expected_sales_vol:.2f}
Expected Completion Rate: {expected_comp_rate:.2f}%"""

            st.code(report_text, language="text")

            # EXPORT TO CSV
            df_data = pd.DataFrame(
                [
                    {
                        "Tarikh": tarikh.strftime("%d/%m/%Y"),
                        "Daily Sales": daily_sales,
                        "Cash Sales": cash_sales,
                        "QR Sales": qr_sales,
                        "Accumulated Sales": accumulated_sales,
                        "Complete Rate (%)": round(complete_rate, 2),
                        "Expected Sales (RM)": round(expected_sales_vol, 2),
                    }
                ]
            )
            csv = df_data.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Muat Turun Rekod Harian (CSV)",
                data=csv,
                file_name=f"Laporan_Sales_{tarikh.strftime('%Y%m%d')}.csv",
                mime="text/csv",
            )

        # TAB 2: METRICS & CARTA
        with tab_chart:
            st.subheader("📊 Kemajuan Target & Agihan Jualan")

            # Progress Bar Target
            st.write(
                f"**Pencapaian Target Jualan ({complete_rate:.1f}% / 100%)**"
            )
            st.progress(min(complete_rate / 100.0, 1.0))

            col_m1, col_m2, col_m3 = st.columns(3)
            col_m1.metric(
                "Accumulated Sales", f"RM {accumulated_sales:,.2f}"
            )
            col_m2.metric(
                "Expected Sales Vol", f"RM {expected_sales_vol:,.2f}"
            )
            col_m3.metric("% Delivery", f"{pct_delivery:.1f}%")

            st.markdown("---")
            st.write("**📈 Perbandingan POS vs Phone (RM)**")

            # Carta Bar POS vs Phone
            chart_data = pd.DataFrame(
                {
                    "Kategori": ["QR", "Grab", "Foodpanda", "Shopee"],
                    "POS System": [pos_qr, pos_grab, pos_fp, pos_shopee],
                    "Phone System": [
                        phone_qr,
                        phone_grab,
                        phone_fp,
                        phone_shopee,
                    ],
                }
            ).set_index("Kategori")

            st.bar_chart(chart_data)

        # TAB 3: SMART ALERTS & PACING
        with tab_alerts:
            st.subheader("🔔 Status & Peringatan Automatik")

            # Alert Imbangan Duit
            if ada_mismatch:
                st.warning(


"⚠️ AMARAN: Terdapat ketidakselarasan baki antara POS System & Phone System! Sila semak semula bahagian Lebih/Kurang."
                )
            else:
                st.success(
                    "🎉 SEMPURNA: Semua imbasan POS System dan Phone System adalah sepadan (RM 0.00)."
                )

            # Alert Sales Pacing
            if complete_rate >= time_progress:
                st.info(
                    f"🚀 ON TRACK: Prestasi jualan korang berada di hadapan garisan masa! (Complete Rate: {complete_rate:.1f}% vs Time Progress: {time_progress:.1f}%)"
                )
            else:
                st.error(
                    f"🐢 BEHIND TARGET: Prestasi jualan sedikit perlahan berbanding garisan masa bulan ini. (Complete Rate: {complete_rate:.1f}% vs Time Progress: {time_progress:.1f}%)"
                )

elif password != "":
    st.error("Kata laluan salah!")
