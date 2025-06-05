import streamlit as st
from PIL import Image
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Curriculum Vitae",
    page_icon="📄",
    layout="wide"
)

# CSS untuk navigation bar
st.markdown("""
<style>
    /* Navigation bar styling */
    .nav-bar {
        display: flex;
        justify-content: space-around;
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .nav-item {
        padding: 0.5rem 1rem;
        cursor: pointer;
        font-weight: bold;
    }
    
    .nav-item:hover {
        background-color: #d0d2d6;
        border-radius: 5px;
    }
    
    .nav-item.active {
        border-bottom: 3px solid #4a8af4;
        color: #4a8af4;
    }
    
    /* Profile section styling */
    .profile-img {
        border-radius: 50%;
        border: 3px solid #4a8af4;
    }
</style>
""", unsafe_allow_html=True)

# State untuk halaman aktif
if 'page' not in st.session_state:
    st.session_state.page = 'Biodata'

# Navigation bar
nav_items = ['Biodata', 'Pendidikan', 'Pengalaman Kerja', 'Pengalaman Organisasi', 'Pengalaman Pelatihan', 'Skills']
nav_bar = st.container()
with nav_bar:
    cols = st.columns(len(nav_items))
    for i, item in enumerate(nav_items):
        if cols[i].button(item, key=f"nav_{i}"):
            st.session_state.page = item

# Konten berdasarkan halaman aktif
if st.session_state.page == 'Biodata':
    # Header dengan foto profil
    col1, col2 = st.columns([1, 3])
    with col1:
        # Ganti dengan path foto Anda
        image = Image.open('foto.jpg')
        st.image(image, width=200, output_format='JPG', caption='Hola World', use_container_width=False, clamp=False, channels='RGB')
    
    with col2:
        st.title("Alfajar Tri Ramadani")
        st.subheader("Murid")
        st.write("odajimayuken22@gmail.com | 0838953526")
        st.write("Bandung Barat, Jawa Barat")
    
    # Informasi Biodata
    st.header("Informasi Pribadi")
    bio_col1, bio_col2 = st.columns(2)
    with bio_col1:
        st.write("Tempat, Tanggal Lahir: Bandung Barat, 31/Agustus/2008")
        st.write("Jenis Kelamin: Laki-laki")
    with bio_col2:
        st.write("Kewarganegaraan: Indonesia")
        st.write("Status Pernikahan: Belum Menikah")
    
    st.header("Tentang Saya")
    st.write("""
Hai!, Nama saya Alfajar Tri Ramadani, seorang siswa Pengembangan Perangkat Lunak dan Gim di SMKN 4 Padalarang 
yang memiliki minat dalam pemrograman. Saya mahir dalam JavaScript untuk pengembangan mobile dan Python 
untuk Data Science. Saya memiliki pengalaman dengan framework seperti React.js, Laravel dan beberapa framework/library untuk data science, serta memahami manajemen 
basis data berbasis SQL. Saya dikenal sebagai orang yang disiplin, pandai mengatur waktu, dan berkomitmen untuk 
menghasilkan pekerjaan berkualitas tinggi serta tepat waktu.
    """)

elif st.session_state.page == 'Pendidikan':
    st.title("Riwayat Pendidikan")
    
    st.header("Pendidikan Formal")
    edu_data = {
        "Tahun": ["2023-2026", "2020-2023"],
        "Jenjang": ["Sekolah Menengah Kejuruan", "Sekolah Menengah Pertama"],
        "Institusi": ["SMK Negeri 4 Padalarang", "SMP Negeri 1 Cipatat"],
        "Detail": ["Nilai: 92.6", "Nilai: 85.3"]
    }
    st.table(pd.DataFrame(edu_data))
    
    st.header("Pendidikan Non-Formal")
    st.write("""
    - Oracle Database - Oracle Academy
    - MySQL for Developers - Oracle University
    - Bootcamp Data Science - Sanber Campus 
    - Game Dev Counstruct, Javascript, Phaser, Unity - Gamelab Indonesia
    - Bootcamp Web, UI/UX, Dart, Python - LearningX Academy
    """)

elif st.session_state.page == 'Pengalaman Kerja':
    st.title("Pengalaman Kerja")
    st.write("""
    - Graphic Designer media sosial di SMKN 4 Padalarang
    """)
elif st.session_state.page == 'Pengalaman Organisasi':
    st.title("Pengalaman Organisasi")
    
    org_data = {
        "Periode": ["2023-2025", "2021-2023"],
        "Posisi": ["Sekretaris", "Ketua MPK "],
        "Organisasi": ["Nep4l TV", "MPK SMPN 1 Cipatat"],
    }
    
    st.table(pd.DataFrame(org_data))
    
elif st.session_state.page == 'Pengalaman Pelatihan':
    st.title("Pengalaman Pelatihan")
    
    training_data = {
        "Tahun": ["2025", "2023-sekarang"],
        "Pelatihan": ["Bootcamp Data Science", "Game Dev Counstruct, Javascript, Phaser, Unity"],
        "Penyelenggara": ["Sanber Campus", "Gamelab Indonesia"],
        "Detail": ["Belajar dasar-dasar data science, analisis data, dan machine learning.", 
                   "Belajar pengembangan game menggunakan Construct, JavaScript, Phaser, dan Unity."],
    }
    
    st.table(pd.DataFrame(training_data))
    
elif st.session_state.page == 'Skills':
    st.title("Skills & Kemampuan")

    st.header("Technical Skills")
    
    tech_skills = {
        "Figma": 90,
        "JavaScript": 85,
        "PHP": 85,
        "Python": 80,
        "React": 80,
        "SQL": 80,
        "Java": 50,
    }
    
    for skill, level in tech_skills.items():
        st.write(f"{skill}")
        st.progress(level)
    
    # Soft Skills dengan card
    st.header("Soft Skills")
    soft_col1, soft_col2, soft_col3 = st.columns(3)
    
    with soft_col1:
        st.markdown("""
        <div style="background-color:#4a8af4; padding:1rem; border-radius:10px;">
            <h4 style="margin:0;">Komunikasi</h4>
            <p style="margin:0.5rem 0 0 0;">Kemampuan presentasi dan negosiasi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with soft_col2:
        st.markdown("""
        <div style="background-color:#4a8af4; padding:1rem; border-radius:10px;">
            <h4 style="margin:0;">Kerja Tim</h4>
            <p style="margin:0.5rem 0 0 0;">Kolaborasi dalam tim lintas fungsi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with soft_col3:
        st.markdown("""
        <div style="background-color:#4a8af4; padding:1rem; border-radius:10px;">
            <h4 style="margin:0;">Manajemen Waktu</h4>
            <p style="margin:0.5rem 0 0 0;">Penyelesaian proyek tepat waktu</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Bahasa dengan indikator visual
    st.header("Kemampuan Bahasa")
    lang_data = {
        "Bahasa": ["Indonesia", "Inggris"],
        "Level": ["Bahasa Ibu", "(TOEIC 635)"],
        "Kemampuan": [90, 65]
    }
    
    for i, lang in enumerate(lang_data["Bahasa"]):
        cols = st.columns([1, 2, 1])
        with cols[0]:
            st.write(f"**{lang}**")
        with cols[1]:
            st.progress(lang_data["Kemampuan"][i])
        with cols[2]:
            st.write(lang_data["Level"][i])