import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests
import os
import ta  # Technical Analysis library

st.set_page_config(page_title="TradeSense (Educational Only)", page_icon="logo/TradeSense transparent.png")
st.image("logo/TradeSense transparent.png", width=120)

# ----- Banner -----
st.markdown(
    "<div style='background-color: #FFF3CD; padding: 10px; border-radius: 8px; border: 1px solid #FFEEBA; color: #8A6D3B;'>"
    "<b>Educational only:</b> This app does NOT provide financial advice. Recommendations are for learning and demo purposes only.</div><br>",
    unsafe_allow_html=True,
)

st.title("TradeSense :chart_with_upwards_trend:")

# ===== SIDEBAR: About & Portfolio =====
st.sidebar.image("logo/TradeSense transparent.png", width=80)
st.sidebar.title("TradeSense")

st.sidebar.markdown("---")
st.sidebar.header("About TradeSense")
st.sidebar.write(
    "TradeSense helps you analyze NASDAQ stocks with educational charts, news, and company info. "
    "It's for learning only, not investment advice."
)

st.sidebar.markdown("---")
st.sidebar.header("📈 My Mock Portfolio")

# ===== Mock Portfolio Simulator (Session State) =====
if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}
if "cash" not in st.session_state:
    st.session_state.cash = 10000.0  # Start with $10,000

add_ticker = st.sidebar.text_input("Add Ticker (e.g. AAPL)").strip().upper()
add_qty = st.sidebar.number_input("Quantity", min_value=1, max_value=10000, value=1, step=1)
if st.sidebar.button("Buy (Add)"):
    if add_ticker:
        # Get latest price
        try:
            latest_price = yf.Ticker(add_ticker).history(period="1d")['Close'][-1]
        except Exception:
            latest_price = 0
        total_cost = latest_price * add_qty

        if total_cost == 0:
            st.sidebar.warning(f"Could not fetch price for {add_ticker}.")
        elif total_cost > st.session_state.cash:
            st.sidebar.warning(f"Not enough cash! You need ${total_cost:,.2f}, but only have ${st.session_state.cash:,.2f}.")
        else:
            st.session_state.portfolio.setdefault(add_ticker, 0)
            st.session_state.portfolio[add_ticker] += add_qty
            st.session_state.cash -= total_cost
            st.sidebar.success(f"Bought {add_qty} {add_ticker} at ${latest_price:.2f} each (${total_cost:,.2f}).")

# Show portfolio table and value
if st.session_state.portfolio:
    port_df = pd.DataFrame(list(st.session_state.portfolio.items()), columns=["Ticker", "Quantity"])
    try:
        # Get latest prices
        prices = {}
        for tkr in st.session_state.portfolio.keys():
            try:
                prices[tkr] = yf.Ticker(tkr).history(period="1d")['Close'][-1]
            except Exception:
                prices[tkr] = 0
        port_df["Latest Price"] = port_df["Ticker"].map(prices)
        port_df["Market Value"] = port_df["Quantity"] * port_df["Latest Price"]
        st.sidebar.dataframe(port_df, hide_index=True)
        st.sidebar.write(f"**Total Portfolio Value: ${port_df['Market Value'].sum():,.2f}**")
    except Exception:
        st.sidebar.dataframe(port_df, hide_index=True)
        st.sidebar.write("Error fetching prices.")

    # Sell logic
    sell_ticker = st.sidebar.selectbox("Sell Ticker", [""] + list(st.session_state.portfolio.keys()))
    sell_qty = st.sidebar.number_input("Sell Quantity", min_value=1, max_value=10000, value=1, step=1, key="sell_qty")
    if st.sidebar.button("Sell"):
        if sell_ticker and sell_ticker in st.session_state.portfolio:
            try:
                latest_price = yf.Ticker(sell_ticker).history(period="1d")['Close'][-1]
            except Exception:
                latest_price = 0
            sell_qty_final = min(sell_qty, st.session_state.portfolio[sell_ticker])
            st.session_state.portfolio[sell_ticker] -= sell_qty_final
            st.session_state.cash += sell_qty_final * latest_price
            if st.session_state.portfolio[sell_ticker] <= 0:
                del st.session_state.portfolio[sell_ticker]
            st.sidebar.success(f"Sold {sell_qty_final} {sell_ticker} at ${latest_price:.2f} each (${sell_qty_final * latest_price:,.2f}).")
else:
    st.sidebar.info("Your mock portfolio is empty. Add stocks above!")

st.sidebar.write(f"**Cash Remaining:** ${st.session_state.cash:,.2f}")

# ===== MAIN APP =====

# ---- Helper: Human Readable Large Numbers -----
def human_format(num):
    if not num or num == 0:
        return "N/A"
    for unit in ['','K','M','B','T']:
        if abs(num) < 1000.0:
            return f"{num:3.1f}{unit}"
        num /= 1000.0
    return f"{num:.1f}P"

# ---- Simple Sentiment Function ----
def get_sentiment(text):
    positive_keywords = [
        "surge", "soar", "beats", "record", "growth", "profit", "acquire", "win", "rises", "gains",
        "up", "tops", "outperform", "strong", "raises", "expands", "positive", "improves"
    ]
    negative_keywords = [
        "slump", "drops", "lawsuit", "misses", "loss", "decline", "falls", "drops", "down",
        "warning", "recall", "layoff", "cuts", "negative", "disappoint", "miss"
    ]
    text_lower = text.lower()
    if any(word in text_lower for word in positive_keywords):
        return "🟢 Positive"
    elif any(word in text_lower for word in negative_keywords):
        return "🔴 Negative"
    else:
        return "🟡 Neutral"

# ----- News Fetching Function -----
def get_news(ticker, api_key):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={ticker}&language=en&sortBy=publishedAt&pageSize=5&apiKey={api_key}"
    )
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("status") == "ok":
            return data["articles"]
        else:
            return []
    except Exception:
        return []

# ----- Timeframes Map -----
timeframes = {
    "1 Month": "1mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "2 Years": "2y"
}

# ===== Ticker Input & Selection =====
st.markdown("---")
st.header("🔍 Analyze a Stock")
ticker = st.text_input("NASDAQ Stock Ticker (e.g. AAPL, TSLA, MSFT)").strip().upper()
timeframe = st.selectbox(
    "Select timeframe for analysis:",
    list(timeframes.keys()),
    index=1
)
period = timeframes[timeframe]

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        df = stock.history(period=period)

        if df.empty:
            st.warning("No historical data found for this ticker.")
        else:
            # ---- COMPANY PROFILE & METRICS ----
            st.markdown("---")
            st.header("🏢 Company Profile & Key Metrics")
            long_name = info.get('longName', ticker)
            business_summary = info.get('longBusinessSummary', None)
            ceo = info.get('companyOfficers', [{}])[0].get('name', None)
            market_cap = info.get('marketCap', None)
            dividend_yield = info.get('dividendYield', None)
            hq = info.get('city', '') + (', ' + info.get('state', '') if info.get('state') else '')
            founded = info.get('startDate', None)
            website = info.get('website', None)

            col1, col2 = st.columns([2,2])

            with col1:
                if business_summary:
                    st.write(f"**Description:** {business_summary}")
                if ceo:
                    st.write(f"**CEO:** {ceo}")
                if market_cap:
                    st.write(f"**Market Cap:** {human_format(market_cap)} USD")
                if dividend_yield:
                    st.write(f"**Dividend Yield:** {dividend_yield*100:.2f}%")
            with col2:
                if hq.strip(', '):
                    st.write(f"**Headquarters:** {hq.strip(', ')}")
                if founded:
                    st.write(f"**Founded:** {pd.to_datetime(founded, unit='s').year}")
                if website:
                    st.write(f"**Website:** [{website}]({website})")

            # ---- TECHNICAL EXPLANATIONS ----
            st.info("**SMA:** Simple Moving Average. Shows price trends over a set period.")
            st.info("**RSI:** Relative Strength Index (14 days). Measures recent price momentum; above 70 = overbought, below 30 = oversold.")
            st.info("**P/E Ratio:** Price to Earnings. Compares stock price to company earnings; a basic value indicator.")

            # ---- Calculate Indicators ----
            close = df['Close']
            price = close.iloc[-1]
            pe_ratio = info.get('trailingPE', None)
            sector = info.get('sector', 'N/A')

            # SMAs
            df['SMA50'] = close.rolling(window=50).mean()
            df['SMA200'] = close.rolling(window=200).mean()

            # RSI (14-period)
            df['RSI14'] = ta.momentum.RSIIndicator(close, window=14).rsi()

            # Sector P/E averages (static for demo; can use dynamic API later)
            sector_pe_map = {
                "Technology": 28,
                "Healthcare": 20,
                "Financial Services": 14,
                "Consumer Cyclical": 25,
                "Industrials": 20,
                "Energy": 12,
                "Consumer Defensive": 19,
                "Communication Services": 18,
                "Utilities": 16,
                "Real Estate": 18,
                "Basic Materials": 15,
                "N/A": 20
            }
            sector_pe_avg = sector_pe_map.get(sector, 20)

            # ---- Show Chart ----
            st.markdown("---")
            st.header("📊 Price Trend & Technical Indicators")
            chart_type = st.selectbox(
                "Choose chart type", 
                ("Candlestick with SMAs", "Line Chart with SMAs & RSI")
            )

            if chart_type == "Candlestick with SMAs":
                fig = go.Figure()
                fig.add_trace(go.Candlestick(
                    x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='Candlestick'
                ))
                fig.add_trace(go.Scatter(
                    x=df.index, y=df['SMA50'],
                    line=dict(color='royalblue', width=2), name='SMA 50'
                ))
                fig.add_trace(go.Scatter(
                    x=df.index, y=df['SMA200'],
                    line=dict(color='orange', width=2), name='SMA 200'
                ))
                fig.update_layout(
                    xaxis_title="Date",
                    yaxis_title="Price (USD)",
                    template="plotly_white",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=df.index, y=df['Close'], mode='lines', name='Close Price'
                ))
                fig.add_trace(go.Scatter(
                    x=df.index, y=df['SMA50'],
                    line=dict(color='royalblue', width=2), name='SMA 50'
                ))
                fig.add_trace(go.Scatter(
                    x=df.index, y=df['SMA200'],
                    line=dict(color='orange', width=2), name='SMA 200'
                ))
                fig.update_layout(
                    xaxis_title="Date",
                    yaxis_title="Price (USD)",
                    template="plotly_white",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)

                # RSI Chart
                st.markdown("#### Relative Strength Index (RSI 14)")
                fig_rsi = go.Figure()
                fig_rsi.add_trace(go.Scatter(
                    x=df.index, y=df['RSI14'], mode='lines', name='RSI 14'
                ))
                fig_rsi.add_hline(y=70, line_dash="dot", line_color="red", annotation_text="Overbought", annotation_position="top left")
                fig_rsi.add_hline(y=30, line_dash="dot", line_color="green", annotation_text="Oversold", annotation_position="bottom left")
                fig_rsi.update_layout(
                    yaxis_title="RSI",
                    template="plotly_white",
                    height=250
                )
                st.plotly_chart(fig_rsi, use_container_width=True)

            # ---- Display News Headlines with Sentiment, in Expander ----
            st.markdown("---")
            st.header("📰 Latest News Headlines")
            news_api_key = os.environ.get("NEWS_API_KEY")
            with st.expander("Click to expand/collapse news"):
                if news_api_key:
                    news = get_news(ticker, news_api_key)
                    if news:
                        for article in news:
                            sentiment = get_sentiment(article['title'])
                            st.markdown(
                                f"- **{sentiment}** &nbsp; [{article['title']}]({article['url']}) "
                                f"<span style='font-size: 0.8em;'>({article['source']['name']})</span>",
                                unsafe_allow_html=True
                            )
                    else:
                        st.info("No recent news found for this stock.")
                else:
                    st.info("Add your NewsAPI.org key to an environment variable named `NEWS_API_KEY` to see latest headlines here.")

            # ---- Recommendation Logic ----
            st.markdown("---")
            st.header("🎯 Educational Recommendation")
            reasons = []
            # Use latest available SMAs for logic
            latest_sma_50 = df['SMA50'].iloc[-1] if not np.isnan(df['SMA50'].iloc[-1]) else None
            latest_sma_200 = df['SMA200'].iloc[-1] if not np.isnan(df['SMA200'].iloc[-1]) else None

            if latest_sma_50 and price > latest_sma_50:
                reasons.append("The stock price is above its 50-day moving average (positive momentum).")
            else:
                reasons.append("The stock price is below its 50-day moving average (caution).")

            if latest_sma_200 and price > latest_sma_200:
                reasons.append("The stock price is above its 200-day moving average (long-term strength).")
            elif latest_sma_200:
                reasons.append("The stock price is below its 200-day moving average (long-term caution).")

            if pe_ratio is not None:
                if pe_ratio < sector_pe_avg:
                    reasons.append(f"The P/E ratio ({pe_ratio:.1f}) is below the sector average ({sector_pe_avg}).")
                else:
                    reasons.append(f"The P/E ratio ({pe_ratio:.1f}) is above the sector average ({sector_pe_avg}).")
            else:
                reasons.append("P/E ratio not available.")

            latest_rsi = df['RSI14'].iloc[-1]
            if latest_rsi >= 70:
                reasons.append(f"RSI is {latest_rsi:.0f}: This stock may be overbought.")
            elif latest_rsi <= 30:
                reasons.append(f"RSI is {latest_rsi:.0f}: This stock may be oversold.")
            else:
                reasons.append(f"RSI is {latest_rsi:.0f}: No overbought or oversold signal.")

            # Decision with new wording
            if (latest_sma_50 and price > latest_sma_50) and pe_ratio is not None and pe_ratio < sector_pe_avg:
                rec = "Explore Further"
                emoji = "🔎"
            elif (latest_sma_50 and price < latest_sma_50) and pe_ratio is not None and pe_ratio > sector_pe_avg:
                rec = "Be Cautious"
                emoji = "⚠️"
            else:
                rec = "Observe"
                emoji = "👀"

            st.markdown(f"## Recommendation: {rec} {emoji}")
            st.markdown("### Why?")
            for reason in reasons:
                st.write(f"- {reason}")

            st.caption(
                "This recommendation is for educational purposes only and is not financial advice. "
                "Always do your own research and consult a financial advisor before investing."
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
