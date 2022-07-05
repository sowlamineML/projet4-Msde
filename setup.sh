mkdir _p ~/.streamlit/
echo"\
[server]\n\
headless=true\n\
port=$PORT\n\
enableCORS=false\n\
">~/.streamlit/config.toml
