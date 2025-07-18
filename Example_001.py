from playwright.sync_api import Playwright, sync_playwright, expect
import asyncio
import time

path=[
    r"C:\Users\Administrator\Desktop\dddwg\New folder (13)\testtt - Copy.txt",
    r"C:\Users\Administrator\Desktop\dddwg\New folder (13)\testtt.txt",
]

folderName="tttt111" 
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")
    
    page = context.new_page()
    url = "your url"
    page.goto(url, wait_until="domcontentloaded", timeout=100000)    
    
    # input("请在弹出的浏览器窗口中手动完成登录，然后回到命令行按回车继续...")
    # context.storage_state(path="auth.json")

    locator = page.get_by_text("Project Files")
    locator.wait_for(state="visible", timeout=2000000)  
    
    # page.screenshot(path="screenshot.png", full_page=True)

    page.get_by_test_id("resizable-frame-list").get_by_text("Model").click()
    page.get_by_test_id("resizable-frame-list").get_by_text("Model").click(button="right")
    page.get_by_text("Add subfolder").click()
    time.sleep(1)
    page.get_by_placeholder("Enter a folder name").fill(folderName)
    page.get_by_placeholder("Enter a folder name").press("Enter")
    time.sleep(1)
    page.get_by_text(folderName).click()
    page.get_by_test_id("drop-zone").get_by_role("gridcell", name=folderName).locator("div").nth(1).click()
    time.sleep(1)

    with page.expect_file_chooser() as fc_info:
        page.get_by_test_id("action-toolbar-split-button").click()
        page.get_by_test_id("modal-container").get_by_test_id("button").click()

        # page.get_by_text("Upload files").click()
        file_chooser = fc_info.value
        file_chooser.set_files(path)
        
    while True:
        text=page.get_by_text("1 file has been successfully uploaded.") if len(path)==1 else page.get_by_text(f"{len(path)} files have been successfully uploaded.")
        if text.is_visible():
            break
        else:
            time.sleep(1)
    
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
