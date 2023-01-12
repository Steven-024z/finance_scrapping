from selenium import webdriver


def get_driver(url):
  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  #driver.get("https://automated.pythonanywhere.com")
  driver.get(url)
  return driver


def main():
  #url = "https://www.macrotrends.net/stocks/charts/CSV/carriage-services/stock-price-history"
  url = "https://automated.pythonanywhere.com"
  driver = get_driver(url)
  #element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
  element = driver.find_element(by="xpath",
                                value="/html/body/div[1]/div/h1[2]")
  print(element.text)
  #element = driver.find_element(
  #  by="xpath", value="/html/body/div[3]/div[3]/div[1]/div[2]/span/strong")
  #print(f"CSV {element.text}")

  # url = "https://www.macrotrends.net/stocks/charts/GOOGL/alphabet/stock-price-history"
  # google_driver = get_driver(url)

  # element = google_driver.find_element(
  #   by="xpath", value="/html/body/div[3]/div[3]/div[1]/div[2]/span/strong")

  # print(f"google {element.text}")


main()
