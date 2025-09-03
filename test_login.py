# MUST сургуулийн веб автомат тест - Selenium WebDriver ашигласан
# Зорилго: Нэвтрэх болон гарах үйлдлийг автоматжуулах

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome хөтчийн тохиргоо
chrome_options = Options()
chrome_options.binary_location = r"d:\TEMUULEN\chrome-win64\chrome.exe"

try:    
    # ChromeDriver үүсгэх
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("Chrome хөтөч амжилттай нээгдлээ!")
    
    # MUST сайт руу орох
    driver.get("https://student.must.edu.mn")
    print(f"Сайт нээгдлээ: {driver.title}")
    
    # Нэвтрэх мэдээлэл
    username = "B222270077"
    password = "Temka3459."
    
    # Нэвтрэх талбаруудыг олж бөглөх
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(2)
    
    # Нэвтрэх товчийг олж дарах - олон арга ашиглах
    try:
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    except:
        try:
            login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        except:
            try:
                login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Нэвтрэх')]")
            except:
                try:
                    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
                except:
                    login_button = driver.find_element(By.TAG_NAME, "button")
    
    login_button.click()
    time.sleep(3)
    
    # ҮЙЛДЛИЙН ҮР ДҮНГ ШАЛГАХ (Assertions)
    current_url = driver.current_url
    login_success = False
    
    # Шалгалт 1: URL өөрчлөгдсөн эсэх
    if "login" not in current_url.lower():
        print("НЭВТРЭХ АМЖИЛТТАЙ - URL өөрчлөгдлөө")
        login_success = True
    
    # Шалгалт 2: Dashboard элемент олдсон эсэх  
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, "НҮҮР")
        print("НЭВТРЭХ АМЖИЛТТАЙ - Dashboard олдлоо")
        login_success = True
    except:
        pass
    
    # Эцсийн шалгалт
    assert login_success, "НЭВТРЭХ АМЖИЛТГҮЙ"
    print("*** НЭВТРЭХ БҮРЭН АМЖИЛТТАЙ ***")
    
    # POPUP/OVERLAY АРИЛГАХ
    print("Popup цонх арилгаж байна...")
    
    # Арга 1: ESC товч дарах
    try:
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(2)
    except:
        pass
    
    # Арга 2: Хажуугийн цэс дээр дарах
    try:
        actions = ActionChains(driver)
        actions.move_by_offset(50, 300).click().perform()
        time.sleep(2)
    except:
        pass
    
    # Арга 3: Хүлээх (popup автоматаар алга болох)
    time.sleep(3)
    
    # СИСТЕМЭЭС ГАРАХ
    print("Системээс гарч байна...")
    
    logout_selectors = [
        "//a[contains(text(), 'Гарах')]",
        "//*[contains(text(), 'Гарах')]",
        "//a[contains(@href, 'logout')]"
    ]
    
    logout_success = False
    for logout_selector in logout_selectors:
        try:
            logout_element = driver.find_element(By.XPATH, logout_selector)
            logout_element.click()
            print("ГАРАХ ТОВЧ ДАРАГДЛАА")
            time.sleep(3)
            logout_success = True
            break
        except:
            continue
    
    # Гарсан эсэхийг шалгах
    if logout_success:
        if "login" in driver.current_url.lower():
            print("*** ГАРАХ АМЖИЛТТАЙ ***")
        else:
            print("Гарах товч дарагдсан боловч шалгалт тодорхойгүй")
    else:
        print("Гарах товч олдсонгүй")

except Exception as e:
    print(f"Алдаа гарлаа: {e}")

finally:
    # Хөтчийг хаах
    try:
        driver.quit()
        print("Тест дууслаа!")
    except:
        pass
