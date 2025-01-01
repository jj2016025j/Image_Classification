from ai_image.prompt.data.pose import Poses
from ai_image.utils import weighted_sample

class PosePrompts:
    def __init__(self):
        self.pose = Poses

    def generate_action(self, mode='positive'):
        return weighted_sample(self.pose.action, count=1, mode=mode)[0]

    def generate_gaze(self, mode='positive'):
        return weighted_sample(self.pose.gaze, count=1, mode=mode)[0]

    def generate_expression(self, mode='positive'):
        return weighted_sample(self.pose.expression, count=1, mode=mode)[0]

    def generate_emotion(self, mode='positive'):
        return weighted_sample(self.pose.emotion, count=1, mode=mode)[0]

    def generate_arm_action(self, mode='positive'):
        return weighted_sample(self.pose.arm_action, count=1, mode=mode)[0]

    def generate_leg_action(self, mode='positive'):
        return weighted_sample(self.pose.leg_action, count=1, mode=mode)[0]

    def generate_prompts(self, mode='positive'):
        pose_details = [
            self.generate_action(mode=mode),
            self.generate_gaze(mode=mode),
            self.generate_expression(mode=mode),
            self.generate_emotion(mode=mode),
            self.generate_arm_action(mode=mode),
            self.generate_leg_action(mode=mode),
        ]
        
        return pose_details
    
# 測試生成提示詞
if __name__ == "__main__":
    pose_prompts = PosePrompts()
    print("Pose Action:", pose_prompts.generate_prompts( mode='positive'))