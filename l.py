# streamlit_app.py
import streamlit as st
from kiteconnect import KiteConnect

# Put your API Key and Secret from Zerodha Developer Console
API_KEY = "afzia78cwraaod5x"
API_SECRET = "m06lquimu24meln9tw8m6k09eymsg7qi"

kite = KiteConnect(api_key=API_KEY)

st.title("Zerodha Kite Access Token Generator")

# Step 1: Generate login URL
login_url = kite.login_url()
st.write("### Step 1: Login using this URL")
st.markdown(f"[Click here to login]({login_url})")

# Step 2: Paste request token after login
request_token = st.text_input("Paste the request token here:")

if st.button("Get Access Token"):
    if request_token:
        try:
            data = kite.generate_session(request_token, api_secret=API_SECRET)
            access_token = data["access_token"]
            st.success(f"✅ Your Access Token: {access_token}")
            
            # Save it in a file (optional)
            with open("access_token.txt", "w") as f:
                f.write(access_token)
            st.info("Access token also saved in access_token.txt")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please paste request token first.")
