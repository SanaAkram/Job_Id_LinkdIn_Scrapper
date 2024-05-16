from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


def scrape_job_details(driver):
    # Wait for the job listings to load
    job_listings = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-search-result"))
    )

    jobs = []
    for job in job_listings:
        job_url = job.find_element(By.TAG_NAME, "a").get_attribute("href")
        job_title = job.find_element(By.TAG_NAME, "h2").text
        company_name = job.find_element(By.TAG_NAME, "h3").text
        location = job.find_element(By.TAG_NAME, "h4").text.strip()
        date_posted = job.find_element(By.CLASS_NAME, "job-listed").text.replace("Listed ", "")

        job_data = {
            "job_url": job_url,
            "job_title": job_title,
            "company_name": company_name,
            "location": location,
            "date_posted": date_posted
        }

        additional_details = scrape_additional_job_details(driver, job_url)
        job_data.update(additional_details)
        jobs.append(job_data)

    return jobs

def scrape_additional_job_details(driver, job_url):
    driver.get(job_url)

    # Wait for the job details to load
    job_summary = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-highlights"))
    )
    # Extract additional details
    details = {
        "salary": job_summary.find_elements(By.CSS_SELECTOR, ".job-summary li")[0].text,
        "contact": job_summary.find_elements(By.CSS_SELECTOR, ".job-summary li")[2].text,
        "employment_type": job_summary.find_elements(By.CSS_SELECTOR, ".job-summary li")[3].text,
        "job_type": job_summary.find_elements(By.CSS_SELECTOR, ".job-summary li")[4].text,
        "category": job_summary.find_elements(By.CSS_SELECTOR, ".job-summary li")[5].text,
        "sub_category": job_summary.find_elements(By.CSS_SELECTOR, ".job-summary li")[6].text,
        "listed_date": job_summary.find_elements(By.CSS_SELECTOR, ".job-summary li")[7].text.replace("Listed ", ""),
        "responsibilities": driver.find_element(By.XPATH,
                                                "//h4[contains(text(), 'Responsibilities')]/following-sibling::div").text,
        "skills_required": driver.find_element(By.XPATH,
                                               "//h4[contains(text(), 'Skills Required')]/following-sibling::div").text,
        "experience_required": driver.find_element(By.XPATH,
                                                   "//h4[contains(text(), 'Experience Required')]/following-sibling::div").text,
        "benefits": driver.find_element(By.XPATH, "//h4[contains(text(), 'Benefits')]/following-sibling::div").text,
    }

    return details

def main():
    # Initialize WebDriver
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to the website
        driver.get("https://job.id/search/")
        # Scrape job details
        jobs = scrape_job_details(driver)

        # Print the job information
        for job in jobs:
            print(job)

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()
