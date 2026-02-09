from selenium.common.exceptions import NoSuchElementException, TimeoutException

# def search_dork(dork):
#     print(f"{G}Searching Google for: {dork}{RR}")

#     def create_driver(visible=False):
#         options = Options()
#         if not visible:
#             options.add_argument("--headless=new")   # modern headless
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         options.add_argument("--disable-blink-features=AutomationControlled")  # helps a bit
#         options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         options.add_experimental_option('useAutomationExtension', False)
        
#         # Optional: make it slightly stealthier (still not perfect)
#         # from selenium_stealth import stealth  ← if you install selenium-stealth
#         driver = webdriver.Chrome(options=options)
        
#         # Optional stealth patch (if you add the package)
#         # stealth(driver,
#         #     languages=["en-US", "en"],
#         #     vendor="Google Inc.",
#         #     platform="Win32",
#         #     webgl_vendor="Intel Inc.",
#         #     renderer="Intel Iris OpenGL Engine",
#         #     fix_hairline=True,
#         # )
        
#         return driver

#     driver = create_driver(visible=False)
#     current_page = 1
#     search_url = None

#     try:
        driver.get("https://www.google.com")
        time.sleep(1.5)

        search_box = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(dork)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        search_url = driver.current_url  # save so we can reload in visible mode

        while True:
            if is_captcha_page(driver):
                print(f"{R}CAPTCHA detected! Switching to visible browser...{RR}")
                print(f"{Y}→ Solve the CAPTCHA manually in the opened window, then press ENTER here.{RR}")
                
                # Close headless
                driver.quit()
                
                # Re-open in visible mode
                driver = create_driver(visible=True)
                driver.get(search_url)  # reload same search
                time.sleep(3)

                # Wait for user to solve it
                input(f"{C}Press ENTER after solving CAPTCHA...{RR}")

                # Optional: wait until CAPTCHA disappears (better UX)
                try:
                    WebDriverWait(driver, 60).until_not(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[src*="recaptcha/api2"]'))
                    )
                    print(f"{G}CAPTCHA seems solved — continuing...{RR}")
                except TimeoutException:
                    print(f"{Y}Continuing anyway (60s timeout reached){RR}")

            # Normal results parsing
            results = []
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.g")))
                result_divs = driver.find_elements(By.CSS_SELECTOR, "div.g")
                for div in result_divs:
                    try:
                        title = div.find_element(By.TAG_NAME, "h3").text
                        link = div.find_element(By.TAG_NAME, "a").get_attribute("href")
                        results.append((title, link))
                    except:
                        pass
            except:
                pass

            clear_screen()
            print(f"{C}Results for: {dork}{RR}")
            print(f"{Y}Page: {current_page}{RR}")
            for i, (title, _) in enumerate(results, 1):
                print(f"{G}{i}. {title}{RR}")

            print(f"\n{C}Commands:{RR} -next, -prev, -back, or number to view link")
            inp = input(f"{C}dorkbase search{RR}> ").strip().lower()

            if inp == "-back":
                break
            elif inp == "-next":
                try:
                    next_btn = WebDriverWait(driver, 6).until(
                        EC.element_to_be_clickable((By.ID, "pnnext"))
                    )
                    next_btn.click()
                    current_page += 1
                    time.sleep(2.5)
                except:
                    print(f"{R}No next page.{RR}")
                    input(f"{C}Press enter...{RR}")
            elif inp == "-prev":
                try:
                    prev_btn = WebDriverWait(driver, 6).until(
                        EC.element_to_be_clickable((By.ID, "pnprev"))
                    )
                    prev_btn.click()
                    current_page -= 1
                    time.sleep(2.5)
                except:
                    print(f"{R}No previous page.{RR}")
                    input(f"{C}Press enter...{RR}")
            elif inp.isdigit():
                num = int(inp)
                if 1 <= num <= len(results):
                    print(f"\n{G}Link:{RR} {results[num-1][1]}")
                    input(f"{C}Press enter to continue...{RR}")
            else:
                print(f"{R}Invalid command.{RR}")
                input(f"{C}Press enter...{RR}")

    except Exception as e:
        print(f"{R}Error during search: {e}{RR}")
    finally:
        driver.quit()