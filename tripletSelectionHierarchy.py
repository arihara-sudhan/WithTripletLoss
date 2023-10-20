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


#(APN) : (super-sub-folder query image, same super-sub-folder but positive, same/different super-sub-folder but negative)
class Triplet:
    def __init__(self, train_folder):
        self.train_folder = train_folder
        self.labels = [label for label in os.listdir(train_folder) if label != '.ipynb_checkpoints']
        self.label_to_path = {}
        for label in self.labels:
            label_path = os.path.join(train_folder, label)
            subdirectories = [subdir for subdir in os.listdir(label_path) if os.path.isdir(os.path.join(label_path, subdir))]
            self.label_to_path[label] = [os.path.join(label_path, subdir) for subdir in subdirectories]

    def get_triplet(self):
        anchor_label = random.choice(self.labels)
        anchor_subdir = random.choice(self.label_to_path[anchor_label])
        anchor_path = random.choice(os.listdir(anchor_subdir))
        positive_label = anchor_label
        positive_subdir = anchor_subdir
        positive_path = random.choice(os.listdir(positive_subdir))
        # Ensure the negative label is different from the positive label within the same superclass
        negative_label = random.choice([label for label in self.labels if label != anchor_label or label not in self.label_to_path[anchor_label]])
        negative_subdir = random.choice(self.label_to_path[negative_label])
        negative_path = random.choice(os.listdir(negative_subdir))

        anchor_image = os.path.join(anchor_subdir, anchor_path)
        positive_image = os.path.join(positive_subdir, positive_path)
        negative_image = os.path.join(negative_subdir, negative_path)

        anchor_label_num = self.labels.index(anchor_label)
        positive_label_num = self.labels.index(positive_label)
        negative_label_num = self.labels.index(negative_label)

        anchor_label_name = f"{anchor_label}-{os.path.basename(anchor_subdir)}"
        positive_label_name = f"{positive_label}-{os.path.basename(positive_subdir)}"
        negative_label_name = f"{negative_label}-{os.path.basename(negative_subdir)}"

        return anchor_image, positive_image, negative_image, anchor_label_num, positive_label_num, negative_label_num, anchor_label_name, positive_label_name, negative_label_name
