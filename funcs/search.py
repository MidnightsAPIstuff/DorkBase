import webbrowser
from urllib.parse import quote_plus

from .config import C, RR
from .utils import clear_screen


def search_dork(dork):
    print(f"{C}Preparing Google search for: {dork}{RR}")

    # Build clean Google search URL
    encoded_dork = quote_plus(dork.strip())
    google_url = f"https://www.google.com/search?q={encoded_dork}"

    try:
        # This opens in the default browser (usually the user's main Chrome)
        # If Chrome is set as default, it will use the existing profile with login
        webbrowser.open(google_url, new=2)  # new=2 → new tab if possible

        clear_screen()
        print(f"{C}Opened in your regular Chrome:{RR}")
        print(f"   {google_url}")
        print()
        print(f"{C}→ Search should now be visible in a new tab.{RR}")
        print(f"{C}→ Use your normal browser controls (next/prev pages, click links etc.){RR}")
        print(f"{C}→ Close this terminal window or press Enter when done.{RR}")
        input(f"{C}Press Enter to return to menu...{RR}")

    except Exception as e:
        print(f"{C}Failed to open browser: {str(e)}{RR}")
        print(f"{C}You can manually open this URL:{RR}")
        print(f"   {google_url}")
        input(f"{C}Press Enter to continue...{RR}")
