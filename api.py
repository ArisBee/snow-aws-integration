import logging
import boto3
import os
import pysnow

#TOPIC = os.environ['Topic']
INSTANCE = os.environ['Instance']
CLIENTID = os.environ['clientid']
SECRET = os.environ['secret']
USER = os.environ['user']
PSSWD = os.environ['psswd']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(event)
    try:
        session = {'token': None}

        # Takes care of refreshing the token storage if needed
        def updater(new_token):
            print("OAuth token refreshed!")
            session['token'] = new_token

        #sns = boto3.client('sns')
        snow = pysnow.OAuthClient(client_id=CLIENTID, 
                                client_secret=SECRET,
                                instance=INSTANCE )

        if not session['token']:
            # No previous token exists. Generate new.
            session['token'] = snow.generate_token(USER, PSSWD)

        snow.set_token(session['token'])
    except Exception as e:
        logger.error("Unable to Authenticate:"+e)
    
    try:
        if event['context']['http-method']=="GET":
            short_desc = event['params']['querystring']['token'] #accessing the parameters from api call
            return 'something' + short_desc
        elif event['context']['http-method']=="POST":
            message = event
            message['body-json']['short_description']= "WE DID IT!"
            sys_id = message['body-json']['sys_id']
            logger.info(str(message))

            call = snow.resource(api_path='/table/new_call')
            call.parameters.display_value = True

            updated = call.update(query={'sys_id': sys_id},
                          payload={
                              'short_description': 'Processed through API',
                              'description': 'Ticket updated.'
                          })
            # sns.publish(
            #    TopicArn = TOPIC,
            #    Message = str(message)
            # )
            logger.info("The request number is"+ message['body-json']['sys_id'])
            return
    except Exception as e:
        logger.error(e)