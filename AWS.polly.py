import boto3

polly_client = boto3.Session(
                aws_access_key_id="AKIA4A7DY6PRJDZS4PQW",
    aws_secret_access_key="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",
    region_name='us-west-2').client('polly')

response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3',
                Text = 'This is a sample text to be synthesized.')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
