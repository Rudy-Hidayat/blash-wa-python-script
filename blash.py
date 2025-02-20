from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_whatsapp_message_with_pdf(phone_numbers, message, file_path):
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    input("Login ke WhatsApp Web dan tekan Enter setelah selesai...")

    for phone_number in phone_numbers:
        try:
            print(f"Membuka obrolan dengan nomor {phone_number}...")
            driver.get(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")
            
            # Tunggu obrolan dimuat sepenuhnya
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[2]/button/span"))
            )
            
            # Klik tombol kirim pesan teks
            print("Mengirim pesan teks...")
            send_button = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[2]/button/span")
            send_button.click()
            print(f"Pesan teks berhasil dikirim ke {phone_number}.")

            # Tunggu beberapa saat sebelum melampirkan file
            time.sleep(2)

            # Klik ikon untuk melampirkan file
            print("Klik ikon untuk melampirkan file...")
            attachment_icon = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[1]/div/button/span")
            attachment_icon.click()

            # Pilih opsi dokumen
            print("Memilih dokumen...")
            document_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/span[5]/div/ul/div/div/div[1]/li"))
            )
            document_option.click()

            # Tunggu elemen input file muncul
            print("Mengunggah file...")
            document_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )
            document_input.send_keys(file_path)

            # Klik tombol kirim dokumen
            print("Mengirim file...")
            send_doc_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div"))
            )
            send_doc_button.click()
            print(f"File berhasil dikirim ke {phone_number}.")

            # Tunggu beberapa detik sebelum ke nomor berikutnya
            time.sleep(7)

        except Exception as e:
            print(f"Gagal mengirim ke {phone_number}: {e}")
            continue

    print("Pengiriman selesai.")
    driver.quit()

# Daftar nomor yang akan dikirim pesan dan lampiran
phone_numbers = [
"6288888xxxxx",  #Sesuaikan nomornya
]

# Kirim pesan dan lampiran
send_whatsapp_message_with_pdf(
    phone_numbers, 
    "Assalamualaikum Wr. Wb.,%0A%0ABapak/Ibu Pimpinan  , berikut kami lampirkan Undangan  , dengan detail:%0A%0AHari/tanggal : Rabu, 12 Februari 2025%0APukul:  14.00 s.d 16.00 WIB%0ATempat: Ruangx.",
    r"C:\Users\Downloads\Undangan.pdf"
)




