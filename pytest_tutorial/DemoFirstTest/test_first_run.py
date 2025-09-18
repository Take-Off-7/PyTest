from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

def test_lambdatest_playground():
    options = Options()
    # Required for Codespaces (no GUI)
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Always start with a clean, temporary profile
    tmp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={tmp_profile}")

    # Prevent Chrome from trying to use existing default profile
    options.add_argument("--profile-directory=Default")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print("Title: ", driver.title)
    driver.quit()
