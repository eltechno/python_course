import boto3

polly_client = boto3.Session(
                aws_access_key_id="",
    aws_secret_access_key="",
    region_name='us-west-2').client('polly')

#response = polly_client.synthesize_speech(VoiceId='Joanna',
response = polly_client.synthesize_speech(VoiceId='Miguel',
                OutputFormat='mp3',
                Text = 'Gracias por comunicarte con nosotros, en un momento te atenderemos, si quieres comunicarte, con ventas, marca uno, contabilidad, marca dos')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
