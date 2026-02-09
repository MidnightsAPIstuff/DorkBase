from funcs.utils import clear_screen
from funcs.config import (
    BANNER, HELP_TEXT, CREDITS_TEXT,
    C, RR,
    SQL_DORKS, LOG_DORKS, IP_DORKS, XSS_DORKS
)
from funcs.dorks_menu import dorks_menu
from funcs.search import search_dork


def main():
    while True:
        clear_screen()
        print(BANNER)
        print(f"""
                                   {C}╔═════════════════════════════════════════════════╗{RR}
                                   {C}║{RR}  -credits     -  shows credits                  {C}║{RR}
                                   {C}║{RR}  -exit        -  exits tool                     {C}║{RR}
                                   {C}║{RR}  -help        -  displays help information      {C}║{RR}
                                   {C}╚═════════════════════════════════════════════════╝{RR}
        """)

        cmd = input(f"{C}dorkbase{RR}> ").strip().lower()

        if cmd == "-credits":
            clear_screen()
            print(CREDITS_TEXT)
            input(f"{C}dorkbase{RR}> ")

        elif cmd == "-help":
            clear_screen()
            print(HELP_TEXT)
            input(f"{C}dorkbase{RR}> ")

        elif cmd == "-exit":
            break

        # ── All categories ───────────────────────────────────────────────
        elif cmd in ("-sql", "-sql dorks", "-sqldorks"):
            dorks_menu("SQL", SQL_DORKS)

        elif cmd in ("-log", "-log dorks", "-logs"):
            dorks_menu("LOG", LOG_DORKS)

        elif cmd in ("-ip", "-ip dorks", "-ipdorks", "-cams"):
            dorks_menu("IP/Cams", IP_DORKS)

        elif cmd in ("-xss", "-xss dorks"):
            dorks_menu("XSS", XSS_DORKS)

        elif cmd == "-dorks":
            clear_screen()
            print(f"""
                                   {C}╔═════════════════════════════════════════════════╗{RR}
                                   {C}║{RR}          Available Dork Categories               {C}║{RR}
                                   {C}║{RR}  -sql / -sql dorks     →  SQL Injection         {C}║{RR}
                                   {C}║{RR}  -log / -log dorks     →  Logs & Access Logs    {C}║{RR}
                                   {C}║{RR}  -ip  / -ip dorks      →  Cameras & Devices     {C}║{RR}
                                   {C}║{RR}  -xss / -xss dorks     →  Cross-Site Scripting   {C}║{RR}
                                   {C}║{RR}  -back                 →  return to main         {C}║{RR}
                                   {C}╚═════════════════════════════════════════════════╝{RR}
            """)
            input(f"{C}Press enter to continue...{RR}")

        else:
            if cmd.strip():
                print(f"{C}Unknown command: '{cmd}'{RR}")
                print(f"{C}Type -help for available commands{RR}")
                print(f"{C}To search a custom dork → use one of the category menus (-sql, -log, -ip, -xss){RR}")
                input(f"{C}Press enter...{RR}")
            # empty input → just loop

if __name__ == "__main__":
    main()
