from aws_cdk import App
from aws_cdk import Stack
from aws_cdk import Duration

from constructs import Construct

from aws_cdk.aws_sns import Topic

from aws_cdk.aws_chatbot import SlackChannelConfiguration

from aws_cdk.aws_events import Rule
from aws_cdk.aws_events import Schedule

from aws_cdk.aws_events_targets import SnsTopic

from shared_infrastructure.igvf_dev.environment import US_WEST_2


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

        event_notification_topic = Topic(
            self,
            'EventNotificationTopic',
        )

        event_channel.add_notification_topic(
            event_notification_topic
        )


EventNotificationStack(
    app,
    'EventNotificationStack',
    env=US_WEST_2,
)

app.synth()
