#(APN) : (super-sub-folder, same super diff sub-folder, different super-folder)
class Triplet:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.labels = [label for label in os.listdir(data_folder) if label != '.ipynb_checkpoints']
        self.label_to_path = {label: os.path.join(data_folder, label) for label in self.labels}

    def get_triplet(self):
        anchor_label = random.choice(self.labels)
        anchor_subfolder = random.choice(os.listdir(self.label_to_path[anchor_label]))
        anchor_image = os.path.join(self.label_to_path[anchor_label], anchor_subfolder, 
                                    random.choice(os.listdir(os.path.join(self.label_to_path[anchor_label], anchor_subfolder))))

        positive_label = anchor_label
        positive_subfolder = random.choice(os.listdir(self.label_to_path[positive_label]))
        positive_image = os.path.join(self.label_to_path[positive_label], positive_subfolder,
                                    random.choice(os.listdir(os.path.join(self.label_to_path[positive_label], positive_subfolder))))

        negative_label = random.choice(self.labels)
        if negative_label == anchor_label:
            negative_label = random.choice([label for label in self.labels if label != anchor_label])
        negative_subfolder = random.choice(os.listdir(self.label_to_path[negative_label]))
        negative_image = os.path.join(self.label_to_path[negative_label], negative_subfolder, 
                                    random.choice(os.listdir(os.path.join(self.label_to_path[negative_label], negative_subfolder))))

        anchor_label_num = self.labels.index(anchor_label)
        positive_label_num = self.labels.index(positive_label)
        negative_label_num = self.labels.index(negative_label)

        return anchor_image, positive_image, negative_image 
        #return anchor_label, positive_label_num, negative_label_num
                                  



#(APN) : (super-sub-folder, same super-sub-folder, different super-folder)
class Triplet:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.labels = [label for label in os.listdir(data_folder) if label != '.ipynb_checkpoints']
        self.label_to_path = {label: os.path.join(data_folder, label) for label in self.labels}

    def get_triplet(self):
        anchor_label = random.choice(self.labels)
        anchor_subfolder = random.choice(os.listdir(self.label_to_path[anchor_label]))
        anchor_image = os.path.join(self.label_to_path[anchor_label], anchor_subfolder, 
                                    random.choice(os.listdir(os.path.join(self.label_to_path[anchor_label], anchor_subfolder)))

        # Choose the positive subfolder from the same label as the anchor
        positive_subfolder = anchor_subfolder
        positive_image = os.path.join(self.label_to_path[anchor_label], positive_subfolder,
                                    random.choice(os.listdir(os.path.join(self.label_to_path[anchor_label], positive_subfolder)))

        negative_label = random.choice(self.labels)
        if negative_label == anchor_label:
            negative_label = random.choice([label for label in self.labels if label != anchor_label])
        negative_subfolder = random.choice(os.listdir(self.label_to_path[negative_label]))
        negative_image = os.path.join(self.label_to_path[negative_label], negative_subfolder, 
                                    random.choice(os.listdir(os.path.join(self.label_to_path[negative_label], negative_subfolder)))

        anchor_label_num = self.labels.index(anchor_label)
        positive_label_num = self.labels.index(anchor_label)  # Positive is from the same label as the anchor
        negative_label_num = self.labels.index(negative_label)

        return anchor_image, positive_image, negative_image
                                  

#(APN) : (super-sub-folder query image, same super-sub-folder but positive, same super-sub-folder but negative)
class Triplet:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.labels = [label for label in os.listdir(data_folder) if label != '.ipynb_checkpoints']
        self.label_to_path = {label: os.path.join(data_folder, label) for label in self.labels}

    def get_triplet(self):
        # Choose a random class (ODD or EVEN)
        chosen_class = random.choice(self.labels)
        
        # Choose the anchor image from the chosen class
        anchor_label = chosen_class
        anchor_subfolder = random.choice(os.listdir(self.label_to_path[anchor_label]))
        anchor_image = os.path.join(self.label_to_path[anchor_label], anchor_subfolder, 
                                    random.choice(os.listdir(os.path.join(self.label_to_path[anchor_label], anchor_subfolder))))

        # Choose the positive image from the same subfolder
        positive_subfolder = anchor_subfolder
        positive_image = os.path.join(self.label_to_path[anchor_label], positive_subfolder,
                                    random.choice(os.listdir(os.path.join(self.label_to_path[anchor_label], positive_subfolder))))

        # Choose a different subfolder within the same class for the negative image
        negative_subfolder = random.choice([subfolder for subfolder in os.listdir(self.label_to_path[anchor_label]) if subfolder != anchor_subfolder])
        negative_image = os.path.join(self.label_to_path[anchor_label], negative_subfolder, 
                                    random.choice(os.listdir(os.path.join(self.label_to_path[anchor_label], negative_subfolder))))

        anchor_label_num = self.labels.index(anchor_label)
        positive_label_num = self.labels.index(anchor_label)  # Positive is from the same class as the anchor
        negative_label_num = self.labels.index(anchor_label)  # Negative is from the same class as the anchor

        return anchor_image, positive_image, negative_image
