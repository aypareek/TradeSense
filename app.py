import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="TradeSense (Educational Only)", page_icon=":chart_with_upwards_trend:")

# ----- Banner -----
st.markdown(
    "<div style='background-color: #FFF3CD; padding: 10px; border-radius: 8px; border: 1px solid #FFEEBA; color: #8A6D3B;'>"
    "<b>Educational only:</b> This app does NOT provide financial advice. Recommendations are for learning and demo purposes only.</div><br>",
    unsafe_allow_html=True,
)

# ----- App Title -----
st.title("TradeSense :chart_with_upwards_trend:")
st.write("Enter a NASDAQ ticker to get a basic educational recommendation.")

# ----- Input -----
ticker = st.text_input("NASDAQ Stock Ticker (e.g. AAPL, TSLA, MSFT)").strip().upper()

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        df = stock.history(period="6mo")

        if df.empty:
            st.warning("No historical data found for this ticker.")
        else:
            # Calculate indicators
            close = df['Close']
            sma_50 = close.rolling(window=50).mean().iloc[-1]
            price = close.iloc[-1]
            pe_ratio = info.get('trailingPE', None)
            sector = info.get('sector', 'N/A')
            long_name = info.get('longName', ticker)

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

            # Recommendation Logic
            reasons = []
            if price > sma_50:
                reasons.append("The stock price is above its 50-day moving average (positive momentum).")
            else:
                reasons.append("The stock price is below its 50-day moving average (caution).")

            if pe_ratio is not None:
                if pe_ratio < sector_pe_avg:
                    reasons.append(f"The P/E ratio ({pe_ratio:.1f}) is below the sector average ({sector_pe_avg}).")
                else:
                    reasons.append(f"The P/E ratio ({pe_ratio:.1f}) is above the sector average ({sector_pe_avg}).")
            else:
                reasons.append("P/E ratio not available.")

            # Decision
            if price > sma_50 and pe_ratio is not None and pe_ratio < sector_pe_avg:
                rec = "Buy"
                emoji = "🟢"
            elif price < sma_50 and pe_ratio is not None and pe_ratio > sector_pe_avg:
                rec = "Sell"
                emoji = "🔴"
            else:
                rec = "Hold"
                emoji = "🟡"

            # ESG/Ethical Badge Placeholder
            st.markdown("---")
            st.subheader(f"{long_name} ({ticker})")
            st.write(f"**Sector:** {sector}")
            st.write(f"**Latest Price:** ${price:.2f}")
            st.write(f"**P/E Ratio:** {pe_ratio if pe_ratio is not None else 'N/A'}")
            st.write(f"**Sector Average P/E:** {sector_pe_avg}")

            st.markdown("### ESG/Ethical Badge :seedling:")
            st.info("ESG/Ethical rating integration coming soon. (This is a placeholder for future ethical investing features.)")

            st.markdown("---")
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
