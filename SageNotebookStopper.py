# Modules needed for the script
from dateutil.tz import tzlocal
import datetime, boto3

# Connecting with Sagemaker through boto3
sagemaker = boto3.client('sagemaker')


def stop_instance(hour, minutes=False):
    # Listing all the instance
    notebooks = sagemaker.list_notebook_instances()['NotebookInstances']

    logs = {}  # To hold all the values returned by the function

    # Looping through all the notebooks
    for notebook in notebooks:
        # Selecting all the instances that are not stopped
        if notebook['NotebookInstanceStatus'] == 'InService':

            # Calculating time difference between current time and last time modified
            diff = datetime.datetime.now(tz=tzlocal()) - notebook['LastModifiedTime']

            # Converting total time to hours
            if minutes is True:
                total_hours = diff.seconds // 60 + (diff.days * 24 * 60)  # Converts the total to minutes
                hour = hour * 60  # Converts the input hours to minutes
            else:
                total_hours = diff.seconds // 3600 + (diff.days * 24)

            # Stopping instances greater than the hour specified
            if total_hours > hour:
                # Stopping the instance and assigning the return statement to a dictionary
                logs[notebook['NotebookInstanceName']] = sagemaker.stop_notebook_instance(
                    NotebookInstanceName=notebook['NotebookInstanceName'])
    return logs

# Default is 1 hour
stop_instance(1)