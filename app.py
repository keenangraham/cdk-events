from aws_cdk import App

from shared_infrastructure.cherry_lab.environments import US_WEST_2


app = App()


app.synth()
