# Launching on local browser:
pip install -r requirements.txt

pytest -v ./tests/ --browser=chrome_local  
pytest -v ./tests/ --browser=firefox_local  

# Launching on Selenium Grid via Jenkins using Docker:
https://github.com/ragucwa/selenium_docker_runner
