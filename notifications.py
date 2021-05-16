import apprise


class Notifications:
    def __init__(self):
        self.apprise = apprise.Apprise()

        # Add config files
        config = apprise.AppriseConfig()
        config.add('.config/apprise.conf')
        self.apprise.add(config)

    def send(self, message):
        print("Send Apprise notification...")
        self.apprise.notify(
            body=message,
            title='GregouBot Covid19',
            tag='all'
        )
