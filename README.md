# tuxgame aggiornato di nuovo
Test repository

git status  -> status of folders

git add     -> aggiungi file da coomittare (-A aggiunge tutto)

git commit  -> lock repository but stays in the local machine

git push    -> updates github

git pull    -> download all changes

git rm      -> remove file


# APP ENGINE FUNCTIONS FOR BQ

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

