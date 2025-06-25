# ACC_Playwright_Test_Example

## Example_001.py Help

This script demonstrates how to use Playwright to automate the process of creating folders or uploading files in ACC (a web application).

### Usage
1. Make sure you have installed the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Update the `url` variable in `Example_001.py` to your ACC web application address.
3. (Optional) Adjust the `path` and `folderName` variables as needed for your use case.
4. Run the script:
   ```bash
   python Example_001.py
   ```
5. Follow the instructions in the browser window to complete login if prompted.

### Features
- Logs into the ACC web application using Playwright.
- Creates a new folder with a specified name in ACC.
- Uploads one or more files to the created folder in ACC.

---

## get_auth.py Help

This script is used to obtain and save authentication information (login cookies and tokens) for the ACC web application.

### Usage
1. Update the `url` variable in `get_auth.py` to your ACC web application login page.
2. Run the script:
   ```bash
   python get_auth.py
   ```
3. A browser window will open. Manually complete the login process.
4. After logging in, return to the command line and press Enter.
5. The authentication state will be saved to a file named `auth.json`, which can be used by other scripts (such as `Example_001.py`) for automated login.

### Author
Andy Zhu

