#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

SCANNER_ART = f'''{Colors.BOLD}
{Colors.CYAN}    █████{Colors.BLUE}╗ {Colors.CYAN}██{Colors.BLUE}╗   {Colors.CYAN}██{Colors.BLUE}╗{Colors.CYAN}████████{Colors.BLUE}╗ {Colors.CYAN}██████{Colors.BLUE}╗ {Colors.GREEN}███████{Colors.BLUE}╗{Colors.GREEN}██████{Colors.BLUE}╗  {Colors.GREEN}█████{Colors.BLUE}╗ {Colors.GREEN}███{Colors.BLUE}╗  {Colors.GREEN}██{Colors.BLUE}╗{Colors.GREEN}███{Colors.BLUE}╗  {Colors.GREEN}██{Colors.BLUE}╗{Colors.GREEN}███████{Colors.BLUE}╗{Colors.GREEN}██████{Colors.BLUE}╗{Colors.ENDC} 
{Colors.CYAN}   ██{Colors.BLUE}╔══{Colors.CYAN}██{Colors.BLUE}╗{Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║╚══{Colors.CYAN}██{Colors.BLUE}╔══╝{Colors.CYAN}██{Colors.BLUE}╔═══{Colors.CYAN}██{Colors.BLUE}╗{Colors.GREEN}██{Colors.BLUE}╔════╝{Colors.GREEN}██{Colors.BLUE}╔════╝{Colors.GREEN}██{Colors.BLUE}╔══{Colors.GREEN}██{Colors.BLUE}╗{Colors.GREEN}████{Colors.BLUE}╗ {Colors.GREEN}██{Colors.BLUE}║{Colors.GREEN}████{Colors.BLUE}╗ {Colors.GREEN}██{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}╔════╝{Colors.GREEN}██{Colors.BLUE}╔══{Colors.GREEN}██{Colors.BLUE}╗{Colors.ENDC}
{Colors.CYAN}   ███████{Colors.BLUE}║{Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║{Colors.GREEN}███████{Colors.BLUE}╗{Colors.GREEN}██{Colors.BLUE}║     {Colors.GREEN}███████{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}╔{Colors.GREEN}██{Colors.BLUE}╗{Colors.GREEN}██{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}╔{Colors.GREEN}██{Colors.BLUE}╗{Colors.GREEN}██{Colors.BLUE}║{Colors.GREEN}█████{Colors.BLUE}╗  {Colors.GREEN}██████{Colors.BLUE}╔╝{Colors.ENDC}
{Colors.CYAN}   ██{Colors.BLUE}╔══{Colors.CYAN}██{Colors.BLUE}║{Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║   {Colors.CYAN}██{Colors.BLUE}║╚════{Colors.GREEN}██{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}║     {Colors.GREEN}██{Colors.BLUE}╔══{Colors.GREEN}██{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}║╚{Colors.GREEN}████{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}║╚{Colors.GREEN}████{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}╔══╝  {Colors.GREEN}██{Colors.BLUE}╔══{Colors.GREEN}██{Colors.BLUE}╗{Colors.ENDC}
{Colors.CYAN}   ██{Colors.BLUE}║  {Colors.CYAN}██{Colors.BLUE}║╚{Colors.CYAN}██████{Colors.BLUE}╔╝   {Colors.CYAN}██{Colors.BLUE}║   ╚{Colors.CYAN}██████{Colors.BLUE}╔╝{Colors.GREEN}███████{Colors.BLUE}║╚{Colors.GREEN}██████{Colors.BLUE}╗{Colors.GREEN}██{Colors.BLUE}║  {Colors.GREEN}██{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}║ ╚{Colors.GREEN}███{Colors.BLUE}║{Colors.GREEN}██{Colors.BLUE}║ ╚{Colors.GREEN}███{Colors.BLUE}║{Colors.GREEN}███████{Colors.BLUE}╗{Colors.GREEN}██{Colors.BLUE}║  {Colors.GREEN}██{Colors.BLUE}║{Colors.ENDC}
{Colors.BLUE}   ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝{Colors.ENDC}

{Colors.RED}[{Colors.WHITE}█████████████████████{Colors.RED}] {Colors.CYAN}SYSTEM SCAN IN PROGRESS... {Colors.GREEN}98%{Colors.ENDC}
'''

def display_art(use_colors=True):
    """
    Display the ASCII art with optional colors.
    """
    # Enable Windows color support if needed
    import platform
    if platform.system() == 'Windows':
        import os
        os.system('color')

    if use_colors:
        print(SCANNER_ART)
    else:
        # Strip all ANSI escape codes
        import re
        clean_art = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', SCANNER_ART)
        print(clean_art)

def animate_progress():
    """
    Animate the progress bar
    """
    import time
    import os
    import sys

    for i in range(101):
        progress = '█' * (i // 5) + ' ' * (20 - (i // 5))
        sys.stdout.write(f'\r{Colors.RED}[{Colors.WHITE}{progress}{Colors.RED}] {Colors.CYAN}SYSTEM SCAN IN PROGRESS... {Colors.GREEN}{i}%{Colors.ENDC}')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n')

def main():
    display_art()
    # Uncomment next line for animation
    # animate_progress()

if __name__ == "__main__":
    main()
