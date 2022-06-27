class Post:
    
    def __init__(self, posts):
        self.posts = posts


    def get_post(self, id):
        blog = {}
        for post in self.posts:
            if post['id'] == id:
                blog = post
        return blog
