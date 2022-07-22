from aws_cdk import App
from aws_cdk import Stack

from constructs import Construct

from aws_cdk.aws_chatbot import SlackChannelConfiguration

from shared_infrastructure.cherry_lab.environments import US_WEST_2


app = App()


class EventNotificationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        event_channel = SlackChannelConfiguration(
            self,
            'EventChannel',
            slack_channel_configuration_name='aws-events',
            slack_workspace_id='T1KMV4JJZ',
            slack_channel_id='C03QPGPLAMQ',
        )

EventNotificationStack(
    app,
    'EventNotificationStack',
    env=US_WEST_2,
)

app.synth()
