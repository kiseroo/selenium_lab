# Selenium WebDriver Automation Test - Lab 1

## Тухай
MUST-ийн Student портал дээр нэвтрэх үйлдлийг автоматжуулах Selenium WebDriver тест.

## Шаардлага
- Python 3.7+
- Chrome хөтөч
- Интернэт холболт

## Суулгах
```bash
# Dependencies суулгах
pip install -r requirements.txt
```

## Ажиллуулах
```bash
# Тестийг ажиллуулах
python test_login.py
```

## Файлууд
- `test_login.py` - Үндсэн тестийн скрипт
- `requirements.txt` - Python dependencies
- `README.md` - Төслийн тайлбар

## Тестийн үйлдлүүд

	1.	Chrome хөтөч ачааллах
	2.	MUST Student портал руу очих
	3.	Нэвтрэх мэдээлэл оруулах
	4.	Амжилттай нэвтэрсэн эсэхийг шалгах (assert ашиглан)
	5.	Logout хийх
	6.	Хөтчийг хаах

##Нэвтрэх мэдээлэл
	•	Username: B222270077
	•	Password: ...(public repo bolhoor bicheegui)

##Assertion

Жишээ нь:
	•	Нэвтэрсний дараа профайл элемент байгаа эсэхийг шалгана.
	•	Хуудасны URL зөв эсэхийг шалгана.
	•	Эцэст нь тест бүхэлдээ амжилттай болсон эсэхийг шалгана.