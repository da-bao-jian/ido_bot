from bot import Bot

bsc_addr = {
    "WBNB_addr": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
    "CAKE_addr":"0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82" #just for testing
}

def main():

    bot = Bot(
        rpc_endpoint="https://bsc-dataseed.binance.org/",
        t2s=bsc_addr["WBNB_addr"],
        t2b=bsc_addr["CAKE_addr"],
        gas=5,
        slippage=0,
        test=True
    )
    bot.run()

main()