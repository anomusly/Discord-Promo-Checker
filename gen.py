import os
import random
import string
import time
from pystyle import *
from colorama import Fore, Style, Back, init
init()

def clear_screen():
    try:
        os.system('cls')
    except:
        pass

def get_timestamp():
    from datetime import datetime, timezone
    current_time = datetime.now(timezone.utc)
    return current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def print_log(tag, content, color):
    return print(f"{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}GEN: {Fore.BLACK}{get_timestamp()}{Fore.WHITE}] [{color}{tag}{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}{content}{Style.RESET_ALL}")

def analyze_promo_patterns(sample_file=None):
    """Analyze existing promo codes to understand the pattern"""
    patterns = {
        'length': 24,
        'characters': string.ascii_letters + string.digits,
        'base_url': 'https://promos.discord.gg/',
        'case_sensitive': True,
        'char_frequency': {}
    }

    # If sample file provided, analyze it for better patterns
    if sample_file and os.path.exists(sample_file):
        try:
            with open(sample_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            codes = []
            for line in lines:
                line = line.strip()
                if 'promos.discord.gg/' in line:
                    code = line.split('promos.discord.gg/')[-1]
                    if code:
                        codes.append(code)

            if codes:
                # Analyze actual patterns
                lengths = [len(code) for code in codes]
                patterns['length'] = max(set(lengths), key=lengths.count)  # Most common length

                # Character frequency analysis
                all_chars = ''.join(codes)
                char_counts = {}
                for char in all_chars:
                    char_counts[char] = char_counts.get(char, 0) + 1

                patterns['char_frequency'] = char_counts
                patterns['analyzed_codes'] = len(codes)

                print_log('+', f'Analyzed {len(codes)} existing codes from {sample_file}', Fore.GREEN)
                print_log('>', f'Most common length: {patterns["length"]}', Fore.CYAN)

        except Exception as e:
            print_log('!', f'Error analyzing sample file: {e}', Fore.YELLOW)

    return patterns

def generate_promo_code(patterns, use_frequency=True):
    """Generate a single promo code based on analyzed patterns"""
    if use_frequency and patterns.get('char_frequency'):
        # Use weighted selection based on character frequency
        chars = list(patterns['char_frequency'].keys())
        weights = list(patterns['char_frequency'].values())
        code = ''.join(random.choices(chars, weights=weights, k=patterns['length']))
    else:
        # Use uniform random selection
        code = ''.join(random.choice(patterns['characters']) for _ in range(patterns['length']))

    full_url = patterns['base_url'] + code
    return full_url

def generate_multiple_promos(count, patterns, use_frequency=True, show_progress=True):
    """Generate multiple unique promo codes"""
    generated_codes = set()
    promos = []

    progress_interval = max(1, count // 20)  # Show progress every 5%

    while len(promos) < count:
        new_promo = generate_promo_code(patterns, use_frequency)
        # Ensure uniqueness
        if new_promo not in generated_codes:
            generated_codes.add(new_promo)
            promos.append(new_promo)

            # Show progress
            if show_progress and len(promos) % progress_interval == 0:
                progress = (len(promos) / count) * 100
                print_log('>', f'Progress: {progress:.1f}% ({len(promos)}/{count})', Fore.CYAN)

    return promos

def save_promos_to_file(promos, filename):
    """Save generated promos to a file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for promo in promos:
                f.write(promo + '\n')
        return True
    except Exception as e:
        print_log('!', f'Error saving to file: {e}', Fore.RED)
        return False

def display_banner():
    clear_screen()
    ascii_text = '''
                ██████╗ ██████╗  ██████╗ ███╗   ███╗ ██████╗      ██████╗ ███████╗███╗   ██╗
                ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
                ██████╔╝██████╔╝██║   ██║██╔████╔██║██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
                ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
                ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
                ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
    '''
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(ascii_text)))
    print('')
    print(f'{Fore.WHITE}[{Fore.BLUE}%{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}Discord Promo Code Generator')
    print(f'{Fore.WHITE}[{Fore.BLUE}%{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}Generates realistic Discord promo URLs')
    print('')

def get_user_input():
    """Get user input for generation parameters"""
    while True:
        try:
            count = input(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}How many promo codes to generate? {Fore.RED}>>> {Fore.WHITE}')
            count = int(count)
            if count <= 0:
                print_log('!', 'Please enter a positive number', Fore.RED)
                continue
            if count > 1000000:
                print_log('!', 'Maximum 1,000,000 codes per generation', Fore.RED)
                continue
            break
        except ValueError:
            print_log('!', 'Please enter a valid number', Fore.RED)

    filename = input(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}Output filename (default: generated_promos.txt): {Fore.RED}>>> {Fore.WHITE}')
    if not filename.strip():
        filename = 'generated_promos.txt'

    # Ask about sample file for pattern analysis
    sample_file = input(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}Sample file for pattern analysis (optional, press Enter to skip): {Fore.RED}>>> {Fore.WHITE}')
    if not sample_file.strip():
        sample_file = None

    # Ask about generation mode
    use_frequency = True
    if sample_file:
        freq_choice = input(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}Use frequency-based generation? (y/n, default: y): {Fore.RED}>>> {Fore.WHITE}')
        use_frequency = freq_choice.lower() != 'n'

    return count, filename, sample_file, use_frequency

def main():
    display_banner()

    # Get user input
    count, filename, sample_file, use_frequency = get_user_input()

    print('')

    # Analyze patterns from existing codes
    patterns = analyze_promo_patterns(sample_file)

    print_log('>', f'Pattern Analysis Complete', Fore.GREEN)
    print_log('>', f'Code Length: {patterns["length"]} characters', Fore.CYAN)
    print_log('>', f'Character Set: {len(patterns["characters"])} possible characters', Fore.CYAN)
    print_log('>', f'Base URL: {patterns["base_url"]}', Fore.CYAN)

    if patterns.get('analyzed_codes'):
        print_log('>', f'Analyzed {patterns["analyzed_codes"]} sample codes', Fore.CYAN)
        print_log('>', f'Frequency-based generation: {use_frequency}', Fore.CYAN)

    print('')
    print_log('@', f'Starting generation of {count} promo codes...', Fore.BLUE)

    start_time = time.time()

    # Generate promo codes
    try:
        promos = generate_multiple_promos(count, patterns, use_frequency)
        generation_time = time.time() - start_time

        print_log('+', f'Generated {len(promos)} unique promo codes in {generation_time:.2f}s', Fore.GREEN)

        # Save to file
        if save_promos_to_file(promos, filename):
            print_log('+', f'Saved to file: {filename}', Fore.GREEN)
        else:
            print_log('!', 'Failed to save to file', Fore.RED)
            return

        # Display some examples
        print('')
        print_log('>', 'Sample generated codes:', Fore.CYAN)
        for i, promo in enumerate(promos[:5]):
            print(f'{Fore.WHITE}  [{Fore.BLUE}{i+1}{Fore.WHITE}] {Fore.GREEN}{promo}')

        if len(promos) > 5:
            print(f'{Fore.WHITE}  ... and {len(promos) - 5} more codes')

        print('')
        print_log('#', f'Generation Complete!', Fore.BLUE)
        print_log('#', f'Total Generated: {Fore.BLUE}{len(promos)}', Fore.BLUE)
        print_log('#', f'File: {Fore.BLUE}{filename}', Fore.BLUE)
        print_log('#', f'Time Taken: {Fore.BLUE}{generation_time:.2f}s', Fore.BLUE)
        print_log('#', f'Rate: {Fore.BLUE}{len(promos)/generation_time:.0f} codes/sec', Fore.BLUE)

    except Exception as e:
        print_log('!', f'Error during generation: {e}', Fore.RED)
        return

    print('')
    print_log('?', f'Press {Fore.BLUE}Enter {Fore.WHITE}to exit', Fore.BLUE)
    input(f'{Style.BRIGHT}{Fore.CYAN}~~')

if __name__ == '__main__':
    main()
