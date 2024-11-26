import re

def process_message(message_text):
    # Updated pattern to extract name and ticker separately
    pattern = (
        r"➡️\s+(.*?)\|(.*?)\n"                # Token name and ticker
        r"(0x[a-fA-F0-9]+)✂️\n"               # Contract address
        r"📊\s+5M:.*?\|\s+1H:.*?\|\s+24H: (.*?)\n"  # 24H Change
        r"⬆️ Net Inflow: (.*?)\n"             # Net Inflow
        r"⏛ Token Age: (.*?)\n"               # Token Age
        r"🧢 Token FDV: (.*?)\n"               # Token FDV
        r"📊 Token Price: (.*?)\n"             # Token Price
        r"💧 Total Liquidity: (.*?)\n"         # Total Liquidity
        r"💵 Buy Tax: (.*?)\n"                 # Buy Tax
        r"📈 Sell Tax: (.*?)\n"                # Sell Tax
        r"💵 Transfer Tax: (.*?)\n"            # Transfer Tax
        r"🍯 isHoneypot: (.*?)\n"              # isHoneypot
    )
    match = re.search(pattern, message_text, re.DOTALL)

    if match:
        name = match.group(1)
        ticker = match.group(2)
        contract = match.group(3)
        net_inflow = match.group(4)
        token_age = match.group(5)
        token_fdv = match.group(6)
        token_price = match.group(7)
        total_liquidity = match.group(8)
        buy_tax = match.group(9)
        sell_tax = match.group(10)
        transfer_tax = match.group(11)
        is_honeypot = match.group(12)

        # Format the extracted information
        formatted_message = (
            f"➡️ {name} ({ticker})\n"
            f"Contract: {contract}\n"
            f"📊 Net Inflow: {net_inflow}\n"
            f"⏛ Token Age: {token_age}\n"
            f"🧢 Token FDV: {token_fdv}\n"
            f"📊 Token Price: {token_price}\n"
            f"💧 Total Liquidity: {total_liquidity}\n"
            f"💵 Buy Tax: {buy_tax}\n"
            f"📈 Sell Tax: {sell_tax}\n"
            f"💵 Transfer Tax: {transfer_tax}\n"
            f"🍯 isHoneypot: {is_honeypot}"
        )
        return formatted_message
    else:
        return "[Filtered] Could not extract necessary information."
