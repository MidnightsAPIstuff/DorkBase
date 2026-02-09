from .utils import clear_screen
from .config import G, C, RR
from .search import search_dork


def dorks_menu(category, dorks_list):
    while True:
        clear_screen()
        print(f"{C}{category} DORKS{RR}")
        for i, dork in enumerate(dorks_list, 1):
            print(f"{G}{i}. {dork}{RR}")

        print(f"\n{C}Enter number / custom dork / -back{RR}")
        inp = input(f"{C}dorkbase {category.lower()}{RR}> ").strip()

        if inp == "-back":
            break

        elif inp.isdigit():
            try:
                idx = int(inp) - 1
                if 0 <= idx < len(dorks_list):
                    selected_dork = dorks_list[idx]
                    print(f"{Y}Selected dork: {selected_dork}{RR}")
                    print(f"{Y}Starting search...{RR}")
                    search_dork(selected_dork)
                else:
                    print(f"{R}Number out of range (1-{len(dorks_list)}){RR}")
                    input(f"{C}Press enter to continue...{RR}")
            except Exception as e:
                print(f"{R}Error while starting search: {str(e)}{RR}")
                input(f"{C}Press enter to continue...{RR}")

        else:
            if inp:
                print(f"{Y}Searching custom dork: {inp}{RR}")
                try:
                    search_dork(inp)
                except Exception as e:
                    print(f"{R}Error during custom search: {str(e)}{RR}")
                    input(f"{C}Press enter to continue...{RR}")
            else:
                print(f"{R}No input detected.{RR}")
                input(f"{C}Press enter...{RR}")