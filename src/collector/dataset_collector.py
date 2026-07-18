class DatasetCollector:

    def __init__(self, labels):

        self.labels = labels

        self.current_index = 0

        self.samples_collected = 0

    def current_label(self):
        return self.labels[self.current_index]
    
    def next_label(self):
        if self.current_index < len(self.labels) - 1:
            self.current_index += 1
            self.samples_collected = 0
    
    def previous_label(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.samples_collected = 0

    def increment(self):
        self.samples_collected += 1