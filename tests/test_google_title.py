def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    ##assert "Google" in driver.title + "FAIL"
    #assert "Bing" in driver.title  # This will fail