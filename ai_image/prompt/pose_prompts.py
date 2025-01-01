from ai_image.prompt.data.pose import Poses
from ai_image.utils import weighted_sample

class PosePrompts:
    def __init__(self):
        self.pose = Poses

    def generate_action(self):
        return weighted_sample(self.pose.action, count=1)[0]

    def generate_gaze(self):
        return weighted_sample(self.pose.gaze, count=1)[0]

    def generate_expression(self):
        return weighted_sample(self.pose.expression, count=1)[0]

    def generate_emotion(self):
        return weighted_sample(self.pose.emotion, count=1)[0]

    def generate_arm_action(self):
        return weighted_sample(self.pose.arm_action, count=1)[0]

    def generate_leg_action(self):
        return weighted_sample(self.pose.leg_action, count=1)[0]

    def generate_prompts(self):
        pose_details = [
            self.generate_action(),
            self.generate_gaze(),
            self.generate_expression(),
            self.generate_emotion(),
            self.generate_arm_action(),
            self.generate_leg_action(),
        ]
        
        return pose_details
    
# 測試生成提示詞
if __name__ == "__main__":
    pose_prompts = PosePrompts()
    print("Pose Action:", pose_prompts.generate_prompts())