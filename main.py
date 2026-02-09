from funcs.utils import clear_screen
from funcs.config import (
    BANNER, HELP_TEXT, CREDITS_TEXT,
    C, RR,
    SQL_DORKS, IP_DORKS
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

        elif cmd in ("-sql dorks", "-sqldorks", "-sql"):
            dorks_menu("SQL", SQL_DORKS)

        elif cmd in ("-ip dorks", "-ipdorks", "-ip"):
            dorks_menu("IP", IP_DORKS)

        elif cmd == "-dorks":
            clear_screen()
            print(f"""
                                   {C}╔═════════════════════════════════════════════════╗{RR}
                                   {C}║{RR}  Dorks Categories:                              {C}║{RR}
                                   {C}║{RR}  -sql dorks     -  SQL injection dorks          {C}║{RR}
                                   {C}║{RR}  -ip dorks      -  IP / camera dorks            {C}║{RR}
                                   {C}║{RR}  -back          -  return to main               {C}║{RR}
                                   {C}╚═════════════════════════════════════════════════╝{RR}
            """)
            input(f"{C}dorkbase{RR}> ")

        elif cmd:
            # Allow direct dork search from main prompt
            search_dork(cmd)

        else:
            continue


if __name__ == "__main__":
    main()