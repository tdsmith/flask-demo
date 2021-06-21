# GAE Flask app demo

## To run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Then, browse to <http://localhost:8080>.

## To deploy to Google App Engine

Follow the instructions in https://cloud.google.com/appengine/docs/standard/python3/quickstart.

Briefly:

* Create a project in the Google Cloud Console at https://console.cloud.google.com/projectselector2/home/dashboard.
* [Install and set up the Cloud SDK](https://cloud.google.com/sdk/docs/install).
* Initialize your App Engine app with `gcloud app create --project=whatever-name-you-chose-earlier`.
* Run `gcloud app deploy`.

To tear it down, delete the project in the Cloud Console.
