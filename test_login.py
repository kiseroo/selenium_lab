# -*- coding: utf-8 -*-
"""MUST-ийн Student портал дээр нэвтрэх автоматжуулсан тест"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    """Chrome хөтчийг тохируулах функц"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def test_must_login():
    """MUST студентийн портал дээр нэвтрэх тест"""
    driver = setup_driver()
    try:
        # MUST Student портал руу очих
        print("MUST студентийн портал руу очиж байна...")
        driver.get("https://student.must.edu.mn")
        
        # Нэвтрэх хэсгийн элементүүдийг олох
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username")))
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        # Нэвтрэх мэдээлэл оруулах
        print("Нэвтрэх мэдээлэл оруулж байна...")
        username_field.clear()
        username_field.send_keys("B222270077")
        password_field.clear()
        password_field.send_keys("ttt")
        # Public repository учраас password-ийг өөрөөр бичээд github-д оруулсан
        
        # Нэвтрэх товчийг дарах
        print("Нэвтэрэж байна...")
        login_button.click()
        
        # Амжилттай нэвтэрсэн эсэхийг assertion ашиглан шалгах
        profile_element = WebDriverWait(driver, 15).until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'profile')]")),
                EC.presence_of_element_located((By.CLASS_NAME, "profile")),
                EC.presence_of_element_located((By.ID, "profile")),
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'dashboard')]")))))
        
        # Assert амжилттай нэвтэрсэн эсэхийг шалгах
        assert profile_element is not None, "Амжилттай нэвтэрч чадсангүй - профайл элемент олдсонгүй"
        assert "student.must.edu.mn" in driver.current_url, "Буруу хуудас дээр байна"
        print("Амжилттай нэвтэрлээ!")
        print(f"Хуудасны гарчиг: {driver.title}")
        
        # Logout товчийг олж дарах
        try:
            logout_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, 
                    "//a[contains(@href, 'logout') or contains(text(), 'Logout')]")))
            logout_element.click()
            print("Амжилттай гарлаа!")
        except Exception as e:
            print(f"Logout хийхэд алдаа: {e}")
            
    except Exception as e:
        # Assert алдаа гарсан тохиолдолд
        assert False, f"Нэвтрэхэд алдаа гарлаа: {e}. Одоогийн URL: {driver.current_url}"
    finally:
        print("Хөтчийг хааж байна...")
        driver.quit()
    
    return True

if __name__ == "__main__":
    print("=== MUST Student Портал Нэвтрэх Тест ===")
    success = test_must_login()
    # Assert тест амжилттай дуусна гэж найдаж байна  
    assert success, "Тест амжилтгүй боллоо!"
    print("Тест амжилттай дууслаа!")
