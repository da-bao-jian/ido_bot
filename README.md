This is a IDO bot that scans pancakeswap pools for matching pairs to snipe. 

On a high level, it does the following: 
* Bot runs an event loop in the background to monitor the newly created pools
* If the `PairCreated` event matches the desired token pair, bot will send a transaction to purchase the underlying tokens

Since this is only a weekend build, many features can be improved by further development, to name a few:
* amount should be adjusted dynamically according to the pool liquidity;
* bot should implement a emergency sell mechanism. 

To use the bot, put wallet address and private key inside of the `.env` file.

Intall `pipenv` if you don't have it. 

Run the following command:
```
pipenv install && pipenv shell
```
```
python main.py
```
