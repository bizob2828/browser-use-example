# Browser Use Example

Simple script that uses [Browser Use](https://github.com/browser-use/browser-use) to interact with Chrome and OpenAI. 

## Setup
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp env.sample .env
# Fill out `OPENAI_API_KEY`, and `OPENAI_BASE_URL`
python browser_test.py
```



