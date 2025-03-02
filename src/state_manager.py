# class StateManager:
#     def __init__(self):
#         self.state = {}
    
#     def update_state(self, user, key, value):
#         if user not in self.state:
#             self.state[user] = {}
#         self.state[user][key] = value
    
#     def get_state(self, user, key):
#         return self.state.get(user, {}).get(key, None)


class StateManager:
    def __init__(self):
        self.state = {}

    def update_state(self, user, key, value):
        if user not in self.state:
            self.state[user] = {}
        self.state[user][key] = value

    def get_state(self, user, key):
        return self.state.get(user, {}).get(key, None)