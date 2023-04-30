import streamlit as st

st.set_page_config(page_title="BrilliantTemperatureConversion", page_icon=":thermometer:")

st.header('Hello, Nice to meet you! I am Brilliant Temperature Conversion :thermometer::wave:')
st.title('APLIKASI KONVERSI SATUAN SUHU')

st.write("---")
left_column, right_column= st.columns(2)
with left_column:
    st.write('__**INTRO**__ - Sebuah web aplikasi yang dikembangkan untuk mempermudah pengguna sehingga dengan cepat dapat mengkonversi satuan pengukuran suhu yang diinginkan. Satuan pengukuran suhu yang digunakan yaitu Celcius, Farenheit, Reamur, dan Kelvin.')

with right_column:
    st.write('''Aplikasi ini dikembangkan oleh Kelompok 8 mata kuliah Logika Pemrograman Komputer, Kelas E Prodi Penjaminan Mutu Industri Pangan 2022 :
1. Ammar Hamzah             (2220443)
2. Fahira Nurfadhila        (2220453)
3. Naomi Natalia Simatupang (2220473)
4. Nurul Aulia Rahman       (2220479)
5. Sari Marito Simarmata    (2220486)
''')
st.write("---")

st.subheader('Konversi Suhu Dari Skala Celcius')
Celcius = st.number_input('Masukkan nilai suhu dalam Celcius :')
st.write(f'Suhu dalam skala Celcius adalah {Celcius}')

Farenheit=9/5*Celcius+32
Reamur=4/5*Celcius
Kelvin=273+Celcius

if st.button('Konversi suhu skala Celcius'):
    st.markdown('Berikut hasil konversi suhu :')
    st.write(f'Hasil konversi suhu {Celcius}°C ke dalam satuan Farenheit adalah {Farenheit}°F')
    st.write(f'Hasil konversi suhu {Celcius}°C ke dalam satuan Reamur adalah {Reamur}°R')
    st.write(f'Hasil Konversi suhu {Celcius}°C ke dalam satuan Kelvin adalah {Kelvin}K')
else:
    st.write('Silahkan tekan tombol konversi!')
    
import streamlit as st

st.subheader('Konversi Suhu Dari Skala Farenheit')
Farenheit = st.number_input('Masukkan nilai suhu dalam Farenheit :')
st.write(f'Suhu dalam skala Farenheit adalah {Farenheit}')

Celcius=5/9*(Farenheit-32)
Reamur=4/9*(Farenheit-32)
Kelvin=5/9*(Farenheit-32)+273

if st.button('Konversi suhu skala Farenheit'):
    st.markdown('Berikut hasil konversi suhu :')
    st.write(f'Hasil konversi suhu {Farenheit}°F ke dalam satuan Celcius adalah {Celcius}°C')
    st.write(f'Hasil konversi suhu {Farenheit}°F ke dalam satuan Reamur adalah {Reamur}°R')
    st.write(f'Hasil Konversi suhu {Farenheit}°F ke dalam satuan Kelvin adalah {Kelvin}K')
else:
    st.write('Silahkan tekan tombol konversi!')
    
import streamlit as st

st.subheader('Konversi Suhu Dari Skala Reamur')
Reamur = st.number_input('Masukkan nilai suhu dalam Reamur :')
st.write(f'Suhu dalam skala Reamur adalah {Reamur}')

Celcius=Reamur*5/4
Farenheit=(Reamur*9/4)+32
Kelvin=(Reamur*5/4)+273

if st.button('Konversi suhu skala Reamur'):
    st.markdown('Berikut hasil konversi suhu :')
    st.write(f'Hasil konversi suhu {Reamur}°R ke dalam satuan Celcius adalah {Celcius}°C')
    st.write(f'Hasil konversi suhu {Reamur}°R ke dalam satuan Reamur adalah {Farenheit}°F')
    st.write(f'Hasil Konversi suhu {Reamur}°R ke dalam satuan Kelvin adalah {Kelvin}K')
else:
    st.write('Silahkan tekan tombol konversi!')
    
import streamlit as st

st.subheader('Konversi Suhu Dari Skala Kelvin')
Kelvin = st.number_input('Masukkan nilai suhu dalam Kelvin :')
st.write(f'Suhu dalam skala Kelvin adalah {Kelvin}')

Celcius=Kelvin-273
Farenheit=9/5*(Kelvin-273)+32
Reamur=4/5*(Kelvin-273)

if st.button('Konversi suhu skala Kelvin '):
    st.markdown('Berikut hasil konversi suhu :')
    st.write(f'Hasil konversi suhu {Kelvin} K ke dalam satuan Celcius adalah {Celcius}°C')
    st.write(f'Hasil konversi suhu {Kelvin} K ke dalam satuan Farenheit adalah {Farenheit}°F')
    st.write(f'Hasil Konversi suhu {Kelvin} K ke dalam satuan Reamur adalah {Reamur}°R')
else:
    st.write('Silahkan tekan tombol konversi!')
    
st.write("---")
st.header("Thank you for using this web application! :sparkling_heart:")
st.subheader("Let Us Know!")
st.caption(":point_down: Kami menerima saran dan pengembangan yang kalian harapkan dari web aplikasi ini untuk kedepannya.")
with st.form("form1", clear_on_submit=True):
    name = st.text_input("Masukkan nama lengkap")
    email = st.text_input("Masukkan email")
    pesan = st.text_area("Pesan")
    
    submit = st.form_submit_button("Kirim formulir")