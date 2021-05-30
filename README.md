# BinanceHedgeBot
Binance Futures Trading Bot (ab)using Hedge Mode


How the Bot works:

The Bot continously opens and closes Short Positions, at a given Price (TriggerOpenShortOrder)

Price is fetched via a Websocket, for Real Time Data

Use case for the Bot:


If you have a Long Position open, you have a fixed Liquidation Price. Only way to decrease it, would be addin Margin, or opening a Short Position with the same Amount / or bigger: 

Here is the automation of the Bot needed.

In case of unpredictable Market Movements, the Bot opens a Short Position, which will decrease the Liquidation Price of the Long into infinity (or as long as you can pay Funding Fee)


Installation:

the following additional Python Libraries are required:

ccxt
websocket-client


Configuration:

Define your Symbol, Code has ETH/USDT as example

if changed, change the socket to listen to in Line 52 aswell

TriggerOpenShortOrder =  This is the Price, by which the Short Limit Order will be placed. The Bot will open this Limit Order, as soon as Market Price is + 2$ above it (can be changed in Line 17)

OrderAmount = Amount in $ you want to spend for the Trade

OrderLeverage = Leverage which will be used


