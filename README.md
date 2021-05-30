# BinanceHedgeBot
Binance Futures Trading Bot (ab)using Hedge Mode


How the Bot works:

The Bot continously opens and closes Short Positions, at a given Price (TriggerOpenShortOrder)

Price is fetched via a Websocket, for Real Time Data

Use case for the Bot:


If you have a Long Position open, you have a fixed Liquidation Price. Only way to decrease it, would be addin Margin, or opening a Short Position with the same Amount / or bigger: 

Here is the automation of the Bot needed.

In case of unpredictable Market Movements, the Bot opens a Short Position, which will decrease the Liquidation Price of the Long into infinity (or as long as you can pay Funding Fee)







