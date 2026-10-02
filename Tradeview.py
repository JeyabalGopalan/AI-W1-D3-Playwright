# ==========================================
# TRADINGVIEW MARKETS BOT
# ==========================================
# chromium → TradingView → Click Markets
# → Wait for page → Extract information
# → Screenshot → Save text → Close browser


# ==========================================
# IMPORT LIBRARIES
# ==========================================

from playwright.sync_api import sync_playwright
from datetime import datetime


# ==========================================
# START PLAYWRIGHT
# ==========================================

with sync_playwright() as p:

    print("Launching the Chromium browser...")

    # Open Chromium browser
    # headless=False means we can see the browser
    browser = p.chromium.launch(headless=False)


    # ==========================================
    # CREATE NEW PAGE
    # ==========================================

    page = browser.new_page()


    # ==========================================
    # OPEN TRADINGVIEW
    # ==========================================

    print("Navigating to TradingView...")

    page.goto("https://in.tradingview.com/markets")


    # ==========================================
    # FIND MARKETS OPTION
    # ==========================================

    print("Searching for Markets option...")

    # Find the element whose text is exactly "Markets"
    markets = page.get_by_text("Markets", exact=True)


    # Wait until Markets is visible
    markets.wait_for(state="visible")

    print("Markets option found.")


    # ==========================================
    # CLICK MARKETS
    # ==========================================

    print("Clicking Markets...")

    markets.click()


    # ==========================================
    # WAIT FOR PAGE TO LOAD
    # ==========================================

    print("Waiting for TradingView page to load...")

    page.wait_for_load_state("load")

    print("TradingView page loaded successfully.")


    # ==========================================
    # EXTRACT PAGE INFORMATION
    # ==========================================

    print("Extracting TradingView information...")

    # Get all visible text from the page
    market_report = page.locator("body").inner_text()

    print("\n==========================================")
    print("       TRADINGVIEW MARKET REPORT")
    print("==========================================")

    print(market_report)


    # ==========================================
    # TAKE SCREENSHOT
    # ==========================================

    print("\nTaking screenshot...")

    page.screenshot(
        path="tradingview_markets.png",
        full_page=True
    )

    print("Screenshot saved as tradingview_markets.png")


    # ==========================================
    # SAVE REPORT TO TEXT FILE
    # ==========================================

    print("Saving TradingView report...")

    with open("tradingview_markets.txt", "w", encoding="utf-8") as file:

        # Write report title
        file.write(
            f"TradingView Market Report\n"
            f"Generated on: {datetime.now()}\n\n"
        )

        # Write extracted page information
        file.write(market_report)


    print("TradingView report saved as tradingview_markets.txt")


    # ==========================================
    # CLOSE BROWSER
    # ==========================================

    print("Closing the browser...")

    browser.close()

    print("\n==========================================")
    print("       AUTOMATION COMPLETED")
    print("==========================================")