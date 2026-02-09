from .utils import clear_screen
from .config import C, RR
from .search import search_dork


def dorks_menu(category, dorks_list):
    while True:
        clear_screen()
        print(f"{C}{category} DORKS{RR}")
        for i, dork in enumerate(dorks_list, 1):
            print(f"{C}{i}. {dork}{RR}")

        print(f"\n{C}Enter number / custom dork / -back{RR}")
        inp = input(f"{C}dorkbase {category.lower()}> {RR}").strip()

        if inp == "-back":
            break

        elif inp.isdigit():
            idx = int(inp) - 1
            if 0 <= idx < len(dorks_list):
                selected_dork = dorks_list[idx]
                print(f"{C}Selected dork: {selected_dork}{RR}")
                print(f"{C}Starting search...{RR}")
                search_dork(selected_dork)
            else:
                print(f"{C}Number out of range (1–{len(dorks_list)}){RR}")
                input(f"{C}Press enter to continue...{RR}")

        elif inp:
            print(f"{C}Searching custom dork: {inp}{RR}")
            search_dork(inp)

        else:
            print(f"{C}No input entered.{RR}")
            input(f"{C}Press enter...{RR}")
