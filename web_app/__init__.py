import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    
    my_app = create_app()
    my_app.run(debug=True)
