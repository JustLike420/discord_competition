import urllib
import requests
import random
from dotenv import load_dotenv
import os


def get_winner(all_members: list, count: int) -> list:
    winners = random.sample(all_members, count)
    return winners


def print_banner():
    import pyfiglet

    banner = pyfiglet.figlet_format("TOURNAMENT")
    print(banner)


def main():
    print_banner()

    winners_count = int(input('[+] Input winners count: '))
    load_dotenv()
    discord_token = os.getenv('DISCORD_TOKEN')
    headers = {
        'authorization': discord_token
    }

    channel_id = os.getenv('CHANNEL_ID')
    message_id = os.getenv('MESSAGE_ID')
    reaction_id = os.getenv('REACTION_ID')
    encoded_emoji = urllib.parse.quote(reaction_id)

    flag = True
    all_members = []
    while True:
        if flag:
            url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{encoded_emoji}' \
                  f'?limit=100'
            flag = False
        else:
            url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{encoded_emoji}' \
                  f'?limit=100&after={last}'

        req = requests.get(url=url, headers=headers)
        data = req.json()

        if len(data):
            for person in data:
                all_members.append(person['username'] + '#' + person['discriminator'])
            last = data[-1]['id']
        else:
            break

    print(f'[+] Members count: {len(all_members)}\n')

    winners = get_winner(all_members, winners_count)

    with open('winners.txt', 'w', encoding='utf-8') as file:
        for i, winner in enumerate(winners):
            file.write(f'{i + 1} {winner}\n')

    print('[!] Results in winners.txt file.')


if __name__ == '__main__':
    main()
