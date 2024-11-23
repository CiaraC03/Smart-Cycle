from config import Config
import numpy as np

class myConfig(Config):
    """This is my base class to config."""
    """I will be using the config.py class reference"""

NAME = "SmartCycle"

GPU_COUNT = 1

IMAGES_PER_GPU = 1

STEPS_PER_EPOCH = 100

VALIDATION_STEPS = 10

BACKBONE = "resnet50"

OPTIMIZER = 'SGD'

BACKBONE_STRIDES = [4, 8, 16, 32, 64]

NUM_CLASSES = 61

RPN_ANCHOR_SCALES = (32, 64, 128, 256, 512)

RPN_ANCHOR_RATIOS = [0.5, 1, 2]

RPN_ANCHOR_STRIDE = 1

RPN_NMS_THRESHOLD = 0.7

POST_NMS_ROIS_TRAINING = 2000
POST_NMS_ROIS_INFERENCE = 1000

USE_MINI_MASK = False
MINI_MASK_SHAPE = (512, 512)  # (height, width) of the mini-mask

IMAGE_RESIZE_MODE = "square"
IMAGE_MIN_DIM = 800
IMAGE_MAX_DIM = 1024

IMAGE_MIN_SCALE = 0

USE_OBJECT_ZOOM = True
ZOOM_IN_FREQ = 0.5

MASK_SHARE = False

MEAN_PIXEL = np.array([123.7, 116.8, 103.9])

TRAIN_ROIS_PER_IMAGE = 200

ROI_POSITIVE_RATIO = 0.33

# Pooled ROIs
POOL_SIZE = 7
MASK_POOL_SIZE = 14

    # Shape of output mask
    # To change this you also need to change the neural network mask branch
MASK_SHAPE = [28, 28]

    # Maximum number of ground truth instances to use in one image
MAX_GT_INSTANCES = 100

    # Bounding box refinement standard deviation for RPN and final detections.
RPN_BBOX_STD_DEV = np.array([0.1, 0.1, 0.2, 0.2])
BBOX_STD_DEV = np.array([0.1, 0.1, 0.2, 0.2])

    # Max number of final detections
DETECTION_MAX_INSTANCES = 100

    # Minimum probability value to accept a detected instance
    # ROIs below this threshold are skipped
DETECTION_MIN_CONFIDENCE = 0.7

    # Original mrcnn implementation uses the max class confidence to rank instance detection
    # Setting this to True instead sets the detection score to the ratio between this
    # max class confidence and the background confidence.
    # For using this, you should change the DETECTION_MIN_CONFIDENCE to a value
    # between [10,100]
DETECTION_SCORE_RATIO = True

    # Non-maximum suppression threshold for detection
DETECTION_NMS_THRESHOLD = 0.3
DETECTION_CLASSLESS_NMS_THRESHOLD = 0.9

    # Learning rate and momentum
    # The Mask RCNN paper uses lr=0.02, but on TensorFlow it causes
    # weights to explode. Likely due to differences in optimzer
    # implementation.
LEARNING_RATE = 0.001
LEARNING_MOMENTUM = 0.9

    # Weight decay regularization
WEIGHT_DECAY = 0.0001

    # Loss weights for more precise optimization.
    # Can be used for R-CNN training setup.
LOSS_WEIGHTS = {
        "rpn_class_loss": 1.,
        "rpn_bbox_loss": 1.,
        "mrcnn_class_loss": 1.,
        "mrcnn_bbox_loss": 1.,
        "mrcnn_mask_loss": 1.
    }

    # Use RPN ROIs or externally generated ROIs for training
    # Keep this True for most situations. Set to False if you want to train
    # the head branches on ROI generated by code rather than the ROIs from
    # the RPN. For example, to debug the classifier head without having to
    # train the RPN.
USE_RPN_ROIS = True

    # Train or freeze batch normalization layers
    #     None: Train BN layers. This is the normal mode
    #     False: Freeze BN layers. Good when using a small batch size
    #     True: (don't use). Set layer in training mode even when inferencing
TRAIN_BN = False  # Defaulting to False since batch size is often small

    # Gradient norm clipping
GRADIENT_CLIP_NORM = 5.0

def __init__(self):
        """Set values of computed attributes."""
        super().__init__()
        # Effective batch size
        self.BATCH_SIZE = self.IMAGES_PER_GPU * self.GPU_COUNT

        # Input image size
        if self.IMAGE_RESIZE_MODE == "crop":
            self.IMAGE_SHAPE = np.array([self.IMAGE_MIN_DIM, self.IMAGE_MIN_DIM, 3])
        else:
            self.IMAGE_SHAPE = np.array([self.IMAGE_MAX_DIM, self.IMAGE_MAX_DIM, 3])

        # Image meta data length
        # See compose_image_meta() for details
        self.IMAGE_META_SIZE = 1 + 3 + 3 + 4 + 1 + self.NUM_CLASSES

def display(self):
        """Display Configuration values."""
        print("\nConfigurations:")
        for a in dir(self):
            if not a.startswith("__") and not callable(getattr(self, a)):
                print("{:30} {}".format(a, getattr(self, a)))
        print("\n")
