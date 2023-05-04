from API import *
import ccxt
import random
import time

def binance_withdraw(address, amount, wallet_number, chain, token):
    exchange = ccxt.binance({
        'apiKey': binance_apikey,
        'secret': binance_apisecret,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    try:
        exchange.withdraw(
            code=token,
            amount=amount,
            address=address,
            tag=None,
            params={
                "network": chain
            }
        )
        print(f'\n[Binance] Вывел {amount} {token} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n[Binance] Не удалось вывести {amount} {token}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)

def okx_withdraw(address, amount_to_withdrawal, wallet_number, chain, token):
    exchange = ccxt.okx({
        'apiKey': okx_apikey,
        'secret': okx_apisecret,
        'password': okx_passphrase,
        'enableRateLimit': True,
    })

    try:
        chainName = token + "-" + chain
        fee = get_withdrawal_fee(token, chainName)
        exchange.withdraw(token, amount_to_withdrawal, address,
            params={
                "toAddress": address,
                "chainName": chainName,
                "dest": 4,
                "fee": fee,
                "pwd": '-',
                "amt": amount_to_withdrawal,
                "network": chain
            }
        )

        print(f'\n[OKx] Вывел {amount_to_withdrawal} {token} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n[OKx] Не удалось вывести {amount_to_withdrawal} {token}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)

def bybit_withdraw(address, amount_to_withdrawal, wallet_number, chain, token):
    exchange = ccxt.bybit({
        'apiKey': bybit_apikey,
        'secret': bybit_apisecret,
    })

    try:
        exchange.withdraw(
            code=token,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={
                "forceChain": 1,
                "network": chain
            }
        )
        print(f'\n[ByBit] Вывел {amount_to_withdrawal} {token} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n[ByBit] Не удалось вывести {amount_to_withdrawal} {token}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)

def gate_withdraw(address, amount_to_withdrawal, wallet_number, chain, token):
    exchange = ccxt.gate({
        'apiKey': gate_apikey,
        'secret': gate_apisecret,
    })

    try:
        exchange.withdraw(
            code=token,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": chain
            }
        )
        print(f'\n[Gate.io] Вывел {amount_to_withdrawal} {token} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n[Gate.io] Не удалось вывести {amount_to_withdrawal} {token}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)

def kucoin_withdraw(address, amount_to_withdrawal, wallet_number, chain, token):
    exchange = ccxt.kucoin({
        'apiKey': kucoin_apikey,
        'secret': kucoin_apisecret,
        'password': kucoin_passphrase,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=token,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": chain
            }
        )
        print(f'\n[Kucoin] Вывел {amount_to_withdrawal} {token} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n[Kucoin] Не удалось вывести {amount_to_withdrawal} {token}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)

def mexc_withdraw(address, amount_to_withdrawal, wallet_number, chain, token):
    exchange = ccxt.mexc({
        'apiKey': mexc_apikey,
        'secret': mexc_apisecret,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=token,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": chain
            }
        )
        print(f'\n[MEXC] Вывел {amount_to_withdrawal} {token} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n[MEXC] Не удалось вывести {amount_to_withdrawal} {token}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)

def huobi_withdraw(address, amount_to_withdrawal, wallet_number, chain, token):
    exchange = ccxt.huobi({
        'apiKey': huobi_apikey,
        'secret': huobi_apisecret,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=token,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": chain
            }
        )
        print(f'\n[Huobi] Вывел {amount_to_withdrawal} {token} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n[Huobi] Не удалось вывести {amount_to_withdrawal} {token}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)

def choose_cex(address, amount_to_withdrawal, wallet_number, chain, token, switch_cex):
    if switch_cex == "binance":
        binance_withdraw(address, amount_to_withdrawal, wallet_number, chain, token)
    elif switch_cex == "okx":
        okx_withdraw(address, amount_to_withdrawal, wallet_number, chain, token)
    elif switch_cex == "gate":
        gate_withdraw(address, amount_to_withdrawal, wallet_number, chain, token)
    elif switch_cex == "huobi":
        huobi_withdraw(address, amount_to_withdrawal, wallet_number, chain, token)
    elif switch_cex == "kucoin":
        kucoin_withdraw(address, amount_to_withdrawal, wallet_number, chain, token)
    elif switch_cex == "mexc":
        mexc_withdraw(address, amount_to_withdrawal, wallet_number, chain, token)
    else:
        raise ValueError("Неверное значение CEX. Поддерживаемые значения: binance, okx, gate, huobi, kucoin, mexc.")

def get_withdrawal_fee(token, chainName):
    exchange = ccxt.okx({
        'apiKey': okx_apikey,
        'secret': okx_apisecret,
        'password': okx_passphrase,
        'enableRateLimit': True,
        # 'proxies': proxies,
    })
    currencies = exchange.fetch_currencies()
    for currency in currencies:
        if currency == token:
            currency_info = currencies[currency]
            network_info = currency_info.get('networks', None)
            if network_info:
                for network in network_info:
                    network_data = network_info[network]
                    network_id = network_data['id']
                    if network_id == chainName:
                        withdrawal_fee = currency_info['networks'][network]['fee']
                        if withdrawal_fee == 0:
                            return 0
                        else:
                            return withdrawal_fee
    raise ValueError(f"     не могу получить сумму комиссии, проверьте значения symbolWithdraw и network")

def shuffle(wallets_list, shuffle_wallets):
    numbered_wallets = list(enumerate(wallets_list, start=1))
    if shuffle_wallets.lower() == "yes":
        random.shuffle(numbered_wallets)
    return numbered_wallets

def get_token_price(token, switch_cex):
    if switch_cex == "binance":
        exchange = ccxt.binance()
    elif switch_cex == "okx":
        exchange = ccxt.okx()
    elif switch_cex == "gate":
        exchange = ccxt.gate()
    elif switch_cex == "huobi":
        exchange = ccxt.huobi()
    elif switch_cex == "kucoin":
        exchange = ccxt.kucoin()
    elif switch_cex == "mexc":
        exchange = ccxt.mexc()
    else:
        raise ValueError("Неверное значение CEX. Поддерживаемые значения: binance, okx, gate, huobi, kucoin, mexc.")
    price = exchange.fetch_ticker(f'{token}/USDT')['last']
    return price

def workaem(token, chain, switch_cex, amount_usd, decimal_places, shuffle_wallets, delay):
    token = token.upper()
    switch_cex = switch_cex.lower()
    price = get_token_price(token, switch_cex)
    amount = [amount_usd[0]/price, amount_usd[1]/price] 

    with open("wallets.txt", "r") as f:
        print("\
        ██████╗░░█████╗░███╗░░██╗░█████╗░███╗░░██╗░█████╗░  ░█████╗░██╗░░░░░██╗░░░░░██╗░█████╗░███╗░░██╗░█████╗░███████╗\n\
        ██╔══██╗██╔══██╗████╗░██║██╔══██╗████╗░██║██╔══██╗  ██╔══██╗██║░░░░░██║░░░░░██║██╔══██╗████╗░██║██╔══██╗██╔════╝\n\
        ██████╦╝███████║██╔██╗██║███████║██╔██╗██║███████║  ███████║██║░░░░░██║░░░░░██║███████║██╔██╗██║██║░░╚═╝█████╗░░\n\
        ██╔══██╗██╔══██║██║╚████║██╔══██║██║╚████║██╔══██║  ██╔══██║██║░░░░░██║░░░░░██║██╔══██║██║╚████║██║░░██╗██╔══╝░░\n\
        ██████╦╝██║░░██║██║░╚███║██║░░██║██║░╚███║██║░░██║  ██║░░██║███████╗███████╗██║██║░░██║██║░╚███║╚█████╔╝███████╗\n\
        ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝\n\
        ")

        wallets_list = [row.strip() for row in f if row.strip()]
        numbered_wallets = shuffle(wallets_list, shuffle_wallets)

        print(f'Количество кошельков: {len(wallets_list)}')
        print(f"Биржа: {switch_cex}")
        print(f"Сумма в $: ${amount_usd[0]} - ${amount_usd[1]}")
        print(f"Сумма в тоекенах: {amount[0]} - {amount[1]} {token}")
        print(f"Сеть: {chain}")

        for wallet_number, address in numbered_wallets:
            amount_to_withdrawal = round(random.uniform(amount[0], amount[1]), decimal_places)
            choose_cex(address, amount_to_withdrawal, wallet_number, chain, token, switch_cex)
            time.sleep(random.randint(delay[0], delay[1]))
    f.close()
    print(f"\n{token} {chain} VSE\n")
