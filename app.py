from flask import Flask
import sys
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
      return measure_time()


def measure_time():
      start_time=time.time()
      #PLACEHOLDER FOR ACTUAL STOP SIGNAL
      time.sleep(10)
      stop_time=time.time()
      time_spent=stop_time-start_time
      print(time_spent)
      sys.stdout.flush()
      return str(time_spent)

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')
