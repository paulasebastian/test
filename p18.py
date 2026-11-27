
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

driver.find_element(By.ID, "userName").send_keys("John David")
driver.find_element(By.ID, "userEmail").send_keys("john@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Irinjalakuda, Thrissur")
driver.find_element(By.ID, "permanentAddress").send_keys("Kerala, India")

submit = driver.find_element(By.ID, "submit")

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit)

driver.execute_script("arguments[0].click();", submit)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "output"))
)

print("Form submitted successfully!")
print(driver.find_element(By.ID, "output").text)

input("Press Enter to close the browser...")
driver.quit()
