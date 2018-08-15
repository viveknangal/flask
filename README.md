# flask
pip install flask gunicorn
# Run the App as follows 
gunicorn -w 4 -b 127.0.0.1:8100 first:app
