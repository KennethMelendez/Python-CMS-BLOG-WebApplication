class Articles():
    def __init__(self):
        self.articles = [
            {
                'id': 1,
                'title': 'Article One',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin mauris ipsum, pretium accumsan massa molestie id. Pellentesque quis augue eu lorem molestie pellentesque nec ut orci. Suspendisse faucibus scelerisque nibh, vitae congue nisi maximus vel. Mauris rhoncus metus ipsum, sed porta urna scelerisque nec. Donec ac elit volutpat, egestas nulla in, euismod magna. Ut sem est, lobortis eu sapien ut, semper bibendum justo. Pellentesque porttitor porttitor vehicula. Pellentesque nec placerat quam. Mauris ac velit non tortor gravida posuere. Curabitur gravida elementum arcu, vitae congue lectus tincidunt non. Mauris at arcu sit amet risus pellentesque gravida. Phasellus vestibulum cursus augue eget pharetra.',
                'author':'Kenneth Melendez',
                'create_date':'04-25-2017'
            },
            {
                'id': 2,
                'title': 'Article Two',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin mauris ipsum, pretium accumsan massa molestie id. Pellentesque quis augue eu lorem molestie pellentesque nec ut orci. Suspendisse faucibus scelerisque nibh, vitae congue nisi maximus vel. Mauris rhoncus metus ipsum, sed porta urna scelerisque nec. Donec ac elit volutpat, egestas nulla in, euismod magna. Ut sem est, lobortis eu sapien ut, semper bibendum justo. Pellentesque porttitor porttitor vehicula. Pellentesque nec placerat quam. Mauris ac velit non tortor gravida posuere. Curabitur gravida elementum arcu, vitae congue lectus tincidunt non. Mauris at arcu sit amet risus pellentesque gravida. Phasellus vestibulum cursus augue eget pharetra.',
                'author':'Kenneth Melendez',
                'create_date':'04-25-2017'
            },
            {
                'id': 3,
                'title': 'Article Three',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin mauris ipsum, pretium accumsan massa molestie id. Pellentesque quis augue eu lorem molestie pellentesque nec ut orci. Suspendisse faucibus scelerisque nibh, vitae congue nisi maximus vel. Mauris rhoncus metus ipsum, sed porta urna scelerisque nec. Donec ac elit volutpat, egestas nulla in, euismod magna. Ut sem est, lobortis eu sapien ut, semper bibendum justo. Pellentesque porttitor porttitor vehicula. Pellentesque nec placerat quam. Mauris ac velit non tortor gravida posuere. Curabitur gravida elementum arcu, vitae congue lectus tincidunt non. Mauris at arcu sit amet risus pellentesque gravida. Phasellus vestibulum cursus augue eget pharetra.',
                'author':'Kenneth Melendez',
                'create_date':'04-25-2017'
            }
        ]

    def get_articles(self):
        return self.articles    