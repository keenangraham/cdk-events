import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_events.cdk_events_stack import CdkEventsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_events/cdk_events_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkEventsStack(app, "cdk-events")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
