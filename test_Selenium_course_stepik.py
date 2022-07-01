#!/usr/bin/env python
# coding: utf-8

# In[32]:


import re 
import sys
get_ipython().set_next_input("text = 'Shall I compare thee to a summer’s day");get_ipython().run_line_magic('pinfo', 'day')
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer’s lease hath all too short a date:
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimmed;
And every fair from fair sometime declines,
By chance, or nature’s changing course, untrimmed:
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow’st;
Nor shall Death brag thou wander’st in his shade
When in eternal lines to time thou grow’st:
So long as men can breathe or eyes can see,
So long lives this, and this gives life to thee.'.split()
k = []
for i in text:
    if ("’" not in i) and ('-' not in i):
        k.append(re.sub(r'[^\w\s]','', i).lower())
    else:
        k.append(i.replace('?','').replace('!','').replace('.','').replace(',','').replace(';','').lower())

result = {}
for word in k:
    result[word] = result.get(word, 0) + 1
for key,value in sorted(result.items()):
    print(str(key) + ': ' + str(value))


# In[1]:


import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()


# In[1]:


from selenium import webdriver
import time 
import math


# In[2]:


link = "http://suninjuly.github.io/simple_form_find_task.html"


# In[5]:


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input[name='first_name']")
    input1.send_keys("Stanislav")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Dmitriev")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Tver")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[6]:


link = browser.find_element_by_link_text(text)


# In[9]:


try:
    browser = webdriver.Chrome()
    adres = 'http://suninjuly.github.io/find_link_text'
    browser.get(adres)
    
    link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()


    input1 = browser.find_element_by_tag_name("input[name='first_name']")
    input1.send_keys("Stanislav")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Dmitriev")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Tver")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла    


# In[ ]:


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input[name='first_name']")
    input1.send_keys("Stanislav")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Dmitriev")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Tver")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[10]:


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input[type='text']")
    
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[12]:


link = "http://suninjuly.github.io/find_xpath_form"


# In[14]:


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input[name='first_name']")
    input1.send_keys("Stanislav")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Dmitriev")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Tver")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[19]:


try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    labels = browser.find_elements_by_tag_name('label') # Список лэйблов над текстовыми полями
    inputs = browser.find_elements_by_tag_name('input') # Список текстовых полей
    
    for i, label in enumerate(labels):          # Если последний символ
        if label.text[-1] == '*':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Обязалово!')   # то в поле ввода печатаем "Обязалово!"
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# In[22]:


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    
    option2= browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# In[26]:


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    option2= browser.find_element_by_id("robotsRule")
    option2.click()
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# In[43]:


from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import os


# In[41]:


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    
    z_element = int(x_element.text)+int(y_element.text)
    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(z_element))
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()    


# In[42]:


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    
    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    
    option2= browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 


# In[52]:


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_tag_name("input[name='firstname']")
    input1.send_keys("Stanislav")
    input2 = browser.find_element_by_tag_name("input[name='lastname']")
    input2.send_keys("Dmitriev")
    input3 = browser.find_element_by_tag_name("input[name='email']")
    input3.send_keys("Tver")
    
    element = browser.find_element_by_id("file")

    with open("test.txt", "w") as file:
        file.write("automationbypython")  # create test.txt file
    
    path = os.getcwd() + '/' + file.name
    
    #current_dir = os.path.abspath(os.path.dirname(''))    # получаем путь к директории текущего исполняемого файла 
    #file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    element.send_keys('C:/Jupyter/file.txt')
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    print(path)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()    


# In[3]:


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()   


# In[19]:


browser = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit() 


# In[5]:


from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text


# In[5]:


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


# In[6]:


browser = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    if WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100')):
            button = browser.find_element_by_xpath('//button[text()="Book"]')
            button.click()
    
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()  


# In[1]:


assert abs(-42) == 42


# In[3]:


assert -42==42, 'no way hose'


# In[6]:


from selenium import webdriver
import time 
import math
import unittest
import pytest
import ipytests
import ipytests.magics


# In[9]:


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block > div.first_class > input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block > div.second_class > input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block > div.third_class > input.third")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_css_selector("div.second_block > div.first_class > input.first")
        input4.send_keys("Russia")
        input5 = browser.find_element_by_css_selector("div.second_block > div.second_class > input.second")
        input5.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "No way hose")
        
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block > div.first_class > input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block > div.second_class > input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block > div.third_class > input.third")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_css_selector("div.second_block > div.first_class > input.first")
        input4.send_keys("Russia")
        input5 = browser.find_element_by_css_selector("div.second_block > div.second_class > input.second")
        input5.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "No way hose")
        
unittest.main(argv=[''], verbosity=2, exit=False)  


# In[1]:


from selenium import webdriver
import time 
import math
import unittest
import pytest
import ipytest

ipytest.config.rewrite_asserts = True


# In[14]:


def test_registration1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

        # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block > div.first_class > input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block > div.second_class > input.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block > div.third_class > input.third")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector("div.second_block > div.first_class > input.first")
    input4.send_keys("Russia")
    input5 = browser.find_element_by_css_selector("div.second_block > div.second_class > input.second")
    input5.send_keys("Russia")

        # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
    time.sleep(1)

        # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == "Congratulations! You have successfully registered!"
        
def test_registration2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

        # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block > div.first_class > input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block > div.second_class > input.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block > div.third_class > input.third")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector("div.second_block > div.first_class > input.first")
    input4.send_keys("Russia")
    input5 = browser.find_element_by_css_selector("div.second_block > div.second_class > input.second")
    input5.send_keys("Russia")

        # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
    time.sleep(1)

        # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == "Congratulations! You have successfully registered!"

ipytest.run()


# In[17]:


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        assert 1==0

    def test_second_smiling_faces(self, prepare_faces):
        assert 1==1# какие-то проверки
ipytest.run()        


# In[18]:


def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()


# In[3]:


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True 
ipytest.run()      


# In[ ]:




