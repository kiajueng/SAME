import glob

joint_dict = {
    "ToSpine": "LowerBack",
    "LHipJoint": "LeftHipJoint",
    "RHipJoint": "RightHipJoint",
    "LeftToe": "LeftToeBase",
    "RightToe": "RightToeBase",
    "LeftToe_End": "LeftToeBase_End",
    "RightToe_End": "RightToeBase_End",
    "Shoulder_L": "LeftShoulder",
    "UpperArm_L": "LeftArm",
    "LowerArm_L": "LeftForeArm",
    "Hand_L": "LeftHand",
    "Shoulder_R": "RightShoulder",
    "UpperArm_R": "RightArm",
    "LowerArm_R": "RightForeArm",
    "Hand_R": "RightHand",
    "UpperLeg_L": "LeftUpLeg", 
    "LowerLeg_L": "LeftLeg",
    "Foot_L" : "LeftFoot",
    "Toes_L" : "LeftToeBase",
    "UpperLeg_R": "RightUpLeg", 
    "LowerLeg_R": "RightLeg",
    "Foot_R" : "RightFoot",
    "Toes_R" : "RightToeBase",
    "Chest":"Spine1",
}

for i,f in enumerate(glob.glob("/home/kia/MOTION_ESTIMATION/bandai-namco_T_pose/*")):
    new_f_name = "joints_renamed_"+f.split("/")[-1]
    print(new_f_name)
    with open(f, "r+") as f_read:
        with open(f"/home/kia/MOTION_ESTIMATION/bandai-namco_T_pose_rename_joints/{new_f_name}","w+") as f_write:
            for line in f_read:
                for joint_name in joint_dict:
                    if joint_name in line:
                        line = line.replace(joint_name,joint_dict[joint_name])

                f_write.write(line)
                
