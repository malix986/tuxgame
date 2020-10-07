# APP ENGINE FUNCTIONS

# VIRTUAL ENV
virtualenv --python python3 ~/envs/big_query
source ~/envs/big_query/bin/activate

# INSTALL REQUIREMENTS
pip install -r requirements.txt
pip3 install -r requirements.txt

# VIM
vim file.txt
press i to edit
press ESC :wq to save

# BIG QUERY

#    Create a new service account to access the BigQuery API by using:

export PROJECT_ID=$(gcloud config get-value core/project)

gcloud iam service-accounts create big-query-credentials \
  --display-name "my bigquery service account"

#    Next, create credentials that your Python code will use to login as your new service account. Create these credentials and save it as a JSON file ~/key.   json by using the following command:

gcloud iam service-accounts keys create ~/key.json \
  --iam-account big-query-credentials@${PROJECT_ID}.iam.gserviceaccount.com

export GOOGLE_APPLICATION_CREDENTIALS=~/key.json

#   Finally, set the GOOGLE_APPLICATION_CREDENTIALS environment variable, which is used by the BigQuery Python client library, covered in the next step, to find your credentials. The environment variable should be set to the full path of the credentials JSON file you created, by using:

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
  --member "serviceAccount:big-query-credentials@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role "roles/bigquery.user"

#   Local Launch

export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value core/project)
export GOOGLE_APPLICATION_CREDENTIALS: "/Users/amalinverni/Desktop/github-wikigame/my-project-1509808152396-6823ad5c6a5d.json"
export PYTHONIOENCODING: 'utf-8'

dev_appserver.py app.yaml


# prima di deployare
gcloud app deploy -q -v 12345

# hints cleanup query

create or replace table `tuxgame.hint_list` as
SELECT 
character_name, 
trim(REGEXP_REPLACE(hint, r"\==([^)]+)\==", "")) as hint, 
hint_shown, 
hint_guessed, 
hint_wrong, 
hint_raw, 
CASE 
  WHEN hint_raw like '%ISBN%' THEN FALSE
  WHEN length(hint_raw) >= 500 THEN FALSE
  ELSE TRUE
END as is_active
FROM tuxgame.hint_list
