from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure ChromeDriver service and options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Replace the path to where chromedriver is located in your system
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# Function to perform the search
def imdb_search():
    # Navigate to the IMDb search page for names
    driver.get('https://www.imdb.com/search/name/')
    
    # Use explicit waits for input boxes and dropdowns to load
    wait = WebDriverWait(driver, 10)
    window_height = driver.execute_script("return window.innerHeight;")
    driver.execute_script(f"window.scrollBy(0, {window_height / 2});")
    name_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[1]/label/span[1]/div")))
    name_input.click()
    name_box = wait.until(EC.presence_of_element_located((By.NAME,'name-text-input')))
    name_box.send_keys('Tom Hanks')
    # Example: Fill out 'Birth Month' drop-down menu
    birth_month_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[1]/label/span[1]/div")))
    birth_month_dropdown.click()
    birth_month_box = wait.until(EC.presence_of_element_located((By.NAME,'birth-date-start-input')))
    birth_month_box.send_keys("09-07-1956")  # Select July as the birth month
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    current_scroll_position = driver.execute_script("return window.pageYOffset;")

    driver.execute_script(f"window.scrollBy(0, {window_height / 2});")
    new_scroll_position = driver.execute_script("return window.pageYOffset;")
    print(f"Previous position: {current_scroll_position}, New position: {new_scroll_position}")
    gender_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[7]/div[1]/label/span[1]/div")))
    gender_dropdown.click()

    gender_btn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[7]/div[2]/div/section/button[1]")))
    gender_btn.click()
    driver.execute_script("window.scrollBy(0, -1000);") 
  
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '''//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button''')))
    submit_button.click()

# Run the search
imdb_search()

# Close the browser after performing the task
driver.quit()
